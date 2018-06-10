import pygame, sys, random
from pygame.locals import *

FPS = 20
LEFT = 1
RIGHT = 3

CellSize = 25

WindowWidth = 1700
WindowHeight = 900

CellWidth = WindowWidth // CellSize
CellHeight = WindowHeight // CellSize

Concentration = 2 # Concentration of Live Cells when Generated Randomly 

#              R   G   B
Black      = (0  ,0  ,0  )
White      = (255,255,255)
DarkGray   = (40 ,40 ,40 )

def startingOne(lifeDict):
	lifeDict[ 24 , 14 ] = 1
	lifeDict[ 24 , 15 ] = 1
	lifeDict[ 26 , 14 ] = 1
	lifeDict[ 26 , 16 ] = 1
	lifeDict[ 24 , 16 ] = 1
	lifeDict[ 26 , 15 ] = 1
	lifeDict[ 26 , 17 ] = 1
	lifeDict[ 24 , 17 ] = 1
	lifeDict[ 23 , 14 ] = 1
	lifeDict[ 25 , 17 ] = 1
	lifeDict[ 25 , 15 ] = 1
	lifeDict[ 25 , 16 ] = 1
	lifeDict[ 25 , 14 ] = 1

	return lifeDict

def startingTwo(lifeDict):
	lifeDict[2, 5] = 1
	lifeDict[2, 6] = 1
	lifeDict[3, 7] = 1
	lifeDict[3, 8] = 1
	lifeDict[12, 5] = 1
	lifeDict[12, 6] = 1
	lifeDict[12, 7] = 1
	lifeDict[13, 4] = 1
	lifeDict[13, 8] = 1
	lifeDict[14, 3] = 1
	lifeDict[14, 9] = 1
	lifeDict[15, 3] = 1
	lifeDict[15, 9] = 1
	lifeDict[16, 6] = 1
	lifeDict[17, 4] = 1
	lifeDict[17, 8] = 1
	lifeDict[18, 5] = 1
	lifeDict[18, 6] = 1
	lifeDict[18, 7] = 1
	lifeDict[19, 6] = 1
	lifeDict[22, 3] = 1
	lifeDict[22, 4] = 1
	lifeDict[22, 5] = 1
	lifeDict[23, 3] = 1
	lifeDict[23, 4] = 1
	lifeDict[23, 5] = 1
	lifeDict[24, 2] = 1
	lifeDict[24, 6] = 1
	lifeDict[26, 1] = 1
	lifeDict[26, 2] = 1
	lifeDict[26, 6] = 1
	lifeDict[26, 7] = 1
	lifeDict[36, 3] = 1
	lifeDict[36, 4] = 1
	lifeDict[37, 3] = 1
	lifeDict[37, 4] = 1

	return lifeDict

