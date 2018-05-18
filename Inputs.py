#!/usr/bin/python
import argparse
import os.path

PATH_CFG = '/home/rood/Documentos/Teoria/Trabalho/TuringMachine/config.cfg'
class Inputs(object):

	def __init__(self):
		self.pathMT = ''
		self.numPassMT = ''

	def writeFile(self, argumentos, tipoOpc):
		fileCFG = open(PATH_CFG,'w')
		fileCFG.write(tipoOpc)
		fileCFG.write('\n')
		fileCFG.write(argumentos)
		fileCFG.close()

	def readFile(self):
		# leitura do arquivo config.cfg
		fileCFG = open(PATH_CFG,'r')
		lin1 = fileCFG.readline()
		lin2 = fileCFG.readline()
		lin3 = fileCFG.readline()

		if (lin1 == 'r') or (lin1 == 'v'):
			self.pathMT = lin2
		else:
			self.numPassMT = lin2
			self.pathMT = lin3
		fileCFG.close()

		self.numPassMT = self.numPassMT.replace('\n','')
		return [self.pathMT, self.numPassMT]

	def inputArgs(self):
		#Leitura dos argumentos via linha de comando	
		parser = argparse.ArgumentParser(description = 'Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')

		parser.add_argument('-resume','-r', action = 'store', dest = 'fileR', required = False, help = 'Executa o programa até o fim em modo silencioso e depois imprime o conteúdo final da fita.')

		parser.add_argument('-verbose','-v', action = 'store', dest = 'fileV', required = False, help = 'Mostra a execução passo a passo do programa até o fim.')

		parser.add_argument('-step','-s', action = 'store', nargs=2, dest = 'n', required = False, help = 'Mostra n computações passo a passo na tela, depois abre prompt e aguarda nova opção (-r,-v,-s).')

		arguments = parser.parse_args();

		# Salva ultimo comando no arquivo config.cfg
		if arguments.fileR != None:
			# Opcao -r selecionada
			print('fileR')
			self.writeFile(arguments.fileR, 'r')

		# Salva ultimo comando no arquivo config.cfg	
		elif arguments.fileV != None:
			# Opcao -v selecionada
			print('fileV')
			self.writeFile(arguments.fileV, 'v')

		# Salva ultimo comando no arquivo config.cfg
		elif arguments.n != None:
			# Opcao -s selecionada
			strAux = arguments.n[0]+'\n'+arguments.n[1]
			self.writeFile(strAux, 's')


		#Usuario nao informou nenhum parametro
		#Realiza a leitura do ultimo comando realizado
		param = []
		if (arguments.fileR is None) and (arguments.fileV is None) and (arguments.n is None) :
			#Arquivo config.cfg existe
			if os.path.isfile(PATH_CFG):
				param = self.readFile()
			#Arquivo config.cfg nao existe
			else:
				print('Informe os parâmentros, não há registro dos últimos parâmetros.')

		return param