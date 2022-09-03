import boto3
from botocore.exceptions import ClientError
import json
import os
from generate_html import generate_html

def lambda_handler(event, context):
    company_name = event['company_name']
    colab_name = event['colab_name']
    email = event['email']
    number = event['number']
    cnpj = event['cnpj']
    sponsor_type = event['sponsor_type']
    closure_date = event['closure_date']
    
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = os.environ["SENDER"]
    
    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = os.environ["RECIPIENT"]
    
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = os.environ["REGION"]
    
    # The subject line for the email.
    SUBJECT = f"Interesse de patrocínio - {company_name}"
                    
    # The HTML body of the email.
    BODY_HTML = generate_html(
        company_name = company_name,
        colab_name = colab_name,
        email = email,
        number = number,
        cnpj = cnpj,
        sponsor_type = sponsor_type,
        closure_date = closure_date
        )     
    
    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 502,
            'body': json.dumps(e.response['Error']['Message'])
        }
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return {
            'statusCode': 200,
            'body': json.dumps('Email enviado!')
        }
