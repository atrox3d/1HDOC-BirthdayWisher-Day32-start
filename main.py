########################################################################################################################
# https://www.udemy.com/course/100-days-of-code/learn/lecture/21096102
# https://myaccount.google.com/u/3/lesssecureapps
########################################################################################################################
import configmanager
import smtplib
import datetime as dt
import random

CONFIG = configmanager.get_config()
MAIL_ADDRESS = configmanager.get_email()
MAIL_USER = configmanager.get_user()
MAIL_PASSWORD = configmanager.get_password()
MAIL_SERVER = configmanager.get_server()
# print(CONFIG)


def sendmail(message, recipient=MAIL_ADDRESS):
    with smtplib.SMTP(MAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=MAIL_USER, password=MAIL_PASSWORD)
        # msg = "Subject: Prova Python\n\nCiao, come andiamo? questa è una mail di prova mandata da python".encode("utf8")
        # print(msg)
        connection.sendmail(
            from_addr=MAIL_ADDRESS,
            to_addrs=MAIL_ADDRESS,
            msg=message,
        )


def play_with_dates():
    now = dt.datetime.now()
    print(now, type(now))
    print(now.year, type(now.year))

    date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
    print(date_of_birth)


def quote_of_the_day():
    try:
        with open("quotes.txt", "r") as quote_file:
            quotes = quote_file.readlines()
    except FileNotFoundError as fnfe:
        print(fnfe)
    else:
        quote = random.choice(quotes).strip()
        print(quote)
        return quote.split("-")


today = dt.datetime.now().weekday()
if today == 0:
    quote, author = quote_of_the_day()
    print(quote, author)
    subject = "quote of the day"
    text = f"{quote}\n{author}"

    message = f"Subject: {subject}\n\n{text}"
    sendmail(message)
