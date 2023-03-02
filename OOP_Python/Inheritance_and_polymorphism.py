# 025 Наследование и полиморфизм

class CarsClass():
    '''Класс автомобилей'''

    def __init__(self, brand, model, year, probeg):
        '''Инициализация атрибутов'''
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def showCar(self):
        '''Показать информацию о машине'''
        print(f'{self.brand}, {self.model}, '
              f'{self.year} год, {self.probeg} км')

    def drowCar(self, km):
        '''Метод поездки авто'''
        self.probeg = str(int(self.probeg) + km)


# Использование экземпляра класса, как атрибута
class ClassBattery():
    '''Класс батареи'''

    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        '''Выводит информацию о батарее'''
        print('Этот автомобиль имеет заряд батареи: '
              + str(self.battery) + '%')


class ElectroCar(CarsClass):
    '''Класс электрокаров, унаследован от класса CarsClass'''

    def __init__(self, brand, model, year, probeg):  # Указываются атрибуты от родительского класса, которые нужны
        super().__init__(brand, model, year, probeg)  # Связывает потомка и родителя по атрибутам
        self.battery = ClassBattery()

    def showCar(self):
        '''Показать информацию о машине (переопределение метола родительского класса)'''
        print(f'{self.brand}, {self.model}')


s_car = CarsClass('Lada', 'Granta', '2010', '10')
s_car.showCar()
s_car.drowCar(100)  # Проехали на автомобиле
s_car.showCar()

tesla = ElectroCar('Tesla', 'T', '2017', 1000)
tesla.showCar()
# tesla.description_battery()
tesla.battery.description_battery()