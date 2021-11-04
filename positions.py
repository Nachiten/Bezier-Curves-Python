import pygame

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)


# Un punto en el plano
class Position:
    def __init__(self, x, y, text=" "):
        self.x = x
        self.y = y
        self.text = text

    # Muestra el punto en pantalla
    def mostrarEnPantalla(self, screen, color):
        text = font.render(self.text, True, color)
        textRect = text.get_rect()
        if self.y > 540:
            textRect.center = (self.x, self.y + 30)
        else:
            textRect.center = (self.x, self.y - 35)

        screen.blit(text, textRect)
        pygame.draw.circle(screen, color, (self.x, self.y), 12)
        pygame.draw.circle(screen, (120, 120, 120), (self.x, self.y), 10)

    # Dice si el punto fue tocado o no
    def tocoPunto(self, posX, posY):
        return self.x - 10 < posX < self.x + 10 and \
               self.y - 10 < posY < self.y + 10

    # Obtiene la posicion del punto (x,y)
    def getPos(self):
        return self.x, self.y

    # Obtiene el nombre del punto (string)
    def getName(self):
        return self.text
