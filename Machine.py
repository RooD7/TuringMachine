import Regex
import Output

class Machine(object):

	
	def __init__(self):
		self.regex = Regex.Regex()
		self.outLine = Output.Output()
		self.instrucaoAtual = None
		self.paramBloco = []
		self.blocosCod = []
		self.estadoAtual = ''
		self.blocoAtual = None
		self.fita = []
		self.pilhaBloco = []


	def getBloco(self, opcao):
		for b in self.blocosCod:
			if b[0] == opcao:
				print('####  achou o bloco = '+b[0])
				# print(b)
				return b

	def getInicioBloco(self, nomeBloco):
		for b in self.blocosCod:
			if b[0] == nomeBloco:
				return b[2]

	# monta o bloco de codigo a partir das linhas recebidas
	def separaBloco(self, opcao, param):
		# inicio de bloco
		# bloco <identificador do bloco> <estado inicial>
		# bloco main 1
		if opcao == 'iniBloco':
			self.paramBloco = []
			nomeBloco = param.split()
			self.paramBloco.insert(0, nomeBloco[1])
			self.paramBloco.append(param)
		elif opcao == 'fimBloco':
			self.paramBloco.append(param)
			return self.paramBloco
		else:
			self.paramBloco.append(param)
		return None

	# Separa o codigo em blocos de codigo a serem executados
	def separaCodEmBlocos(self, linesFile):
		bloco = []
		for l in linesFile:
			bloco = self.separaBloco(self.regex.aplicaRegex(l), l)
			if (bloco != None):
				self.blocosCod.append(bloco)

		return self.blocosCod


	def getInstrucoes(self, bloco, estado):
		instr = []
		print('GETInstricoes: '+estado)
		print('GETInstricoes: '+bloco[0])
		# print(bloco)
		for b in bloco:
			# print('linha: '+b)
			if (self.regex.aplicaRegex(b) == 'comando') and (int(b.split()[0]) == int(estado)):
				print('comandoo')
				instr.append(b)
			elif (self.regex.aplicaRegex(b) == 'chaBloco') and (int(b.split()[0]) == int(estado)):
				print('chaBlocoo')
				instr.append(b)
		return instr



	# Executa ate o fim
	def run_01(self, palavra, head, linesFile):
		# # Ultima linha executada
		# line = outLine.newLine(bloco,estado,esquerda,head,palavra)
		# # Imprime Ultima linha executada
		self.blocosCod = self.separaCodEmBlocos(linesFile)
		self.blocoAtual = self.getBloco('main')
		self.instrucaoAtual = self.blocoAtual[1]
		self.fita = self.outLine.newLine(self.blocoAtual[0], self.blocoAtual[1].split()[2], '', head, palavra)
		print(self.fita[0])
		print(self.blocoAtual[0])
		# self.pilhaBloco.append([self.blocoAtual[0], self.blocoAtual[1].split()[2]])

		
		if self.instrucaoAtual is not None:
			# print('---- EXECUTA LINHA '+str(i))
			# print('PRE INSTRUCAO ATUAL: '+self.instrucaoAtual)
			instrucaoPilha = None
			estadoPilha = ''
			while(True):
				print('PILHA')
				print(self.pilhaBloco)
				finalizou = self.execBloco(self.blocoAtual, estadoPilha)
				if finalizou == 'pare':
					print('PAROU')
					break
				elif finalizou == 'retorne':
					print('RETORNOU')
					instrucaoPilha = self.pilhaBloco.pop()
					self.blocoAtual = self.getBloco(instrucaoPilha[0])
					estadoPilha = instrucaoPilha[1]
					if estadoPilha == 'pare':
						print('Programa FINALIZADO!')
				else:
					# finalizou possui o nome do proximo bloco
					print('empilhou')
					# instrucaoPilha = self.pilhaBloco.pop()
					# self.pilhaBloco.append(instrucaoPilha)
					self.blocoAtual = self.getBloco(finalizou)
					estadoPilha = ''
				x = input()

			# print('POS INSTRUCAO ATUAL: '+self.instrucaoAtual)
			print(self.fita[0])
		else:
 			print('Bloco *main* nao identificado!')

		return self.blocosCod

	# Executa linha por linha
	def run_02(self, blocosCod):
		pass

	# Executa n linhas
	def run_03(self, blocosCod, n):
		pass

	# retorna a lista das proximas possiveis instrucoes
	def execBloco(self, bloco, estadoAtual):
		if estadoAtual == '':
			print('Estado Atual eh None')
			self.estadoAtual = bloco[1].split()[2]
			print('Estado Atual eh '+self.estadoAtual)
		else:
			self.estadoAtual = estadoAtual
			print('Estado Atual eh '+self.estadoAtual)
		self.fita[1] = bloco[0]
		self.fita[2] = self.estadoAtual
		# print(bloco[0])
		# print(self.estadoAtual)
		# print(self.fita)
		sair = False
		while(not sair):
			print('###### Estado Atual: '+self.estadoAtual)
			x = input()
			instrucoes = self.getInstrucoes(bloco, self.estadoAtual)

			cabecote = self.outLine.getCabecote(self.fita)
			print('###### Instrucoes: ')
			print(instrucoes)
			x = input()
			for i in instrucoes:
				print('###### Instrucao: '+i)
				# <estado atual> <simbolo atual> -- <novo simbolo> <movimento> <novo estado>
				# eh um comando && estado da instrucao corresponde
				if (self.regex.aplicaRegex(i) == 'comando'):
					# letra do cabecote corresponde
					if (i.split()[1] == cabecote) or (i.split()[1] == '*'):
						# print('COMANDO:: '+i)
						self.fita = self.outLine.alteraCabecote(self.fita, i.split()[1], i.split()[3])
						print(self.fita[0])
						self.fita = self.outLine.moveCabecote(self.fita, i.split()[4])
						if (i.split()[5] == 'retorne'):
							return 'retorne'
						elif (i.split()[5] == 'pare'):
							return 'pare'
						else:
							# estado atual eh atualizado para proximo estado
							self.estadoAtual = i.split()[5]

				# <estado atual> <identificador do bloco> <estado de retorno>
				# 10 moveFim 11
				elif (self.regex.aplicaRegex(i) == 'chaBloco'):
					atual = i.split()[0]
					nomeBloco = i.split()[1]
					retorno = i.split()[2]
					if (retorno == 'retorne'):
						return 'retorne'
					elif (retorno == 'pare'):
						return 'pare'
					else:
						# estado atual eh atualizado para proximo estado
						self.pilhaBloco.append([bloco[0], retorno])
						print('Empilhou: '+bloco[0]+' - '+retorno)
						return nomeBloco
			if sair:
				break

		return None

