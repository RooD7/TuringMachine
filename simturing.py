#!/usr/bin/python
import argparse
import os.path
import InputArgs
import InputFile
import Output
import Machine
import Regex

class simturing:

	impArgs = InputArgs.InputArgs()
	impFile = InputFile.InputFile()
	outLine = Output.Output()
	machine  = Machine.Machine()
	regex   = Regex.Regex()

	print('Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')

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
		elif (p[0] == 'h'):
			head = p[1]
	
	if paramArgs is None:
		print('Informe os parâmentros de entrada, não há registro dos últimos parâmetros.')
		exit()

	palavra = input('Forneça a palavra inicial: ')
	
	# ---------------------------------------------------------------
	# --- 2. Rodar baseado nesses argumentos
	
	# leitura do arquivo de entrada
	linesFile = impFile.inputs(pathFile)
	blocosCod = []
	bloco = []

	# Separa o codigo em blocos de codigo a serem executados
	for l in linesFile:
		bloco = machine.separaBloco(regex.aplicaRegex(l), l)
		if (bloco != None):
			blocosCod.append(bloco)

	for i in blocosCod:
		print('___NOVO BLOCO___')
		for j in i:
			print(j)


	# executa e imprime apenas o final da fita
	if opcao == 'r':
		# Executa a maquina
		machine.run_01(blocosCod)
		pass
	# executa e imprime passo a passo a fita
	elif opcao == 'v':
		machine.run_02(blocosCod)
		pass
	# executa e imprime n passos da fita
	elif opcao == 's':
		machine.run_03(blocosCod, steps)
		pass
	


	# print(outLine.newLineClear())
	# line = [model, self.bloco, self.estado, self.esquerda, self.cabecote, self.direita]

	# line1 = outLine.newLine('main','1','E','()','ba')
	# print(line1[0])
	bloco = 'main'
	estado = '10'
	esquerda = ''
	line = outLine.newLine(bloco,estado,esquerda,head,palavra)
	print(line[0])
	line = outLine.moveCabecote(line,'d')
	print(line[0])
	line = outLine.moveCabecote(line,'d')
	print(line[0])
	line = outLine.alteraCabecote(line,'d','D')
	print(line[0])
	line = outLine.moveCabecote(line,'e')
	print(line[0])
	line = outLine.moveCabecote(line,'e')
	print(line[0])

	line = 'bloco main 1 !'
	par = regex.extraiParam(line)
	print(par)
	line = '10 moveFim 11'
	par = regex.extraiParam(line)
	print(par)
	line = 'fim'
	par = regex.extraiParam(line)
	print(par)
	line = '12 a -- A i 30'
	par = regex.extraiParam(line)
	print(par)

	# print('Cabecote: '+outLine.getCabecote(line))

	# --- 3. Solicitar novos argumentos (-r,-v,-s)
	# --- 4. Rodar baseado nesses argumentos
	#
	#


	# extrairParam e executaParam parametros em funcoes separadas?
	# classe Machine com funcoes do tipo
	# 	modoR
	# 		Executa tudo
	# 		Imprime resultado
	# 	modoV
	# 		Executa tudo
	# 		exibe o passo a passo
	# 	modoS
	# 		executa n vezes
	# 		exibe passo a passo