y = bitcoin["Price"].values
x = bitcoin.index.values

plt.figure(figsize=(16,7))
plt.plot(x, y, marker="o", linestyle="--", label='bitcoins price')

plt.axhspan(8000, 10000, alpha = 0.1)  # Colocamos una banda de color para los valores entre 8K i 10K
plt.ylim(0,20000)  # Limitamos el eje x
plt.legend(loc="upper left")  # Colocamos la leyenda
plt.title(u'Precios de Bitcoin al cierre de la sesión')  # Colocamos el título del gráfico
plt.xlabel('Día')  # Colocamos la etiqueta en el eje x
plt.ylabel('Precio')  # Colocamos la etiqueta en el eje y
plt.xticks(rotation=45) # rotamos las etiquetas del eje x
