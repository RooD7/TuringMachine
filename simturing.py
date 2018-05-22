#!/usr/bin/python
import argparse
import os.path
import InputArgs
import InputFile
import Output


class simturing:

	impArgs = InputArgs.InputArgs()
	impFile = InputFile.InputFile()
	outLine = Output.Output()

	# ---------------------------------------------------------------
	# --- 1. Ler argumentos (-r,-v,-s,-h, pathFile) via linha de comando
	paramArgs = impArgs.inputs()
	print('Argumentos de Entrada: ')
	print(paramArgs)

	# extrai parametros recebidos via argumento
	for p in paramArgs:
		if (p[0] == 'r') or (p[0] == 'v'):
			opcao = p[0]
			pathFile = p[1]
		elif (p[0] == 's'):
			opcao = p[0]
			steps = p[1]
			pathFile = p[2]
		elif (l == 'h'):
			head = p[1]


	print('Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')
	
	if paramArgs is None:
		print('Informe os parâmentros de entrada, não há registro dos últimos parâmetros.')
		exit()

	palavra = input('Forneça a palavra inicial: ')
	
	# ---------------------------------------------------------------
	# --- 2. Rodar baseado nesses argumentos
	
	# leitura do arquivo de entrada
	paramFile = impFile.inputs(pathFile)

	# executa e imprime apenas o final da fita
	if opcao == 'r':
		# pathFile
		pass
	# executa e imprime passo a passo a fita
	elif opcao == 'v':
		# pathFile
		pass
	# executa e imprime n passos da fita
	elif opcao == 's':
		# steps
		# pathFile
		pass
		
	# print(outLine.newLineClear())
	# line = [model, self.bloco, self.estado, self.esquerda, self.cabecote, self.direita]
	# line2 = outLine.newLine(line2[1],line2[2], cabItens[0], cabItens[1], cabItens[2])

	# line1 = outLine.newLine('main','1','E','()','ba')
	# print(line1[0])
	# bloco =
	# estado =
	# cabecote =
	line = outLine.newLine('main','10','','[]',palavra)
	print(line[0])
	line = outLine.moveCabecote(line,'d')
	print(line[0])
	line = outLine.moveCabecote(line,'e')
	print(line[0])
	line = outLine.moveCabecote(line,'e')
	print(line[0])
	print('Cabecote: '+outLine.getCabecote(line2))

	# --- 3. Solicitar novos argumentos (-r,-v,-s)
	# --- 4. Rodar baseado nesses argumentos
	#
	#


