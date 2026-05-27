import pandas as pd

df = pd.read_csv("datos/ventas.csv")

print("DATOS:")
print(df)

ventas_totales = (df["ventas"] * df["precio"]).sum()

print("\nVentas totales:", ventas_totales)

producto_mas_vendido = df.loc[df["ventas"].idxmax(), "producto"]

print("Producto más vendido:", producto_mas_vendido)
