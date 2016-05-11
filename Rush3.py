import pygame
import time
from pygame.locals import *
from random import randrange
pygame.init()
pygame.display.set_caption("Rush3")

##########
updates = False
##########

castle =  pygame.image.load("castle.png")
coin =  pygame.image.load("coin.png")
sword =  pygame.image.load("sword.png")

isimler = ["Ralfi", "Riva", "Semih"]

#KEY: 		 R  G  B
red = 		(255,0,0)
green = 	(0,255,0)
blue = 		(0,0,255)
darkBlue =	(0,0,128)
white = 	(255,255,255)
black = 	(0,0,0)
pink = 		(255,200,200)
cyan = 		(0,255,255)
yellow = 	(255,255,0)
brown = 	(139,69,19)
orange = 	(255,165,0)

Width = 955
Height = 640
screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(orange)
screen.blit(background,(0,0))

font = pygame.font.Font(None, 18)
text = font.render("", 1, black)
textpos = text.get_rect()

array = []

#INDEX KEY
OWNER = 0
NUM = 1
TYPE = 2
CARDS = 3
ADJACENT = 4
LOCATION = 5
COLOUR = 6
x,y = 0,1

turnOwner = "BLUE"

#KEY:		 OWNER, NUM, TYPE, CARDS, ADJACENT, LOCATION, COLOUR
array.append(["NONE", 0, "TA", [0, 0], (1, 3), (50,140), cyan])
array.append(["BLUE", 1, "TCA", [0, 0, 0], (0, 2, 4, 5), (15,260), cyan])
array.append(["NONE", 2, "TA", [0, 0], (1, 6), (50,380), cyan])
array.append(["NONE", 3, "TCA", [0, 0, 0], (0, 7, 8), (210,80), green])
array.append(["NONE", 4, "C", [0], (1), (250,200), cyan])
array.append(["NONE", 5, "C", [0], (1), (250,320), cyan])
array.append(["NONE", 6, "AT", [0, 0], (2, 10), (210,440), brown])
array.append(["NONE", 7, "TA", [0, 0], (3, 11), (440,20), green]),
array.append(["NONE", 8, "TC", [0, 0], (3), (440,140), green])
array.append(["NONE", 9, "CT", [0, 0], (14), (370,380), brown])
array.append(["NONE", 10, "AT", [0, 0], (6, 14), (370,500), brown])
array.append(["NONE", 11, "TA", [0, 0], (7, 15), (600,80), green])
array.append(["NONE", 12, "C", [0], (16), (630,200), pink])
array.append(["NONE", 13, "C", [0], (16), (630,320), pink])
array.append(["NONE", 14, "ACT", [0, 0, 0], (9, 10, 17), (530,440), brown])
array.append(["NONE", 15, "AT", [0, 0], (11, 16), (760,140), pink])
array.append(["RED", 16, "ACT", [0, 0, 0], (12, 13, 15, 17), (725,260), pink])
array.append(["NONE", 17, "AT", [0, 0], (14, 16), (760,380), pink])

#Prints the information for group 'number'
def getInfo(number):
	return "OWNER:", array[number][OWNER], "  NUMBER:", array[number][NUM], "  TYPE:", array[number][TYPE], "  CARDS:", array[number][CARDS], "  ADJACENT TO:", array[number][ADJACENT], "  LOCATION:", array[number][LOCATION], "  COLOUR:", array[number][COLOUR]

#Changes the owner of group 'number' to a new color.
def changeOwner(number, new):
	if new.upper() == "RED" or new.upper() == "BLUE":
		array[number][0] = new
		print "Changed owner of", number, "to", new
		print number, "is now", array[number]
		print
	else:
		print "Problem assigning owner"

def attackTo(attacking, defending):
	if number[defending][TYPE] == "TA" or number[defending][TYPE] == "TCA":
		if number[attacking][CARDS][2] > 0 and number[attacking][OWNER] == turnOwner:
			pass
	else: #TODO: No tower, will check for adjacent friendly block for conquering.
		pass

def DrawLines():
	for item in range(len(array)):
		try:
			for adjacent in range(len(array[item][ADJACENT])):
				end = array[item][ADJACENT][adjacent]
				startloc = (array[item][LOCATION][x]+35,array[item][LOCATION][y]+50)
				endloc = (array[end][LOCATION][x]+35,array[end][LOCATION][y]+50)
				pygame.draw.line(screen, black, startloc, endloc, 15)
				if(updates): pygame.display.update()
		except: #print "Problem while printing line", item
			pass

#Draws screen for next update
def Draw():
	screen.blit(background,(0,0))

	DrawLines()

	for item in range(len(array)):
		add = 0
		current = 0
		for count in range(len(array[item][TYPE])):
			pygame.draw.rect(screen, array[item][COLOUR], (array[item][LOCATION][x]+add,array[item][LOCATION][y],70,100), 0)

			if array[item][TYPE][current] == "T":
				screen.blit(castle,(array[item][LOCATION][x]+add+5,array[item][LOCATION][y]+15))
			elif array[item][TYPE][current] == "C":
				screen.blit(coin,(array[item][LOCATION][x]+add+5,array[item][LOCATION][y]+15))
			else:
				screen.blit(sword,(array[item][LOCATION][x]+add+5,array[item][LOCATION][y]+15))

			if array[item][OWNER] == "NONE":
				pygame.draw.rect(screen, black, (array[item][LOCATION][x]+add,array[item][LOCATION][y],70,100), 1)
			elif array[item][OWNER] == "BLUE":
				pygame.draw.rect(screen, blue, (array[item][LOCATION][x]+add,array[item][LOCATION][y],70,100), 3)
			else:
				pygame.draw.rect(screen, red, (array[item][LOCATION][x]+add,array[item][LOCATION][y],70,100), 3)

			add += 70
			current += 1
			
			if(updates): pygame.display.update()
		
		text = font.render(str(item), 1, white)
		textpos.x = array[item][LOCATION][x]+10
		textpos.y = array[item][LOCATION][y]+10
		screen.blit(text, textpos)

#Main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()
			if event.key == K_u:
				if(updates): updates = False
				else: updates = True

	Draw()

	p = pygame.mouse.get_pos()
	
	for position in range(len(array)):
		if p[0] > array[position][LOCATION][0] and p[0] < (array[position][LOCATION][0] + 70*len(array[position][TYPE])):
			if p[1] > array[position][LOCATION][1] and p[1] < (array[position][LOCATION][1] + 100):
				pygame.draw.rect(screen, white, (array[position][LOCATION][x],array[position][LOCATION][y],70*len(array[position][TYPE]),100), 5)

				text = font.render(str(getInfo(position)), 1, white)
				textpos.x = 5
				textpos.y = Height-25
				screen.blit(text, textpos)


	pygame.display.update()