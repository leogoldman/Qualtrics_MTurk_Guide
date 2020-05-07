import boto3
from tqdm import tqdm
import pandas as pd
import numpy as np
import time
import sys

#IMPORTANT: ANY ERRORS IN THIS SCRIPT, MISUSE OF THE SCRIPT, OR IMPROPER INPUTS CAN RESULT IN A LOSS
#OF FUNDS FROM YOUR MTURK ACCOUNT. USE WITH CAUTION.

#Template for paying out bonuses, given Qualtrics results DataFrame and MTurk results DataFrame
#AWS calls to send out bonuses are at bottom (commented out)
#Once these are uncommented out, bonuses may be sent out

# Fill in these fields if you haven't configured your AWS
region_name = 'us-east-1'
aws_access_key_id = 'YOUR_ACCESS_ID'
aws_secret_access_key = 'YOUR_SECRET_KEY'
endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

#####
# If you are not using the above variables because you have already configured
# the AWS client via Terminal, uncomment the boto3.client() call that only has
# one parameter, 'mturk' and comment out the above variables
#####

#client = boto3.client( 'mturk' )

client = boto3.client( 'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key )

#Enter CSV file names and bonus reason
qualtrics_csv = ""
mturk_results_csv = ""
bonus_reason = "Thank you for taking our survey"

#Read in Qualtrics CSV
q_df = pd.read_csv( qualtrics_csv )
q_df = q_df[ 2: ] #This gets rid of the two header rows in Qualtrics dataframes (not incl top row which is variables)
q_df = q_df[ q_df[ "Status" ] != "Survey Preview" ]

#Read in MTurk CSV
m_df = pd.read_csv( mturk_results_csv )

#Template for method that checks if answer is correct (can also be used for attention checks)
#Input: Qualtrics DataFrame
#Output: Qualtrics DataFrame with extra column, "correct_answer_1"
#Remeber that if right_answer is a number, it may need to be a string if it is a string in q_df
def correct_answer_1( df, column_name, right_answer ):
    df[ "correct_answer_1" ] = df.apply( lambda row: 1 if(row[ column_name ] == right_answer) else 0, axis = 1 )
    pct_passed = round( np.mean( df[ "correct_answer_1" ] )*100, 2 )
    print( "\ndf[ 'correct_answer_1' ] created")
    print( pct_passed, "percent answered quetion 1 correctly" )
    return df

#Template for method that assigns each participant a score
#May require heavy editing depending on scoring scheme
def calc_score( df, max_possible_score = None ):
    df[ "raw_score" ] = df[ "correct_answer_1" ] #+ df[ "correct_answer_2" ]

    #Robustness check
    if not max_possible_score is None:
        if np.amax( df["raw_score"] ) > max_possible_score:
            print( "ERROR: raw score above max possible" )

    print( "\nRaw scores calculated. df[ 'raw_score' ] created" )
    print( "Raw score summary:" )
    print( df[ "raw_score" ].describe() )
    return df

#Calculates bonus amounts
#Uses column df[ "raw_score" ]
def create_bonus_amounts( df, base_amt, dollar_per_question ):
    df[ "bonus_amt" ] = base_amt + df[ "raw_score" ] * dollar_per_question
    print( "\nBonuses calculuated. df[ 'bonus_amt' ] created." )
    print( "Qualtrics df bonus column summary" )
    print( df["bonus_amt"].describe() )
    print( "\nBonus column sum (including 20 percent fee)" )
    print( np.sum( df["bonus_amt"] ) * 1.2 )
    return df
    
#Method for matching workers from MTurk results to Qualtrics entry
def get_bonuses( m_df, q_df, q_random_ID_col_name = "Random ID" ):
    m_df[ "bonus_amt" ] = [ "0" for x in range( m_df.shape[0] ) ] #Set everyone's bonus to 0 initially
    for i in range( m_df[ "Answer.surveycode" ].size ):
        temp_code = str( m_df["Answer.surveycode"][i] )
        q_df_ID_col = q_df[ q_random_ID_col_name ]
        index = q_df_ID_col[ q_df_ID_col == temp_code ]
        if index.size > 1:
            print( "Double match! Check ID: ", temp_code )
        elif index.size > 0:
            temp_bonus = q_df[ "bonus_amt" ][ index.index[0] ]
            m_df[ "bonus_amt" ].at[i] = temp_bonus
        else:
            print( "No match for MTurk Surveycode: ", temp_code )
    print( "\n Added bonuses from Qualtrics df to MTurk df" )
    print( "MTurk bonus column summary" )
    print( m_df["bonus_amt"].describe() )
    return m_df

#Run functions
#This may need editing dependending on your bonus scheme
q_df = correct_answer_1( df=q_df, column_name= , right_answer= )
q_df = calc_score( df=q_df, max_possible_score=None )
q_df = create_bonus_amounts( df=q_df, base_amt=, dollar_per_question= )
m_df = get_bonuses( m_df=m_df, q_df=q_df, q_random_ID_col_name = "Random ID" )

###PAY BONUSES (uncomment this if you are sure everything is working properly and ready to go)
print( "ATTENTION: You are about to pay out bonuses" )
if input( "You are about to pay out bonuses. Are you sure you want to continue? y/n  " ) != 'y':
    sys.exit()
#print( "Paying out bonuses" )
# for i in tqdm( range( m_df.shape[0] ) ):
#     response = client.send_bonus(
#         WorkerId = m_df[ "WorkerId" ].at[i],
#         BonusAmount = m_df[ "bonus_amt" ].at[i],
#         AssignmentId = m_df[ "AssignmentId" ].at[i],
#         Reason = bonus_reason #This was set at the top of the script
#         #UniqueRequestToken='string'
#     )
#print( "All done! Bonuses should have been paid :) " )

