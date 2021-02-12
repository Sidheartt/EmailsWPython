import smtplib
import datetime as dt
import random
# 
my_email = "sidcodes@yahoo.com"
password = "dzhymbxolywtajxq"
# 
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="coffeecode0@gmail.com",
#                     msg="Subject:Hello\n\n It was always burning, since the world's been turning")
# connection.close()
#
with open("quotes.txt", "r") as quote:
    all_quotes = quote.readlines()
    selected = random.choice(all_quotes)

now = dt.datetime.now()
if now.weekday() == 4:
    print(selected)
    connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="desaikunda70@gmail.com",
                        msg=f"Subject:Are MoTu \n\n T-shirt tight ho raha h kitna khayega aur fut jayega??? ")







# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1996, month=1, day=2)
#print(date_of_birth)

