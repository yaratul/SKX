import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def check_stripe_key(sk_key):
    url = "https://api.stripe.com/v1/charges"
    headers = {
        "Authorization": f"Bearer {sk_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(Fore.GREEN + "Valid Stripe Secret Key!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid Stripe Secret Key!" + Style.RESET_ALL)

def main():
    sk_key = input("Please enter the Stripe Secret Key (sk_live_...): ")
    check_stripe_key(sk_key)

if __name__ == "__main__":
    main()
