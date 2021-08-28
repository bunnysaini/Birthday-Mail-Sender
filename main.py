import random
import smtplib
import pandas as pd
import datetime as dt

SENDER = "Bunny"                                # Enter Sender's (Your) Name
my_email = "testemail@gmail.com"                # Enter Your Email ID
password = "password"                           # Enter Your Mail Password
data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
today = (dt.datetime.now().month, dt.datetime.now().day)

for index in range(0, len(birthday_dict)):
    if (birthday_dict[index]["month"], birthday_dict[index]["day"]) == today:
        filepath = f"letter_templates/letter_{random.randint(1, 10)}.txt"

        with open(filepath) as letter:
            content = letter.read()
            content = content.replace("[NAME]", birthday_dict[index]["name"])
            content = content.replace("[SENDER]", SENDER)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_dict[index]["email"],
                                msg=f'Subject:Happy Birthday {birthday_dict[index]["name"]}!\n\n{content}')