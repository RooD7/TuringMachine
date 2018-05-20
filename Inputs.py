#!/usr/bin/python
import argparse
import os

PATH_CFG = os.getcwd()+'/config.cfg'
class Inputs(object):

	def __init__(self):
		self.pathMT = ''
		self.numPassMT = ''

	def writeFile(self, argumentos, tipoOpc):
		fileCFG = open(PATH_CFG,'w')
		fileCFG.write(tipoOpc+'\n')
		# fileCFG.write('\n')
		fileCFG.write(argumentos)
		fileCFG.close()

	def appendFile(self, argumentos, tipoOpc):
		fileCFG = open(PATH_CFG,'a')
		fileCFG.write('\n'+tipoOpc+'\n')
		# fileCFG.write('\n')
		fileCFG.write(argumentos)
		fileCFG.close()

	def readFile(self):
		# leitura do arquivo config.cfg
		fileCFG = open(PATH_CFG,'r')
		
		linhas = []
		novaLista = None
		for l in fileCFG:
			l = l.replace('\n','')
			if (l == 'r') or (l == 'v') or (l == 's') or (l == 'h'):
				if novaLista != None: linhas.append(novaLista)
				novaLista = []
				novaLista.append(l)
			else:
				novaLista.append(l)

		linhas.append(novaLista)				
		fileCFG.close()

		return linhas

	def inputArgs(self):
		#Leitura dos argumentos via linha de comando	
		parser = argparse.ArgumentParser(description = 'Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')

		parser.add_argument('-resume','-r', action = 'store', dest = 'fileR', required = False, help = 'Executa o programa até o fim em modo silencioso e depois imprime o conteúdo final da fita.')

		parser.add_argument('-verbose','-v', action = 'store', dest = 'fileV', required = False, help = 'Mostra a execução passo a passo do programa até o fim.')

		parser.add_argument('-step','-s', action = 'store', nargs=2, dest = 'n', required = False, help = 'Mostra n computações passo a passo na tela, depois abre prompt e aguarda nova opção (-r,-v,-s).')

		parser.add_argument('-head', action = 'store', dest = 'head', required = False, help = 'Define os caracteres delimitadores.')

		arguments = parser.parse_args();

		# Salva ultimo comando no arquivo config.cfg
		if arguments.fileR != None:
			# Opcao -r selecionada
			self.writeFile(arguments.fileR, 'r')

		elif arguments.fileV != None:
			# Opcao -v selecionada
			self.writeFile(arguments.fileV, 'v')

		elif arguments.n != None:
			# Opcao -s selecionada
			strAux = arguments.n[0]+'\n'+arguments.n[1]
			self.writeFile(strAux, 's')

		# Acrescenta no final o resultado do comando -head no arquivo config.cfg
		if arguments.head != None:
			print('argumentos HEAD: '+arguments.head)
			self.appendFile(arguments.head, 'h')

		#Usuario nao informou nenhum parametro
		#Realiza a leitura do ultimo comando realizado
		param = []
		if (arguments.fileR is None) and (arguments.fileV is None) and (arguments.n is None) and (arguments.head is None) :
			#Arquivo config.cfg existe
			if os.path.isfile(PATH_CFG):
				param = self.readFile()
			#Arquivo config.cfg nao existe
			else:
				print('Informe os parâmentros, não há registro dos últimos parâmetros.')

		return param