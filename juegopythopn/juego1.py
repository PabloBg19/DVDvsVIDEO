import pygame 
import random

pygame.init()

pantalla=pygame.display.set_mode((1980,720), pygame.FULLSCREEN)
ventana=pygame.Surface((720,1100))
pausa1=pygame.Surface((1980,720))
pygame.display.set_caption("DVD vs VIDEO")
ball=pygame.image.load("file.png")
ballrect=ball.get_rect()

lugar=random.randint(0,720)
lugar1=random.randint(0,720)
lugar2=random.randint(0,720)
lugar3=random.randint(0,720)
lugar4=random.randint(0,720)
lugar5=random.randint(0,720)
lugar6=random.randint(0,720)
lugar7=random.randint(0,720)
lugar8=random.randint(0,720)
lugar9=random.randint(0,720)
lugar10=random.randint(0,720)

mp3=pygame.image.load("mp3.png")
mp3rect=mp3.get_rect()
mp3rect.move_ip(lugar, lugar1)

mp31=pygame.image.load("mp3.png")
mp3rect1=mp3.get_rect()
mp3rect1.move_ip(lugar2, lugar3)

mp32=pygame.image.load("mp3.png")
mp3rect2=mp3.get_rect()
mp3rect2.move_ip(lugar4, lugar5)

mp33=pygame.image.load("mp3.png")
mp3rect3=mp3.get_rect()
mp3rect3.move_ip(lugar6, lugar7)

mp34=pygame.image.load("mp3.png")
mp3rect4=mp3.get_rect()
mp3rect4.move_ip(lugar8, lugar9)

tiempo_golpe=pygame.time.get_ticks()
retraso=3000

pygame.mixer.music.load("musicafondo.mp3")
pygame.mixer.music.play(-1)

velocidadx=3
velocidady=3
speed=[velocidadx, velocidady]

ballrect.move_ip(320, 600)

bate=pygame.image.load("paleta.png")
baterect=bate.get_rect()
baterect.move_ip(240, 1050)
jugando=True

fuente=pygame.font.Font(None, 54)

fuentep=pygame.font.Font(None, 76)

pausa=False
puntaje=0
perdido= False

def menu_pausa():
    global pausa
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Reanudar el juego
                    pausa = False
                elif event.key == pygame.K_q:  # Salir del juego
                    pygame.quit()
                    exit()

        # Fondo del menú de pausa
        pausa1.fill((30, 30, 30))
        mensaje = fuente.render("Juego en Pausa", True, (255, 255, 255))
        reanudar = fuente.render("Presiona ESC para Reanudar", True, (200, 200, 200))
        salir = fuente.render("Presiona Q para Salir", True, (200, 200, 200))

        # Dibujar texto
        pausa1.blit(mensaje, (pantalla.get_width() // 2 - mensaje.get_width() // 2, 200))
        pausa1.blit(reanudar, (pantalla.get_width() // 2 - reanudar.get_width() // 2, 300))
        pausa1.blit(salir, (pantalla.get_width() // 2 - salir.get_width() // 2, 400))

        # Actualizar pantalla de pausa
        pantalla.blit(pausa1, (0, 0))
        pygame.display.flip()

        # Controlar la velocidad del menú
        pygame.time.Clock().tick(30)

while jugando:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            jugando=False
            
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pausa = True
        menu_pausa()
        
    if perdido:
        mensaje =fuente.render("HAS PERDIDO, DVD ESCAPO", True, (255,0,0))
        pantalla.blit(mensaje, (750, 550))
        pygame.display.flip()
        continue
        
    if keys[pygame.K_a]:
        baterect= baterect.move(-3,0)
    if keys[pygame.K_d]:
        baterect= baterect.move(3,0)
        
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        speed[0]+=1 if speed[0]>0 else -1
        speed[1]+=1 if speed[1]>0 else -1
        puntaje+=1
    
    
    ballrect=ballrect.move(speed)


    if baterect.left<0:
        baterect.left=0
    if baterect.right>ventana.get_width():
        baterect.right=ventana.get_width()
    if ballrect.bottom>ventana.get_height():
        perdido=True
        
    
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left<0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
        
    if ballrect.top<0:
        speed[1] = -speed[1]
    
    if retraso<pygame.time.get_ticks():
         
        if mp3rect.colliderect(ballrect):
            speed[1] = -speed[1]
        
        if mp3rect1.colliderect(ballrect):
            speed[1] = -speed[1]
        
        if mp3rect2.colliderect(ballrect):
            speed[1] = -speed[1]
        
        if mp3rect3.colliderect(ballrect):
            speed[1] = -speed[1]
        
        if mp3rect4.colliderect(ballrect):
            speed[1]=-speed[1]

    
            
    
    ventana.fill((0,0,0))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    ventana.blit(mp3, mp3rect)
    ventana.blit(mp31, mp3rect1)
    ventana.blit(mp32, mp3rect2)
    ventana.blit(mp33, mp3rect3)
    ventana.blit(mp34, mp3rect4)
    
    
    pantalla.fill((50,50,50))
    pantalla.blit(ventana, ((pantalla.get_width()-ventana.get_width())//2,
                            (pantalla.get_height()-ventana.get_height())//2))
    
    
    
    
    
    pygame.draw.rect(pantalla, (255, 255, 255), (90, 90, 350, 95), border_radius=30)
    pygame.draw.rect(pantalla, (0, 0, 0), (90, 90, 350, 95), 4, border_radius=30)
        
    texto_puntaje_sombra = fuentep.render(f"PUNTOS: {puntaje}", True, (128, 128, 128))
    pantalla.blit(texto_puntaje_sombra, (105, 115))
        
    texto_puntaje=fuentep.render(f"PUNTOS: {puntaje}",True, (0,0,0)) 
    pantalla.blit(texto_puntaje, (105,115))   
    
    pygame.time.Clock().tick(60)
    pygame.display.flip()
 
       
pygame.quit()        
    