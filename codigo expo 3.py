historial=[]

historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial:", historial)

pagina_actual=historial[2]
print ("pagina actual:", pagina_actual)

pagina_salida = historial.pop()
print("saliendo de ", pagina_salida)

print("historial actualizado", historial)