# TODO Написать 3 класса с документацией и аннотацией типов

from typing import Union

class PenSet:
    def __init__(self, num_pens: int, color: str):
        """
        Создание объекта "Набор ручек"

        :param num_pens: Количество ручек в наборе
        :param color: Цвет ручек

        Примеры:
        >>> pen_set = PenSet(10, "blue")  # инициализация экземпляра класса
        """
        if not isinstance(num_pens, int) or num_pens <= 0:
            raise ValueError("Количество ручек должно быть положительным целым числом")
        self.num_pens = num_pens

        if not isinstance(color, str):
            raise TypeError("Цвет ручек должен быть строкой")
        self.color = color

    def use_pen(self) -> None:
        """
        Использование ручки из набора.

        Пример:
        >>> pen_set = PenSet(10, "blue")
        >>> pen_set.use_pen()
        """
        ...

    def add_pens(self, additional_pens: int) -> None:
        """
        Добавление дополнительных ручек к набору.

        :param additional_pens: Количество добавляемых ручек

        :raise ValueError: Если количество добавляемых ручек отрицательно, вызываем ошибку

        Пример:
        >>> pen_set = PenSet(10, "blue")
        >>> pen_set.add_pens(5)
        """
        if not isinstance(additional_pens, int) or additional_pens < 0:
            raise ValueError("Количество добавляемых ручек должно быть неотрицательным целым числом")
        ...


class MarkerSet:
    def __init__(self, num_markers: int, tip_size: float):
        """
        Создание объекта "Набор фломастеров"

        :param num_markers: Количество фломастеров в наборе
        :param tip_size: Размер наконечника фломастера

        Примеры:
        >>> marker_set = MarkerSet(8, 0.5)  # инициализация экземпляра класса
        """
        if not isinstance(num_markers, int) or num_markers <= 0:
            raise ValueError("Количество фломастеров должно быть положительным целым числом")
        self.num_markers = num_markers

        if not isinstance(tip_size, (int, float)) or tip_size <= 0:
            raise ValueError("Размер наконечника должен быть положительным числом")
        self.tip_size = tip_size

    def draw(self, area: Union[int, float]) -> None:
        """
        Нанесение рисунка фломастером на поверхность.

        :param area: Площадь, которую можно нарисовать

        :raise ValueError: Если площадь отрицательна или не является числом, вызываем ошибку

        Пример:
        >>> marker_set = MarkerSet(8, 0.5)
        >>> marker_set.draw(10.5)
        """
        ...

    def replace_marker(self, new_tip_size: float) -> None:
        """
        Замена фломастера с указанным размером наконечника.

        :param new_tip_size: Новый размер наконечника

        :raise ValueError: Если новый размер наконечника отрицательный или не является числом, вызываем ошибку

        Пример:
        >>> marker_set = MarkerSet(8, 0.5)
        >>> marker_set.replace_marker(0.8)
        """
        ...


class Notebook:
    def __init__(self, num_pages: int, paper_type: str):
        """
        Создание объекта "Тетрадь"

        :param num_pages: Количество страниц в тетради
        :param paper_type: Тип бумаги

        Примеры:
        >>> notebook = Notebook(100, "lined")  # инициализация экземпляра класса
        """
        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.num_pages = num_pages

        if not isinstance(paper_type, str):
            raise TypeError("Тип бумаги должен быть строкой")
        self.paper_type = paper_type

    def write_on_page(self, text: str) -> None:
        """
        Запись текста на страницу тетради.

        :param text: Текст для записи

        :raise ValueError: Если текст не является строкой, вызываем ошибку

        Пример:
        >>> notebook = Notebook(100, "lined")
        >>> notebook.write_on_page("Hello, world!")
        """
        ...

    def tear_out_page(self, page_number: int) -> None:
        """
        Вырывание страницы из тетради.

        :param page_number: Номер страницы для вырывания

        :raise ValueError: Если номер страницы отрицательный или не является целым числом, вызываем ошибку

        Пример:
        >>> notebook = Notebook(100, "lined")
        >>> notebook.tear_out_page(5)
        """
        ...
