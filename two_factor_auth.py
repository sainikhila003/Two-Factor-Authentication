import pyotp
import getpass
import time

# Simulated user database
users = {
    "alice": {
        "password": "password123",
        "otp_secret": pyotp.random_base32()
    }
}

def login():
    username = input("Username: ")
    if username not in users:
        print("User not found!")
        return False

    password = getpass.getpass("Password: ")
    if password != users[username]["password"]:
        print("Incorrect password!")
        return False

    totp = pyotp.TOTP(users[username]["otp_secret"])
    otp_input = input("Enter the 6-digit OTP from your authenticator app: ")

    if totp.verify(otp_input):
        print("✅ Login successful!")
        return True
    else:
        print("❌ Invalid OTP!")
        return False

if __name__ == "__main__":
    print("=== Two-Factor Authentication System ===\n")
    login()
