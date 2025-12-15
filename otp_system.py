import random
import time
from getpass import getpass

MAX_RETRIES = 3

def generate_otp():
    return random.randint(100000, 999999)

def send_otp(email, otp):
    print(f"\nSending OTP to {email}...")
    time.sleep(1)
    print("(Simulation) OTP sent successfully!")

def get_user_otp():
    return getpass("Enter the 6-digit OTP: ")

def verify_otp(generated_otp, entered_otp):
    return str(generated_otp) == entered_otp

def otp_verification_flow():
    print("Welcome to OTP Verification System")
    email = input("Enter your email address: ").strip()

    otp = generate_otp()
    send_otp(email, otp)

    attempts = 0
    while attempts < MAX_RETRIES:
        entered_otp = get_user_otp()
        if verify_otp(otp, entered_otp):
            print("OTP verified successfully. Access granted.")
            return
        else:
            attempts += 1
            print("Incorrect OTP")

    print("Access denied.")

if __name__ == "__main__":
    otp_verification_flow()
9+
