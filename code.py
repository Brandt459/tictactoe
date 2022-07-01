import pygame
import sys

width = 600
height = 600
size = (width, height)

screen = pygame.display.set_mode(size=size)

ximage = pygame.image.load('x.png')
oimage = pygame.image.load('o.png')

class Game:
    def __init__(self):
        self.turn = True
        self.marks = []
        self.gameover = False
    
    def placeMark(self, i, j):
        if not (i, j, self.turn) in self.marks and not (i, j, not self.turn) in self.marks:
            self.marks.append((i, j, self.turn))
            self.turn = not self.turn
        player = True
        for _ in range(2):
            bldtotal = 0
            tldtotal = 0
            for i in range(3):
                vtotal = 0
                htotal = 0
                for j in range(3):
                    if (i * 200, j * 200, player) in self.marks:
                        vtotal += 1
                    if (j * 200, i * 200, player) in self.marks:
                        htotal += 1
                if (i * 200, (2 - i) * 200, player) in self.marks:
                    bldtotal += 1
                if (i * 200, i * 200, player) in self.marks:
                    tldtotal += 1
                if vtotal == 3 or htotal == 3:
                    self.gameover = True
            if bldtotal == 3 or tldtotal == 3:
                self.gameover = True
            player = False

game = Game()

while True:           
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game.gameover:
            pos = pygame.mouse.get_pos()
            for xindex, i in enumerate(range(0, width, 200)):
                for yindex, j in enumerate(range(0, height, 200)):
                    if pygame.Rect((i, j), (200, 200)).collidepoint((pos[0], pos[1])):
                        game.placeMark(i, j)

        if event.type == pygame.QUIT:
            sys.exit()

    for xindex, i in enumerate(range(0, width, 200)):
        for yindex, j in enumerate(range(0, height, 200)):
            box = pygame.Surface((200, 200))
            box.fill((220, 220, 220))
            if (i, j, True) in game.marks or (i, j, False) in game.marks:
                image = ximage if (i, j, True) in game.marks else oimage
                box.blit(pygame.transform.scale(image , (200, 200)), ((0, 0), (200, 200)))
            pygame.draw.rect(box, (0, 0, 0), pygame.Rect((0, 0), (200, 200)), 1)
            screen.blit(box, (i, j))
    
    pygame.display.flip()