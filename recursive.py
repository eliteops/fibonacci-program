def fact(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fact(num-2)+fact(num-1)
    
n = int(input())
for i in range(n):
  print(fact(i))
