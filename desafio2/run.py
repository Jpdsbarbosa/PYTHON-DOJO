from models import Elevador
from controller import GerenciadorDeElevadores

elevador1 = Elevador(1)
elevador2 = Elevador(2)
gerenciadorDeElevadores = GerenciadorDeElevadores(elevador1, elevador2)

while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))

    resposta = gerenciadorDeElevadores.locomover(andar, elevadorId)
    
    print(resposta)
    print()