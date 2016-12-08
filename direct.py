# -*- coding: utf-8 -*-
from base import Fact
from base import Production


def check_current_rule(rule, result, terms):

	for item in rule:
		if item[0] != 'operation' and item not in terms:
			return False
		
	# rule have all neccessary terms now we have to validate them
	if len(rule) > 1:
		# Исключаем из перебора все кроме операций (которые идут через один)
		res = False
		iterations = (i for i in range(1, len(rule), 2))
		for i in iterations:
			# print rule[i-1][1], ' ', rule[i][1], ' ', rule[i+1][1]
			if rule[i][1] == '&&':
				# print rule[i-1][1] and rule[i+1][1]
				res = res or rule[i-1][1] and rule[i+1][1]
			else:
				# print rule[i-1][1] or rule[i+1][1]
				res = res or rule[i-1][1] or rule[i+1][1]
		if res:
			return result[0]
		else:
			return False
	else:
		return result[0]


def facts_to_list(terms):
	# put facts into list of tuples for better usage
	facts = []
	for term in terms:
		facts.append((term.getName(), term.getValue()))

	return facts


def direct_otput(rules, terms, goal):

	facts  = facts_to_list(terms)

	print
	print 'Перед проверкой правил, факты = ', facts

	if goal in facts:
		return True

	ext = len(facts)

	while True:
		for rule in rules:
			new_fact =  check_current_rule(rule.getAntecendent(), rule.getConsecvent(), facts)
			if new_fact and new_fact not in facts:
				facts.append(new_fact)
		# Если после проверки всех правил фактов не добавилось, значит можно выходить из цикла
		if ext == len(facts):
			break
		# Если добавилось, то нужно с новым набором фактов проверить правила
		else:
			ext = len(facts)

	print 'После проверки правил, факты = ', facts
	print 
	
	if goal in facts:
		return True

	return False