def startingThree(lifeDict):	
	lifeDict[ 28 , 1 ] = 1
	lifeDict[ 57 , 1 ] = 1
	lifeDict[ 25 , 2 ] = 1
	lifeDict[ 26 , 2 ] = 1
	lifeDict[ 27 , 2 ] = 1
	lifeDict[ 28 , 2 ] = 1
	lifeDict[ 54 , 2 ] = 1
	lifeDict[ 55 , 2 ] = 1
	lifeDict[ 56 , 2 ] = 1
	lifeDict[ 57 , 2 ] = 1
	lifeDict[ 20 , 3 ] = 1
	lifeDict[ 23 , 3 ] = 1
	lifeDict[ 25 , 3 ] = 1
	lifeDict[ 26 , 3 ] = 1
	lifeDict[ 49 , 3 ] = 1
	lifeDict[ 52 , 3 ] = 1
	lifeDict[ 54 , 3 ] = 1
	lifeDict[ 55 , 3 ] = 1
	lifeDict[ 20 , 4 ] = 1
	lifeDict[ 49 , 4 ] = 1
	lifeDict[ 7 , 5 ] = 1
	lifeDict[ 8 , 5 ] = 1
	lifeDict[ 9 , 5 ] = 1
	lifeDict[ 10 , 5 ] = 1
	lifeDict[ 19 , 5 ] = 1
	lifeDict[ 23 , 5 ] = 1
	lifeDict[ 25 , 5 ] = 1
	lifeDict[ 26 , 5 ] = 1
	lifeDict[ 36 , 5 ] = 1
	lifeDict[ 37 , 5 ] = 1
	lifeDict[ 38 , 5 ] = 1
	lifeDict[ 39 , 5 ] = 1
	lifeDict[ 48 , 5 ] = 1
	lifeDict[ 52 , 5 ] = 1
	lifeDict[ 54 , 5 ] = 1
	lifeDict[ 55 , 5 ] = 1
	lifeDict[ 7 , 6 ] = 1
	lifeDict[ 11 , 6 ] = 1
	lifeDict[ 17 , 6 ] = 1
	lifeDict[ 18 , 6 ] = 1
	lifeDict[ 20 , 6 ] = 1
	lifeDict[ 21 , 6 ] = 1
	lifeDict[ 23 , 6 ] = 1
	lifeDict[ 25 , 6 ] = 1
	lifeDict[ 27 , 6 ] = 1
	lifeDict[ 28 , 6 ] = 1
	lifeDict[ 29 , 6 ] = 1
	lifeDict[ 30 , 6 ] = 1
	lifeDict[ 31 , 6 ] = 1
	lifeDict[ 36 , 6 ] = 1
	lifeDict[ 40 , 6 ] = 1
	lifeDict[ 46 , 6 ] = 1
	lifeDict[ 47 , 6 ] = 1
	lifeDict[ 49 , 6 ] = 1
	lifeDict[ 50 , 6 ] = 1
	lifeDict[ 52 , 6 ] = 1
	lifeDict[ 54 , 6 ] = 1
	lifeDict[ 56 , 6 ] = 1
	lifeDict[ 57 , 6 ] = 1
	lifeDict[ 58 , 6 ] = 1
	lifeDict[ 59 , 6 ] = 1
	lifeDict[ 60 , 6 ] = 1
	lifeDict[ 7 , 7 ] = 1
	lifeDict[ 17 , 7 ] = 1
	lifeDict[ 18 , 7 ] = 1
	lifeDict[ 20 , 7 ] = 1
	lifeDict[ 22 , 7 ] = 1
	lifeDict[ 24 , 7 ] = 1
	lifeDict[ 27 , 7 ] = 1
	lifeDict[ 28 , 7 ] = 1
	lifeDict[ 29 , 7 ] = 1
	lifeDict[ 30 , 7 ] = 1
	lifeDict[ 31 , 7 ] = 1
	lifeDict[ 36 , 7 ] = 1
	lifeDict[ 46 , 7 ] = 1
	lifeDict[ 47 , 7 ] = 1
	lifeDict[ 49 , 7 ] = 1
	lifeDict[ 51 , 7 ] = 1
	lifeDict[ 53 , 7 ] = 1
	lifeDict[ 56 , 7 ] = 1
	lifeDict[ 57 , 7 ] = 1
	lifeDict[ 58 , 7 ] = 1
	lifeDict[ 59 , 7 ] = 1
	lifeDict[ 60 , 7 ] = 1
	lifeDict[ 8 , 8 ] = 1
	lifeDict[ 11 , 8 ] = 1
	lifeDict[ 14 , 8 ] = 1
	lifeDict[ 15 , 8 ] = 1
	lifeDict[ 18 , 8 ] = 1
	lifeDict[ 22 , 8 ] = 1
	lifeDict[ 23 , 8 ] = 1
	lifeDict[ 24 , 8 ] = 1
	lifeDict[ 27 , 8 ] = 1
	lifeDict[ 29 , 8 ] = 1
	lifeDict[ 30 , 8 ] = 1
	lifeDict[ 37 , 8 ] = 1
	lifeDict[ 40 , 8 ] = 1
	lifeDict[ 43 , 8 ] = 1
	lifeDict[ 44 , 8 ] = 1
	lifeDict[ 47 , 8 ] = 1
	lifeDict[ 51 , 8 ] = 1
	lifeDict[ 52 , 8 ] = 1
	lifeDict[ 53 , 8 ] = 1
	lifeDict[ 56 , 8 ] = 1
	lifeDict[ 58 , 8 ] = 1
	lifeDict[ 59 , 8 ] = 1
	lifeDict[ 13 , 9 ] = 1
	lifeDict[ 16 , 9 ] = 1
	lifeDict[ 18 , 9 ] = 1
	lifeDict[ 19 , 9 ] = 1
	lifeDict[ 42 , 9 ] = 1
	lifeDict[ 45 , 9 ] = 1
	lifeDict[ 47 , 9 ] = 1
	lifeDict[ 48 , 9 ] = 1
	lifeDict[ 13 , 10 ] = 1
	lifeDict[ 18 , 10 ] = 1
	lifeDict[ 19 , 10 ] = 1
	lifeDict[ 42 , 10 ] = 1
	lifeDict[ 47 , 10 ] = 1
	lifeDict[ 48 , 10 ] = 1
	lifeDict[ 13 , 11 ] = 1
	lifeDict[ 16 , 11 ] = 1
	lifeDict[ 18 , 11 ] = 1
	lifeDict[ 19 , 11 ] = 1
	lifeDict[ 42 , 11 ] = 1
	lifeDict[ 45 , 11 ] = 1
	lifeDict[ 47 , 11 ] = 1
	lifeDict[ 48 , 11 ] = 1
	lifeDict[ 8 , 12 ] = 1
	lifeDict[ 11 , 12 ] = 1
	lifeDict[ 14 , 12 ] = 1
	lifeDict[ 15 , 12 ] = 1
	lifeDict[ 18 , 12 ] = 1
	lifeDict[ 22 , 12 ] = 1
	lifeDict[ 23 , 12 ] = 1
	lifeDict[ 24 , 12 ] = 1
	lifeDict[ 27 , 12 ] = 1
	lifeDict[ 29 , 12 ] = 1
	lifeDict[ 30 , 12 ] = 1
	lifeDict[ 37 , 12 ] = 1
	lifeDict[ 40 , 12 ] = 1
	lifeDict[ 43 , 12 ] = 1
	lifeDict[ 44 , 12 ] = 1
	lifeDict[ 47 , 12 ] = 1
	lifeDict[ 51 , 12 ] = 1
	lifeDict[ 52 , 12 ] = 1
	lifeDict[ 53 , 12 ] = 1
	lifeDict[ 56 , 12 ] = 1
	lifeDict[ 58 , 12 ] = 1
	lifeDict[ 59 , 12 ] = 1
	lifeDict[ 7 , 13 ] = 1
	lifeDict[ 17 , 13 ] = 1
	lifeDict[ 18 , 13 ] = 1
	lifeDict[ 20 , 13 ] = 1
	lifeDict[ 22 , 13 ] = 1
	lifeDict[ 24 , 13 ] = 1
	lifeDict[ 27 , 13 ] = 1
	lifeDict[ 28 , 13 ] = 1
	lifeDict[ 29 , 13 ] = 1
	lifeDict[ 30 , 13 ] = 1
	lifeDict[ 31 , 13 ] = 1
	lifeDict[ 36 , 13 ] = 1
	lifeDict[ 46 , 13 ] = 1
	lifeDict[ 47 , 13 ] = 1
	lifeDict[ 49 , 13 ] = 1
	lifeDict[ 51 , 13 ] = 1
	lifeDict[ 53 , 13 ] = 1
	lifeDict[ 56 , 13 ] = 1
	lifeDict[ 57 , 13 ] = 1
	lifeDict[ 58 , 13 ] = 1
	lifeDict[ 59 , 13 ] = 1
	lifeDict[ 60 , 13 ] = 1
	lifeDict[ 7 , 14 ] = 1
	lifeDict[ 11 , 14 ] = 1
	lifeDict[ 17 , 14 ] = 1
	lifeDict[ 18 , 14 ] = 1
	lifeDict[ 20 , 14 ] = 1
	lifeDict[ 21 , 14 ] = 1
	lifeDict[ 23 , 14 ] = 1
	lifeDict[ 25 , 14 ] = 1
	lifeDict[ 27 , 14 ] = 1
	lifeDict[ 28 , 14 ] = 1
	lifeDict[ 29 , 14 ] = 1
	lifeDict[ 30 , 14 ] = 1
	lifeDict[ 31 , 14 ] = 1
	lifeDict[ 36 , 14 ] = 1
	lifeDict[ 40 , 14 ] = 1
	lifeDict[ 46 , 14 ] = 1
	lifeDict[ 47 , 14 ] = 1
	lifeDict[ 49 , 14 ] = 1
	lifeDict[ 50 , 14 ] = 1
	lifeDict[ 52 , 14 ] = 1
	lifeDict[ 54 , 14 ] = 1
	lifeDict[ 56 , 14 ] = 1
	lifeDict[ 57 , 14 ] = 1
	lifeDict[ 58 , 14 ] = 1
	lifeDict[ 59 , 14 ] = 1
	lifeDict[ 60 , 14 ] = 1
	lifeDict[ 7 , 15 ] = 1
	lifeDict[ 8 , 15 ] = 1
	lifeDict[ 9 , 15 ] = 1
	lifeDict[ 10 , 15 ] = 1
	lifeDict[ 19 , 15 ] = 1
	lifeDict[ 23 , 15 ] = 1
	lifeDict[ 25 , 15 ] = 1
	lifeDict[ 26 , 15 ] = 1
	lifeDict[ 36 , 15 ] = 1
	lifeDict[ 37 , 15 ] = 1
	lifeDict[ 38 , 15 ] = 1
	lifeDict[ 39 , 15 ] = 1
	lifeDict[ 48 , 15 ] = 1
	lifeDict[ 52 , 15 ] = 1
	lifeDict[ 54 , 15 ] = 1
	lifeDict[ 55 , 15 ] = 1
	lifeDict[ 20 , 16 ] = 1
	lifeDict[ 49 , 16 ] = 1
	lifeDict[ 20 , 17 ] = 1
	lifeDict[ 23 , 17 ] = 1
	lifeDict[ 25 , 17 ] = 1
	lifeDict[ 26 , 17 ] = 1
	lifeDict[ 49 , 17 ] = 1
	lifeDict[ 52 , 17 ] = 1
	lifeDict[ 54 , 17 ] = 1
	lifeDict[ 55 , 17 ] = 1
	lifeDict[ 25 , 18 ] = 1
	lifeDict[ 26 , 18 ] = 1
	lifeDict[ 27 , 18 ] = 1
	lifeDict[ 28 , 18 ] = 1
	lifeDict[ 54 , 18 ] = 1
	lifeDict[ 55 , 18 ] = 1
	lifeDict[ 56 , 18 ] = 1
	lifeDict[ 57 , 18 ] = 1
	lifeDict[ 28 , 19 ] = 1
	lifeDict[ 57 , 19 ] = 1

	return lifeDict

	return lifeDict

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

