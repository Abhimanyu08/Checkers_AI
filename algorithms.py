import sys
import time
from prob_class import prob
from node_class import Node
from global_variables import *
from utils import *
# from algorithms import *
def abprune_decision(pro):
    global memory
    def abprune_value(node,a,b):
        global no_of_nodes
          # node = Node(pro.instate,'MAX')
        if terminal_test(node.state):
          return utility_func(node.state),node

        if node.player == 'MAX':
          v = -float('inf')
          c = []
          children = node.expand(pro)
          for child in children:
            # p = pro(child.state)
            no_of_nodes += 1
            v = max(v,abprune_value(child,a,b)[0])
            c.append((child,v))
            a = max(a,v)
            if a > b:
              break
          return v,max(c, key = lambda x:x[1])[0]
        
        elif node.player == 'MIN':
          v = float('inf')
          c = []
          children = node.expand(pro)
          for child in children:
            no_of_nodes += 1
            # c = child
            # p = pro(child.state)
            v = min(v,abprune_value(child,a,b)[0])
            c.append((child,v))
            b = min(b,v)
            if a > b:
              break
          return v,min(c, key = lambda x:x[1])[0]

    node = Node(pro.instate,'MAX')
    memory = sys.getsizeof(node)
    _,c = abprune_value(node,-float('inf'),float('inf'))
    return c.action

def minmax_decision(prob):
    global no_of_nodes_mm,memory
    def minmax_value(node):
        global no_of_nodes_mm
        if terminal_test(node.state):
            return utility_func(node.state)

        elif node.player == 'MAX':
            v = -float('inf') 
            for child in node.expand(prob):
                no_of_nodes_mm += 1
                v = max(v, minmax_value(child))
            return v

        else:
            v = float('inf') 
            for child in node.expand(prob):
                no_of_nodes_mm += 1
                # nstate = prob.nstate(a,state)
                v = min(v, minmax_value(child))
            return v
    node = Node(prob.instate,player = 'MAX')
    values = []
    children = node.expand(prob)
    for child in children:
        no_of_nodes_mm += 1
        values.append((child,minmax_value(child)))
    result_node = max(values, key= lambda x: x[1])[0]
    memory = sys.getsizeof(result_node)
    # no_of_nodes_mm += result_node.depth*4
    return result_node.action
