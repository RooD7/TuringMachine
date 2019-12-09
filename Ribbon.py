
class Ribbon(object):

	# [print, block, state, left, head, right]

	def __init__(self):
		self.ribbon = []

	def getRibbon(self):
		return self.ribbon

	def setRibbon(self, ribbon):
		self.ribbon = ribbon

	def getPrint(self):
		return self.ribbon[0]
	
	def setPrint(self, fprint):
		self.ribbon[0] = fprint

	def getBlock(self):
		return self.ribbon[1]

	def setBlock(self, block):
		self.ribbon[1] = block

	def getState(self):
		return self.ribbon[2]

	def setState(self, state):
		self.ribbon[2] = state

	def getLeft(self):
		return self.ribbon[3]

	def setLeft(self, left):
		self.ribbon[3] = left

	def getHead(self):
		return self.ribbon[4]

	def setHead(self, head):
		self.ribbon[4] = head

	def getRight(self):
		return self.ribbon[5]

	def setRight(self, right):
		self.ribbon[5] = right