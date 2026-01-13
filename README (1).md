# Password Strength Checker 🔐

A simple Python tool that evaluates the strength of passwords and provides helpful feedback.

## Features

- ✅ Checks password length
- ✅ Validates character complexity (uppercase, lowercase, numbers, special chars)
- ✅ Detects common passwords
- ✅ Provides actionable feedback
- ✅ Colorful emoji-based output
- ✅ Secure password input (hidden while typing)

## How to Run

```bash
python3 password_checker.py
```

## Password Scoring

The tool scores passwords out of 6 points:
- 1 point for being at least 8 characters
- 1 point for being at least 12 characters
- 1 point for lowercase letters
- 1 point for uppercase letters
- 1 point for numbers
- 1 point for special characters

**Strength Ratings:**
- 🔴 WEAK (0-2 points)
- 🟡 MODERATE (3-4 points)
- 🟢 STRONG (5-6 points)

## Example Usage

```
Enter a password to check: ********
==================================================
Password Strength: 🟢 STRONG
Score: 6/6
==================================================

✅ Excellent! Your password is strong!
```

## Requirements

- Python 3.6+
- No external dependencies required!

## Tips for Strong Passwords

- Use at least 12 characters
- Mix uppercase and lowercase letters
- Include numbers and special characters
- Avoid common words and patterns
- Don't reuse passwords across sites
