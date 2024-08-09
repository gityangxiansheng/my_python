# 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 邮件内容
subject = '亲爱的狗蛋！'
body = '邮件正文！'
 
# 构建邮件
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 
msg['To'] = 
 
# 发送邮件
smtp_server = 'smtp.qq.com'
smtp_port = 587
sender_email = ''
password = ''
 
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, [msg['To']], msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败:', str(e))
