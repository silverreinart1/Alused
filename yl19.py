string = input('Sisesta tekst:')
count = 0
vowels = ["a","e","i","o","u","õ","ä","ö","ü"]

for i in string.lower():
      if i in vowels:
            count += 1

print(count)
