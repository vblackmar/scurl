yes = input()
code = list(yes)
stack = []
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
