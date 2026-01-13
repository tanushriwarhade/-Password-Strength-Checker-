#!/usr/bin/env python3
"""
Password Strength Checker
A simple tool to evaluate password security
"""

import re
import getpass


class PasswordChecker:
    def __init__(self):
        self.common_passwords = [
            'password', '123456', '12345678', 'qwerty', 'abc123',
            'monkey', '1234567', 'letmein', 'trustno1', 'dragon'
        ]
    
    def check_strength(self, password):
        """Evaluate password strength and return score and feedback"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters")
        
        if len(password) >= 12:
            score += 1
        
        # Complexity checks
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Add special characters (!@#$%^&*)")
        
        # Common password check
        if password.lower() in self.common_passwords:
            score = 0
            feedback.insert(0, "WARNING: This is a commonly used password!")
        
        return score, feedback
    
    def get_strength_label(self, score):
        """Return strength label based on score"""
        if score <= 2:
            return "WEAK"
        elif score <= 4:
            return "MODERATE"
        else:
            return "STRONG"
    
    def display_result(self, password, score, feedback):
        """Display the password strength analysis"""
        strength = self.get_strength_label(score)
        
        print("\n" + "="*50)
        print(f"Password Strength: {strength}")
        print(f"Score: {score}/6")
        print("="*50)
        
        if feedback:
            print("\nSuggestions to improve your password:")
            for tip in feedback:
                print(f"   {tip}")
        else:
            print("\nExcellent! Your password is strong!")
        print()


def main():
    print("Password Strength Checker")
    print("-" * 50)
    
    checker = PasswordChecker()
    
    while True:
        try:
            # Use getpass to hide password input
            password = getpass.getpass("\nEnter a password to check (or 'quit' to exit): ")
            
            if password.lower() == 'quit':
                print("\nGoodbye! Stay secure!")
                break
            
            if not password:
                print("Please enter a password")
                continue
            
            score, feedback = checker.check_strength(password)
            checker.display_result(password, score, feedback)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! Stay secure!")
            break


if __name__ == "__main__":
    main()
