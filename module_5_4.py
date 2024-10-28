class House:
    # Атрибут класса для хранения истории построенных домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Получаем название дома из args
        house_name = args[0] if args else "Unnamed House"

        # Создаем новый объект
        instance = super(House, cls).__new__(cls)

        # Добавляем название дома в историю
        cls.houses_history.append(house_name)

        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


# Пример работы с классом House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки'] (h2 и h3 удалены, но история осталась)
