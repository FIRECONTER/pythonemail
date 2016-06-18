#encoding:utf-8
import smtplib
from email.mime.text import MIMEText
mail_list=['??@163.com']# set the address of the mail the reciever's address
mail_host="smtp.163.com" #set the address server
mail_user="??"#set the user's email
mail_pass="??"#set the user's pass word
mail_postfix="163.com"#set the suffix
def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)# connect the server
        server.login(mail_user,mail_pass)# login the user's account
        server.sendmail(me, to_list, msg.as_string())# send email to the reciever
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if send_mail(mail_list,"hello","hello world"):
    print "send ok"
else:
    print "send failed"