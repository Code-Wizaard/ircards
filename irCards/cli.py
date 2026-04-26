import sys
from .card_utils import CardValidator
from .iban_utils import IbanValidator

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m Banker.cli <type: card|iban> <value>")
        return

    ctype, val = sys.argv[1], sys.argv[2]
    if ctype == "card":
        info = CardValidator(val).get_info()
        for index, value in info.items():
            print(index + " : " + str(value))
    elif ctype == "iban":
        info = IbanValidator(val).get_info()
        for index, value in info.items():
            print(index + " : " + str(value))

if __name__ == "__main__":
    main()
