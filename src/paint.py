#!/usr/bin/python
from color import printc
from getchunix import getch
import os

screenSize = 32
yPos = 0
xPos = 0
colorPos = {}
ctn = ['normal','black','blue','green','cyan','red','purple','yellow','dark gray','bright cyan']


def save():
	global colorPos
	name = raw_input('save to - name (no extension): ')
	if name != '':
		n = open(name + '.txt','w')
		for i in colorPos:
			n.write(str(i) + ':' + str(colorPos[i]))
			n.write('\n')
		n.close()

def openp():
	global colorPos
	name = raw_input('open - name (no extension): ')
	if name != '':		
		n = open(name + '.txt','r')
		colorPos = {}
		for line in n:
			colorPos[eval(line[0:(line.index(':'))])] = line[(line.index(':') + 1):].strip('\n')

def draw(i):
	global xPos
	global yPos
	global colorPos
	global ctn
	if i == 'w':
		yPos -= 1
	elif i == 's':
		yPos += 1
	elif i == 'a':
		xPos -= 1
	elif i == 'd':
		xPos += 1
	elif str(i) in '0123456789':
		colorPos[(xPos,yPos)] = ctn[int(i)]
	elif i == 'x':
		exit()
	elif i == 'e':
		try:
			del colorPos[(xPos,yPos)]
		except:
			pass
	elif i == 'n':
		save()
	elif i == 'm':
		openp()
	else:
		print 'error: command not found'
	yPos %= screenSize
	xPos %= screenSize

def paint():
	global xPos
	global yPos
	global colorPos
	global screenSize
	global ctn
	os.system('clear')
	for y in range(screenSize):
		for x in range(screenSize):
			if x == xPos and y == yPos:
				printc(u'\u2605','bright green'),
				continue
			elif (x,y) in colorPos:
				printc(u'\u25A0',colorPos[(x,y)]),
				continue
			printc(u'\u25A0','white'),
		print ''
	print '{1 - black, 2 - blue, 3 - green, 4 - cyan, 5 - red, 6 - purple, 7 - yellow/brown, 8 - dark gray, 9 - bright cyan, 0 - normal}\n'

			

#os.system('gnome-terminal')
paint()
print '\n'
while True:
	draw(getch())
	paint()

