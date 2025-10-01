class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color 
        self.size: str = size
        self.wetness: int= 0

print("Qual a cor da sua toalha?")
color = input()
print("Qual o tamanho?")
size = input()
emilly: Towel = Towel(color, size)
print(f"A cor da sua toalha é {emilly.color} e o tamanho dela é {emilly.size}")

