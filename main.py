from curves import *


# Analizo si se clickeo un punto y lo muevo si corresponde
def moverObjeto(unaPos):
    global linear_positionsPosibles
    global quadratic_positionsPosibles
    global cubic_positionsPosibles

    seModificoLista = escanearLista(linear_positions, unaPos)

    if seModificoLista:
        linear_positionsPosibles = linear_positions
        resetCurves()
        return

    seModificoLista = escanearLista(quadratic_positions, unaPos)

    if seModificoLista:
        quadratic_positionsPosibles = quadratic_positions
        resetCurves()
        return

    seModificoLista = escanearLista(cubic_positions, unaPos)

    if seModificoLista:
        cubic_positionsPosibles = cubic_positions
        resetCurves()
        return


# Escanear todos los puntos para una lista (determinada curva) para ver si se toco alguno
def escanearLista(lista, unaPos):
    global pickingUpPoint
    global pointPickedUp

    posX = unaPos[0]
    posY = unaPos[1]

    index = 0

    for position in lista:
        if pickingUpPoint:
            if pointPickedUp == position.getPos():
                name = position.getName()
                lista[index] = Position(posX, posY, name)
                pickingUpPoint = False
                return True
        else:
            if position.tocoPunto(posX, posY):
                pickingUpPoint = True
                pointPickedUp = position.getPos()
                return False
        index += 1

    return False


# Reiniciar todas las curvas a t = 0
def resetCurves():
    global t

    t = 0
    quadratic_curve.clear()
    cubic_curve.clear()
    curve1.clear()
    curve2.clear()
    curve3.clear()


# Dibujar los puntos de las curvas
def drawPoints():
    for point in linear_positions:
        point.mostrarEnPantalla(screen, black)
    for point in quadratic_positions:
        point.mostrarEnPantalla(screen, black)
    for point in cubic_positions:
        point.mostrarEnPantalla(screen, black)


# Generar los botones y textos en la pantalla
def generarObjetosConstantes():
    # Colores a utilizar (r,g,b)
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
    text = font.render(" t = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (500, 50)
    screen.blit(text, textRect)

    # Speed
    textSpeed = font.render(" speed = " + str(speed)[:5], True, black)
    textRect = textSpeed.get_rect()
    textRect.center = (850, 50)
    screen.blit(textSpeed, textRect)

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


# Generar los puntos para cada curva
def generarPuntosDeCurvas():
    global linear_positions
    global quadratic_positions
    global cubic_positions

    if showLinear:
        linear_positions = linear_positionsPosibles
    else:
        linear_positions = []

    if showCuadratic:
        quadratic_positions = quadratic_positionsPosibles
    else:
        quadratic_positions = []

    if showCubic:
        cubic_positions = cubic_positionsPosibles
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


# Generar un nuevo boton y mostrarlo en la pantalla
def generarBotonEn(posX, posY, sizeX, sizeY, color):
    pygame.draw.rect(screen, color, (posX, posY, sizeX, sizeY))


# Modificar el booleano que corresponda en base a cual boton se toco
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
            generarPuntosDeCurvas()

            return
        index += 1


# Datos de la pantalla
width, height = 1920, 1080
size = (1366, 768)

pygame.init()
screen = pygame.display.set_mode(size)

# Reloj
clock = pygame.time.Clock()
fps = 60

# Tipo de letra
font = pygame.font.Font('freesansbold.ttf', 32)

# Colores (r,g,b)
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)
blue = (2, 146, 242)
purple = (205, 163, 255)

# Datos mostrados sobre curvas
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

# Puntos default para cada curva
linear_positionsPosibles = [Position(50, 600, "P0"),
                            Position(250, 200, "P1")]

quadratic_positionsPosibles = [Position(460, 600, "P0"),
                               Position(580, 450, "P1"),
                               Position(520, 200, "P2")]

cubic_positionsPosibles = [Position(750, 600, "P0"),
                           Position(980, 200, "P1"),
                           Position(1120, 600, "P2"),
                           Position(1300, 200, "P3")]

# Curvas a utilizar
quadratic_curve = []
cubic_curve = []
curve1 = []
curve2 = []
curve3 = []

# Ubicacion y tamaño de los botones
posXBoton = 80
sizeXBoton = 50
posYBoton = 102
sizeYBoton = 30

# Las posiciones en X de los distintos botones
offsetsBotones = [35, 250, 310, 680, 740, 800]

# Datos sobre cuando se agarra un punto para moverlo
pickingUpPoint = False
pointPickedUp = (0, 0)

# Juego corriendo
run = True
# Juego en pausa
runClock = True

# Generar los puntos de cada curva
generarPuntosDeCurvas()

while run:
    screen.fill(white)
    clock.tick(fps)
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Bezier Curves - FPS : {}".format(frameRate))

    # Escaneo los eventos ocurridos en el juego
    for event in pygame.event.get():
        # Si se quito el juego
        if event.type == pygame.QUIT:
            run = False
        # Si se presiono una tecla
        if event.type == pygame.KEYDOWN:
            # Si se presiono escape
            if event.key == pygame.K_ESCAPE:
                run = False
            # Si se presiono espacio, pauso
            if event.key == pygame.K_SPACE:
                runClock = not runClock
            # Si se presiono r, reinicio t
            if event.key == pygame.K_r:
                resetCurves()
                screen.fill(white)
                generarObjetosConstantes()
                drawPoints()
                pygame.display.update()
            # Si se presiono +, aumento la velocidad
            if event.key == pygame.K_PLUS:
                speed = min(0.03, speed + 0.002)
            # Si se presiono -, disminuyo la velocidad
            if event.key == pygame.K_MINUS:
                speed = max(0.001, speed - 0.002)
        # Si se clickeo el mouse, analizo si se clickeo un boton o un punto
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickearBoton(pygame.mouse.get_pos())
            moverObjeto(pygame.mouse.get_pos())
            continue

    # No ejecuto el resto si estoy en pausa
    if not runClock:
        continue

    generarObjetosConstantes()

    # Generar curvas
    if showLinear:
        curvaLineal(linear_positions, t, screen, red, True)
    if showCuadratic:
        curvaCuadratica(quadratic_positions, t, screen, red, quadratic_curve, green, True, showCuadraticRedCurve)
    if showCubic:
        curvaCubica(cubic_positions, t, screen, red, cubic_curve, green, blue, curve1, curve2, curve3,
                    showCubicRedCurve, showCubicBlueCurve)

    # Generar mas curvas
    if len(cubic_curve) > 2:
        if showCubicBlueCurve:
            pygame.draw.lines(screen, (179, 179, 179), False, curve1, 3)
            pygame.draw.lines(screen, (179, 179, 179), False, curve2, 3)
        if showCubicRedCurve:
            pygame.draw.lines(screen, red, False, cubic_curve, 5)

    if len(quadratic_curve) > 2:
        pygame.draw.lines(screen, red, False, quadratic_curve, 5)

    # Vuelvo a 0 si t paso de 1
    if t >= 1:
        resetCurves()

    # Dibujo todos los puntos
    drawPoints()

    # Incremento t
    t += speed

    # Actualizo el display
    pygame.display.update()

# Si salio del ciclo for, termina el programa
pygame.quit()
