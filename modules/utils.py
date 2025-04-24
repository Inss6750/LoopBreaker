import time
import random
import requests

def random_delay(min_sec=1, max_sec=3):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def rotate_ip(proxy_api_url=None):
    """
    Placeholder for IP rotation via proxy provider API.
    Example: Smartproxy, BrightData, etc.
    """
    if proxy_api_url:
        try:
            response = requests.get(proxy_api_url)
            if response.status_code == 200:
                print("[*] IP rotated via proxy provider.")
            else:
                print("[!] Proxy API call failed.")
        except Exception as e:
            print(f"[!] IP rotation error: {e}")
    else:
        print("[!] No proxy API URL specified. Skipping IP rotation.")

def log(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")