import smtplib
import datetime

sender = "paulo.sergio.santos.teste@gmail.com"
password = "t3st3t3st3"
to = input("Email do destinatário: ")
subject = input("Assunto: ")
body = input("Mensagem do email: ")
header = "From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (sender, to, subject)
msg = header + body
print("Enviando email... ")
mailserver = smtplib.SMTP("smtp.gmail.com", 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(sender, password)
mailserver.sendmail(sender, to, msg)
mailserver.close()
print("Email enviado de %s para %s: %s" % (sender, to, datetime.datetime.now()))
