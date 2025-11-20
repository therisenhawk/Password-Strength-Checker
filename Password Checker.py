def check_password_strength(password):
    length = len(password)  # Shows the length of a password as integer

    # Checking if password contains any upper, lower, special characters or a number
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    has_special = any(char in special_characters for char in password)

    # Calculate score
    score = 0

    # Length points
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Character type points
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Convert score to a label
    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    elif score == 5:
        strength = "Strong"
    else:  # score == 6
        strength = "Very strong"

    # Adding suggestions to a password
    suggestions = []

    if length < 8:
        suggestions.append("Password should be at least 8 characters.")
    if not has_lower:
        suggestions.append("Password must contain at least one lowercase letter.")
    if not has_upper:
        suggestions.append("Password must contain at least one uppercase letter.")
    if not has_digit:
        suggestions.append("Password must contain at least one digit.")
    if not has_special:
        suggestions.append("Password must contain at least one special character (e.g. !, @, #, $).")

    return strength, suggestions


def main():

    
    print("Type 'q' to quit.\n")

    while True:
        password = input("Enter a password to check (or 'q' to quit): ")

        if password.lower() == "q":
            print("\nGoodbye!")
            break  # break if user types q

        strength, suggestions = check_password_strength(password)
        print(f"\nPassword strength: {strength}")

        if suggestions:
            print("\nSuggestions to improve your password:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print("Your password looks strong!")

        print()  # blank line before next round


if __name__ == "__main__":
    main()
