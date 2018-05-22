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

	def newLine(self, bloco, estado, esquerda, cabecote, direita):
		bloco = '{0:>16}'.format(bloco)
		self.bloco = bloco.replace(' ','.')

		self.estado = '%04d' %(int(estado))

		esquerda = '{0:>20}'.format(esquerda)
		self.esquerda = esquerda.replace(' ','_')

		# cabecote = cabecote.split()
		self.cabecote = '%s%s%s' %(cabecote[0], direita[0], cabecote[1])

		direita = direita[:0] + direita[1:]
		direita = '{0:20}'.format(direita)
		self.direita = direita.replace(' ','_')

		model = '{Bloco}.{Estado}: {Esquerda}{Cabecote}{Direita}'
		model = model.format(Bloco=self.bloco, Estado=self.estado, Esquerda=self.esquerda, Cabecote=self.cabecote, Direita=self.direita)

		return model
