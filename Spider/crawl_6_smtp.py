import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def send_email():
    rq=time.strftime("%Y-%m-%d")
    email_from="...@..."
    smtpserver="smtp."
    password="..."
    email_to="...@..."

    subject="{rq} weibo".format(rq=rq)
    data=analysis_html()
    table='<table>'
    for ea in data:
        table+='<tr><td>{order}:{title}:{readers}:{level}</td></tr>'.format(order=ea[0],title=ea[1],readers=ea[2],level=ea[3])
    table+='</table>'
    content=table
    
    msg=MIMEText(content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=email_from
    msg['To']=email_to
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(email_from,password)
    print('Sending...')

    smtp.sendmail(email_from,email_to,msg.as_string())
    smtp.quit()
    print('Sent!')