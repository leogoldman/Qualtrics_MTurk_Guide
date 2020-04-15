# Getting Started with Amazon Mechanical Turk

**Objective:** This document is intended to get the user from a place of no familiarity with Amazon Mechanical Turk (MTurk) to a position where “batches” (jobs) can be posted on MTurk and payments can be made efficiently (via the Amazon Web Services (AWS) API). If sample sizes are expected to be very small and paying workers manually is acceptable, all the user needs is a regular Amazon account. For larger jobs, linking an AWS account will be helpful. 

**Step 1**: Select or create a regular Amazon account. This is the same as an account that any consumer on Amazon would use.
Note: MTurk workers will see your full name and possibly email address.

**Step 2**: Using this Amazon account, sign into MTurk as a requester.

The following steps are also outlined in the [“Developer” section](https://requester.mturk.com/developer) of your MTurk Account.

**Step 3**: [Create an AWS account](https://aws-portal.amazon.com/gp/aws/developer/registration/index.html). This will require you to enter the name and address of your employer and input a credit card for payment information, although you may sign up for a free plan and then will not be charged (there may be a $1 authentication charge that is reimbursed).

**Step 4**: Link your Amazon and AWS accounts.
1.	Log into your MTurk Requester account.
2.	Select “Developer” in the toolbar
3.	Scroll down and select “Link Accounts.”

**Step 5**: Acquire your AWS account keys. These will be needed to use the AWS API for bulk tasks such as bonusing workers or assigning qualification scores, without using the interface on the MTurk website.

  * To obtain account keys, log into your AWS account, select the account dropdown menu in the upper-right of the screen > “My Security Credentials” > “Access Keys” > “Create Access Key” and this should let you download both your Access Key and Secret Access Key in a CSV file.

You are now set up to post batches for MTurk workers to complete, and to pay workers efficiently via the AWS API. For more information on this, see the “Paying MTurk Worker Bonuses via Amazon Web Services (AWS) API” documentation.
