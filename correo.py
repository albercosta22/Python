import json
import smtplib
import boto3

def lambda_handler(event, context):
    
    remitente = "albercm22@hotmail.com" 
    destinatario = "albcosta22@gmail.com" 
    asunto = "Instancia creada" 
    mensaje = """Se ha creado una nueva instancia en su servidor HTTP"""

    email = """From: %s
    To: %s 
    MIME-Version: 1.0 
    Content-type: text/html 
    Subject: %s 
    
    %s
    """ % (remitente, destinatario, asunto, mensaje) 
    try: 
        smtp = smtplib.SMTP('localhost') 
        smtp.sendmail(remitente, destinatario, email) 
        print("Correo enviado") 
    except: 
        print("""Error: el mensaje no pudo enviarse. 
        Compruebe que sendmail se encuentra instalado en su sistema""")
    return {
            'statusCode': 200,
    }