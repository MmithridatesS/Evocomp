import numpy as np

class State_space:
    def __init__(self, state_dims, num_actions):
        assert len(state_dims) != 0
        assert num_actions != 0
        if type(state_dims) == tuple:
            shape = list(state_dims) + list(state_dims)
            shape.append(num_actions)
            self.state_action_space = np.zeros(shape)
            self.shape = shape
        elif type(state_dims) == int:
            self.shape = (state_dims, state_dims, num_actions)
            self.state_action_space = np.zeros(shape)
            
        else: 
            pass
    #outputting the size of the state_action_space
    def show_size(self):
        print(np.shape(self.state_action_space))
    
    
    #showing a random element of state_action_space
    def show_element(self):
        idx_list = []
        for i in range(len(self.shape)):
            idx_list.append(np.random.randint(0,self.shape[i]))
        return(self.state_action_space[idx_list])
            
    
    def initialize_uniform(self):
        prob = 1 / np.shape(self.state_action_space)[-1]
        print(prob)
        self.state_action_space.fill(prob)

class GridSpace:
    def __init__(self, grid_size, rewards, num_actions = 4,pi = 'uniform_random'):
        #arrestions
        assert type(grid_size) == tuple and len(grid_size) != 0

        #setting the reward
        if rewards == 'def':
           self.__rewards__ = np.ones(grid_size) 
        else:
            self.__rewards__ = rewards
        
        #setting the policy
        if pi == 'uniform_random':
            self.__pi__ = [np.ones(grid_size)/num_actions for _ in range(num_actions)]
            self.__pi__ = np.stack(arrays=self.__pi__, axis = 0)
        
        #setting the grid shape
        self.__grid_shape__ = list(grid_size)
        
        #setting value_function
        self.__V__ = np.zeros(grid_size) 
        
        #setting terminal_states
        self.__terminal_states__ = [None]
        
        
    #getters   
    def get_pi(self):
        return self.__pi__.shape
    def get_rewards(self):
        return self.__rewards__
    def get_grid_shape(self): 
        return self.__grid_shape__
    
    #setting rewards and terminals   
    def set_rewards(self,rewards, terminals):
        self.__rewards__ = rewards
        self.set_terminal(terminals)
    
    def set_terminal(self, *args):
        self.__terminal_states__ = args
        self.exclude_terminals()
        return args
            
    def exclude_terminals(self):
        print(self.__terminal_states__)
        for state in self.__terminal_states__:
            self.__rewards__[state[0], state[1]] = 0

        
    def deterministic_transition(self, state:tuple, action):
        nextstate_prob = np.zeros(self.__grid_shape__)
        
        if action == 'up' and state[0] != 0:
            nextstate_prob[state[0]-1, state[1]] = 1
            
        elif action == 'down' and state[0] != self.__grid_shape__[0]:
            nextstate_prob[state[0]+1, state[1]] = 1
            
        elif action == 'right' and state[1] != self.__grid_shape__[1]:
            nextstate_prob[state[0],state[1]+1] = 1
            
        elif action == 'left' and state[1] != 0:
            nextstate_prob[state[0],state[1]-1] = 1
        
        else:
            nextstate_prob[state[0], state[0]] = 1
        
        
        return np.stack([self.__rewards__, nextstate_prob])
    

def main():
    gs = GridSpace((10,12), 'def')
    print(gs.get_rewards())
    gs.set_rewards(gs.get_grid_shape, [(0,0), (9,11)])
    print(gs.deterministic_transition((2,2), 'left'))

if __name__ == '__main__':
    main()