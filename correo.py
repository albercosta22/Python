import boto3
import json

def send_email(subject, body):
    ses = boto3.client('ses', region_name='us-east-1')  
    sender_email = 'albercm22@hotmail.com'  
    recipient_email = 'albercm22@hotmail.com'  
    
    email_body = f"""
    <html>
    <head></head>
    <body>
      <h1>{subject}</h1>
      <p>{body}</p>
    </body>
    </html>
    """
    
    response = ses.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Html': {'Data': email_body}}
        }
    )
    
    return response

def lambda_handler(event, context):
    if event['detail-type'] == 'EC2 Instance Launch Successful':
        instance_id = event['detail']['EC2InstanceId']
        subject = 'Nueva instancia creada en el grupo de autoescalado'
        body = f'Se ha creado la instancia con ID: {instance_id}'
        response = send_email(subject, body)
        print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Correo enviado exitosamente')
    }
