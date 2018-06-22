#!/usr/bin/python
# -*- coding: utf-8 -*-
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

		return self.param