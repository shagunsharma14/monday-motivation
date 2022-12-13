# ------------------------------SMTP module--------------------------------------------------------- #
# import smtplib
# # NOTE --> Don't forget to change your email app's email settings
# # NOTE --> For yahoo gmail outlook etc.,every app has their own location of server
# # my_email = "@gmail.com"
# # password = " "
#
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com")  as connection:# location of email provider's smtp server
#     connection.starttls() # secure connection Transport Layer Security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )
# ------------------------------datetime module---------------------------------------------------- #
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
# --------------------------------Wednesday Motivation------------------------------------------- #
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
# to check current day of the week
day_of_week = now.weekday()
if day_of_week == 1:
    # open the quotes.txt file
    with open("quotes.txt") as quotes_file:
        quotes_data = quotes_file.readlines()
        # pick random quote from the list
        quote = random.choice(quotes_data)

    # smtplib to send the email
    EMAIL = "@gmail.com"
    PASSWORD = " "
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs="@gmail.com",
                            msg=f"Subject:Wednesday Motivation\n\n"
                                f"{quote}")
