import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 2:
        strength = "WEAK ❌"
    elif score == 3 or score == 4:
        strength = "MEDIUM ⚠️"
    else:
        strength = "STRONG ✅"

    return strength, feedback


print("🔐 PASSWORD STRENGTH CHECKER 🔐")
print("-" * 35)

pwd = input("Enter your password: ")
strength, tips = check_password_strength(pwd)

print("\nPassword Strength:", strength)

if tips:
    print("\nSuggestions to improve:")
    for tip in tips:
        print("-", tip)
else:
    print("\nGreat! Your password is strong and secure 💪")