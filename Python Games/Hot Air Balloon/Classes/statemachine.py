class StateMachine:
    """
    This is the class which will keep track of all the states in the game.
    It will also change the state of the game

    usage:
        gstatemachine = StateMachine(states)
        where states represent different states of the game
    """

    def __init__(self, states={}):
        
        self.states = states
        self.current = None
    
    def change(self, state, **params):
        assert state in self.states

        if self.current != None : self.current.leave()
        self.current = self.states[state]
        self.current.enter(**params)
    
    def update(self, params):
        self.current.update(params)