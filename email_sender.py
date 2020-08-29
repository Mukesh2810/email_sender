import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('../Web Development/mywebsite/t20leagues.html').read_text())
email = EmailMessage()
email['from'] = 'Mukesh Singh'
email['to'] = 'rakeshsinghrs2810@gmail.com'
email['subject'] = 'Sending dummmy email through Python Code'

#email.set_content('Hello,its me Rakesh.\n Hope wherever you are you must be fine and shine.')
email.set_content(html.substitute({'adj': 'Fabulous'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('kritikauniversal28@gmail.com','mUK.sIN28')
	smtp.send_message(email)
	print('ALL GOOD TO GO.')