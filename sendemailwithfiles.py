#encoding:utf-8
from smtplib import SMTP
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
#define the sendemail function
msg = MIMEMultipart()# create the MIMEMultipart

server_address = 'smtp.163.com'
user = 'dreamer1991713'
password = '1991713wxt'
reciever = 'dreamer1991713@163.com'
subfix = '163.com'
#create the file
fi1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
fi1['Content-Type'] = 'application/octet-stream'
fi1['Content-Disposition'] = 'attachment;filename="test.txt"'# filename is the name in the eamil
msg.attach(fi1)# attach the fi1 to the MIMEMultipart

def sendemail(mail_to,sub,content):
    try:
        server = SMTP()
        server.connect(server_address)
        server.login(user,password)
        msg['subject'] = sub
        msg['from'] = user+'@'+subfix
        msg['to'] = mail_to
        server.sendmail(msg['from'],msg['to'],msg.as_string())
        server.quit()
        return True
    except Exception,e:
        print(str(e))
        return False


if sendemail(reciever,'getfiles',None):
    print('ok')
else:
    print('failed')
