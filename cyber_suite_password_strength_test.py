# Decided to add comments due to size

# Define special characters
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"

print("===== PASSWORD STRENGTH CHECKER =====")
print("This tool analyzes your password and rates its strength.\n")

# Get password
password = input("Enter a password to check: ")

# Init counters
length = len(password)
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Analyze each character
for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char in SPECIAL_CHARS:
        special_count += 1

# Init score
score = 0

# Length (25 points max)
if length >= 12:
    score += 25
elif 8 <= length <= 11:
    score += 15
elif 6 <= length <= 7:
    score += 10
else:
    score += 0

# Character variety (60 points max)
if upper_count > 0:
    score += 15
if lower_count > 0:
    score += 15
if digit_count > 0:
    score += 15
if special_count > 0:
    score += 15

# Character type diversity bonus (15 points max)
types_used = sum([upper_count > 0, lower_count > 0, digit_count > 0, special_count > 0])
if types_used >= 3:
    score += 15

# Determine strength
if score >= 80:
    strength = "STRONG"
elif score >= 60:
    strength = "MODERATE"
elif score >= 40:
    strength = "WEAK"
else:
    strength = "VERY WEAK"

# Output analysis
print("\n===== PASSWORD ANALYSIS =====")
print(f"Length: {length} characters")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")

print(f"\nSecurity Score: {score}/100")
print(f"Strength Assessment: {strength}")

# Improvement suggestions
print("\n===== IMPROVEMENT SUGGESTIONS =====")
if length < 12:
    print("- Use at least 12 characters for better security")
if upper_count == 0:
    print("- Add uppercase letters (A-Z)")
if lower_count == 0:
    print("- Add lowercase letters (a-z)")
if digit_count == 0:
    print("- Add numbers (0-9)")
if special_count == 0:
    print("- Add special characters (!@#$%^&*)")
else:
    print("- Excellent password! Remember to use different passwords for different accounts.")