import smtplib
import pandas
import os
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

choice = input("Enter 1. Add event 0. Exit : ")
while choice:
    event_name = input("Enter the event name: ")
    receiver_add = input("Enter email id of the receiver: ")
    r_year = input("Enter the year to receive (ex: 2023 or 2024): ")
    r_month = input("Enter the month to receive: ")
    r_day = input("Enter the day to receive: ")
    if os.path.exists("events1.csv") == 0:
        file = open("events1.csv", "a")
        file.write("name,email,year,month,day")
        file.close()

    file = open("events1.csv", "a")
    file.write(f"\n{event_name},{receiver_add},{r_year},{r_month},{r_day}")
    file.close()

    print(f"Event name: {event_name} \nReceiver address: {receiver_add} \nDate of remainder: {r_day}-{r_month}-{r_year}"
        f"\nYour remainder is saved successfully.")

    choice = input("Enter 1. Add event 0. Exit : ")









