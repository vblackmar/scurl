yes = input()
code = list(yes)
stack = []
def stack1():
  return(int(stack[-1]))
def stack2():
  return(int(stack[-2]))
for x in code:
  if x == "I" or x == "i":
    stack.append(10)
  elif x == "Z" or x == "z":
    stack.append(20)
  elif x == "E" or x == "e":
    stack.append(30)
  elif x == "A" or x == "a":
    stack.append(40)
  elif x == "S" or x == "s":
    stack.append(50)
  elif x == "G" or x == "g":
    stack.append(60)
  elif x == "T" or x == "t":
    stack.append(70)
  elif x == "O" or x == "o":
    stack.append(80)
  elif x == "N" or x == "n":
    stack.append(90)
  elif x == "+":
    stack.append(stack2() + stack1())
  elif x == "-":
    stack.append(stack2() - stack1())
  elif x == "*":
    stack.append(stack2() * stack1())
  elif x == "/":
    stack.append(stack2() / stack1())
  elif x == "P" or x == "p":
    print(stack1())
  elif x.isspace():
    continue
  elif x.isdigit() and len(x) == 1:
    stack.append(x)
  else:
    print(f"What is {x}?")
    break
