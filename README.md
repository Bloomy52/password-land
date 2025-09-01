# Secure Password Generator

A flexible and interactive command-line utility for generating strong, customizable passwords in Python.

## Features

- **Alphanumeric Passwords:** Combine random words, numbers, and punctuation for strong, memorable passwords.
- **Word-Only Passwords:** Create passphrases using multiple random words (default 4+).
- **Numeric Passwords:** Generate secure numeric codes (default 8+ digits).
- **Random ASCII Passwords:** Fully random combinations of letters, numbers, and symbols.
- **Customizable Lengths:** Choose password or passphrase length based on type.
- **Uses Secure Randomization:** Relies on Python's `secrets` and `random` modules for robust entropy.
- **Easy to Use:** Interactive command-line interface guides you through options.

## Requirements

- Python 3.x
- `words_alpha.txt` (included in the repository for word-based passwords)

## Quick Start (Recommended for Most Users)

**Download the latest version:**

1. Go to the [Releases page](https://github.com/Bloomy52/secure-password-generator/releases).
2. Download the latest release zip file.
3. Extract the zip file to a folder on your computer.

**Run the password generator:**
```bash
python secure_pwgen.py
```

**Follow the prompts:**
- Select your password type:
  - Alphanumeric
  - Alphabetic (words only)
  - Numeric
  - Completely random (ASCII)
- Enter your desired length or number of words/digits as prompted.

## For Developers or Advanced Users

If you prefer, you can clone the repository:
```bash
git clone https://github.com/Bloomy52/secure-password-generator.git
cd secure-password-generator
python secure_pwgen.py
```

## Example

```
Welcome to the Secure Password Generator!
To Begin, please select the type of password you would like using a num-pad/num-row on your keyboard.
Alphanumeric Password: 1
Alphabetic Password: 2
Numeric Password: 3
Completely Random Password: 4
1
This password will contain words, numbers, and punctuation.
<Your generated password will appear here>
```

## Latest Changes

- Removed default parameters from word-only, numeric, and ASCII password generation functions.
- Removed default parameter references from docstrings.
- Removed unnecessary comment near importing modules area.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
