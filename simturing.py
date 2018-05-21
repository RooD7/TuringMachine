#!/usr/bin/python
import argparse
import os.path
import InputArgs
import InputFile


class simturing:

	impArgs = InputArgs.InputArgs()
	param = impArgs.inputs()

	impFile = InputFile.InputFile()
	param2 = impFile.inputs('palindrome.MT')

	print('Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')
	
	if param is None:
		print('Informe os parâmentros de entrada, não há registro dos últimos parâmetros.')
	else:
		# palavra = input('Forneça a palavra inicial: ')
		print('Argumentos de Entrada: ')
		print(param)


