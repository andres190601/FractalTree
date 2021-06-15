import pygame, math, numpy as np, cv2 as cv, io, sys
from io import StringIO
from random import randint, random, sample
from PIL import Image
import cv2 as cv

target1 = cv.imread('silueta2.jpg')
target2 = cv.resize(target1, (1000, 750))
target = np.asarray(target2)

tasaMutacion = 0.6
cantidadIndividuos = 100
cantidadSeleccion = 20
cantidadGeneraciones = 10
verbose = True
ejemploArbol = [0, 0, 0, 0, 0, 0, 0, 0]



pygame.init()
white, black = ((255,255,255), (0, 0, 0))
window = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
screen.fill(white)







def drawTree(x1, y1, angulo, profundidad, grosor, decrecimiento_grosor, decrecimiento_longitud, decrecimiento_angulo):
    if profundidad > 0:
        valorRandAngulo = random()
        valorLargo = 1.0 + (valorRandAngulo * (1.0 - 1.9))
        formatted_string = "{:.1f}".format(valorLargo)
        valorRandAngulo = float(formatted_string)
        x2 = x1 + (int(math.cos(math.radians(angulo)) * profundidad * decrecimiento_longitud)  * valorRandAngulo)
        y2 = y1 + (int(math.sin(math.radians(angulo)) * profundidad * decrecimiento_longitud)  * valorRandAngulo)
        grosor = math.ceil(grosor * decrecimiento_grosor)
        pygame.draw.line(screen, (black), (x1, y1), (x2, y2), grosor)
        drawTree(x2, y2, angulo - decrecimiento_angulo, profundidad - 1, grosor, decrecimiento_grosor, decrecimiento_longitud, decrecimiento_angulo)
        drawTree(x2, y2, angulo + decrecimiento_angulo, profundidad - 1, grosor, decrecimiento_grosor, decrecimiento_longitud, decrecimiento_angulo)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)

def crearIndividuo():
    valorGrosorPrev = random()
    valorGrosor = 0.7 + (valorGrosorPrev * (1.12 - 0.7))
    formatted_string = "{:.2f}".format(valorGrosor)
    valorGrosor = float(formatted_string)
    valorLargoPrev = random()
    valorLargo = 19 + (valorLargoPrev * (19 - 22))
    formatted_string = "{:.1f}".format(valorLargo)
    valorLargo = float(formatted_string)
    individuo = [500, 750, -90, randint(7,12), randint(5,45), valorGrosor, valorLargo, randint(13,40)]
    # drawTree(individuo[0], individuo[1], individuo[2], individuo[3], individuo[4], individuo[5], individuo[6], individuo[7])
    return individuo

def crearPoblacion():
    poblacionArboles = [crearIndividuo() for i in range(cantidadIndividuos)]
    return poblacionArboles

def fitness(individuo):
    screen.fill(white)
    drawTree(individuo[0], individuo[1], individuo[2], individuo[3], individuo[4], individuo[5], individuo[6], individuo[7])
    pygame.display.flip()
    pygame.time.delay(1)
    arrayArbol = pygame.surfarray.array3d(window)
    arrayArbol = arrayArbol.swapaxes(0, 1)
    return np.sum((target-arrayArbol)**2)

def seleccion(poblacionArboles):
    fitnessRate = [(fitness(arbol), arbol) for arbol in poblacionArboles]
    fitnessRate = [arbol[1] for arbol in sorted(fitnessRate, reverse=True)]
    seleccionados  = fitnessRate[len(fitnessRate) - cantidadSeleccion :]
    return seleccionados

def reproduccion(poblacion, seleccionados):
    punto = 0
    padre = []

    for i in range(len(poblacion)):
        punto = np.random.randint(3, len(ejemploArbol) - 1)
        padre = sample(seleccionados,2)

        poblacion[i][:punto] = padre[0][:punto]
        poblacion[i][punto:] = padre[1][punto:]

    return poblacion

def mutacion(poblacion):

    for i in range(len(poblacion)):
        if np.random.random() <= tasaMutacion:
            punto = randint(3, len(ejemploArbol) - 1)

            if punto == 3:
                nuevoValor = randint(7, 12)

            elif punto == 4:
                nuevoValor = randint(5, 45)

            elif punto == 5:
                valorGrosorPrev = random()
                valorGrosor = 0.7 + (valorGrosorPrev * (1.12 - 0.7))
                formatted_string = "{:.2f}".format(valorGrosor)
                nuevoValor = float(formatted_string)

            elif punto == 6:
                valorLargoPrev = random()
                valorLargo = 19 + (valorLargoPrev * (19 - 22))
                formatted_string = "{:.1f}".format(valorLargo)
                nuevoValor = float(formatted_string)

            elif punto == 7:
                nuevoValor = randint(13, 40)

            while nuevoValor == poblacion[i][punto]:
                if punto == 3:
                    nuevoValor = randint(7, 12)

                elif punto == 4:
                    nuevoValor = randint(5, 45)

                elif punto == 5:
                    valorGrosorPrev = random()
                    valorGrosor = 0.7 + (valorGrosorPrev * (1.12 - 0.7))
                    formatted_string = "{:.2f}".format(valorGrosor)
                    nuevoValor = float(formatted_string)

                elif punto == 6:
                    valorLargoPrev = random()
                    valorLargo = 19 + (valorLargoPrev * (19 - 22))
                    formatted_string = "{:.1f}".format(valorLargo)
                    nuevoValor = float(formatted_string)

                elif punto == 7:
                    nuevoValor = randint(13, 40)

            poblacion[i][punto] = nuevoValor

            return poblacion

def runAlgoGenetico():

    poblacion = crearPoblacion()

    for i in range(cantidadGeneraciones):
        print('________________________________')
        print('GENERACION: ', i)
        print('GROSOR: ', poblacion)

        seleccionados = seleccion(poblacion)
        poblacion = reproduccion(poblacion, seleccionados)
        poblacion = mutacion(poblacion)

    print('________________________________')
    print('PROFUNIDAD: ', poblacion[0][3])
    print('GROSOR: ', poblacion[0][4])
    print('DECRECIMIENTO GROSOR: ', poblacion[0][5])
    print('DECRECIMIENTO LONGITUD: ', poblacion[0][6])
    print('DECRECIMIENTO ANGULO: ', poblacion[0][7])
    print('________________________________')
    print(poblacion[0])
    cv.imshow('Arbol target',target2)





runAlgoGenetico()













while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Press Esc to quit.
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.QUIT:
                running = False