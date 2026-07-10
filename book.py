def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()
    
    chapter1 = contents[53:272]
        
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
        
main() 
git config --global user.email "dclovers15@gmail.com "
git config --global user.name "2real"