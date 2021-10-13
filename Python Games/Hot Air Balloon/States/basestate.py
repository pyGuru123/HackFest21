class Base:
    """
    This is the base state for our game. All the other states will inherit this class

    Base:
        __init__()          -> constructor function
        enter(**params)     -> used in statemachin class to enter in a certain state
        render()            -> used to render the state
        update(*params)     -> updates the state
        leave()             -> exits the state and used in statemachine class
    """

    def __init__(self) -> None:
        """
        Built in functinaliy of python class.
        It works as a constructor for the class.
        """
        pass

    def enter(self, **params) -> None: 
        """
        This method is called first when the state is changed.
        """
        
        pass

    def render(self) -> None: 
        """
        This method renders all the drawing and sprites on the screen.
        The update method keeps calling this method to constantly render sprites and other game objects on screen.
        """
        pass

    def update(self, params) -> None:
        """
        This method is called once in each game loop.
        All the updates and changes are done in this mehod.
        It takes on argument as a parameter(in most case that is events).
        """
        self.render()
    
    def leave(self) -> None: 
        """
        This method is called during the state change. 
        The state machine calls this method to leave the current state and enter into the next one.
        """
        pass