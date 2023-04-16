import smtplib
import datetime as dt
import random


my_email = "alle.darstar@gmail.com"
password = "PASSWORD"

now = dt.datetime.now()
dzien_tygodnia = now.weekday()

def find_quote():
    with open(".\Day32_Birthday_Wisher\quotes.txt") as cyt_file:
        cytaty = cyt_file.readlines()
        print(type(cytaty))
        print(f"Quotes number = {len(cytaty)}")
        cyt_los = random.randrange(len(cytaty))
        print(f"Quote number = {cyt_los}")
        cyt_found = cytaty[cyt_los]
        print(cytaty[cyt_los])
    return cyt_found


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    found_quote = find_quote()
    if dzien_tygodnia == 1:
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="darstar.misc@gmail.com", 
            msg=f"Subject:Cool quote\n\n{found_quote}."
            )


