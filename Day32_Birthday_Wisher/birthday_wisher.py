import smtplib
import pandas as pd
import random
import datetime as dt
import os

people = pd.read_csv("./Day32_Birthday_Wisher/birthdays.csv")
# print(people)
# print(type(people))

my_email = "alle.darstar@gmail.com"
password = "bxosjlkgphmvxfrl"

now = dt.datetime.now()
dzis_dzien = now.day
dzis_miesiac = now.month

for person in people.itertuples():
    print(person.name, person.month, person.day)
    if dzis_dzien == person.day and dzis_miesiac == person.month:
        # print("Happy Birthday")
        list_templates = os.listdir("./Day32_Birthday_Wisher/letter_templates")
        # print(list_templates)
        template_chosen = random.choice(list_templates)
        # print(template_chosen)
        with open("./Day32_Birthday_Wisher/letter_templates/" + template_chosen) as letter_file:
            template_chosen_txt = letter_file.read()
            # print(template_chosen_txt) 
            # print(type(template_chosen_txt))
            new_letter_text = template_chosen_txt.replace("[NAME]", person.name)
            # print(new_letter_text)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="darstar.misc@gmail.com", 
                msg=f"Subject:Happy Birthday\n\n{new_letter_text}."
                )

