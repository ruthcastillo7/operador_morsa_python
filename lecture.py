#permite unificar sentencias de asignación dentro de expresiones. Su nombre proviene de la forma que adquiere :=
#Supongamos un ejemplo en el que computamos el perímetro de una circunferencia, indicando al usuario que debe incrementarlo siempre y cuando no llegue a un mínimo establecido.
radio= 4.25
perimetro= 2*3.14*radio
if perimetro < 100:
	print("Aumentar el radio para alcanzar el perímetro mínimo")
	print("Actual perimetro: 	", perimetro)
#Aumentar el radio para alcanzar el perímetro mínimo.
#Actual perimeter: 26.69

##Versión con operador morsa
radio=4.25
if (perimetro := 2*3.14*radio) < 100:
	print("Aumentar el radio para alcanzar el perímetro mínimo")
	print("Actual perimeter: ", perimetro)
#Aumentar el radio para alcanzar el perímetro mínimo.
#Perímetro real: 26,69

#Consejo: Como hemos comprobado, el operador morsa permite realizar asignaciones dentro de expresiones, lo que, en muchas ocasiones, permite obtener un código más compacto. Sería conveniente encontrar un equilibrio entre la expresividad y la legibilidad.