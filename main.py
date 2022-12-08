import doctest
from typing import Union  # TODO Написать 3 класса с документацией и аннотацией типов


class Cars:
    def __init__(self, max_speed: Union[int, float], time_for_100: Union[int, float], car_is_ok: bool):
        """
        Создание и подготовка к работе объекта "Машина"
        :param max_speed: Максимальная скорость, достигаемая машиной (км/ч)
        :param time_for_100: Время для достижения скорости 100 км/ч (с)
        :param car_is_ok: Параметр, показывающий, что машина не нуждается в ремонте, если True
        Примеры:
        >>> car = Cars(180, 11.2, False)  # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Макс. скорость должна быть типа int и float")
        if max_speed <= 0:
            raise ValueError("Макс. скорость должна быть положительным числом")
        self.max_speed = max_speed
        if not isinstance(time_for_100, (int, float)):
            raise TypeError("Время для разгона до 100 км/ч должно быть типа int и float")
        if time_for_100 <= 0:
            raise ValueError("Время для разгона до 100 км/ч должно быть положительным числом")
        self.time_for_100 = time_for_100
        if not isinstance(car_is_ok, bool):
            raise TypeError("Описание состояния машины должно быть типа bool")
        self.car_is_ok = car_is_ok

    def upgrading(self, upgrade_for_max_speed: Union[int, float], upgrade_for_time_for_100: Union[int, float]) -> None:
        """
        Улучшение параметров машины
        :param upgrade_for_max_speed: Величина, на которую увеличится макс. скорость (км/ч)
        :param upgrade_for_time_for_100: Величина, на которую уменьшится время для разгона до 100 км/ч (с)
        :raise ValueError: Если upgrade_for_max_speed неположительная величина, вызываем ошибку
        :raise ValueError: Если upgrade_for_time_for_100 неположительная величина, вызываем ошибку
        :raise ValueError: Если upgrade_for_time_for_100 больше или равен значению time_for_100, вызываем ошибку
        Примеры:
        >>> car = Cars(180, 11.2, True)
        >>> car.upgrading(5.5, 0.7)
        """
        ...

    def repairing(self) -> None:
        """
        Если car_is_ok == True: Печатается строка о том, что машина в порядке
        Если car_is_ok == False: car_is_ok становится True, выводится строка о том, что машину починили
        Примеры:
        >>> car = Cars(180, 11.2, False)
        >>> car.repairing()
        """
        ...


class Pens:
    def __init__(self, color: str, max_time_for_emptiness: int, time_for_emptiness: int):
        """
        Создание и подготовка к работе объекта "Ручка"
        :param color: цвет ручки
        :param time_for_emptiness: Время, через которое ручка перестанет писать
        :param max_time_for_emptiness: Максимальное время работы ручки без замены стилуса
        Примеры:
        >>> pen = Pens('red', 10, 7)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError('Название цвета должно быть типа str')
        self.color = color
        if not isinstance(max_time_for_emptiness, int):
            raise TypeError("Максимальное время для работы ручки должно быть типа int")
        if max_time_for_emptiness <= 0:
            raise ValueError("Максимальное время для работы ручки должно быть положительным числом")
        self.max_time_for_emptiness = time_for_emptiness
        if not isinstance(time_for_emptiness, int):
            raise TypeError("Время для работы ручки должно быть типа int")
        if time_for_emptiness < 0:
            raise ValueError("Время для работы ручки должно быть неотрицательным числом")
        if max_time_for_emptiness < time_for_emptiness:
            raise ValueError("Время для работы ручки не должно превышать максимальное значение")
        self.time_for_emptiness = time_for_emptiness

    def writing(self, time_of_writing: int) -> None:
        """
        Имитирует процесс писания. Уменьшает time_for_emptiness.
        Если time_for_emptiness стало равным нулю, сообщает пользователю
        :param time_of_writing: Время, в течение которого используется ручка
        :raise ValueError: Если функция продолжает работу при time_for_emptiness = 0, вызывает ошибку
        Примеры:
        >>> pen = Pens('red', 10, 7)  # инициализация экземпляра класса
        >>> pen.writing(2)
        """
        ...

    def has_pen_right_color(self, color_you_need: str) -> bool:
        """
        Сравнивает цвет ручки с необходимым
        :param color_you_need: нужный цвет ручки
        :raise TypeError: если color_you_need не строка, вызывает ошибку
        Примеры:
        >>> pen = Pens('red', 10, 7)
        >>> pen.has_pen_right_color('aquamarine')
        """
        ...

    def change_stylus(self) -> None:
        """
        Меняет стилус. Время работы ручки становится максимальным
        :raise ValueError: если время работы ручки имеет максимальное значение, то вызывает ошибку
        Примеры:
        >>> pen = Pens('red', 7, 2)
        >>> pen.change_stylus()
        """
        ...


class GroupsOfPolytech:
    def __init__(self, number: str, amount_of_students: int, amount_of_losers):
        """
        Создание и подготовка к работе объекта "Группа"
        :param number: номер группы формата *******/*****, где * - цифры
        :param amount_of_students: количество студентов
        :param amount_of_losers: количество неуспевающих
        Примеры:
        >>> group = GroupsOfPolytech('4731204/10003', 13, 2)
        """
        if not isinstance(number, str):
            raise TypeError("Номер группы должен быть типа str")
        if len(str(int(number.split('/')[0]))) != 7 or len(str(int(number.split('/')[1]))) != 5 \
                or number.count('/') != 1:
            raise ValueError("Номер группы должен быть формата *******/*****, где * - цифры")
        self.number = number
        if not isinstance(amount_of_students, int):
            raise TypeError("Количество студентов должно быть типа int")
        if amount_of_students <= 0:
            raise ValueError("Количество студентов должно быть положительным числом")
        self.amount_of_students = amount_of_students
        if not isinstance(amount_of_losers, int):
            raise TypeError("Количество неуспевающих должно быть типа int")
        if amount_of_losers <= 0:
            raise ValueError("Количество неуспевающих должно быть положительным числом")
        if amount_of_losers > amount_of_students:
            raise ValueError("Количество неуспевающих не должно превышать общее число студентов")
        self.amount_of_losers = amount_of_losers

    def session(self, amount_of_new_losers: int) -> None:
        """
        Оформляет неуспевающими определенное число студентов
        :param amount_of_new_losers: число людей, ставших неуспевающими
        :raise ValueError: Если число людей, ставших неуспевающими,
        больше числа успевающих (число всех - число неуспевающих), то вызывает ошибку
        Примеры:
        >>> group = GroupsOfPolytech('4731204/10003', 13, 2)
        >>> group.session(2)
        """
        ...

    def expulsion(self, amount_of_expelled: int) -> None:
        """
        Отчисляет определенное число неуспевающих студентов
        :param amount_of_expelled: число отчисляемых
        :raise ValueError: Если число отчисляемых больше числа неуспевающих, то вызывает ошибку
        Примеры:
        >>> group = GroupsOfPolytech('4731204/10003', 13, 2)
        >>> group.expulsion(1)
        """
        ...

    def closing_extra_session(self, amount_of_ex_losers: int) -> None:
        """
        Закрывает долги определенного числа студентов
        :param amount_of_ex_losers: число людей, закрывших долги
        :raise ValueError: Если число людей, закрывших долги,
        больше числа неуспевающих, то вызывает ошибку
        Примеры:
        >>> group = GroupsOfPolytech('4731204/10003', 13, 2)
        >>> group.closing_extra_session(1)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
