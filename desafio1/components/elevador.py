class Elevador:

    def __init__(self) -> None:
        self.__andar = 1

    def locomover(self, andar: int) -> None:
        if andar < 1 or andar > 15: return self.__mensagem_de_erro()
        else:
            return self.__alterar_andar_e_retornar_informacao(andar)

    def __alterar_andar_e_retornar_informacao(self, andar) -> None:
        self.__andar = andar
        if andar == 1: return self.__mensagem_de_alteracao_para_terreo()
        return self.__mensagem_de_alteracao_de_andar()

    def __mensagem_de_erro(self) -> None:
        return f'Andar Incorreto! Elevador no {self.__andar}º andar'

    def __mensagem_de_alteracao_de_andar(self) -> None:
        return f'Elevador indo para o {self.__andar}º andar'
    
    def __mensagem_de_alteracao_para_terreo(self) -> None:
        return f'Elevador indo/ou para o Terreo'
