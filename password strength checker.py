import re

def check_password_strength(password):
    score = 0

    # Length  
    if len(password) >= 8:  
        score += 1  

    # Digit  
    if re.search(r"\d", password):  
        score += 1  

    # Uppercase  
    if re.search(r"[A-Z]", password):  
        score += 1  

    # Lowercase  
    if re.search(r"[a-z]", password):  
        score += 1  

    # Special char  
    if re.search(r"\W", password):  
        score += 1  

    # Strength  
    if score >= 4:  
        return "Strong password"  
    elif score == 3:  
        return "Moderate password"  
    else:  
        return "Weak password"


password = input("Enter your password: ")
print(check_password_strength(password))
