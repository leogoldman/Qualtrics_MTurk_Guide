import boto3
from tqdm import tqdm #Keep this package if you want progress bars (used in final for loop around line 54)

# Fill in these fields if you haven't configured your AWS
# region_name = 'us-east-1'
# aws_access_key_id = 'YOUR_ACCESS_ID'
# aws_secret_access_key = 'YOUR_SECRET_KEY'
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'
#
#
# Enter the HIT ID (as a STRING) whose workers you are trying to assign a qualifciation to (this can be found in your results page or downloaded CSV)
hit_id = '3VQTAXTYO7LWU6YVLF26YZRGP66UBM'
#
# Enter the friendly name of the qualification types that you are trying to assign to workers. It is OK if there is only one item in the list (keep it as a list)
qual_ids = [ "Prev_Worker_Cor_r3" ]

client = boto3.client( 'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key )

paginator = client.get_paginator( 'list_assignments_for_hit' )
response_iterator = paginator.paginate(
    HITId=hit_id,
    AssignmentStatuses=[
        'Approved' # This can be changed to 'Submitted' if desired
    ],
    PaginationConfig={
        'MaxItems': 1000, # This may need changing for particularly large HITs
        'PageSize': 100
        #'StartingToken': # Leave this commented out
    }
)

worker_ids = []
for page in response_iterator:
    qty = len( page['Assignments'] )
    for i in range( qty ):
        worker_ids.append( page['Assignments'][i]['WorkerId'] )

print( len(worker_ids), "workers took the HIT and will be assigned qualification" )

# Helper function to turn friendly qualification name to qualification ID
def get_qualification_id( qualifiation_name ):
    response = client.list_qualification_types(
        Query= qualifiation_name,
        MustBeRequestable=False,
        MustBeOwnedByCaller=True,
        #NextToken='string',
        MaxResults=10
    )
    return response['QualificationTypes'][0]['QualificationTypeId']

for qual in qual_ids:
    print( "Assigning workers to qualification:", qual )
    qual = get_qualification_id( qual ) # This converts the qualificaiton type from friendly name to qualification ID
    for i in tqdm( range( len(worker_ids) ) ):
        response = client.associate_qualification_with_worker(
            QualificationTypeId=qual,
            WorkerId=worker_ids[i],
            IntegerValue=1, # Change this value if you would like to assign a score other than 1
            SendNotification=False
        )
    print( "Done with qualification:", qual )

print( "All done! :)" )
