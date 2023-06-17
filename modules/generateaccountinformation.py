
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import calendar
import mechanicalsoup
import string
import logging

from .config import Config
from .getIdentity import getRandomIdentity

USERNAME_FILE = "usernames.txt"

#generating a username
def username(identity):
    n = str(random.randint(1,99))
    name = str(identity).lower().replace(" ","")
    username = name + n
    logging.info("Username: {}".format(username))
    return(username)


#generate password
def generatePassword():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(12))

def generate_random_birthday():
    year = random.randint(1900, 2023)  # Generate a random year between 1900 and 2023
    month = random.randint(1, 12)  # Generate a random month between 1 and 12

    # Define the maximum number of days based on the selected month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        # Handle February with leap years
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28

    day = random.randint(1, max_day)  # Generate a random day based on the maximum for the month

    month_name = calendar.month_name[month]
    month_name = month_name.capitalize()

    birthday = (month_name, str(day), str(year))
    return birthday

def genEmail(username) :
    return ''.join(username + "@" + str(Config["email_domain"]))

def select_username(file_path):
    usernames = []
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        username = ""
        for i, line in enumerate(lines):
            username = line.strip()
            if username and not username.startswith('*'):
                lines[i] = '*' + line.lstrip('*')
                break
        file.seek(0)
        file.writelines(lines)
    return username
        
def new_account():
    account_info = {}
    #identity, gender, birthday = getRandomIdentity(country=Config["country"])
    username = select_username(USERNAME_FILE)
    account_info["username"] = username
    account_info["name"] = username.replace(".", " ")
    account_info["password"] = generatePassword()
    account_info["email"] = "eltifi.iyad@outlook.com"
    account_info["gender"] = random.choice(["male", "female"])
    
    birth_date = generate_random_birthday()
    account_info["birth_month"]= birth_date[0]
    account_info["birth_day"] = birth_date[1]
    account_info["birth_year"] = birth_date[2]
    
    return(account_info)
