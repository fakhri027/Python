print('##  Program Python Triangle type 1  ##')
print('=======================================')
print()
 
tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()
 
for i in range(tinggi_segitiga):
  for j in range(i+1):
    print(' *',end='')
  print()