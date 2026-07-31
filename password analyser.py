print("=" * 45)
print("     PASSWORD STRENGTH ANALYZER")
print("=" * 45)

# Get password from user
password = input("Enter your password: ")

# Flags
uppercase_found = False
lowercase_found = False
digit_found = False
special_found = False

# Check every character
for character in password:

    if character.isupper():
        uppercase_found = True

    if character.islower():
        lowercase_found = True

    if character.isdigit():
        digit_found = True

    if not character.isupper() and not character.islower() and not character.isdigit():
        special_found = True

# Display analysis
print("\nPassword Analysis")
print("-" * 25)

print("Length >= 8 :", len(password) >= 8)
print("Uppercase   :", uppercase_found)
print("Lowercase   :", lowercase_found)
print("Digit       :", digit_found)
print("Special Char:", special_found)

# Display strength
if len(password) < 8:
    print("\nPassword Strength : WEAK")

elif uppercase_found and lowercase_found and digit_found and special_found:
    print("\nPassword Strength : STRONG")

else:
    print("\nPassword Strength : MEDIUM")