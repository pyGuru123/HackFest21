class StateMachine:

    def __init__(self, states={}):
        """
        The state machine will handle all the state changes in the game
        """

        self.states = states
        self.current = {}

    def change(self, state, **params):
        
        """
        This function will be transitioning states
        """
        if not state in self.states : return 

        self.current = self.states[state]
        self.current.enter(**params)

    def update(self, params):
        
        self.current.update(params)