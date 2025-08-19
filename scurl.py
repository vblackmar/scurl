yes = input()
code = list(yes)
stack = []
def stack1():
  stack1 = stack[-1]
  stack.pop(-1)
  return(int(stack1))
def stack2():
  stack2 = stack[-2]
  stack.pop(-2)
  return(int(stack2))
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
    try:
        stack.append(stack2() + stack1())
    except IndexError:
        print("Not enough values on stack")
        break
  elif x == "-":
    try:
        stack.append(stack2() - stack1())
    except IndexError:
        print("Not enough values on stack")
        break
  elif x == "*":
    try:
        stack.append(stack2() * stack1())
    except IndexError:
        print("Not enough values on stack")
        break
  elif x == "/":
    try:
        stack.append(stack2() / stack1())
    except IndexError:
        print("Not enough values on stack")
        break
    except ZeroDivisionError:
        print("Cannot divide by zero")
        break
  elif x == "P" or x == "p":
    try:
        print(stack1())
    except IndexError:
        print("No value on stack to be printed")
        break
  elif x.isspace():
    continue
  elif x.isdigit() and len(x) == 1:
    stack.append(x)
  else:
    print(f"What is {x}?")
    break
