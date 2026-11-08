
import secrets
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):

    character_groups = []

    if use_lower:
        character_groups.append(string.ascii_lowercase)

    if use_upper:
        character_groups.append(string.ascii_uppercase)

    if use_digits:
        character_groups.append(string.digits)

    if use_symbols:
        character_groups.append("!@#$%^&*()-_=+[]{}?")

    if not character_groups:
        raise ValueError("Select at least one character type.")

    if length < len(character_groups):
        raise ValueError(
            "Password length must be at least the number of selected types."
        )

    # Ensure at least one character from every selected type
    password_chars = [
        secrets.choice(group) for group in character_groups
    ]

    # Combine all selected character types
    all_characters = "".join(character_groups)

    # Fill the remaining password length
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_characters))

    # Shuffle the characters securely
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():

    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be positive.")
            return

        print("\nSelect character types (y/n):")

        use_lower = input("Include lowercase letters? ").lower() == "y"
        use_upper = input("Include uppercase letters? ").lower() == "y"
        use_digits = input("Include numbers? ").lower() == "y"
        use_symbols = input("Include symbols? ").lower() == "y"

        password = generate_password(
            length,
            use_lower,
            use_upper,
            use_digits,
            use_symbols
        )

        print("\n========== RESULT ==========")
        print("Generated Password:", password)
        print("============================")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
