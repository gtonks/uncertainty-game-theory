class FoodSource:
    def __init__(self) -> None:
        self.__doves = 0
        self.__hawks = 0

    def add_dove(self):
        self.__doves += 1

    def remove_dove(self):
        self.__doves -= 1

    def add_hawk(self):
        self.__hawks += 1

    def remove_hawk(self):
        self.__hawks -= 1

    def get_doves(self) -> int:
        return self.__doves
    
    def get_hawks(self) -> int:
        return self.__hawks
