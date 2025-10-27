produto = float(input("Qual o preço do produto?: "))
desconto = (produto * 5)/100
valorfinal = produto - desconto

print(f"O preço do produto é {produto}, é com 5% de desconto fica {valorfinal}")