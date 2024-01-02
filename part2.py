while True:
  lines = input("What should be the height of christmas tree Y?")
  if lines.isnumeric():
    if int(lines) < 3:
      print("Please input a minimum height of 3")
    else:
      break
  else:
    print("Input is not a number!")
    
width = int(lines)*2-1
height = int(lines) + 2

def christmas_tree(width,height):
  tree = []
  mid_index = int((width-1)/2)
  for i in range(height):
    treeline = [' ']*width
    if i == 0:    #Star on top of the tree
      treeline[mid_index] = 'X'
    elif i == 1:  #Tip of the tree
      treeline[mid_index] = '^'
    elif i == height-1:   #Stem of the tree
      treeline[mid_index - 1] = '|'
      treeline[mid_index + 1] = '|'
    else: 
      line_number = i-2
      left_edge = int(mid_index-(1+line_number))
      right_edge = int(mid_index+(1+line_number))
      treeline[left_edge] = '/'
      treeline[right_edge] = '\\'
      treeline[left_edge+1:right_edge] = '*' * (right_edge-left_edge-1)
    tree.append(treeline)
  
  return tree


tree = christmas_tree(width,height)
output = '\n'.join(map(''.join, tree))
print(output)
