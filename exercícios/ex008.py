medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hec = medida * 0.01
de = medida * 0.1
cm = medida * 100
mm = medida * 1000
dm = medida * 10000
print(f"A media de {medida}m corresponde a\n{km} quilômetro\n{hec} hectômetro\n{de} decâmetro\n{dm} decimetro\n{cm :.0f} centimetro\n{mm :.0f} milimetro")