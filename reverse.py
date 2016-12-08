# -*- coding: utf-8 -*-
from base import Fact
from base import Production


def check_current_rule(result, rule, terms, goal):

	if goal in result:
		return rule

	return False

def facts_to_list(terms):
	# put facts into list of tuples for better usage
	facts = []
	for term in terms:
		facts.append((term.getName(), term.getValue()))

	return facts


def reverse_output(rules, terms, goal):
	facts  = facts_to_list(terms)
	print 'goal = ', goal

	if goal in facts:
		return True

	while True:
		for rule in rules:
			new_goal = check_current_rule(rule.getConsecvent(), rule.getAntecendent(), facts, goal)

			# Если проход по консеквентам вернул что-то новое, то меняется текущая цель
			if new_goal and new_goal != goal:
				if len(new_goal) > 1:
					# Если антецедент правила состоит из нескольких термов и операторов
					# то мы должны его разбить и проверить каждую часть 
					for item in new_goal:
						if item not in facts:
							if item[0] != 'operation':
								goal = item
							else:
								goal = None
				else:
					goal = new_goal[0]

				print 'new goal = ', goal

		if goal is None:
			break

	return goal