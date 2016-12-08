# -*- coding: utf-8 -*-

from base import Fact
from base import Production
from direct import direct_otput
from reverse import reverse_output

"""
База знаний для продукционной модели

Facts:
				sky_clouded=True
				pressure_low=True

Productions:
				-- [!]sky_clouded [||]&& pressure_low -> gonna_rain

				sky_clouded && pressure_low -> gonna_rain
				gonna_rain -> need_umbrella

"""


Facts = []
Facts.append(Fact('sky_clouded',True))
Facts.append(Fact('pressure_low',True))
#Facts.append(Fact('have_umbrella',True))

Productions = []
Productions.append(Production('sky_clouded && pressure_low -> gonna_rain'))
Productions.append(Production('gonna_rain -> take_umbrella'))
#Productions.append(Production('gonna_rain && have_umbrella -> take_umbrella'))

Goal = ('take_umbrella', True)

print """++++++++ База Знаний +++++++++
Facts:
				sky_clouded = True
				pressure_low = True

Productions:
				sky_clouded && pressure_low -> gonna_rain
				gonna_rain -> take_umbrella

Goal:
				take_umbrella



"""


print '======== Прямой вывод ========'

if direct_otput(Productions, Facts, Goal):
	print Goal[0], ' -> yes.'
else:
	print Goal[0], ' -> no.'

print '=============================='
print
print
print '======== Обратный вывод ========'
print
if not reverse_output(Productions, Facts, Goal):
	print
	print Goal[0], ' -> you\'re right about it.'
else:
	print
	print Goal[0], ' -> you\'re wrong about it.'

print '================================'
