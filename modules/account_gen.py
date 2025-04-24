from faker import Faker
import random

fake = Faker()

def generate_account():
    account = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "birthdate": fake.date_of_birth(minimum_age=21, maximum_age=65).strftime("%Y-%m-%d"),
        "country": fake.country_code(representation="alpha-2")
    }

    print(f"[*] Generated account: {account['email']} ({account['country']})")
    return account