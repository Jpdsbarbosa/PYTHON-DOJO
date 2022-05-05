class Elevador:

    def __init__(self, id: int) -> None:
        self.__id = id 
        self.__andar = 1

    def set_andar(self, andar: int) -> None:
        self.__andar = andar

    def get_andar(self) -> int:
        return self.__andar

    def check_id(self, id: int) -> bool:
        return (self.__id == id)

    def get_id(self) -> int:
        return self.__id