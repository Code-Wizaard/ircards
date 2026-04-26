Here's a comprehensive `README.md` for your irCards package:

```markdown
# irCards

A Python package for validating Iranian bank cards and IBANs.

## Features

- **Card Validation**: Validate bank card numbers using Luhn algorithm
- **Bank Identification**: Identify the bank from card BIN (Bank Identification Number)
- **IBAN Validation**: Validate Iranian IBANs (International Bank Account Numbers)
- **Card Masking**: Securely mask card numbers for display
- **IBAN Masking**: Mask IBANs while preserving bank identifier and last 4 digits
- **CLI Interface**: Command-line interface for quick validation

## Installation

```bash
pip install irCards
```

## Usage

### Python API

#### Card Validation

```python
from irCards import CardValidator

# Validate a card
card = CardValidator("6037991234567890")
info = card.get_info()

print(info)
# Output:
# {
#     "card_number": "6037991234567890",
#     "is_valid": True,
#     "masked_card": "603799******7890",
#     "length": 16,
#     "bank": "بانک ملی ایران"
# }
```

#### IBAN Validation

```python
from irCards import IbanValidator

# Validate an IBAN
iban = IbanValidator("IR820540102680020817909002")
info = iban.get_info()

print(info)
# Output:
# {
#     "iban": "IR820540102680020817909002",
#     "is_valid": True,
#     "masked_iban": "IR**************9002",
#     "length": 26
# }
```

### CLI Usage

After installation, you can use the command-line interface:

```bash
# Validate a card
python -m irCards.cli card 6037991234567890

# Validate an IBAN
python -m irCards.cli iban IR820540102680020817909002
```

Example output:
```
card_number : 6037991234567890
is_valid : True
masked_card : 603799******7890
length : 16
bank : بانک ملی ایران
```

## API Reference

### CardValidator

#### Parameters
- `card_number` (str|int): The card number to validate

#### Methods

| Method | Description |
|--------|-------------|
| `get_info()` | Returns a dictionary with card information |
| `_validate_luhn()` | Internal method implementing Luhn algorithm |
| `_mask_number()` | Internal method for card number masking |

#### Return Values from `get_info()`

| Key | Description |
|-----|-------------|
| `card_number` | The original card number |
| `is_valid` | Boolean indicating if card passes Luhn check |
| `masked_card` | Masked version (first 6, last 4 digits visible) |
| `length` | Length of the card number |
| `bank` | Bank name in Persian (or "Unknown") |

### IbanValidator

#### Parameters
- `iban` (str): The IBAN to validate

#### Methods

| Method | Description |
|--------|-------------|
| `get_info()` | Returns a dictionary with IBAN information |

#### Return Values from `get_info()`

| Key | Description |
|-----|-------------|
| `iban` | The original IBAN |
| `is_valid` | Boolean indicating if IBAN is valid |
| `masked_iban` | Masked version (preserves "IR" and last 4 digits) |
| `length` | Length of the IBAN |

## Validation Rules

### Card Validation
- Uses **Luhn algorithm** (mod 10 algorithm)
- Automatically removes any non-digit characters
- Identifies bank from the first 6 digits (BIN)
- Minimum length: 8 digits (for masking logic)

### IBAN Validation
- Country code must be "IR" (Iran)
- Length must be exactly 26 characters
- Implements **MOD 97 algorithm** (ISO 7064)
- Removes spaces and converts to uppercase automatically

## Supported Banks

The package includes BIN (Bank Identification Number) prefixes for all major Iranian banks including:
- بانک ملی ایران (603799)
- بانک ملت (610433)
- بانک صادرات (603769)
- بانک تجارت (585983)
- And more...

*See `banks_dict.py` for the complete list.*

## Requirements

- Python 3.7+

## Development

### Setup for Development

```bash
# Clone the repository
git clone https://github.com/yourusername/irCards.git
cd irCards

# Install in development mode
pip install -e .

# Or with build tools
pip install build
python -m build
```

### Running Tests

```bash
python -m unittest discover tests
```

## License

[Add your license here - MIT, GPL, etc.]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

[Your Name]

## Version History

- **1.0.0** - Initial release
  - Card validation with Luhn algorithm
  - IBAN validation for Iran
  - Bank identification from BIN
  - CLI interface

## Notes

- Card numbers are validated only syntactically (Luhn algorithm), not against a live database
- Bank identification is based on known BIN prefixes and may not cover all banks
- Always use masked versions when displaying card numbers or IBANs in UI/logs
```

This README provides:
- Clear installation instructions
- Usage examples for both Python API and CLI
- Complete API reference
- Validation rules explanation
- Security notes about masking
- Development setup instructions

You can customize it with your actual GitHub repository URL, license, version number, and author information.