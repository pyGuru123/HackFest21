class Base:

    """
    This is a base states class all the other state classes will inherit from this class
    """

    def __init__(self): pass

    def render(self): pass

    def update(self, params=None) : pass

    def enter(self, **params) : pass

    def Exit(self) : pass