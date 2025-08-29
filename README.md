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

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bloomy52/secure-password-generator.git
   cd secure-password-generator
   ```

2. **Word List Provided:**
   - The `words_alpha.txt` file is included and required for word-based password generation.
   - No additional download is required.

3. **Run the password generator:**
   ```bash
   python secure_pwgen.py
   ```

4. **Follow the prompts:**
   - Select your password type:
     - Alphanumeric
     - Alphabetic (words only)
     - Numeric
     - Completely random (ASCII)
   - Enter your desired length or number of words/digits as prompted.

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

- The selection menu and user prompts have been updated for clarity.
- The project structure has been organized for easier use and maintenance.
- Unused or deprecated files have been removed.

## WordNet Data Attribution

This project uses lexical data from [WordNet 3.0](https://wordnet.princeton.edu/).

The original WordNet database files include a license notice at the top of each file.  
For technical reasons, this license notice has been removed from the data files as used by the project.  
The full WordNet license is included in [licenses/WordNet-LICENSE.txt](licenses/WordNet-LICENSE.txt), and the accompanying README is in [licenses/WordNet-README.txt](licenses/WordNet-README.txt).

All use of the WordNet data is governed by the terms of that license.  
Any modifications to the data are not endorsed by Princeton University.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
