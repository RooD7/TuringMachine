import re

class Regex(object):

	def __init__(self):
		# Declaracao de bloco
		expB1 = r'^bloco\s[a-zA-Z0-9]{1,16}\s[0-9]{1,4}\n?'
		# Chamada de bloco
		expB2 = r'^[0-9]{1,4}\s[a-zA-Z0-9]{1,16}\s[0-9]{1,4}\n?'
		# Fim de bloco
		expB3 = r'^fim?'
		# Comandos
		expC1 = r'^[0-9]{1,4}\s(\*|_|[a-zA-Z]{0,16})\s-{2}\s(\*|_|[a-zA-Z]{0,16})\s(i|d|e)\s(\*|[0-9]{1,4})\n?'

		self.regB1 = re.compile(expB1)
		self.regB2 = re.compile(expB2)
		self.regB3 = re.compile(expB3)
		self.regC1 = re.compile(expC1)

	def aplicaRegex(self, linha):
		# Declaracao de bloco
		if self.regB1.match(linha) != None:
			return 'iniBloco'
		# Chamada de bloco
		elif self.regB2.match(linha) != None:
			return 'chaBloco'
		# Fim de bloco
		elif self.regB3.match(linha) != None:
			return 'fimBloco'
		# Comandos
		elif self.regC1.match(linha) != None:
			return 'comando'

		return None

	def extraiParam(self, line):
		line = line.replace('--','')
		return line.split()