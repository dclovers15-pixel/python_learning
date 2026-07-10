import csv 

name = input("Enter your name: ")
house = input("Enter your house: ")
 

with open("student.tes.csv", "a") as file:
     writer = csv.DictWriter(file , fieldnames=["name", "house"])
     writer.writerow({"name": name, "house": house})