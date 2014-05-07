# coding=utf-8

__author__ = 'nRikee'


def hora_a_texto ( hora, lang='es' ):
	h = hora [ 0 ]
	m = hora [ 1 ]

	# ----- Personalizable -----
	if lang == 'es':
		inicio_singular = 'Es la '
		inicio_plural = 'Son las '

		horas = [ 'una', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce' ]
		minutos = [ '', ' y cuarto ', ' y media ', ' menos cuarto ' ]

		ini_manana = 5
		ini_tarde = 15
		ini_noche = 20

		am = ' de la mañana.'
		pm = ' de la tarde.'
		nm = ' de la noche.'
	elif lang == 'ca':
		inicio_singular = 'Es la '
		inicio_plural = 'Son les '

		horas = [ 'una', 'dos', 'tres', 'quatre', 'cinc', 'sis', 'set', 'vuit', 'nou', 'deu', 'onze', 'dotze' ]
		minutos = [ '', ' i quart ', ' i mitja ', ' menys quart ' ]

		ini_manana = 5
		ini_tarde = 15
		ini_noche = 20

		am = ' del matí.'
		pm = ' de la vesprada.'
		nm = ' de la nit.'
	# ----- Personalizable -----

	imprecisa = ''

	# Si pasa la hora de y 40 se debe sumar 1 a la hora
	if m > 40:
		h += 1

	# Primera parte
	indice = ( h - 1 ) % len ( horas )
	if horas [ indice ] == 'una':
		imprecisa += inicio_singular
	else:
		imprecisa += inicio_plural

	# Segunda parte
	imprecisa += horas [ indice % (12 + 1) ]

	# Tercera parte, minutos
	indice = ( ( m + 5 ) / 15 ) % len ( minutos )
	imprecisa += minutos [ indice ]

	# Parte final
	if ini_manana <= hora < ini_tarde:
		imprecisa += am
	elif ini_tarde <= hora < ini_noche:
		imprecisa += pm
	elif ini_noche <= hora < ini_manana:
		imprecisa += nm

	return imprecisa


# ----- Algunos ejemplos ----- #
print "08:04", hora_a_texto ( [ 8, 4 ] )
print "16:25", hora_a_texto ( [ 16, 25 ], lang='es' )

print "21:50", hora_a_texto ( [ 21, 50 ], lang='ca' )
print "23:56", hora_a_texto ( [ 23, 56 ], lang='ca' )
