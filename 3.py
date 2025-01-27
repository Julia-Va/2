class Car:

    def __init__(self, mark: str, speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param mark: Марка автомобиля.
        :param speed: Максимальная скорость в км/ч.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self.mark = mark
        self.speed = speed

    def start_moving(self) -> None:
        """
        Начать движение транспортного средства.

        >>> car = Car("Porsche 911", 330)
        >>> car.start_moving()
        """
        ...

    def will_stop(self) -> None:
        """
        Остановить транспортное средство.

        >>> car = Car("Porsche 911", 330)
        >>> car.will_stop()
        """
        ...
