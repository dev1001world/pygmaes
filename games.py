import pygame, sys, random
pygame.init()
#colores a usar
randoms = random.randint(10,20)
colors = {
    "black":(0,0,0),
    "white":(255,255,255),
    "red":(255,0,0),
    "green":(0,255,0),
    "blue":(0,0,255),
    "yellow":(255,255,0),
    "pink":(255,192,203),
    "cyan":(0,255,255),
    "magenta":(255,0,255)
}
#variables de los jugadores
playerOne_position=[85,300]
playerTwo_position=[950,300]
width = 25
height = 150
speedOneY = 0
speedTwoY = 0
#variables de la pelota
ballPosition = [530,300]
ballSpeed_x = 10
ballSpeed_y = 10
#uso de pantalla
size = (1060,600)
screen = pygame.display.set_mode(size)
clock_exe = pygame.time.Clock()
#variables de la partida
gameOver = False
PlayerOne_cont = 0
PlayerTwo_cont = 0
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    surface_text = font.render(text, True, colors["magenta"])
    rect_text = surface_text.get_rect()
    rect_text.midtop=(x,y)
    surface.blit(surface_text, rect_text)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #uso del teclado
        if event.type == pygame.KEYDOWN:
            #player 1
            if event.key == pygame.K_w:
                speedOneY-=10
            if event.key == pygame.K_s:
                speedOneY+=10
            #player 2 
            if event.key == pygame.K_UP:
                speedTwoY-=10
            if event.key == pygame.K_DOWN:
                speedTwoY+=10
        if event.type == pygame.KEYUP:
            #player 1
            if event.key == pygame.K_w:
                speedOneY=0
            if event.key == pygame.K_s:
                speedOneY=0
            #player 2 
            if event.key == pygame.K_UP:
                speedTwoY=0
            if event.key == pygame.K_DOWN:
                speedTwoY=0
    #pantalla
    screen.fill(colors["black"])
    #dibujar cancha
    for i in range(100,700,100):
        li=pygame.draw.rect(screen,colors["yellow"],(520,i,10,10))
    #movie players 
    playerOne_position[1]+=speedOneY
    playerTwo_position[1]+=speedTwoY
    #movie de la pelota
    ballPosition[0] += ballSpeed_x 
    ballPosition[1] += ballSpeed_y
    #variables de los jugadores en la pantalla
    one=pygame.draw.line(screen,colors["red"],(3,0),(3,600),5)
    two=pygame.draw.line(screen,colors["red"],(1056,0),(1056,600),5)
    playingOne=pygame.draw.rect(screen,colors["white"],(playerOne_position[0],playerOne_position[1]-75,width,height))
    playingTwo=pygame.draw.rect(screen,colors["white"],(playerTwo_position[0],playerTwo_position[1]-75,width,height))
    ballPlaying=pygame.draw.circle(screen,colors["cyan"],(ballPosition[0],ballPosition[1]),15)
    #coliciones con los jugadores  
    if ballPlaying.colliderect(playingOne) or ballPlaying.colliderect(playingTwo):
        ballSpeed_x *=-1
    #coliciones con la pantalla
    if ballPosition[0] <  15 or ballPosition[0] > 1045:
            ballSpeed_x *= -1
    if ballPosition[1] <  15 or ballPosition[1] > 585:
            ballSpeed_y *= -1
    #colicion pantalla jugador
    if playerOne_position[1] > 515 or playerOne_position[1] < 75:
        speedOneY = 0
    if playerTwo_position[1] > 515 or playerTwo_position[1] < 75:
        speedTwoY = 0
    #contador
    if PlayerOne_cont == 100:
        print("judadoe uno ganaste")
        gameOver = True
    elif ballPlaying.colliderect(two):
        PlayerOne_cont += 1
        print(PlayerOne_cont)
    if PlayerTwo_cont == 100:
        print("judadoe dos ganaste")
        gameOver = True
    elif ballPlaying.colliderect(one):
        PlayerTwo_cont += 1
        print(PlayerTwo_cont)

    draw_text(screen,"player one: " + str(PlayerOne_cont), 25, 100,20)

    draw_text(screen,"player twos: " + str(PlayerTwo_cont), 25, 950,20)
    #end
    pygame.display.flip()
    clock_exe.tick(60)