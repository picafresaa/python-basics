#Fernanda Sánchez Estudillo
#A01735803
#02 de marzo de 2026

#entradas: tipo de silla, tipo de cliente, cantidad de sillas
#salida: total a pagar
def costo_silla(tipo_silla):
	if(tipo_silla == "E"):
		costo = 900
	elif (costo_silla == "B"):
		costo == 700
	else:
		costo = 1500
	return costo
	
def p_descuento(subtotal, tipo_cliente):
	if (tipo_cliente == "F"):
		return 0.2
	else: 
		if (subtotal >= 10000):
			return  0.1
		elif (subtotal >= 20000):
			return 0.15
		else: 
			return 0

def main():
	print("tienda de sillas")
	tipo_s = input("Tipo de silla B)Basica E)Estandar L)Lujo:")
	tipo_cliente=input("Tipo de cliente N)Normal F)Frecuente: ")
	cantidad = int(input("Cantidad de sillas: "))
	
	subtotal = costo_silla(tipo_s) * cantidad
	descuento = subtotal * p_descuento(subtotal, tipo_cliente)
	precio_final = subtotal - descuento
	print(f"Subtotal = {subtotal:.2f}")
	print(f"Descuento = {descuento:.2f}")
	print(f"Total = {precio_final:.2f}")
	
	
main()