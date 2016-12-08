# -*- coding: utf-8 -*-
import re

class Fact():

	name = None
	value = False
	term = None

	def __init__(self, name, value=False):
		self.name = name
		self.value = value
		self.term = (self.name, self.value)

	def getValue(self):
		return self.value

	def getName(self):
		return self.name

	def getFact(self):
		return self.term


class Production():

	antecedent = None
	consecvent = None
	rule = None
	operations = ('&&', '||')

	def __init__(self, prod):

		sides = re.split(r' -> ', prod)
		
		antecedent = self.parseSide(sides[0])
		consecvent = self.parseSide(sides[1])

		self.antecedent = antecedent
		self.consecvent = consecvent
		# print 'anc = ', antecedent
		# print 'conc = ', consecvent

		self.rule = (self.antecedent, self.consecvent)

	def parseSide(self, side):

		parts =  re.split(r' ', side)
		if len(parts) == 1:
			return [(parts[0], True)]
		if len(parts) == 2:
			return [(parts[1], False)]

		res = []
		iterations = (i for i in range(len(parts)))

		for i in iterations:
			part = parts[i]

			if part == '!':
				res.append((parts[i+1], False))
				iterations.next()
			elif part not in self.operations:
				res.append((part, True))
			else:
				res.append(('operation', part))

		return res

	def AnswerQuestion(self, facts):
		pass


	def getProduction(self):
		return self.rule

	def getConsecvent(self):
		return self.consecvent

	def getAntecendent(self):
		return self.antecedent


