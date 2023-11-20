mina = {
  "Eesnimi": "Silver",
  "Perenimi": "Reinart",
  "Sünniaasta": "2007",
  "Elukoht": "Uduvere",
  "Lemmik magustoit": "Kook",
}

print(mina.get('Elukoht'))

mina['Lemmik magustoit'] = 'Kook'

mina['height'] = '1.80'

del mina['Sünniaasta']

mina.clear()

for s, r in mina.items():
    print(s, r)

#me['personal_code'] = '12345678910'

if 'personal_code' in mina:
    print(mina['Isikukood on dictionaris '])
else:
    print('Isikukood ei ole dictionaris')

print(len(mina))
