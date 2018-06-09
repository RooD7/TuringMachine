#!/usr/bin/python

class Output(object):
	def __init__(self):
		self.bloco = '................'
		self.estado = '0000'
		self.esquerda = '____________________'
		self.cabecote = '(e)'
		self.direita = '____________________'

	def newLineClear(self):
		return self.bloco+'.'+self.estado+': '+self.esquerda+self.cabecote+self.direita

	def getCabecote(self, line):
		stra = line[4]
		return stra[1]

	def moveCabecote(self, line, direcao):
		# print('Antigo: ', self.esquerda+' - '+self.cabecote+' - '+self.direita)
		# print('Novo: ', esquerda+' - '+cabecote+' - '+direita)
		esquerda = line[3]
		cabecote = line[4]
		direita  = line[5]
		# move para esquerda
		if direcao == 'e':
			self.direita  = cabecote[1] + direita
			self.cabecote = '%s%s%s' %(cabecote[0], esquerda[len(esquerda)-1], cabecote[2])
			self.esquerda = esquerda[:len(esquerda)-1]
		# move para direita
		elif direcao == 'd':
			self.esquerda  = esquerda + cabecote[1]
			self.cabecote  = '%s%s%s' %(cabecote[0], direita[0], cabecote[2])
			self.direita   = direita[1:]
		elif direcao == 'i':
			pass

		# cria uma nova linha para poder atualizar a string line[0]
		return self.newLine(line[1], line[2], self.esquerda,self.cabecote,self.direita)

	def alteraCabecote(self, line, read, white):
		if self.getCabecote(line) != read:
			print('Cabecote - Erro Escrita!')
			print('Cabecote('+self.getCabecote(line)+') - read('+read+')')
			exit()

		cabecote = line[4]
		self.cabecote = '%s%s%s' %(cabecote[0], white, cabecote[2])
		return self.newLine(line[1], line[2], line[3], self.cabecote, line[5])

	def newLine(self, bloco, estado, esquerda, cabecote, direita):
		bloco = '{0:>16}'.format(bloco)
		self.bloco = bloco.replace(' ','.')

		self.estado = '%04d' %(int(estado))

		esquerda = '{0:>20}'.format(esquerda)
		self.esquerda = esquerda.replace(' ','_')

		# cabecote = cabecote.split()
		# self.cabecote = '%s%s%s' %(cabecote[0], direita[0], cabecote[1])
		if len(cabecote) == 2:
			self.cabecote = '%s%s%s' %(cabecote[0], direita[0], cabecote[1])
			direita = direita[:0] + direita[1:]
		else:
			self.cabecote = cabecote

		# direita = direita[:0] + direita[1:]
		direita = '{0:20}'.format(direita)
		self.direita = direita.replace(' ','_')

		model = '{Bloco}.{Estado}: {Esquerda}{Cabecote}{Direita}'
		model = model.format(Bloco=self.bloco, Estado=self.estado, Esquerda=self.esquerda, Cabecote=self.cabecote, Direita=self.direita)

		itens = [model, self.bloco, self.estado, self.esquerda, self.cabecote, self.direita]
		return itens
