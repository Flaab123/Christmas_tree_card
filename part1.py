while True:
  lines = input("What should be the height of christmas tree Y?")
  if lines.isnumeric():
    if int(lines) < 3:
      print("Please input a minimum height of 3")
    else:
      break
  else:
    print("Input is not a number!")


tree = [((int(lines)-i-1)*" " + (2*int(i)+1)*"*" + (int(lines)-i-1)*" ") for i in range(int(lines))]
output = "\n".join(tree)
print(output)
