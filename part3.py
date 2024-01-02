while True:
  lines = input("What should be the height of christmas tree Y?")
  if lines.isnumeric():
    if int(lines) < 3:
      print("Please input a minimum height of 3")
    else:
      break
  else:
    print("Input is not a number!")
    
while True:
  interval = input("What should be the interval of the decorations?")
  if interval.isnumeric():
    if int(interval) < 1:
      print("Please input a minimum interval of 1")
    else:
      break
  else:
    print("Input is not a number!")    
    
width = int(lines)*2-1
height = int(lines)+2
interval = int(interval)

def christmas_tree(width,height):
  tree = []
  mid_index = int((width-1)/2)
  
  # Create base tree, without decorations
  for i in range(height):
    treeline = [' ']*width
    if i == 0:    #Star on top of the tree
      treeline[mid_index] = 'X'
    elif i == 1:  #Tip of the tree
      treeline[mid_index] = '^'
    elif i == height-1:   #Stem of the tree
      treeline[mid_index-1] = '|'
      treeline[mid_index+1] = '|'
    else: 
      line_number = i-2
      left_edge = int(mid_index-(1+line_number))
      right_edge = int(mid_index+(1+line_number))
      treeline[left_edge] = '/'
      treeline[right_edge] = '\\'
      treeline[left_edge+1:right_edge] = '*' * (right_edge-left_edge-1)
    tree.append(treeline)
  
  decorations_indices = range(1,int(((height-4)*(height-3)/2))+1)
  decorations_indices = [x for x in decorations_indices if (x-1) % interval == 0]
  prev_max_decorations = 0
  
  # Fill tree with decorations
  for i in range(3,height-1):
    mid_index = int((width-1)/2)
    left_edge = int(mid_index-(i-1))
    tree_decor_ind = range(prev_max_decorations+1,prev_max_decorations+i-1)
    for j in range(0,i-2):
      if tree_decor_ind[j] in decorations_indices:
        tree[i][left_edge+(j+1)*2] = 'O'
    prev_max_decorations = prev_max_decorations + i-2
    
  return tree

tree = christmas_tree(width,height)
output = '\n'.join(map(''.join, tree))
print(output)
