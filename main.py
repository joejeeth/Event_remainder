import smtplib
import pandas
from random import randint
import datetime as d

dt = d.datetime
now = dt.now()
day = now.day
month = now.month
today = (month, day)

data = pandas.read_csv("events.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    person = birthday_dict[today]

    name = person["name"]
    email = person["email"]

    with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as file:
        l = file.read()

    final_letter = l.replace("[NAME]", name)

    my_email = "your mail id"
    password = "its password"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Important Event\n\n"
                                                                                        f"{final_letter}")