def startingGridRandom(lifeDict):
	for item in lifeDict:
		lifeDict[item] = random.randint(0, Concentration)
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
			elif checkCell[0] == CellWidth:
				checkCell = (0, Y)
			X, Y = checkCell
			if checkCell[1] == -1:
				checkCell = (X, CellHeight -1)
			elif checkCell[1] == CellHeight:
				checkCell = (X, 0)
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

def setLiveState(mousePositionX, mousePositionY, lifeDict):
	cellPositionX = round(mousePositionX / CellSize)
	cellPositionY = round(mousePositionY / CellSize)
	lifeDict[cellPositionX, cellPositionY] = 1


	return lifeDict

def setDeadState(mousePositionX, mousePositionY, lifeDict):
	cellPositionX = round(mousePositionX / CellSize)
	cellPositionY = round(mousePositionY / CellSize)
	lifeDict[cellPositionX, cellPositionY] = 0

	return lifeDict

def terminate():
	pygame.quit()
	sys.exit()

def main():
	pygame.init()

	global DisplayScreen

	Steps = 0
	run = False
	leftDown = False
	rightDown = False

	FPSClock = pygame.time.Clock()
	DisplayScreen = pygame.display.set_mode((WindowWidth, WindowHeight))
	pygame.display.set_caption('Game Of Life')
	DisplayScreen.fill(White)
	lifeDict = blankGrid()
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
				elif event.key == K_r:
					lifeDict = startingGridRandom(lifeDict)
					run = True
				elif event.key == K_b:
					lifeDict = blankGrid()
					colourGrid(lifeDict)
					drawGrid()
					pygame.display.update()
					run = False
				elif event.key == K_1:
					lifeDict = startingOne(lifeDict)
					run = True
				elif event.key == K_2:
					lifeDict = startingTwo(lifeDict)
					run = True
				elif event.key == K_3:
					lifeDict = startingThree(lifeDict)
					run = True
				elif event.key == K_SPACE:
					if run == True:
						run = False
						print ("//////////////////////////////////////////////////////////////////////////////////////////////")
						for item in lifeDict:
							if lifeDict[item] == 1:
								cellX, cellY = item
								print ("lifeDict[",cellX,",",cellY,"] = 1")
						print ("//////////////////////////////////////////////////////////////////////////////////////////////")
					else:
						print ("//////////////////////////////////////////////////////////////////////////////////////////////")
						for item in lifeDict:
							if lifeDict[item] == 1:
								cellX, cellY = item
								print ("lifeDict[",cellX,",",cellY,"] = 1")
						print ("//////////////////////////////////////////////////////////////////////////////////////////////")
						run = True
			elif event.type == MOUSEBUTTONDOWN: 
				if event.button == LEFT:
					leftDown = True
				elif event.button == RIGHT:
					rightDown = True
			
			elif event.type == pygame.MOUSEBUTTONUP: 
				if event.button == LEFT:
					leftDown = False
				elif event.button == RIGHT:
					rightDown = False
					
		if leftDown == True:
			mousePositionX, mousePositionY = pygame.mouse.get_pos()
			lifeDict = setLiveState(mousePositionX, mousePositionY, lifeDict)
			colourGrid(lifeDict)
			drawGrid()
			pygame.display.update()

		if rightDown == True:
			mousePositionX, mousePositionY = pygame.mouse.get_pos()
			lifeDict = setDeadState(mousePositionX, mousePositionY, lifeDict)
			colourGrid(lifeDict)
			drawGrid()
			pygame.display.update()

		if run == True:
			lifeDict = tick(lifeDict)
			colourGrid(lifeDict)
			drawGrid()
			pygame.display.update()
		FPSClock.tick(FPS)

if __name__=='__main__':
	main()