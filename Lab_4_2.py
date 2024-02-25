if __name__ == "__main__":
    # Write your solution here
    class
        """Базовый класс Транспортное средство"""

        def __init__(self, brand: str, model: str, year: int):
            """
            Конструктор класса
 :param brand: Марка транспортного средства
 :param model: Модель транспортного средства
 :param year: Год выпуска транспортного средства
            """
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """
 Возвращает строковое представление объекта
 :return: Строковое представление объекта
            """
            return f"{self.brand} {self.model}, {self.year}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для отладки
            :return: Строковое представление объекта
            """
            return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"


    class Car(Vehicle):
        """Дочерний класс Легковой автомобиль"""

        def __init__(self, brand: str, model: str, year: int, num_seats: int):
            """
 Конструктор класса
 :param brand: Марка автомобиля
 :param model: Модель автомобиля
 :param year: Год выпуска автомобиля
 :param num_seats: Количество сидячих мест в автомобиле
            """
            super().__init__(brand, model, year)
            self.num_seats = num_seats

        def __str__(self) -> str:
            """
 Возвращает строковое представление объекта
 :return: Строковое представление объекта
            """
            return f"{self.brand} {self.model}, {self.year}, {self.num_seats} сидячих мест"

        def start_engine(self) -> str:
            """
 Запускает двигатель автомобиля
 :return: Сообщение о запуске двигателя
            """
            return f"Автомобиль {self.brand} {self.model} с двигателем запущен"

        def stop_engine(self) -> str:
            """
 Останавливает двигатель автомобиля
 :return: Сообщение об остановке двигателя
            """
            return f"Автомобиль {self.brand} {self.model} с двигателем остановлен"


    class Truck(Vehicle):
        """Дочерний класс Грузовой автомобиль"""

        def __init__(self, brand: str, model: str, year: int, payload: float):
            """
            Конструктор класса
            :param brand: Марка грузового автомобиля
            :param model: Модель грузового автомобиля
            :param year: Год выпуска грузового автомобиля
            :param payload: Грузоподъемность грузового автомобиля в тоннах
            """
            super().__init__(brand, model, year)
            self.payload = payload

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта
            :return: Строковое представление объекта
            """
            return f"{self.brand} {self.model}, {self.year}, Грузоподъемность: {self.payload} т"

        def load_cargo(self, weight: float) -> str:
            """
            Погружает груз на грузовик
 :param weight: Вес груза в тоннах
 :return: Сообщение о погрузке груза
            """
            return f"На грузовик {self.brand} {self.model} погружен груз массой {weight} т"

        def unload_cargo(self, weight: float) -> str:
            """
 Разгружает грузовик
 :param weight: Вес груза в тоннах
 :return: Сообщение о разгрузке грузовика
            """
            return f"С грузовика {self.brand} {self.model} разгружен груз массой {weight} т"


    car = Car("Toyota", "Camry", 2022, 5)
    print(car) # Toyota Camry, 2022, 5 сидячих мест
    print(car.start_engine()) # Автомобиль Toyota Camry с двигателем запущен

    truck = Truck("Volvo", "FH16", 20222022, 30)
    print(truck) # Volvo FH16, 2022, Грузоподъемность: 30 т
    print(truck.load_cargo(15)) # На грузовик Volvo FH16 погружен груз массой 15 т
