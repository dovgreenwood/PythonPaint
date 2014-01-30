
from color import printc

class Map2D(object):
	def __init__(self,initx,inity,xlen,ylen,empty,marker,char,*colors):
		self.xpos = initx
		self.ypos = inity
		self.xlen = xlen
		self.ylen = ylen
		self.empty = empty
		self.marker = marker
		self.char = char
		self.marks = []
		try:
			self.colors = {'empty':colors[0],'marker':colors[1],'char':colors[2]}
		except:
			pass
	def controls(self,up,down,right,left,mark,erase,quit):
		self.UP = up
		self.DOWN = down
		self.RIGHT = right
		self.LEFT = left
		self.MARK = mark
		self.ERASE = erase
		self.QUIT = quit
	def move(self, command):
		if command == self.UP:
			self.ypos -= 1
		elif command == self.DOWN:
			self.ypos += 1
		elif command == self.RIGHT:
			self.xpos += 1
		elif command == self.LEFT:
			self.xpos -= 1
		elif command == self.QUIT:
			exit()
		elif command == self.MARK:
			self.marks.append((self.xpos,self.ypos))
		elif command == self.ERASE:
			try:
				del self.marks[self.marks.index((self.xpos,self.ypos))]
			except:
				pass
		else:
			print 'Error: command entered is unavailable'
		self.xpos %= self.xlen
		self.ypos %= self.ylen
	def __str__(self):
		for y in range(self.ylen):
			for x in range(self.xlen):
				if y == self.ypos and x == self.xpos:
					try:
						printc(self.char,self.colors['char'])
					except:
						print self.char,
					continue
				elif (x, y) in self.marks:
					try:
						printc(self.marker,self.colors['marker'])
					except:
						print self.marker,
					continue
				try:
					printc(self.empty,self.colors['empty'])
				except:
					print self.empty,
			print ''
		return ''























