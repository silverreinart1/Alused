a = float(input("Sisesta A"))
b = float(input("Sisesta B"))
c = float(input("Sisesta C"))
if a + b > c and c + b > a and c + a > b:
    if a == b and b == a and c == a:
        print("ON võrdkülgne")
    elif a == b or b == c or c == a:
        print("ON")
else:
    print("Pole olemas")
