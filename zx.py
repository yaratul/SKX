import requests
import logging
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for colored output
init(autoreset=True)

# Set up logging
logging.basicConfig(filename='stripe_key_check.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def detect_key_type(sk_key):
    if sk_key.startswith("sk_live"):
        return "Live Key"
    elif sk_key.startswith("sk_test"):
        return "Test Key"
    else:
        return "Unknown Key Type"

def check_stripe_key(sk_key):
    key_type = detect_key_type(sk_key)
    logging.info(f"Checking {key_type}: {sk_key}")
    print(f"\nKey Type Detected: {Fore.YELLOW}{key_type}{Style.RESET_ALL}\n")

    tests = {
        "Charges Access": "https://api.stripe.com/v1/charges",
        "Customers Access": "https://api.stripe.com/v1/customers",
        "Refunds Access": "https://api.stripe.com/v1/refunds",
        "Balance Access": "https://api.stripe.com/v1/balance",
        "Payment Intents Access": "https://api.stripe.com/v1/payment_intents",
        "Cards Access": "https://api.stripe.com/v1/payment_methods?type=card",
        "Disputes Access": "https://api.stripe.com/v1/disputes",
    }

    headers = {
        "Authorization": f"Bearer {sk_key}"
    }

    passed = 0
    failed = 0

    print("Verifying Stripe Secret Key Abilities:\n")

    for test_name, url in tests.items():
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "✓ " + Style.RESET_ALL + f"{test_name} - Valid and Accessible")
            logging.info(f"{test_name}: Passed")
            passed += 1
        elif response.status_code == 401:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Unauthorized (Invalid or expired key)")
            logging.warning(f"{test_name}: Unauthorized (Invalid or expired key)")
            failed += 1
        elif response.status_code == 403:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Forbidden (Insufficient permissions)")
            logging.warning(f"{test_name}: Forbidden (Insufficient permissions)")
            failed += 1
        else:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Inaccessible (Error code: {response.status_code})")
            logging.error(f"{test_name}: Inaccessible (Error code: {response.status_code})")
            failed += 1

    print("\nSummary Report:")
    print(f"Total Checks: {passed + failed}")
    print(Fore.GREEN + f"✓ Passed: {passed}")
    print(Fore.RED + f"✗ Failed: {failed}")
    logging.info(f"Summary: Total Checks - {passed + failed}, Passed - {passed}, Failed - {failed}")

def main():
    sk_key = input("Please enter the Stripe Secret Key (sk_live_...): ")
    check_stripe_key(sk_key)

if __name__ == "__main__":
    main()
