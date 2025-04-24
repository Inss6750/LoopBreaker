from modules.browser import get_browser
from modules.account_gen import generate_account
from modules.bonus_logic import claim_bonus, simulate_play

def run():
    print("[] Starting LoopBreaker...")

    account = generate_account()
    driver = get_browser()

    try:
        claim_bonus(driver, account)
        simulate_play(driver)
    finally:
        driver.quit()
        print("[] Session ended.")

if name == "main":
    run()