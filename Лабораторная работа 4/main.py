import doctest


class HeadPhones:
    def __init__(self, color: str, country: str, are_working: bool):
        """
        Создание и подготовка к работе объекта "Наушники"
        :param color: Цвет наушников
        :param country: Страна - производитель
        :param are_working: Состояние (работают ли)
        Пример:
        >>> headphones1 = HeadPhones("Чёрный", "Китай", False)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color
        if not isinstance(color, str):
            raise TypeError("Название страны-производителя должно быть типа str")
        self._country = country  # если цвет теоретически поменять можно, то страну-производителя никак не стоит
        if not isinstance(are_working, bool):
            raise TypeError("Оценка состояния должна быть типа bool")
        self.are_working = are_working

    def __str__(self) -> str:
        if self.are_working:
            update = ''
        else:
            update = 'не'
        return f'Наушники {self.color} цвета из {self._country} в {update}рабочем состоянии'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color={self.color}, country={self._country}, " \
               f"headphone are in good condition={self.are_working})"

    def change_color(self, new_color: str) -> None:
        """
        Меняет цвет наушников
        :param new_color: Новый цвет
        Пример:
        >>> headphones1 = HeadPhones("Чёрный", "Китай", False)
        >>> headphones1.change_color("Аквамарин")
        """
        ...

    def repairing(self) -> str:
        """
        Если are_working == True, выводится строка об исправности.
        В противном случае are_working присваивается значение True, выводится строка о проведённом ремонте
        :return: Строка об исправности / проведённом ремонте
        Пример:
        >>> headphones1 = HeadPhones("Чёрный", "Китай", False)
        >>> headphones1.repairing()
        """
        ...


class WiredHeadPhones(HeadPhones):
    def __init__(self, color: str, country: str, are_working: bool, length: int):
        """
        Создание и подготовка к работе объекта "Проводные наушники"
        :param color: Цвет наушников
        :param country: Страна-производитель
        :param are_working: Состояние (работают ли)
        :param length: Длина проводов (см)
        Пример:
        >>> wired1 = WiredHeadPhones("Жёлтый", "Франция", True, 20)
        """
        super().__init__(color, country, are_working)
        if not isinstance(length, int):
            raise TypeError("Длина наушников должна быть типа int")
        if length <= 0:
            raise ValueError("Длина наушников должна быть положительной величиной")
        self.length = length

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color={self.color}, country={self._country}, length={self.length}), " \
               f"headphone are in good condition={self.are_working})"

    def repairing(self, new_length: int = None) -> str:
        """
        1) Если are_working == True, выводится строка об исправности.
        В противном случае are_working присваивается значение True, выводится строка о проведённом ремонте
        2) Если задаётся параметр new_length, атрибуту length объекта присваивается это значение,
        выводится сообщение о замене (для этого была перегрузка)
        :return: Строка об исправности / проведённом ремонте, замене длины наушников (если таковая была произведена)
        Пример:
        >>> wired1 = WiredHeadPhones("Жёлтый", "Франция", True, 20)
        >>> wired1.repairing(25)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
