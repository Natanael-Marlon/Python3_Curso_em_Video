nums = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
num  = int(input('Digite um numero ate 20: '))
if(num <= 20 ):
  cont = num
  for cont in range(0 ,len(nums)):
    print(f'{nums[cont]}')

