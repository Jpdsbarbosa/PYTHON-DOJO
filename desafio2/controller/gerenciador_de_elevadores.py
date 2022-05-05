class GerenciadorDeElevadores:

    def __init__(self, elevador1: int, elevador2: int) -> None:
        self.__elevadores = [elevador1, elevador2]

    def locomover(self, andar: int, id: int) -> None:
        if andar < 1 or andar > 15: return self.__mensagem_de_erro()
        else:
            return self.__filtrar_elevador_e_alterar_andar(andar, id)

    def __filtrar_elevador_e_alterar_andar(self, andar, id):
        for elevador in self.__elevadores:
            if elevador.check_id(id):
                return self.__alterar_andar_e_retornar_informacao(andar, elevador)

    def __alterar_andar_e_retornar_informacao(self, andar, elevador) -> None:
        elevador.set_andar(andar)
        if andar == 1: return self.__mensagem_de_alteracao_para_terreo(elevador)
        return self.__mensagem_de_alteracao_de_andar(elevador)

    def __mensagem_de_erro(self) -> None:
        return f'Andar Incorreto!'

    def __mensagem_de_alteracao_de_andar(self, elevador) -> None:
        return f'Elevador {elevador.get_id()} indo para o {elevador.get_andar()}º andar'
    
    def __mensagem_de_alteracao_para_terreo(self, elevador) -> None:
        return f'Elevador {elevador.get_id()} indo/ou para o Terreo'
