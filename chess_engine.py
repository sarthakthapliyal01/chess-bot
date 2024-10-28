'''
this class is responsible for storing all the information about the current state of chess game.it will also be responsible for determining the valid move in current state. it will also keep a move log.

'''

class gamestate():
    def __init__(self):
        self.board = [
            ["bR","bK","bB","bQ","bK","bB","bK","bR"]
            ["bp","bp","bp","bp","bp","bp","bp","bp"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["wp","wp","wp","wp","wp","wp","wp","wp"]
            ["wR","wK","wB","wQ","wK","wB","wK","wR"] 
        ]
        self.whitetomove=True
        self.movelog = []
            

        