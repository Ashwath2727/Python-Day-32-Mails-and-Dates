##################### Extra Hard Starting Project ######################
import random
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd

PLACEHOLDER = "[NAME]"
MY_EMAIL = "miniash3127@gmail.com"
PASSWORD = ""
now = dt.datetime.now()

birthday_dict = pd.read_csv('birthdays.csv').to_dict(orient='records')
# print(birthday_dict)

for person in birthday_dict:
    # print(person)

    if person["month"] == now.month and person["day"] == now.day:
        print(f"selected ==============> {person}")
        random_letter_num = random.randint(1, 3)
        print(random_letter_num)

        with open(f"letter_templates/letter_{random_letter_num}.txt", "r") as letter_file:
            words = letter_file.read()

            final_letter = words.replace(PLACEHOLDER, person["name"].strip())
            print(final_letter)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday!\n\n{final_letter}"
            )





