import string
from random import *
import time
import csv
from faker import Faker
x = 0
#choose how many emails you wanna to be created 
while x < 1000:
    characters = string.ascii_letters + string.digits  # string.punctuation
    # string.digits  # string.punctuation
    characters2 = string.ascii_letters.lower()
    fake = Faker('en_CA')
    i = ""
    i = fake.name().strip()

    email = "".join(i.strip()) + "@gmail.com"
    email = email.replace(" ", "").lower()
    #email = "'" + f'{email}' + "'" + ", "

    password = "".join(choice(characters) for x in range(randint(8, 12)))

    print(f"GMAIL Email {x}:  {email}")
    print(f"Password {x}:  {password}")
    print("-----------------------------------------------------")

    ls = []
    ls.append([email.strip(), password])

    #put your file location to be created
    with open("/Users/Matrix10/Downloads/Projects/1files/gmail.csv", "a", newline='', encoding='utf-8-sig') as file:
        wr = csv.writer(file)
        # delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL
        #wr.writerow(["EMAIL GMAIL", "PASSWORD"])
        wr.writerows(ls)

    x += 1
    time.sleep(0)
