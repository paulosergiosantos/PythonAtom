import smtplib
import datetime

sender = "paulo.sergio.santos.teste@gmail.com"
password = "t3st3t3st3"
to = "paulosergio.natercia@gmail.com"
subject = "Teste de envio de mail usando Python"
header = "From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (sender, to, subject)
body = "Mensagem do email"
msg = header + body
print(msg)
mailserver = smtplib.SMTP("smtp.gmail.com", 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(sender, password)
mailserver.sendmail(sender, to, msg)
mailserver.close()
print("Email '%s' enviado de %s para %s: %s" % (subject, sender, to, datetime.datetime.now()))
