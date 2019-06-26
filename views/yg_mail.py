
import smtplib
import random

from email.mime.text import MIMEText


def senMail(user, pwd, send, recevier, content, title):
	
	mail_host = 'smtp.163.com'
	message = MIMEText(content, "plain", "utf-8")
	message['From'] = send
	message['To'] = ','.join(recevier)
	message['Subject'] = title
	
	try:
		obj = smtplib.SMTP_SSL(mail_host, 465)
		obj.login(user, pwd)
		obj.sendmail(send, recevier, message.as_string())
		
		print('发送成功')
	except smtplib.SMTPException as e:
		print('发送失败！',e)


def sendmail(mail):
	num = ''.join([str(random.randint(0, 9)) for _ in range(4)])
	
	mail_user = "felix_cto@163.com"
	mail_pwd = "zy1993"
	sender = mail_user
	receivers = [mail]
	
	content = "验证码：%s。您在使用邮件验证功能，该验证码仅用于验证身份，请勿泄露给他人使用！3分钟有效！" % (num)
	title = '易果短信验证码'
	senMail(mail_user, mail_pwd, sender, receivers, content, title)
	return num
	
result = sendmail('yyz315@qq.com')
print(result)