#!/usr/bin/python
import argparse
import os.path
import Inputs


class simturing:

	imp = Inputs.Inputs()
	param = imp.inputArgs()

	print('Simulador de Máquina de Turing - Version 1.0\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação.\nAna Paula Silva Cunha, IFMG, 2018.\nRodrigo Sousa Alves, IFMG, 2018.\n')
	
	print('Argumentos de Entrada: ')
	print(param)
	# palavra = input('Forneça a palavra inicial: ')

