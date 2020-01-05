#NAME - ABHIMANYU
#ID - 2016A2PS0793P
from tkinter import *
import sys
import time
from prob_class import prob
from node_class import Node
from global_variables import *
from utils import *
from algorithms import *
# from gameplay import play

root = Tk()
lc = Canvas(root,height = 400,width = 200,bg = 'black')
lc.pack(side = LEFT, fill = BOTH)
rc = Canvas(root,height = 400, width = 400,bg = 'white')
rc.pack(side = LEFT,fill = BOTH)
# can = Canvas(frame)
# can.pack()
def gui(canvas):
    h = int(canvas['height'])
    w = int(canvas['width'])
    for i in range(4):
        for j in range(4):
            canvas.create_rectangle(i*(h/4),j*(w/4),(i+1)*(h/4),(j+1)*(w/4))

def getcord(evor):
    global x,y
    x = evor.x
    y = evor.y
    # print(x,y)
    return click_to_cord(x,y)

gui(rc)

def click_to_cord(x,y):
    co1 = int(x/100)
    co2 = int(y/100)
    cords = (co1,co2)
    return cords

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
        # lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes_mm),tags = ('nnodes',))
    else:
        maxmove = abprune_decision(pro)
        # lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes),tags = ('nnodes',))
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




def place_coins(canvas,move,chance):
  if chance == 'MAX':
    canvas.create_oval(move[0]*100,move[1]*100,(move[0]+1)*100, (move[1]+1)*100, fill = 'green')
  else:
    canvas.create_oval(move[0]*100,move[1]*100,(move[0]+1)*100, (move[1]+1)*100, fill = 'blue')

def start_game():
  global state,chance,rc,time
  # gui(rc)
  pro = prob(state)
  if flag:
      st = time.time()
      move = minmax_decision(pro)
      et = time.time()
      ti = (et-st)*(1e+06)
      # lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes_mm),tags = ('nnodes',))
      # lc.create_text(150,330,fill = 'white',text = 'MEMORY FOR ONE NODE-' + str(memory) + ' bytes',tags = ('mory',))
      # lc.create_text(150,350,fill = 'white', text = 'NODES/MICROSECOND = ' + str(no_of_nodes_mm/ti), tags = ('npm',))
  else:
      st = time.time()
      move = abprune_decision(pro)
      et = time.time()
      ti = (et-st)*(1e+06)
      # lc.create_text(150,300,fill = 'white',text = 'NODES GENERATED HITHERTO-' + str(no_of_nodes),tags = ('nnodes',))
      # lc.create_text(150,330,fill = 'white',text = 'MEMORY FOR ONE NODE-' + str(memory) + ' bytes',tags = ('mory',))
      # lc.create_text(150,350,fill = 'white',text = 'NODES/MICROSECOND = ' + str(no_of_nodes/ti),tags = ('npm',)) 
  state = pro.nstate(dict(state),move,chance)
  print(state)
  place_coins(rc,move,chance)
  chance = 'MIN'


rc.bind("<Button 1>", play)

def exits():
    sys.exit()
def restart():
  global state,chance,rc,no_of_nodes,no_of_nodes_mm
  rc.delete('all')
  lc.delete('label')
  lc.delete('nnodes')
  state = {'H':[], 'M': [], 'choices':[(0,0),(1,0),(2,0),(3,0)]}
  chance = 'MAX'
  no_of_nodes = 0
  no_of_nodes_mm = 0
  gui(rc)
  # start_game()
def pwm():
  global flag
  flag = True
  print(flag)

def pwab():
  global flag
  flag = False
  print(flag)
mb = Button(lc,text = 'PLAY USING MINIMAX',bg = 'red',fg = 'white',height = 2,width = 50,command = pwm)
ab = Button(lc,text = 'PLAY USING A.B PRUNING',bg = 'red',fg = 'white',height = 2,width = 20,command = pwab)

start = Button(lc,text = 'START GAME',bg = 'red',fg = 'white',height = 2,width = 20,command = start_game)
exi = Button(lc,text = 'EXIT',bg = 'red',fg = 'white',height = 2, width = 20,command = exits)
rest = Button(lc,text = 'CLEAR BOARD',bg = 'red',fg = 'white',height = 2,width = 20,command = restart)

mb.pack(side = TOP, fill = BOTH)
ab.pack(side = TOP, fill = BOTH)
start.pack(side = TOP, fill = BOTH)
exi.pack(side = TOP, fill = BOTH)
rest.pack(side = TOP, fill = BOTH)

# lc.create_line(50,150,50,200,fill = 'white',width = 3)




   














root.mainloop()