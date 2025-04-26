#🔐 Project 02: Password Strength Meter
#Password Generator: Add a feature to suggest a strong password.
#"User-Friendly Interface: Use Streamlit for a GUI version.
# Blacklist Common Passwords: Reject weak passwords like "password123".
# Custom Scoring Weights: Give different weights to complexity factors.
# Password Strength Meter: Provide a score based on complexity.
# Password History: Store previously used passwords and check against them.
# Password Expiration: Notify users when passwords are about to expire.
# Password Generator: Suggest a strong password
import streamlit as st

import random
import string
import re
def check_password_strength(password):
    score = 0
    # Check length
    if len(password) >= 8:
        score += 1
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{})', password):
        score += 1
    # Check for common passwords
    common_passwords = ["password123", "12345678", "qwerty", "abc123", "letmein"]
    if password in common_passwords:
        score -= 1
    # Check for previously used passwords
    # This is a placeholder. In a real application, you would check against a database.
    
    


    