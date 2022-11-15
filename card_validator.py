from credit_card import CreditCard

card_number = CreditCard(input("Please input credit card number: "))
print("This credit card number is VALID" if card_number.validate_checksum_luhn() else "INVALID")
print(f"This credit card's issuer is {card_number.check_issuer()}")
print(f"This credit card number belongs to the {card_number.check_industry()} industry")
