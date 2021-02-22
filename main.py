########################################################################################################################
# https://www.udemy.com/course/100-days-of-code/learn/lecture/21096102
# https://myaccount.google.com/u/3/lesssecureapps
########################################################################################################################
import configmanager
import smtplib

CONFIG = configmanager.get_config()
MAIL_ADDRESS = configmanager.get_email()
MAIL_USER = configmanager.get_user()
MAIL_PASSWORD = configmanager.get_password()
MAIL_SERVER = configmanager.get_server()
print(CONFIG)

with smtplib.SMTP(MAIL_SERVER) as connection:
    connection.starttls()
    connection.login(user=MAIL_USER, password=MAIL_PASSWORD)
    msg = "Subject: Prova Python\n\nCiao, come andiamo? questa è una mail di prova mandata da python".encode("utf8")
    print(msg)
    connection.sendmail(
        from_addr=MAIL_ADDRESS,
        to_addrs=MAIL_ADDRESS,
        msg=msg,
    )
