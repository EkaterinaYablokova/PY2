class SocialNetwork:
    """ Базовый класс. """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Социальная сеть {self.name}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'


class VK(SocialNetwork):  # наследуется от SocialNetwork
    """ВКонтакте"""
    def __init__(self, name: str, colors: str = "Сине-белый"):
        super().__init__(name)
        self.colors = colors

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.colors!r})'

    def __str__(self):
        return f"Социальная сеть: {self.name} Цвета: {self.colors}"


class Youtube(SocialNetwork):
    """Ютуб"""
    def __init__(self, name: str, year: int = "2005"):
        super().__init__(name)
        self.year = year

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.year!r})'

    def __str__(self):
        return f"Социальная сеть: {self.name} Год создания: {self.year}"

    if __name__ == "__main__":
        #  тестируем класс
        vk = SocialNetwork('ВКонтакте')
        print(vk.name)
        vk1 = VK('Сине-белый')
        print(vk1.colors)

        yt = SocialNetwork('Ютуб')
        print(yt.name)
