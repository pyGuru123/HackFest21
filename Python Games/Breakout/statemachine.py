import pygame

class StateMachine:

    def __init__(self, states=None):

        self.empty = {}

        self.states = states or {}
        self.current = self.empty

    def change(self, state):

        if not state in self.states: return

        self.current = self.states[state]
        self.current.enter()
    
    def render(self):
        self.current.render()
    
    def update(self, params):
        self.current.update(params)