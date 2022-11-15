issuers = {
    "Visa":                 { "length": [13, 16],       "iin": [4]},
    "American Express":     { "length": [15],           "iin": [34, 37]},
    "MasterCard":           { "length": [16],           "iin": [i for i in range(51, 56)]},
    }

mii = {
    0:	"ISO/TC 68 and other industry assignments",
    1:	"Airlines",
    2:	"Airlines, financial and other future industry assignments",
    3:	"Travel and entertainment",
    4:	"Banking and financial",
    5:	"Banking and financial",
    6:	"Merchandising and banking/financial",
    7:	"Petroleum and other future industry assignments",
    8:	"Healthcare, telecommunications and other future industry assignments",
    9:	"For assignment by national standards bodies",
}


class CreditCard:
    def __init__(self, num: str) -> None:
        if num.isdigit():
            self.number = num
        else:
            print("Inserted card number is INVALID")


    def validate_checksum_luhn(self) -> bool:
        '''Validate card number using Luhn algorithm'''
        reversed_number = self.number[::-1]
        sum = 0

        for i in range(len(reversed_number)):
            temp = int(reversed_number[i]) * (2 if (i % 2) else 1)
            sum += int(temp) if int(temp) < 10 else int(temp) % 10 + 1
        
        if sum % 10 == 0:
            return True
        return False


    def check_issuer(self) -> str:
        '''
        Check which issuer issued the card\n
        iin - first 6 to 8 digits of a card number are knon as the issuer identification number. These identify the card issuing institution.
        '''
        for issuer in issuers:
            if len(self.number) in issuers[issuer]["length"]:
                for i in range(8):
                    temp = int(self.number[:i + 1])
                    if temp in issuers[issuer]["iin"]:
                        return issuer
        return "Unknown issuer"


    def check_industry(self) -> str:
        return mii[int(self.number[0])]