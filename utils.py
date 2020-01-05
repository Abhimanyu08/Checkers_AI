def check_triplets(ls):
  for i in ls:
    if (i[0]+1,i[1]) in ls:
      if (i[0]+2,i[1]) in ls:
        return True
      else:
        pass
    if (i[0],i[1]+1) in ls:
      if (i[0],i[1]+2) in ls:
        return True
      else:
        pass
    if (i[0]+1,i[1]+1) in ls:
      if (i[0]+2,i[1]+2) in ls:
        return True
      else:
        pass
    if (i[0]-1,i[1]+1) in ls:
      if (i[0]-2,i[1]+2) in ls:
        return True
      else:
        pass
  return False 

def terminal_test(state):
    if check_triplets(state['H']) or check_triplets(state['M']):
        return True
    elif not state['choices']:
        return True
    return False

def utility_func(state):
    if check_triplets(state['H']):
        return -1
    elif check_triplets(state['M']):
        return 1
    else: return 0
