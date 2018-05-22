#!/usr/bin/python
import os
import re

class InputFile(object):

	def __init__(self):
		self.param = []

	def inputs(self, patchFile):
		#Realiza a leitura do arquivo
		if os.path.isfile(patchFile):
			# self.param = self.readFile()
			file = open(patchFile,'r')
			# for l in file:
			# 	print(l)
			self.param = file.readlines()
			# print(self.param)
			file.close()
			
		else:
			self.param = None		
			print('Arquivo informado não existe!')	
			exit()

		# Chamada de bloco
		expB1 = r'^[0-9]{1,4}\s[a-zA-Z0-9]{1,16}\s[0-9]{1,4}\n?'
		expB2 = r'^bloco\s[a-zA-Z0-9]{1,16}\s[0-9]{1,4}\n?'
		expB3 = r'^fim?'
		expC1 = r'^[0-9]{0,4}\s[a-zA-Z]{0,16}\n?'
		regB1 = re.compile(expB1)
		regB2 = re.compile(expB2)
		regB3 = re.compile(expB3)
		regC1 = re.compile(expC1)
		
		i = 0
		j = 0
		h = 0
		m = 0
		for l in self.param:
			if regB1.match(l) != None:
				# print('SIM')
				i = i + 1
			if regB2.match(l) != None:
				j = j + 1
			if regB3.match(l) != None:
				h = h + 1
			if regC1.match(l) != None:
				m = m + 1

		# print('Bloco chamada: '+str(i))
		# print('Bloco criacao: '+str(j))
		# print('Bloco fim blo: '+str(h))
		# print('Comando basic: '+str(m))
		return self.param