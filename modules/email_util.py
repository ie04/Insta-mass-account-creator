import email as mail
import imaplib
import re
def check_confirmation_code(email, password):
    
    mail_server = imaplib.IMAP4_SSL('outlook.office365.com')
    mail_server.login(email, password)
    mail_server.select('INBOX')

    result, data = mail_server.search(None, 'FROM "no-reply@mail.instagram.com"')
    email_ids = data[0].split()
    while True:   
        if email_ids:
            # Fetch the email details
            result, data = mail_server.fetch(email_ids[-1], '(RFC822)')
            raw_email = data[0][1]
            msg = mail.message_from_bytes(raw_email)

            # Extract information from the email
            sender = msg['From']
            subject = msg['Subject']
            body = ""

            # Process the email body based on its content type
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8')
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8')

            # Check for a 6-digit string in the email body
            match = re.search(r'\b\d{6}\b', body)
            if match:
                code = match.group(0)
                print("Verification code found:", code)
                return code