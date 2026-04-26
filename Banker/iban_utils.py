import re

class IbanValidator:
    def __init__(self, iban):
        self.iban = re.sub(r'\s+', '', iban).upper()
        self.is_valid = self._validate()
        self.length = len(self.iban)
        self.masked_iban = self._mask_iban()

    def _validate(self):
        if not self.iban.startswith("IR") or len(self.iban) != 26:
            return False
        rearranged = self.iban[4:] + self.iban[:4]
        numerical_iban = ""
        for char in rearranged:
            if char.isdigit():
                numerical_iban += char
            else:
                numerical_iban += str(ord(char) - 55)
        try:
            return int(numerical_iban) % 97 == 1
        except ValueError:
            return False

    def _mask_iban(self):
        if len(self.iban) < 10:
            return self.iban
        return "IR" + "*" * (len(self.iban) - 6) + self.iban[-4:]

    def get_info(self):
        return {
            "iban": self.iban,
            "is_valid": self.is_valid,
            "masked_iban": self.masked_iban,
            "length": self.length,
        }