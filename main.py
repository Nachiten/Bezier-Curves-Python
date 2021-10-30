from curves import *

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
showLinear = True

showQuadratic = True
showCuadraticRedCurve = True

showCubic = True
showCubicBlueCurve = True
showCubicRedCurve = True


# parameters
t = 0
speed = 0.002

# Generate line points
if showLinear:
    linear_positions = [Position(50, 600, "P0"),
                        Position(250, 200, "P1")]
else:
    linear_positions = []

if showQuadratic:
    Quadratic_positions = [Position(460, 600, "P0"),
                           Position(580, 450, "P1"),
                           Position(520, 200, "P2")]
else:
    Quadratic_positions = []

if showCubic:
    cubic_positions = [Position(1050 - 300, 600, "P0"),
                       Position(1280 - 300, 200, "P1"),
                       Position(1420 - 300, 600, "P2"),
                       Position(1600 - 300, 200, "P3")]
else:
    cubic_positions = []

quadratic_curve = []
cubic_curve = []
curve1 = []
curve2 = []
curve3 = []

run = True
runClock = True
while run:
    screen.fill(white)
    clock.tick(fps)
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Bezier Curve - FPS : {}".format(frameRate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                runClock = not runClock

    if not runClock:
        continue

    # T = 0.38 Text
    text = font.render(" T = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (680, 50)
    screen.blit(text, textRect)

    if showLinear:
        # Linear Text
        linear = font.render("Lineal:", True, black)
        textRect = linear.get_rect()
        textRect.center = (240, 120)
        screen.blit(linear, textRect)

    if showQuadratic:
        # Quadratic Text
        Quadratic = font.render("Cuadrática:", True, black)
        textRect = Quadratic.get_rect()
        textRect.center = (550, 120)
        screen.blit(Quadratic, textRect)

    if showCubic:
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

    # Curves
    if showLinear:
        LinearCurve(linear_positions, t, screen, red, True)
    if showQuadratic:
        QuadraticCurve(Quadratic_positions, t, screen, red, quadratic_curve, green, True, showCuadraticRedCurve)
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
        t = 0
        quadratic_curve.clear()
        cubic_curve.clear()
        curve1.clear()
        curve2.clear()
        curve3.clear()

    # draw points
    for point in linear_positions:
        point.display(screen, black)
    for point in Quadratic_positions:
        point.display(screen, black)
    for point in cubic_positions:
        point.display(screen, black)

    t += speed
    pygame.display.update()

pygame.quit()
