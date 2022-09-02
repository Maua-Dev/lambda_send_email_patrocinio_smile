import boto3
from botocore.exceptions import ClientError
import json
from generate_html import generate_html

def lambda_handler(event, context):
    name = event['name']
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "dev@maua.br"
    
    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "caiobbgtoledo@gmail.com"
    
    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    
    # CONFIGURATION_SET = "ConfigSet"
    
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "sa-east-1"
    
    # The subject line for the email.
    SUBJECT = "Amazon SES Test (SDK for Python)"
                    
    # The HTML body of the email.
    BODY_HTML = generate_html(name)     
    
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
