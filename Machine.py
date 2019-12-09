# -*- coding: utf-8 -*-

import Regex
import Output
import Ribbon
import copy

class Machine(object):
	
	def __init__(self):
		self.regex = Regex.Regex()
		self.outLine = Output.Output()
		self.instrucaoAtual = None
		self.paramBloco = []
		self.blocosCod = []
		self.estadoAtual = ''
		self.listaDePrints = []
		self.contInteracoes = 0
		self.blocoAtual = None
		self.fita = Ribbon.Ribbon()
		self.pilhaBloco = []


	def getBloco(self, opcao):
		for b in self.blocosCod:
			if b[0] == opcao:
				# print('####  achou o bloco = '+b[0])
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
		# comeca novo bloco pegando as intrucoes do cabecalho do bloco
		if estado == None:
			estado = bloco[1].split()[2]
		for b in bloco:
			# print('linha: '+b)
			if (self.regex.aplicaRegex(b) == 'comando') and (int(b.split()[0]) == int(estado)):
				instr.append(b)
			elif (self.regex.aplicaRegex(b) == 'chaBloco') and (int(b.split()[0]) == int(estado)):
				instr.append(b)		
		return instr

	def getInstrucao(self, bloco, estado):
		blocoAtual = self.getBloco(bloco)
		for b in blocoAtual:
			if (((self.regex.aplicaRegex(b) == 'comando') or (self.regex.aplicaRegex(b) == 'chaBloco')) and 
					(int(b.split()[0]) == int(estado))):
				return b
		return None


	# # Executa ate o fim
	# def run(self, palavra, head, linesFile):
	# 	self.listaDePrints = []
	# 	self.blocosCod = self.separaCodEmBlocos(linesFile)
	# 	self.blocoAtual = self.getBloco('main')
	# 	self.instrucaoAtual = self.blocoAtual[1]
	# 	self.fita.setRibbon(self.outLine.newLine(self.blocoAtual[0], self.blocoAtual[1].split()[2], '', head, palavra))
	# 	# print(self.fita[0])
	# 	# print(self.blocoAtual[0])
	# 	self.contInteracoes = 0
	# 	if self.instrucaoAtual is not None:
	# 		instrucaoPilha = None
	# 		estadoPilha = ''
	# 		while(True):
	# 			# print('PILHA')
	# 			# print(self.pilhaBloco)
	# 			finalizou = self.execBloco(self.blocoAtual, estadoPilha)
	# 			self.contInteracoes += 1
	# 			# print(self.contInteracoes)
	# 			if(self.contInteracoes == 500):
	# 				return None
	# 			# finaliza a execucao da maquina
	# 			if finalizou == 'pare':
	# 				print('Programa FINALIZADO!')
	# 				break
	# 			# volta a executar o ultimo bloco da pilha (continua de onde parou)
	# 			elif finalizou == 'retorne':
	# 				# print('RETORNOU')
	# 				instrucaoPilha = self.pilhaBloco.pop()
	# 				self.blocoAtual = self.getBloco(instrucaoPilha[0])
	# 				estadoPilha = instrucaoPilha[1]
	# 				if estadoPilha == 'pare':
	# 					print('Programa FINALIZADO!')
	# 					break
	# 			# retorna o nome do proximo bloco a ser executado
	# 			else:
	# 				# print('EMPILHOU')
	# 				self.blocoAtual = self.getBloco(finalizou)
	# 				estadoPilha = ''
	# 			# x = input()
	# 		self.listaDePrints.append(self.fita.getPrint())
	# 	else:
 	# 		print('Bloco *main* nao identificado!')
	# 	return self.listaDePrints

	# # Executa ate o fim
	# def run(self, palavra, head, linesFile):
	# 	self.listaDePrints = []
	# 	self.blocosCod = self.separaCodEmBlocos(linesFile)
	# 	self.blocoAtual = self.getBloco('main')
	# 	self.instrucaoAtual = self.blocoAtual[1]
	# 	self.fita = self.outLine.newLine(self.blocoAtual[0], self.blocoAtual[1].split()[2], '', head, palavra)
	# 	# print(self.fita[0])
	# 	# print(self.blocoAtual[0])
	# 	self.contInteracoes = 0
	# 	if self.instrucaoAtual is not None:
	# 		instrucaoPilha = None
	# 		estadoPilha = ''
	# 		while(True):
	# 			# print('PILHA')
	# 			# print(self.pilhaBloco)
	# 			finalizou = self.execBloco(self.blocoAtual, estadoPilha)
	# 			self.contInteracoes += 1
	# 			# print(self.contInteracoes)
	# 			if(self.contInteracoes == 500):
	# 				return None
	# 			# finaliza a execucao da maquina
	# 			if finalizou == 'pare':
	# 				print('Programa FINALIZADO!')
	# 				break
	# 			# volta a executar o ultimo bloco da pilha (continua de onde parou)
	# 			elif finalizou == 'retorne':
	# 				# print('RETORNOU')
	# 				instrucaoPilha = self.pilhaBloco.pop()
	# 				self.blocoAtual = self.getBloco(instrucaoPilha[0])
	# 				estadoPilha = instrucaoPilha[1]
	# 				if estadoPilha == 'pare':
	# 					print('Programa FINALIZADO!')
	# 					break
	# 			# retorna o nome do proximo bloco a ser executado
	# 			else:
	# 				# print('EMPILHOU')
	# 				self.blocoAtual = self.getBloco(finalizou)
	# 				estadoPilha = ''
	# 			# x = input()
	# 		self.listaDePrints.append(self.fita[0])
	# 	else:
 	# 		print('Bloco *main* nao identificado!')
	# 	return self.listaDePrints

	# # retorna a lista das proximas possiveis instrucoes
	# def execBloco(self, bloco, estadoAtual):
	# 	if estadoAtual == '':
	# 		# print('Estado Atual eh None')
	# 		self.estadoAtual = bloco[1].split()[2]
	# 		# print('Estado Atual eh '+self.estadoAtual)
	# 	else:
	# 		self.estadoAtual = estadoAtual
	# 		# print('Estado Atual eh '+self.estadoAtual)
	# 	self.fita[1] = bloco[0]
	# 	self.fita[2] = self.estadoAtual
	# 	# print('Bloco em execucao: '+bloco[0])
	# 	# print(self.estadoAtual)
	# 	print(self.fita)
	# 	sair = False
	# 	while(True):
	# 		# print('###### Estado Atual: '+self.estadoAtual)
	# 		# x = input()
	# 		instrucoes = self.getInstrucoes(bloco, self.estadoAtual)

	# 		cabecote = self.outLine.getCabecote(self.fita)
	# 		# print('###### Instrucoes: ')
	# 		# print(instrucoes)
	# 		# x = input()
	# 		for i in instrucoes:
	# 			print('###### Instrucao: '+i)
	# 			# <estado atual> <simbolo atual> -- <novo simbolo> <movimento> <novo estado>
	# 			# eh um comando && estado da instrucao corresponde
	# 			if (self.regex.aplicaRegex(i) == 'comando'):
	# 				# letra do cabecote corresponde
	# 				if (i.split()[1] == cabecote) or (i.split()[1] == '*'):
	# 					# print('###Executa ### Instrucao: '+i)
	# 					x = i.split()
	# 					for s in x:
	# 						if s is '!':
	# 							sair = True

	# 					self.fita[2] = self.estadoAtual
	# 					self.fita = self.outLine.alteraCabecote(self.fita, i.split()[1], i.split()[3])
	# 					self.listaDePrints.append(self.fita[0])
	# 					# print(self.fita[0])
	# 					self.fita = self.outLine.moveCabecote(self.fita, i.split()[4])
	# 					if (i.split()[5] == 'retorne'):
	# 						return 'retorne'
	# 					elif (i.split()[5] == 'pare'):
	# 						# print('pare')
	# 						return 'pare'
	# 					else:
	# 						# estado atual eh atualizado para proximo estado
	# 						self.estadoAtual = i.split()[5]
	# 						break

	# 			# <estado atual> <identificador do bloco> <estado de retorno>
	# 			# 10 moveFim 11
	# 			elif (self.regex.aplicaRegex(i) == 'chaBloco'):
	# 				atual = i.split()[0]
	# 				nomeBloco = i.split()[1]
	# 				retorno = i.split()[2]

	# 				x = i.split()
	# 				for s in x:
	# 					if s is '!':
	# 						sair = True
	# 				# print('chamou bloco: '+i)

	# 				# estado atual eh atualizado para proximo estado
	# 				self.pilhaBloco.append([bloco[0], retorno])
	# 				# print('Empilhou: '+bloco[0]+' - '+retorno)
	# 				return nomeBloco
	# 			if sair is True:
	# 				for x in self.listaDePrints:
	# 					print(x)
	# 					exit(1)
	# 	return None

	def getNaoDeterminismo(self, intrs, letra):
		det = []
		if intrs == []:
			return []
		for i in intrs:
			# letra do cabecote corresponde
			if (self.regex.aplicaRegex(i) == 'chaBloco'):
				det.append(i)
			elif letra == i.split()[1] or (i.split()[1] == '*'):
				det.append(i)
		return det
		
	def addFilaDeInstr(self, pilha, idd, instr, fita):
		id2 = idd
		for t in instr:
			pilha.append((id2,t,fita))
			#Copia o bloco atual pro novo id
			if id2 != idd:
				# blocos = copy.deepcopy(self.pilhaBloco)
				# if blocos != None:
				# 	for b in blocos:
				# 		self.addPilhaBloco(id2, b)
				blocos = self.getPilhaBloco(idd-1)
				if blocos != None:
					for b in blocos:
						self.addPilhaBloco(id2, b)
				#Copia o print atual pro novo id
				if self.listaDePrints != []:
					prints = []
					for p in self.listaDePrints:
						if p[0] == idd-1:
							prints.append((id2, p[1]))
					self.listaDePrints += prints
				self.contInteracoes[id2] = 0
			id2 += 1
		return(pilha,id2-1)

	def addFilaDeInstrIni(self, pilha, idd, instr, fita):
		id2 = idd
		for t in instr:
			pilha.append((id2,t,fita))
			#Copia o bloco atual pro novo id
			if id2 != idd:
				# blocos = copy.deepcopy(self.pilhaBloco)
				# if blocos != None:
				# 	for b in blocos:
				# 		self.addPilhaBloco(id2, b)
				blocos = self.getPilhaBloco(idd-1)
				if blocos != None:
					for b in blocos:
						self.addPilhaBloco(id2, b)
				#Copia o print atual pro novo id
				if self.listaDePrints != []:
					prints = []
					for p in self.listaDePrints:
						if p[0] == idd-1:
							prints.append((id2, p[1]))
					self.listaDePrints = prints + self.listaDePrints
				self.contInteracoes[id2] = 0
			id2 += 1
		return(pilha,id2-1)

	def addPilhaBloco(self, idd, bloco):
		for pb in self.pilhaBloco:
			if pb[0] == idd:
				pb[1].append(bloco)
				return
		self.pilhaBloco.append((idd, [bloco]))

	def getItemPilhaBloco(self, idd):
		for pb in self.pilhaBloco:
			# if pb[1] != []:
			if pb[0] == idd and pb[1] != []:
				return pb[1].pop()
		return None

	def getPilhaBloco(self, idd):
		for pb in self.pilhaBloco:
			if pb[0] == idd:
				return pb[1]
		return None
		
	# Executa ate o fim
	def run(self, palavra, head, linesFile):
		self.listaDePrints = []
		self.filaDeInstr  = []
		self.contInteracoes = dict()
		# self.retornoBloco = dict
		self.idd = 0
		self.ignora = []
		self.falhou = False
		self.backup = []
		self.blocosCod = self.separaCodEmBlocos(linesFile)
		self.blocoAtual = self.getBloco('main')
		self.instrucaoAtual = self.blocoAtual[1]
		self.fita.setRibbon(self.outLine.newLine(self.blocoAtual[0], self.blocoAtual[1].split()[2], '', head, palavra))
		# print(self.fita[0])
		# print(self.blocoAtual[0])
		self.contInteracoes[self.idd] = 0
		self.estadoAtual = self.blocoAtual[1].split()[2]
		while(True):
			self.instrucaoAtual = self.getNaoDeterminismo(self.getInstrucoes(self.blocoAtual,self.estadoAtual),self.fita.getHead()[1])
			if self.instrucaoAtual != []:
				(self.filaDeInstr,self.idd) = self.addFilaDeInstr(self.filaDeInstr, self.idd, self.instrucaoAtual, copy.deepcopy(self.fita))
				# print(self.filaDeInstr)
				while self.filaDeInstr != []:
					if self.falhou:
						[self.fita, self.listaDePrints, self.pilhaBloco, self.idd, self.filaDeInstr] = self.backup
						self.filaDeInstr.pop(0)
						self.falhou = False
					if len(self.filaDeInstr) > 1:
						self.backup = [copy.deepcopy(self.fita),copy.deepcopy(self.listaDePrints),copy.deepcopy(self.pilhaBloco), self.idd, copy.deepcopy(self.filaDeInstr)]
						self.falhou = False
					t = self.filaDeInstr.pop(0)
					(idd, instrucao,fi) = t
					if idd in self.ignora:
						break
					(comando, params) = self.execInstrucao(t)
					if (comando, params) == (None, None):
						for p in self.listaDePrints:
							if p[0] == idd:
								self.listaDePrints.remove(p)
						for f in self.filaDeInstr:
							if f[0] == idd:
								self.filaDeInstr.remove(f)
						for p in self.pilhaBloco:
							if p[0] == idd:
								self.pilhaBloco.remove(p)
						self.falhou = True
					else:
						# self.fita.setRibbon(fit)
						self.contInteracoes[idd] += 1
						# print(self.contInteracoes[self.idd])
						if(self.contInteracoes[idd] == 100):
							self.ignora.append(idd)
							return None
						# finaliza a execucao da maquina
						if comando == 'pare':
							print('Programa FINALIZADO!')
							return self.listaDePrints
						# volta a executar o ultimo bloco da pilha (continua de onde parou)
						elif comando == 'retorne':
							# retornoPilha = [nomeBloco, retorno]
							retornoPilha = self.getItemPilhaBloco(idd)
							if retornoPilha != None:
								self.blocoAtual = self.getBloco(retornoPilha[0])
								if retornoPilha[1] == 'pare':
									print('Programa FINALIZADO!')
									return self.listaDePrints
								else:
									self.estadoAtual = retornoPilha[1]
									if self.filaDeInstr != []:
										self.instrucaoAtual = self.getNaoDeterminismo(self.getInstrucoes(self.blocoAtual,self.estadoAtual),self.fita.getHead()[1])
										if self.instrucaoAtual != []:
											(self.filaDeInstr,self.idd) = self.addFilaDeInstr(self.filaDeInstr, self.idd, self.instrucaoAtual, copy.deepcopy(self.fita))
						#('newState', instrucao.split()[5], newRibbon)
						elif comando == 'newState':
							self.estadoAtual = params
							# if self.filaDeInstr != []:
							self.instrucaoAtual = self.getNaoDeterminismo(self.getInstrucoes(self.blocoAtual,self.estadoAtual),self.fita.getHead()[1])
							if self.instrucaoAtual != []:
								(self.filaDeInstr,self.idd) = self.addFilaDeInstrIni(self.filaDeInstr, self.idd, self.instrucaoAtual, copy.deepcopy(self.fita))
							else:
								self.falhou = True
						# ('chaBloco', [nomeBloco, retorno], fita)
						elif comando == 'chaBloco':
							# params = [nomeBloco, antigoBloco, retorno]
							novoBloco, antigoBloco, estRetorno = params[0], params[1], params[2]
							self.addPilhaBloco(idd, [antigoBloco, estRetorno])
							self.blocoAtual = self.getBloco(novoBloco)
							# comeca novo bloco
							self.estadoAtual = self.blocoAtual[1].split()[2]
						#('iniBloco', nomeBloco, proxEstado, newRibbon)
						elif comando == 'iniBloco':
							self.blocoAtual = self.getBloco(params[0])
							self.estadoAtual = params[1]
						# self.listaDePrints.append((self.idd, self.fita.getPrint()))
			else:
				self.instrucaoAtual = self.getNaoDeterminismo(self.getInstrucoes(self.blocoAtual,self.estadoAtual),self.fita.getHead()[1])
				if self.instrucaoAtual == []:
					return self.listaDePrints
		return self.listaDePrints

	# retorna a lista das proximas possiveis instrucoes
	def execInstrucao(self, inst):
		# (id atual,instrucao atual, fita atual)
		(idd, instrucao,fi) = inst
		self.fita = fi
		print('### '+str(idd)+' ### Instrucao: '+instrucao)
		# <estado atual> <simbolo atual> -- <novo simbolo> <movimento> <novo estado>
		# eh um comando && estado da instrucao corresponde
		if (self.regex.aplicaRegex(instrucao) == 'comando'):
			# letra do cabecote corresponde
			cabecote = self.outLine.getCabecote(self.fita.getRibbon())
			if (instrucao.split()[1] == cabecote) or (instrucao.split()[1] == '*'):
				# self.fita.setState(self.estadoAtual)
				self.fita.setRibbon(self.outLine.alteraCabecote(self.fita.getRibbon(), instrucao.split()[1], instrucao.split()[3]))
				# print(self.self.fita[0])
				# if not (idd, self.fita.getPrint()) in self.listaDePrints:
				self.listaDePrints.append((idd, self.fita.getPrint()))
				self.fita.setRibbon(self.outLine.moveCabecote(self.fita.getRibbon(), instrucao.split()[4]))
				if (instrucao.split()[5] == 'retorne'):
					return ('retorne', None)
				elif (instrucao.split()[5] == 'pare'):
					# print('pare')
					return ('pare', None)
				else:
					# estado atual eh atualizado para proximo estado
					return ('newState', instrucao.split()[5])
			else:
				return (None, None)

		# <estado atual> <identificador do bloco> <estado de retorno>
		# 10 moveFim 11
		elif (self.regex.aplicaRegex(instrucao) == 'chaBloco'):
			atual = instrucao.split()[0]
			nomeBloco = instrucao.split()[1]
			retorno = instrucao.split()[2]

			print('chamou bloco: '+nomeBloco)

			# estado atual eh atualizado para proximo estado
			# self.pilhaBloco.append([self.blocoAtual[0], retorno])
			# print('Empilhou: '+bloco[0]+' - '+retorno)
			# return ('chaBloco', [nomeBloco, self.blocoAtual[0], retorno])
			return ('chaBloco', [nomeBloco, self.blocoAtual[0], retorno])
		#bloco main 1
		elif (self.regex.aplicaRegex(instrucao) == 'iniBloco'):
			nomeBloco = instrucao.split()[1]
			proxEstado = instrucao.split()[2]

			# estado atual eh atualizado para proximo estado
			# self.pilhaBloco.append([self.blocoAtual[0], retorno])
			# print('Empilhou: '+bloco[0]+' - '+retorno)

			return ('iniBloco', [nomeBloco, proxEstado])
		return (None, None)