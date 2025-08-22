
f = open("/Users/Avani Gupta/11scie.csv")
import csv
with open("11scie.csv","r")as file:
  reader=csv.reader(file)
  for row in reader:
      print(row)