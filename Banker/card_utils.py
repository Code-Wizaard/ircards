from .banks_dict import banks_dict
import re

class CardValidator:
    def __init__(self, card_number):
        self.number = re.sub(r'\D', '', str(card_number))
        self.is_valid_luhn = self._validate_luhn()
        self.masked_number = self._mask_number()
        self.length = len(self.number)

    def _validate_luhn(self):
        total = 0
        alt = False
        for digit in reversed(self.number):
            x = int(digit)
            if alt:
                x *= 2
                if x > 9:
                    x -= 9
            total += x
            alt = not alt
        return total % 10 == 0

    def _mask_number(self):
        if len(self.number) < 10:
            return self.number
        return self.number[:6] + "*" * (len(self.number) - 10) + self.number[-4:]

    def get_info(self):
        return {
            "card_number": self.number,
            "is_valid": self.is_valid_luhn,
            "masked_card": self.masked_number,
            "length": self.length,
            "bank": self._get_bank_from_bin()
        }

    def _get_bank_from_bin(self):
        for prefix, name in banks_dict.items():
            if self.number.startswith(prefix):
                return name
        return "Unknown"
