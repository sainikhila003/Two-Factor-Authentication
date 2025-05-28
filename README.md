# 🔐 Two-Factor Authentication (2FA) System

A simple implementation of Two-Factor Authentication (2FA) to enhance login security by requiring a second verification step using Time-based One-Time Passwords (TOTP).

## 🚀 Features

- Supports TOTP-based 2FA compatible with Google Authenticator or Authy
- Generates and verifies one-time passwords
- Provides QR code for easy setup on authenticator apps
- Simple command-line interface (can be extended to web apps)
- Optional backup codes for recovery

## 🛠️ Technologies Used

- Python 3
- `pyotp` for TOTP generation and verification
- `qrcode` for QR code generation
- `Pillow` for image handling (QR code)

## 📦 Requirements

Install dependencies:

```bash
pip install pyotp qrcode[pil]

