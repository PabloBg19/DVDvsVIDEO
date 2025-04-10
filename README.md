Juego DVD vs VIDEO
Descripción General
"DVD vs VIDEO" es un juego 2D simple creado con Pygame, donde un logo de DVD (representado por una pelota) rebota por la pantalla. El jugador controla una paleta para evitar que la pelota caiga por la parte inferior de la pantalla mientras interactúa con múltiples obstáculos "mp3". El juego incluye un menú de pausa, música de fondo y un sistema de puntuación. Si la pelota se escapa por la parte inferior, el jugador pierde.

Características
Pelota que Rebota: Un logo de DVD rebota por la pantalla con velocidad creciente al chocar con la paleta.
Control de Paleta: Mueve la paleta a la izquierda y derecha con las teclas A y D.
Obstáculos: Cinco objetos "mp3" colocados aleatoriamente que pueden desviar la pelota.
Puntuación: Gana puntos al golpear la pelota con la paleta.
Menú de Pausa: Presiona ESC para pausar el juego y acceder al menú.
Game Over: Pierdes si la pelota cae por debajo de la paleta.
Música de Fondo: Se reproduce continuamente durante el juego.
Requisitos
Python 3.x: Asegúrate de tener Python instalado en tu sistema.
Pygame: Instala la librería Pygame usando pip:

pip install pygame
Recursos: El juego requiere los siguientes archivos en el mismo directorio que el script:
file.png: Imagen para la pelota que rebota (logo de DVD).
mp3.png: Imagen para los obstáculos.
paleta.png: Imagen para la paleta.
musicafondo.mp3: Archivo de música de fondo.
Cómo Ejecutar
Clona o descarga este repositorio en tu máquina local.
Asegúrate de que todos los recursos necesarios (file.png, mp3.png, paleta.png, musicafondo.mp3) estén en el mismo directorio que el script.
Instala las dependencias:

pip install pygame
Ejecuta el juego:

python dvd_vs_video.py
(Reemplaza dvd_vs_video.py con el nombre real de tu archivo de script.)
Controles
A: Mueve la paleta a la izquierda.
D: Mueve la paleta a la derecha.
ESC: Pausa el juego y abre el menú de pausa.
ESC (en el menú de pausa): Reanuda el juego.
Q (en el menú de pausa): Sale del joc.
Cerrar Ventana: Sal del juego cerrando la ventana.
Mecánica del Juego
El logo de DVD comienza a rebotar con una velocidad inicial.
Usa la paleta para mantener la pelota en juego y ganar puntos.
Evita que la pelota caiga por debajo de la paleta, o el juego termina con el mensaje "HAS PERDIDO, DVD ESCAPO".
La velocidad de la pelota aumenta cada vez que choca con la paleta.
Los obstáculos "mp3" colocados aleatoriamente pueden desviar la pelota después de un breve retraso.
