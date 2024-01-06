import random
import string
from datetime import date, timedelta

def generate_random_name():
    first_names = ["John", "Jane", "Michael", "Emma", "Christopher", "Olivia", "William", "Sophia", "James", "Ava", "Peter", "Kelly", "Victoria", "Evelyn", "Janice", "Sara", "Julia", "Charlotte", "Albert", "Philip", "Mason"]
    family_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Perez", "Thompson", "Harris", "Clark", "Torres", "Lopez", "Gonzalez", "Campbell", "Rivera", "Carter", "Flores"]

    random_first_name = random.choice(first_names)
    random_family_name = random.choice(family_names)

    return random_first_name, random_family_name

def generadorNumero(HowManyNumbersDoyouWant):     # number
    numerosRandoms = ""
    numeroRandom = ""

    for i in range(HowManyNumbersDoyouWant):
        numeroRandom = random.randint(0, 21)
        numerosRandoms += str(numeroRandom)

    return numerosRandoms

def generate_random_birthday():     # date birthday
    start_date = date(1950, 1, 1)
    end_date = date(2000, 12, 31)
    random_birthday = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_birthday.strftime("%d-%m-%Y")

def generadoremailsFakes(Domain, proxy):     # ISP hotmail or outlook
    random_first_name, random_family_name = generate_random_name()
    email = "{}.{}{}".format(random_first_name.lower(), random_family_name.lower(), generadorNumero(3))

    if Domain == "1":
        email += "@outlook.com"
    elif Domain == "2":
        email += "@hotmail.com"

    password = "".join(random.sample(pss, length))
    birthday = generate_random_birthday()

    print("{},{},{},{},{},US,{}".format(email, password, proxy, random_first_name, random_family_name, birthday))

def generarEmails(numerosEmails):      # Number proxy 'add all proxy do you want'
    Domain = input("Type the domain number you want 1:@outlook, 2:@hotmail: ")

    # add proxy here
    proxies =  """
94.154.162.187
94.154.162.188
94.154.162.189
94.154.162.190
94.154.162.191
    """

    proxy_list = [proxy.strip() for proxy in proxies.split("\n") if proxy.strip()]

    for i in range(0, numerosEmails):
        proxy = random.choice(proxy_list)
        generadoremailsFakes(Domain, proxy)

    return Domain

# Password Generator

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "@"

upper, lower, nums, syms = True, True, True, True

pss = ""

if upper:
    pss += uppercase_letters
if lower:
    pss += lowercase_letters
if nums:
    pss += digits
if syms:
    pss += symbols

length = 10

while True:
    amount = int(input("Enter the number of emails to generate: "))  # Adjust the number of emails as needed
    domain = generarEmails(amount)
    generate_more = input("Do you want to generate more emails? (yes/no): ".format(domain))
    if generate_more.lower() != 'yes':
        break
