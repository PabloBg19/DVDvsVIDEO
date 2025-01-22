import pygame 
import random

pygame.init()

pantalla=pygame.display.set_mode((1980,720), pygame.FULLSCREEN)
ventana=pygame.Surface((720,1100))
pygame.display.set_caption("DVD vs VIDEO")
ball=pygame.image.load("file.png")
ballrect=ball.get_rect()

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

puntaje=0
perdido= False

while jugando:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            jugando=False
            
    if perdido:
        mensaje =fuente.render("HAS PERDIDO, DVD ESCAPO", True, (255,0,0))
        pantalla.blit(mensaje, (750, 550))
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
        pygame.draw.rect(pantalla, (255, 255, 255), (90, 90, 250, 100), border_radius=10)
        pygame.draw.rect(pantalla, (0, 0, 0), (90, 90, 250, 100), 4, border_radius=10)
        texto_puntaje_sombra = fuentep.render(f"PUNTOS: {puntaje}", True, (128, 128, 128))
        pantalla.blit(texto_puntaje_sombra, (105, 115))
        texto_puntaje=fuentep.render(f"PUNTOS: {puntaje}",True, (0,0,0)) 
        pantalla.blit(texto_puntaje, (105,115))   
        pygame.display.flip()
        pygame.time.Clock().tick(60)
pygame.quit()        
    