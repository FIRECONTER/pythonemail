#encoding:utf-8
import smtplib
from email.mime.text import MIMEText
# email.mime.text is a module
mail_to = ['dreamer1991713@163.com']# this is a list so you can send the email to many persons
user = 'dreamer1991713'
password = '1991713wxt'
mail_host = 'smtp.163.com'
mail_sufix = '163.com'
def sendMessage(sub,content):
    me = 'hello'+'<'+user+'@'+mail_sufix+'>'
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = me
    msg['from'] = user
    msg['to'] = ';'.join(mail_to)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)# the SMTP port is 25
        server.login(user,password)
        server.sendmail(me,mail_to,msg.as_string())
        server.close()
        return True
    except Exception,e:
        print str(e)
        return False
if sendMessage('hello','helloworld'):
    print 'ok'
else:
    print 'failed'




