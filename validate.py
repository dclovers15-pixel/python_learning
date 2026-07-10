import re



email = input("Enter your email: ").strip()
if re.search (r"^\w+@(\w+\.)\w+\.(com|org|edu|gov)$", email, re.IGNORECASE): 
    print("Valid")
else:
    print("Invalid")
