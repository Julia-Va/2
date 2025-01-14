import doctest

class Messenger:

    def __init__(self, name: str, users: int):
        """
                Создание и подготовка к работе объекта "Мессенджер"

                :param name: Название мессенджера.
                :param users: Количество пользователей мессенджера.
                >>> messenger = Messenger(Telegram, 950000000)
                """
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.users = users

    def add_user(self, username: str) -> bool:
        """
        Добавить нового пользователя.

        :param username: Название мессенджер.
        :return: Успешно ли добавление.
        >>> messenger = Messenger("Telegram", 950000000)
        >>> messenger.add_user("new_user")
        True
        """
        ...

    def post_update(self, message: str) -> None:
        """
        Опубликовать сообщение.

        :param message: Текст сообщения.
        :return: Идентификатор сообщения.
        >>> messenger = Messenger("Telegram", 950000000)
        >>> messenger.post_update("Hello, my name is Julia")
        """
        ...
if __name__ == "__main__":
    doctest.testmod()