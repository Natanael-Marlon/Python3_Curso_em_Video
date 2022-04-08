import random
ale = random.randint(1,5) , random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5)
mai = 0
men = 5
for c in range(0,len(ale) ):
  print(f' {ale[c]}')
  if ale[c] > mai:
    mai = ale[c]
  if ale[c]< men :
    men = ale[c]
print(f'o maior {mai} e o menor {men}')