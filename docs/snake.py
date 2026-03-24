import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones
ANCHO = 600
ALTO = 400
TAMANO_CUADRO = 20
VELOCIDAD = 10

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
VERDE_OSCURO = (0, 200, 0)

# Direcciones
ARRIBA = (0, -1)
ABAJO = (0, 1)
IZQUIERDA = (-1, 0)
DERECHA = (1, 0)

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        inicio_ancho = ANCHO // 2
        inicio_alto = ALTO // 2
        self.cuerpo = [
            (inicio_ancho, inicio_alto),
            (inicio_ancho - TAMANO_CUADRO, inicio_alto),
            (inicio_ancho - 2 * TAMANO_CUADRO, inicio_alto)
        ]
        self.direccion = DERECHA
        self.nueva_direccion = DERECHA
        self.crecer = False
    
    def cambiar_direccion(self, nueva_direccion):
        direcciones_opuestas = {
            ARRIBA: ABAJO,
            ABAJO: ARRIBA,
            IZQUIERDA: DERECHA,
            DERECHA: IZQUIERDA
        }
        if nueva_direccion != direcciones_opuestas.get(self.direccion):
            self.nueva_direccion = nueva_direccion
    
    def mover(self):
        self.direccion = self.nueva_direccion
        cabeza_x, cabeza_y = self.cuerpo[0]
        nuevo_cabeza = (
            cabeza_x + self.direccion[0] * TAMANO_CUADRO,
            cabeza_y + self.direccion[1] * TAMANO_CUADRO
        )
        self.cuerpo.insert(0, nuevo_cabeza)
        if not self.crecer:
            self.cuerpo.pop()
        else:
            self.crecer = False
    
    def crece(self):
        self.crecer = True
    
    def choca_consigo(self):
        return self.cuerpo[0] in self.cuerpo[1:]
    
    def choca_bordes(self, ancho, alto):
        cabeza_x, cabeza_y = self.cuerpo[0]
        return (cabeza_x < 0 or cabeza_x >= ancho or
                cabeza_y < 0 or cabeza_y >= alto)
    
    def dibujar(self, pantalla):
        for i, segmento in enumerate(self.cuerpo):
            color = VERDE_OSCURO if i == 0 else VERDE
            pygame.draw.rect(
                pantalla, color,
                (segmento[0], segmento[1], TAMANO_CUADRO, TAMANO_CUADRO)
            )


class Food:
    def __init__(self):
        self.posicion = (0, 0)
    
    def inicializar_posicion(self, ancho, alto, snake_body):
        self.posicion = self.aleatorizar_posicion(ancho, alto, snake_body)
    
    def aleatorizar_posicion(self, ancho, alto, snake_body):
        while True:
            x = random.randint(0, (ancho - TAMANO_CUADRO) // TAMANO_CUADRO) * TAMANO_CUADRO
            y = random.randint(0, (alto - TAMANO_CUADRO) // TAMANO_CUADRO) * TAMANO_CUADRO
            if (x, y) not in snake_body:
                return (x, y)
    
    def dibujar(self, pantalla):
        pygame.draw.rect(
            pantalla, ROJO,
            (self.posicion[0], self.posicion[1], TAMANO_CUADRO, TAMANO_CUADRO)
        )


def mostrar_puntuacion(puntuacion, fuente):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    return texto


def main():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Snake Game")
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 36)
    
    snake = Snake()
    comida = Food()
    comida.inicializar_posicion(ANCHO, ALTO, snake.cuerpo)
    puntuacion = 0
    juego_terminado = False
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if juego_terminado:
                    if evento.key == pygame.K_r:
                        snake.reset()
                        comida.inicializar_posicion(ANCHO, ALTO, snake.cuerpo)
                        puntuacion = 0
                        juego_terminado = False
                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if evento.key in (pygame.K_UP, pygame.K_w):
                        snake.cambiar_direccion(ARRIBA)
                    elif evento.key in (pygame.K_DOWN, pygame.K_s):
                        snake.cambiar_direccion(ABAJO)
                    elif evento.key in (pygame.K_LEFT, pygame.K_a):
                        snake.cambiar_direccion(IZQUIERDA)
                    elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                        snake.cambiar_direccion(DERECHA)
        
        if juego_terminado:
            pantalla.fill(NEGRO)
            
            texto_puntuacion = mostrar_puntuacion(puntuacion, fuente)
            pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, ALTO // 2 - 80))
            
            texto_game_over = fuente.render("GAME OVER", True, ROJO)
            pantalla.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO // 2 - 30))
            texto_game_over_small = fuente.render("Presiona 'R' para reiniciar o 'Q' para salir", True, BLANCO)
            pantalla.blit(texto_game_over_small, (ANCHO // 2 - texto_game_over_small.get_width() // 2, ALTO // 2 + 20))
            
            pygame.display.flip()
            reloj.tick(VELOCIDAD)
            continue
        
        snake.mover()
        
        if snake.choca_consigo():
            juego_terminado = True
        
        if snake.choca_bordes(ANCHO, ALTO):
            juego_terminado = True
        
        if snake.cuerpo[0] == comida.posicion:
            snake.crece()
            puntuacion += 10
            comida.inicializar_posicion(ANCHO, ALTO, snake.cuerpo)
        
        pantalla.fill(NEGRO)
        
        snake.dibujar(pantalla)
        comida.dibujar(pantalla)
        
        texto_puntuacion = mostrar_puntuacion(puntuacion, fuente)
        pantalla.blit(texto_puntuacion, (10, 10))
        
        pygame.display.flip()
        reloj.tick(VELOCIDAD)


if __name__ == "__main__":
    main()
