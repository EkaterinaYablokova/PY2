import doctest  # TODO Написать 3 класса с документацией и аннотацией типов


class Fridge:
    def __init__(self, capacity_volume: float, temp: int):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param capacity_volume: Объем холодильника
        :param temp: Температура в холодильнике

        Примеры:
        >>> fridge = Fridge(200, -2)  #  инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, float):
            raise TypeError("Объем холодильника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем холодильника должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(temp, (int, float)):
            raise TypeError("Температура в холодильнике должна быть int или float")
        if temp > 0:
            raise ValueError("Температура в холодильнике не может быть положительным числом")
        self.temp = temp

    def is_empty_fridge(self) -> bool:
        """
        Функция, которая проверяет является ли холодильник пустым

        :return: Является ли холодильник пустым

        Примеры:
        >>> fridge = Fridge(5, 0)
        >>> fridge.is_empty_fridge()
        """
        ...

    def add_product_to_fridge(self, product: int) -> None:
        """
        Добавление продуктов в холодильник.
        :param product: Количество добавляемых продуктов

        :raise ValueError: Если количество добавляемых продуктов превышает свободное место в холодильнике,
        то вызываем ошибку

        Примеры:
        >>> fridge = Fridge(5, 0)
        >>> fridge.add_product_to_fridge(4)
        """
        if not isinstance(product, int):
            raise TypeError("Добавляемый продукт должен быть типа int")
        if product < 0:
            raise ValueError("Добавляемый продукт должен быть положительным числом")
        self.product = product
        ...

    def remove_product_from_fridge(self, estimate_product: int) -> None:
        """
        Извлечение продуктов из холодильника.

        :param estimate_product: Количество извлекаемых продуктов
        :raise ValueError: Если количество извлекаемых продуктов превышает количество всего продуктов в холодильнике,
        то возвращается ошибка

        :return: Количество реально извлеченных продуктов

        Примеры:
        >>> fridge = Fridge(5, 5)
        >>> fridge.remove_product_from_fridge(4)
        """
        if not isinstance(estimate_product, int):
            raise TypeError("Извлекаемый продукт должен быть типа int")
        if estimate_product < 0:
            raise ValueError("Извлекаемый продукт должен быть положительным числом")
        self.estimate_product = estimate_product
        ...


if __name__ == "__main__":
    fridge = Fridge(200, -2)
    doctest.testmod()


class Car:
    def __init_(self, speed: int, brand: str):
        """
        Создание и подготовка к работе объекта "Машина"

        :param speed: Скорость автомобиля
        :param brand: Брэнд автомобиля
        """
        if not isinstance(speed, int):
            raise TypeError("Скоросто должна быть типа int")
        if speed < 0:
            raise ValueError("Скорость должна быть положительной")
        self.speed = speed
        self.brand = brand


class Wardrobe:
    def __init__(self, quantity: int, colour: str):
        """

        :param quantity: Количество штанов в шкафу
        :param colour: Цвет штанов
        """
        if not isinstance(quantity, float):
            raise TypeError("Количестов брюк должно быть типа int или float")
        if quantity <= 0:
            raise ValueError("Количестов брюк должно быть положительным числом")
        self.quantity = quantity
        self.colour = colour


class House:
    def __init__(self, street, number):
        """
        Характеристики дома
        :param street:
        :param number:
        """
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        print("Дом на улице" + self.street + " под номером " + str(self.number) + " построен.")

    def age_of_house(self, year):
        """
        возраст дома
        :param year:
        """
        self.age += year

    pass
