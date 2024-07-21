str = input().split()
if len(str) != 3:
  print("引数の数は３にしてください")
  exit()

def digit_check(num):
  for i in range(len(num)):
    if num[0] == '-':
      continue
    if num[i].isdigit():
      continue
    else:
     print("整数のみ入力してください")
     exit()
  return int(num)

num1 = digit_check(str[0])
op = str[1]
num2 = digit_check(str[2])


if op == '+':
 print(int(num1 + num2))
elif op == '-':
 print(int(num1 - num2))
  
elif op == '*':
 print(int(num1 * num2))
elif op == '/':
  if num2 == 0:
    print("0では割れません")
    exit()
  print(int(num1 / num2))
else :
  print("+ - * / の演算子の中から１つを使用してください")
