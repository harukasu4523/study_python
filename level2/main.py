str = input().split()
if len(str) != 3:
  print("引数の数は３にしてください")
  exit()

num1 = float(str[0])
op = str[1]
num2 = float(str[2])

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