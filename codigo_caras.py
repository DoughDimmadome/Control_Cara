from pyPS4Controller.controller import controller

class MyController(Controller):

    def __init__(self, **kwargs):
        controller.__init__(self, **kwargs):
