'''
this is our main driver file. it will be responsible for handling user input and dislaying the current game state object

'''

import pygame as p
import chess

WIDTH = HEIGHT =512
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}

'''
intialize a global dictionary of images. this will be called exactly once in a main 
'''

def loadimages():
    pieces= ["bB","bK","bN","bp","bQ","bR","wB","WK","wN","wp","wQ","wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("./pieceimages/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
the main driver of our code. this will handle user input and updating the graphics 
'''

def main():
    p.init
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess.Board() 
    loadimages()

    running=True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running=False  
        drawgamestate(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
responsible for all the graphics within a current game state.
'''
def drawgamestate(screen, gs):
    drawboard(screen)  # Draw squares on the board
    drawpieces(screen, gs)  # Pass the board directly to drawpieces

'''
draw squares on board. top left square is always light
'''

def drawboard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color=colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


'''
draw the pieces of board using the current gamestate.board
'''
def drawpieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]  # Access piece using 2D list indexing
            if piece != "--":  # Check if there is a piece
                piece_image = IMAGES.get(piece) 
                if piece_image:  # Ensure the image exists
                    screen.blit(piece_image, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))






if __name__=="__main__":
    main()


