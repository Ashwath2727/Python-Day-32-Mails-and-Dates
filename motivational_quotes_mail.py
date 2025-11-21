import random
import smtplib
import datetime as dt

my_email = "miniash3127@gmail.com"
password = "tzanpwfapikjhafs"

now = dt.datetime.now()

if now.weekday() == 4:
    with open("quotes.txt") as file:
        quotes = file.readlines()

        current_quote = random.choice(quotes)

    print(current_quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="ashwathrox123@gmail.com",
            msg=f"Subject: Quotes made!\n\n{current_quote}"
        )