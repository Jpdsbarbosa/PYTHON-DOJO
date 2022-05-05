from components import Elevador

elevador = Elevador()

while True:
    andar = int(input("Defina um andar: "))
    resposta = elevador.locomover(andar)
    print(resposta)
    print()
