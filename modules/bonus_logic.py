import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

def claim_bonus(driver, account):
    print("[] Claiming bonus...")

    try:
        driver.get("https://example-casino.com/signup")  # ← Replace with actual casino URL
        time.sleep(random.uniform(2, 4))

        driver.find_element(By.NAME, "first_name").send_keys(account["first_name"])
        driver.find_element(By.NAME, "last_name").send_keys(account["last_name"])
        driver.find_element(By.NAME, "email").send_keys(account["email"])
        driver.find_element(By.NAME, "password").send_keys(account["password"])
        driver.find_element(By.NAME, "birthdate").send_keys(account["birthdate"])
        driver.find_element(By.NAME, "country").send_keys(account["country"])
        time.sleep(random.uniform(1, 2))

        driver.find_element(By.ID, "signup-button").click()
        print("[+] Signup submitted.")

    except Exception as e:
        print(f"[!] Error during bonus claim: {e}")

def simulate_play(driver):
    print("[] Simulating play...")

    try:
        time.sleep(random.uniform(3, 6))
        # Mimic simple user interaction like scrolling or clicking
        for _ in range(random.randint(1, 3)):
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(random.uniform(0.5, 1.5))

        print("[+] Simulated play complete.")
    except Exception as e:
        print(f"[!] Error during simulated play: {e}")