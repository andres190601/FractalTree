import pygame
import sys


pygame.init()
pygame.display.set_caption("Fractal Tree")
white, black = (255,255,255),(0,0,0)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
screen.fill(white)
fontGrande = pygame.font.Font('arial.ttf', 22)
fontRegular = pygame.font.Font('arial.ttf', 18)
text = fontGrande.render('Arboles Fractales', True, black, white)
textBoton1 = fontRegular.render('Prueba fitness', True, white, black)
textBoton2 = fontRegular.render('Generar arbol', True, white, black)
textRect = text.get_rect()
textBoton1Rect = textBoton1.get_rect()
textBoton2Rect = textBoton2.get_rect()

textRect.center = (width // 2, 40)
textBoton1Rect.center = (width // 2, 160)
textBoton2Rect.center =  (width // 2, 240)



running = True

def main():
    while running:
        screen.fill(white)
        screen.blit(text,textRect)
        screen.blit(textBoton1, textBoton1Rect)
        screen.blit(textBoton2, textBoton2Rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width // 2 -80 <= mouse[0] <= width // 2 + 140 and 140 <= mouse[1] <= 170:
                    pygame.quit()
                if width // 2 - 80 <= mouse[0] <= width // 2 + 140 and 220 <= mouse[1] <= 250:
                    ventanaGeneracionArbol()
            mouse = pygame.mouse.get_pos()

        pygame.display.update()

def ventanaGeneracionArbol():
    (width, height) = (300, 500)
    screenArbol = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Generar arbol')
    screenArbol.fill(white)
    pygame.display.flip()
    running = True
    textoGrosor = ''
    textoProfundidad = ''
    textoDecGrosor = ''
    textoDecLongitud = ''
    textoDecAngulo = ''
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    input_rect1 = pygame.Rect(width // 2, 100, 140, 32)
    input_rect2 = pygame.Rect(width // 2, 150, 140, 32)
    input_rect3 = pygame.Rect(width // 2, 200, 140, 32)
    input_rect4 = pygame.Rect(width // 2, 250, 140, 32)
    input_rect5 = pygame.Rect(width // 2, 300, 140, 32)
    active1 = False
    active2 = False
    active3 = False
    active4 = False
    active5 = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

if __name__=='__main__':
    main()
    pygame.quit()