# 1) Базовый объект и методы
#   - Создай объект класса PetAnimal без конструктора (как в уроке).
#   - Присвой ему поля name и age.
#   - Вызови make_sound, sleep, wake_up и выведи объект через print (сработает __str__).
from abc import ABC

from lesson_9_OOP.oop_9 import PetAnimal, Dog, Cat

wolf = PetAnimal('Garry', 10)
wolf.wake_up()
wolf.sleep()
wolf.wake_up()
print(wolf)


#   3) Наследование: CatV2
#   - Создай наследника CatV2(Cat) и переопредели метод make_sound, чтобы печатал "Мяу".
#   - Создай объект CatV2, вызови make_sound и sleep (унаследованный метод).
class CatV2(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Мяу')


catV2_1 = CatV2('Aliss', 2)
catV2_1.make_sound()
catV2_1.sleep()


#   4) Переопределение и super(): DogV2
#   - Создай наследника DogV2(Dog), переопредели make_sound ("Гав") и wake_up.
#   - Внутри wake_up сначала выведи свою строку, затем вызови super().wake_up() и затем super().make_sound().
#   - Создай объект DogV2 и вызови wake_up. Убедись в корректном порядке сообщений.
class DogV2(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Гав')

    def wake_up(self):
        print('и сделал Гав')
        super().wake_up()
        super().make_sound()


dogRex = DogV2('Rex', 10)
dogRex.wake_up()


#   5) Конструктор у наследника PetAnimalInit
#   - Создай класс PetAnimalInit(PetAnimal) и реализуй __init__(self, name: str, age: int), присваивая поля name и age через self.
#   - Создай объекты PetAnimalInit/CatV2/DogV2 с использованием конструктора там, где это применимо.
class PetAnimalInit(PetAnimal):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


petAnimalInit_1 = PetAnimalInit('Bax', 2)
cat_tos = CatV2('Gosha', 4)
dog_me = DogV2('Gor', 5)


#   6) Расширение DogBreed: новое свойство и __str__
#   - Создай наследника DogBreed(DogV2), добавь поле breed и конструктор __init__(self, name, age, breed) с вызовом super().__init__(name, age).
#   - Переопредели __str__ в DogBreed так, чтобы добавить породу, используя super().__str__ в составе результата.
class DogBreed(DogV2):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f'Домашний Питомец: имя - {self.name}, возраст - {self.age}, порода - {self.breed}'
#   7) Полиморфизм на списке питомцев
#   - Создай список из разных животных: [PetAnimal(), CatV2(...), DogBreed(...), PetAnimalInit(...)].
#   - Напиши функцию run_morning_routine(pets), которая для каждого вызывает wake_up и make_sound.
#   - Покажи, что для разных классов вызываются разные реализации (переопределения).
animals = [
    PetAnimal(name="Generic Pet", age=2),

    CatV2(
        name="Misty",
        age=3
    ),

    DogBreed(
        name="Rex",
        age=4,
        breed="German Shepherd"
    ),

    PetAnimalInit(
        name="Kesha",
        age=1
    )
]
def run_morning_routine(pets):
    for i in animals:
        i.wake_up()
        i.make_sound()
#   8) Интерфейс (ABC): Car
#   - Создай класс-наследник от Car (например, GasCar или ElectricCar).
#   - Реализуй методы startup, drive, stop простыми print-сообщениями.
#   - Создай объект и вызови все три метода.
class Car(ABC):
    def startup(self):
        pass
    def drive(self):
        pass
    def stop(self):
        pass

class GasCar(Car):
    def startup(self):
        print('Тронулись')
    def drive(self):
        print('едем')
    def stop(self):
        print('Остановился')
gasCarMers = GasCar()
gasCarMers.startup()
gasCarMers.drive()
gasCarMers.stop()
#   9) Память и ссылки (id)
#   - Создай pet_a = PetAnimalInit("Rex", 2) и сделай pet_b = pet_a.
#   - Выведи id(pet_a) и id(pet_b), докажи, что это одна и та же ячейка (изменение pet_b.name меняет pet_a.name).
pet_a = PetAnimalInit('Rex', 2)
pet_b = pet_a
print(id(pet_a))
print(id(pet_b))
pet_b.name = 'Mery'
print(id(pet_a))
print(id(pet_b))
