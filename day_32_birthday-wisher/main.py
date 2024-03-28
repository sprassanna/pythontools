##################### Extra Hard Starting Project ######################
import datetime

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
birthday = pd.read_csv('./birthdays.csv')

my_email = ''
my_password = ''

to_email= ''

matching_record = birthday[birthday['day'] == now.day]
actual_name = (', '.join(matching_record['name']))

any_num = random.randint(1,3)

to_be_sent_letter = f'letter_{any_num}.txt'

with open(f'./letter_templates/{to_be_sent_letter}','r') as letter_file:
    content = letter_file.read()
    replaced_content = content.replace('[NAME]',actual_name)

    print(replaced_content)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as connection:
        connection.login(user=my_email,password=my_password)

        connection.sendmail(from_addr=my_email,to_addrs=to_email,msg=f'Subject: Happy Birthday \n\n {replaced_content}')







