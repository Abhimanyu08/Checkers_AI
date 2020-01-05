def play(evor):
  global state,chance
  lc.delete('nnodes')
  lc.delete('mory')
  lc.delete('npm')
  pro = prob(state)
  minmove = getcord(evor)
  if minmove in state['choices']:  
    state = pro.nstate(dict(state),minmove,chance)
    print(state)
    place_coins(rc,minmove,chance)
    chance = 'MAX'
    if terminal_test(state):
      if utility_func(state) == -1:
        lc.create_text(50,250,fill = 'white',text = 'HUMAN WINS',tags = ('label',))
      elif utility_func(state) == 0:
        lc.create_text(50,250,fill = 'white',text = 'IT\'S A DRAW',tags = ('label',))
    pro = prob(state)
    if flag:
        maxmove = minmax_decision(pro)
        lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes_mm),tags = ('nnodes',))
    else:
        maxmove = abprune_decision(pro)
        lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes),tags = ('nnodes',))
    state = pro.nstate(dict(state),maxmove,chance)
    print(state)
    if terminal_test(state):
      if utility_func(state) == 1:
        lc.create_text(50,250,fill = 'white',text = 'MACHINE WINS',tags = ('label',))
      elif utility_func(state) == 0:
        lc.create_text(50,250,fill = 'white',text = 'IT\'S A DRAW',tags = ('label',))
    place_coins(rc,maxmove,chance)
    # root.after(2000,func=place_coins(rc,maxmove,chance))
    chance = 'MIN'
