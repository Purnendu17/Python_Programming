a=int(input("Enter hours worked in a week: "))
b=int(input("Enter hourly wage: "))
if a<=40:
    print("Regular Pay:",a*b)
else:
    c=a-40
    d=150*b*c/100
    e=40*b
    print("Regular Pay:",e)
    print("Overtime Pay:", d)
    print("Total Pay:", d+e)