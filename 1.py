import doctest

class Furniture:

    def __init__(self, material: str, weight: float):
        """
                Создание и подготовка к работе объекта "Мебель"

                :param material: Материал изделия.
                :param weight: Вес изделия.
                >>> furniture = Furniture(wood, 14)
                """

        if weight <= 0:

            raise ValueError("Вес должен быть положительным числом.")

        self.material = material

        self.weight = weight

    def assemble(self) -> bool:

        """

        Собрать мебель.

        :return: Сообщение о завершении сборки.

        >>> chair = Chair("wood", 7.0)

        >>> chair.assemble()

        'Мебель собрана.'

        """
        ...
    def move(self, new_location: str) -> bool:
        """
        Переместить мебель в новое место.

        :param new_location: Новое местоположение.
        :return: Успешно ли перемещение.
        >>> chair = Chair("wood", 7.0)
        >>> chair.move("living room")
        True
        """
if __name__ == "__main__":
    doctest.testmod()