import requests
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def check_stripe_key(sk_key):
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

    print("\nVerifying Stripe Secret Key Abilities:\n")

    for test_name, url in tests.items():
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "✓ " + Style.RESET_ALL + f"{test_name} - Valid and Accessible")
        elif response.status_code == 401:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Unauthorized (Invalid or expired key)")
        elif response.status_code == 403:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Forbidden (Insufficient permissions)")
        else:
            print(Fore.RED + "✗ " + Style.RESET_ALL + f"{test_name} - Inaccessible (Error code: {response.status_code})")

def main():
    sk_key = input("Please enter the Stripe Secret Key (sk_live_...): ")
    check_stripe_key(sk_key)

if __name__ == "__main__":
    main()
