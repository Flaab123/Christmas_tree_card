def christmas_tree(width,height,interval):
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

def base_postcard(width,height):
  card = []
  
  # Create base tree, without decorations
  for i in range(height):
    cardline = [' ']*width
    if i == 0 or i == height-1:
      cardline[0:] = '-'*width
    elif i == height-4:  #Tip of the tree
      cardline[0:] = ' '*width
      cardline[int(width/2-5):int(width/2+5)] = [x for x in 'Merry Xmas']
      cardline[0] = '|'
      cardline[-1] = '|'
    else: 
      cardline[0:] = ' '*width
      cardline[0] = '|'
      cardline[-1] = '|'
    card.append(cardline)
  return card

def stamp_tree(card,width,height,interval,x,y):
  tree = christmas_tree(width,height,interval)
  start = [y,x-int((width-1)/2)]
  xcoords = []
  for i in range(height):
    for j in range(width):
      if tree[i][j] != ' ':
        card[start[0]+i][start[1]+j] = tree[i][j]
  return card

user_input = input()
user_input = user_input.split(" ")

if len(user_input) == 2:
  width = int(user_input[0])*2-1
  height = int(user_input[0])+2
  interval = int(user_input[1])
  tree = christmas_tree(width,height,interval)
  output = '\n'.join(map(''.join, tree))
  print(output)
elif len(user_input) % 4 == 0:
  width = [int(x)*2-1 for x in user_input[0::4]]
  height = [int(x)+2 for x in user_input[0::4]]
  interval = [int(x) for x in user_input[1::4]]
  y_coor = [int(x) for x in user_input[2::4]]
  x_coor = [int(x) for x in user_input[3::4]]
  trees = int(len(user_input)/4)
  card = base_postcard(50,30)
  for i in range(trees):
    card = stamp_tree(card,width[i],height[i],interval[i],x_coor[i],y_coor[i])
  
print('\n'.join(map(''.join, card)))



