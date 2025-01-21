import pygame 
import random

pygame.init()

pantalla=pygame.display.set_mode((1980,720), pygame.FULLSCREEN)
ventana=pygame.Surface((640,780))
pygame.display.set_caption("DVD vs VIDEO")
ball=pygame.image.load("file.png")
ballrect=ball.get_rect()

pygame.mixer.music.load("musicafondo.mp3")
pygame.mixer.music.play(-1)

velocidadx=3
velocidady=3
speed=[velocidadx, velocidady]

ballrect.move_ip(0, 0)

bate=pygame.image.load("paleta.png")
baterect=bate.get_rect()
baterect.move_ip(240, 750)
jugando=True

fuente=pygame.font.Font(None, 54)

fuentep=pygame.font.Font(None, 76)

puntaje=0
perdido= False

while jugando:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            jugando=False
            
    if perdido:
        mensaje =fuente.render("HAS PERDIDO, DVD ESCAPO", True, (255,0,0))
        ventana.blit(mensaje, (180, 200))
        pygame.display.flip()
        continue
        
    keys=pygame.key.get_pressed()
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

    
    ventana.fill((0,0,0))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    
    pantalla.fill((200,200,200))
    pantalla.blit(ventana, ((pantalla.get_width()-ventana.get_width())//2,
                            (pantalla.get_height()-ventana.get_height())//2))
    pygame.display.flip()
    
    
    
    if not perdido:    
        texto_puntaje=fuentep.render(f"PUNTAJE: {puntaje}",True, (0,0,0)) 
        pantalla.blit(texto_puntaje, (10,10))   
        pygame.display.flip()
        pygame.time.Clock().tick(60)
pygame.quit()        
    