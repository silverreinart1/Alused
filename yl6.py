a = input("Sisesta A: ")
b = input("Sisesta B: ")
c = input("Sisesta C: ")

if int(a) < int(b)and int(a)> int(c):
    print("a", a)
elif int(b) > int(c):
    print("b", b)
else:
    print("c", c)
