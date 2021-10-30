from curves import *

posXBoton = 80
sizeXBoton = 50

posYBoton = 102
sizeYBoton = 30

def resetCurves():
    global t

    t = 0
    quadratic_curve.clear()
    cubic_curve.clear()
    curve1.clear()
    curve2.clear()
    curve3.clear()

def drawPoints():
    # draw points
    for point in linear_positions:
        point.display(screen, black)
    for point in quadratic_positions:
        point.display(screen, black)
    for point in cubic_positions:
        point.display(screen, black)


def generateConstantObjects():
    grayColor = (50, 50, 50)
    redColor = (255, 30, 30)
    blueColor = (30, 30, 255)

    # Lineal
    generarBotonEn(posXBoton + offsetsBotones[0], posYBoton, sizeXBoton, sizeYBoton, grayColor)

    # Cuadratica
    generarBotonEn(posXBoton + offsetsBotones[1], posYBoton, sizeXBoton, sizeYBoton, grayColor)
    generarBotonEn(posXBoton + offsetsBotones[2], posYBoton, sizeXBoton, sizeYBoton, redColor)

    # Cubica
    generarBotonEn(posXBoton + offsetsBotones[3], posYBoton, sizeXBoton, sizeYBoton, grayColor)
    generarBotonEn(posXBoton + offsetsBotones[4], posYBoton, sizeXBoton, sizeYBoton, blueColor)
    generarBotonEn(posXBoton + offsetsBotones[5], posYBoton, sizeXBoton, sizeYBoton, redColor)

    # T = 0.38 Text
    text = font.render(" T = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (680, 50)
    screen.blit(text, textRect)

    # Linear Text
    linear = font.render("Lineal:", True, black)
    textRect = linear.get_rect()
    textRect.center = (240, 120)
    screen.blit(linear, textRect)

    # Quadratic Text
    Quadratic = font.render("Cuadrática:", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (550, 120)
    screen.blit(Quadratic, textRect)

    # Cubic text
    cubic = font.render("Cúbica:", True, black)
    textRect = cubic.get_rect()
    textRect.center = (1000, 120)
    screen.blit(cubic, textRect)

    # Line Separators ---- | ----- | ------
    posXLine1 = 380
    posXLine2 = 700
    pygame.draw.line(screen, purple, (posXLine1, 700), (posXLine1, 150), 1)
    pygame.draw.line(screen, purple, (posXLine2, 700), (posXLine2, 150), 1)


def generateLinePoints():
    global linear_positions
    global quadratic_positions
    global cubic_positions

    # Generate line points
    if showLinear:
        linear_positions = [Position(50, 600, "P0"),
                            Position(250, 200, "P1")]
    else:
        linear_positions = []

    if showCuadratic:
        quadratic_positions = [Position(460, 600, "P0"),
                               Position(580, 450, "P1"),
                               Position(520, 200, "P2")]
    else:
        quadratic_positions = []

    if showCubic:
        cubic_positions = [Position(1050 - 300, 600, "P0"),
                           Position(1280 - 300, 200, "P1"),
                           Position(1420 - 300, 600, "P2"),
                           Position(1600 - 300, 200, "P3")]
        # cubic_positions = [Position(750, 450, "P0"),
        #                   Position(980, 200, "P1"),
        #                   Position(1120, 600, "P2"),
        #                   Position(750, 350, "P3")]
    else:
        cubic_positions = []

    global quadratic_curve
    global cubic_curve
    global curve1
    global curve2
    global curve3

    quadratic_curve = []
    cubic_curve = []
    curve1 = []
    curve2 = []
    curve3 = []


def generarBotonEn(posX, posY, sizeX, sizeY, color):
    pygame.draw.rect(screen, color, (posX, posY, sizeX, sizeY))


def cambiarVariableSegunIndex(index):
    global showLinear
    global showCuadratic
    global showCuadraticRedCurve
    global showCubic
    global showCubicBlueCurve
    global showCubicRedCurve

    if index == 0:
        showLinear = not showLinear
    elif index == 1:
        showCuadratic = not showCuadratic
    elif index == 2:
        showCuadraticRedCurve = not showCuadraticRedCurve
    elif index == 3:
        showCubic = not showCubic
    elif index == 4:
        showCubicBlueCurve = not showCubicBlueCurve
    elif index == 5:
        showCubicRedCurve = not showCubicRedCurve


def clickearBoton(unaPos):
    posX = unaPos[0]
    posY = unaPos[1]

    index = 0

    for unOffset in offsetsBotones:
        # Si toco determinado boton
        if posXBoton + unOffset < posX < posXBoton + sizeXBoton + unOffset \
                and posYBoton < posY < posYBoton + sizeYBoton:
            cambiarVariableSegunIndex(index)

            # Reseteo el tiempo para evitar bugs
            global t
            t = 0

            # Reseteo las listas de curvas
            generateLinePoints()

            return
        index += 1


width, height = 1920, 1080
size = (1366, 768)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 32)

# colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)
blue = (2, 146, 242)
purple = (205, 163, 255)

# --- MOSTRAR CURVAS ---
showLinear = False

showCuadratic = False
showCuadraticRedCurve = False

showCubic = False
showCubicBlueCurve = False
showCubicRedCurve = False

# Parametro t
t = 0
speed = 0.003


# Posiciones de los puntos para cada curva
linear_positions = []
quadratic_positions = []
cubic_positions = []

# Curvas a utilizar
quadratic_curve = []
cubic_curve = []
curve1 = []
curve2 = []
curve3 = []

# Generar los puntos de cada curva
generateLinePoints()

# Las posiciones en X de los distintos botones
offsetsBotones = [35, 250, 310, 680, 740, 800]

# Juego corriendo
run = True
# Juego en pausa
runClock = True

while run:
    screen.fill(white)
    clock.tick(fps)
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Bezier s - FPS : {}".format(frameRate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                runClock = not runClock
            if event.key == pygame.K_r:
                resetCurves()
                screen.fill(white)
                generateConstantObjects()
                drawPoints()
                pygame.display.update()
            if event.key == pygame.K_PLUS:
                speed = min(0.03, speed + 0.002)
            if event.key == pygame.K_MINUS:
                speed = max(0.001, speed - 0.002)
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickearBoton(pygame.mouse.get_pos())
            continue

    if not runClock:
        continue

    generateConstantObjects()

    # Curves
    if showLinear:
        LinearCurve(linear_positions, t, screen, red, True)
    if showCuadratic:
        QuadraticCurve(quadratic_positions, t, screen, red, quadratic_curve, green, True, showCuadraticRedCurve)
    if showCubic:
        CubicCurve(cubic_positions, t, screen, red, cubic_curve, green, blue, curve1, curve2, curve3,
                   showCubicRedCurve, showCubicBlueCurve)

    if len(cubic_curve) > 2:
        pygame.draw.lines(screen, (179, 179, 179), False, curve1, 3)
        pygame.draw.lines(screen, (179, 179, 179), False, curve3, 3)
        pygame.draw.lines(screen, (179, 179, 179), False, curve2, 3)
        pygame.draw.lines(screen, red, False, cubic_curve, 5)

    if len(quadratic_curve) > 2:
        pygame.draw.lines(screen, red, False, quadratic_curve, 5)

    if t >= 1:
        resetCurves()

    drawPoints()

    t += speed
    pygame.display.update()

pygame.quit()
