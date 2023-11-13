string = input('Sisesta tekst:')
vowels = 0

for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='õ' or i=='ä' or i=='ö' or i=='ü' ):
            vowels=vowels+1

print(vowels)
