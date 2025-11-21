import smtplib

my_email = "miniash3127@gmail.com"
password = "" # get the password from the gmail app passwords section

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ashwathrox123@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )