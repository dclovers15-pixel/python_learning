import re

name = input("Enter your name: ").strip()
match = re.search(r"^(.+), (.+)$", name)
if match:
    last, first = match.groups()
    name = f"{first} {last}"
    print(f"hello, {name}")
      
