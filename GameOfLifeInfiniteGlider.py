# 363 in 60s
# 6000 Cells

import pygame, sys, random
from pygame.locals import *

FPS = 5
LEFT = 1
RIGHT = 3

Steps = 0

CellSize = 75

CellWidth = 8
CellHeight = 8

WindowWidth = CellWidth * CellSize
WindowHeight = CellHeight * CellSize

Concentration = 2

#              R   G   B
Black      = (0  ,0  ,0  )
White      = (255,255,255)
DarkGray   = (40 ,40 ,40 )

def drawGrid():
	for x in range(0, WindowWidth, CellSize):
		pygame.draw.line(DisplayScreen, DarkGray, (x, 0), (x , WindowHeight))
	for y in range(0, WindowHeight, CellSize):
		pygame.draw.line(DisplayScreen, DarkGray, (0, y), (WindowWidth, y))

def blankGrid():
	gridDict = {}
	for y in range(CellHeight):
		for x in range(CellWidth):
			gridDict[x, y] = 0
	return gridDict

def startingGlider(lifeDict):
	lifeDict[ 3 , 2 ] = 1
	lifeDict[ 3 , 4 ] = 1
	lifeDict[ 4 , 4 ] = 1
	lifeDict[ 4 , 3 ] = 1
	lifeDict[ 2 , 4 ] = 1

	return lifeDict

def colourGrid(lifeDict):
	for item in lifeDict:
		x = item[0]
		y = item[1]
		x = x * CellSize
		y = y * CellSize

		if lifeDict[item] == 1:
			pygame.draw.rect(DisplayScreen, Black, (x, y, CellSize, CellSize))
		else:
			pygame.draw.rect(DisplayScreen, White, (x, y, CellSize, CellSize))

def getNeighbours(item, lifeDict):
	neighbours = 0
	for x in range (-1, 2):
		for y in range(-1, 2):
			checkCell = (item[0] + x, item[1] + y)
			X, Y = checkCell
			if checkCell[0] == -1:
				checkCell = (CellWidth -1, Y)
			elif checkCell[0] == CellHeight:
				checkCell = (0, Y)
			X, Y = checkCell
			if checkCell[1] == -1:
				checkCell = (X, CellHeight -1)
			elif checkCell[1] == CellHeight:
				checkCell = (X, 0)
			if checkCell[0] < CellWidth and checkCell[0] >= 0:
				if checkCell[1] < CellHeight and checkCell[1] >= 0:
					if lifeDict[checkCell] == 1:
						if x == 0 and y == 0:
							neighbours += 0
						else:
							neighbours += 1

	return neighbours

def tick(lifeDict):
	newTick = {}
	for item in lifeDict:
		numberNeighbours = getNeighbours(item, lifeDict)
		if lifeDict[item] == 1:
			if numberNeighbours < 2:
				newTick[item] = 0
			elif numberNeighbours > 3:
				newTick[item] = 0
			else:
				newTick[item] = 1
		else:
			if numberNeighbours == 3:
				newTick[item] = 1
			else:
				newTick[item] = 0

	return newTick

def terminate():
	pygame.quit()
	sys.exit()

def main():
	pygame.init()

	global DisplayScreen

	FPSClock = pygame.time.Clock()
	DisplayScreen = pygame.display.set_mode((WindowWidth, WindowHeight))
	pygame.display.set_caption('Game Of Life')
	DisplayScreen.fill(White)
	lifeDict = blankGrid()
	lifeDict = startingGlider(lifeDict)
	colourGrid(lifeDict)
	drawGrid()
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()

		lifeDict = tick(lifeDict)
		colourGrid(lifeDict)
		drawGrid()
		pygame.display.update()
		FPSClock.tick(FPS)

if __name__=='__main__':
	main()