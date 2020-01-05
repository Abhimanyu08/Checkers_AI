class Node():
    def __init__(self,state,player,parent = None,action = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.player = player
        # if parent:
        #   self.depth = parent.depth + 1
        # else:
        #   self.depth = 0

    def get_child(self,prob,action,player):
        nstate = prob.nstate(self.state,action,player)
        if self.player == 'MAX':
            return Node(nstate,'MIN',self,action)
        elif self.player == 'MIN':
            return Node(nstate,'MAX',self,action)
    
    def expand(self,prob):
        return [self.get_child(prob,action,self.player) for action in prob.actions(self.state)]
