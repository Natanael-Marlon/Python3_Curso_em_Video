n1 = int(input('Diga um numero '))
n2 = int(input('Diga mais um numero '))
n3 = int(input('Diga e mais um numero '))
if(n1 > n2 and n1 > n3): 
  print('{} é maior {} e {}'.format(n1,n2,n3))
  if(n2 > n3):
    print('{} é maior {}'.format(n2,n3))
    print('{} é menor'.format(n3))
  else:
    print('{} é maior {}'.format(n3,n2))
    print('{} é menor'.format(n2))
else:
  if(n2 > n1 and n2 > n3): 
    print('{} é maior {} e {}'.format(n2,n1,n3))
    if(n1 > n3):
      print('{} é maior {}'.format(n1,n3))
      print('{} é menor'.format(n3))
    else:
      print('{} é maior {}'.format(n3,n1))
      print('{} é menor'.format(n1))
  else:
    if(n3 > n1 and n3 > n2): 
      print('{} é maior {} e {}'.format(n3,n1,n2))
      if(n1 > n2):
        print('{} é maior {}'.format(n1,n2))
        print('{} é menor'.format(n2))
      else:
        print('{} é maior {}'.format(n2,n1))
        print('{} é menor'.format(n1))
    else:
      print('{} é menor'.format(n2))