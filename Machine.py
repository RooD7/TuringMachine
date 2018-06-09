
class Machine(object):

	paramBloco = []

	def separaBloco(self, opcao, param):
		# inicio de bloco
		# bloco <identificador do bloco> <estado inicial>
		# bloco main 1
		if opcao == 'iniBloco':
			self.paramBloco = []
			self.paramBloco.insert(0, param)
		elif opcao == 'fimBloco':
			self.paramBloco.append(param)
			return self.paramBloco
		else:
			self.paramBloco.append(param)

		return None


	def executaParam(self, param):
		# inicio de bloco
		# bloco <identificador do bloco> <estado inicial>
		# bloco main 1
		if opcao == 'iniBloco':
			param += line.split()

		# chamada de bloco
		# <estado atual> <identificador do bloco> <estado de retorno>
		# 10 moveFim 11
		elif opcao == 'chaBloco':
			param += line.split()

		# fim de bloco
		# fim
		elif opcao == 'fimBloco':
			param += line.split()

		# comando
		# <estado atual> <simbolo atual> -- <novo simbolo> <movimento> <novo estado>
		# 12 a -- A i 30
		elif opcao == 'comando':
			line = line.replace('--','')
			param += line.split()

		return param

	# Executa ate o fim
	def run_01(self, blocosCod):
		# # Ultima linha executada
		# line = outLine.newLine(bloco,estado,esquerda,head,palavra)
		# # Imprime Ultima linha executada
		# print(line)
		pass

	# Executa linha por linha
	def run_02(self, blocosCod):
		pass

	# Executa n linhas
	def run_03(self, blocosCod, n):
		pass

	def nextInst(self, blocosCod):
		pass

