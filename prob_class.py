class prob():
    def __init__(self,instate):
        self.instate = instate
        
    def actions(self,state):
        return state['choices']

    def nstate(self,state,action,player):
        nstate = {}
        h = list(state['H'])
        m = list(state['M'])
        c = list(state['choices'])
        if player == 'MAX':
            m.append(action)
            
        else:
            h.append(action)
        c.remove(action)
        if action[1] + 1 < 4:
            c.append((action[0],action[1]+1))
        else:
            pass
        nstate['H'] = h
        nstate['M'] = m
        nstate['choices'] = c
        
        return nstate