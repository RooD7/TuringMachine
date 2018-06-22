import re

class Regex(object):

	def __init__(self):
		# Declaracao de bloco
		expB1 = r'^bloco\s[a-zA-Z0-9]{1,16}\s[0-9]{1,4}([ |\t]*![ |\t]*)?([ |\t]*;[ |\t]*[\w| ]+)?\s?'
		# Chamada de bloco
		expB2 = r'^[0-9]{1,4} ([a-zA-Z]+) (pare|[0-9]{1,4})([ |\t]*![ |\t]*)?([ |\t]*;[ |\t]*[\w| ]+)?\s?'
		# Fim de bloco
		expB3 = r'^fim([ |\t]*![ |\t]*)?([ |\t]*;[ |\t]*[\w| ]+)?\s?'
		# Comandos
		expC1 = r'^[0-9]{1,4} (\*|_|([a-zA-Z]{1})) -{2} (\*|_|([a-zA-Z]{1})) (i|d|e) (\*|([0-9]{1,4})|pare|retorne)([ |\t]*![ |\t]*)?([ |\t]*;[ |\t]*[\w| ]+)?\s?'

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