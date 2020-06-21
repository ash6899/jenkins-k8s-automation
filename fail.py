import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "codewithash99@gmail.com"
host_pass = '12345@aB'
guest_address = "yashkhandelwal2017@gmail.com"
subject = "Regarding Your Last Commit "
content = '''Hello,
                Developer this is an email regarding your recent commit.
                 ERROR !! There is some error in your last commit.
                 Or either rollback to the prvious version by 
                 changing the version in the version file and again commit'''+'\n or Again commit by removing the error !!  '
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
