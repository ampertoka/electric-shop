# общее поведение, свойства объектов и мы хотим иъ объединить ими
# РОДИТЕЛЬ или БАЗОВЫЙ КЛАСС всегда обладает наиболее общим
from abc import ABC

# как классы в энтерпрайзе испольщзуются
# у меня есть поставщик нейронок (LLMProvider), который описывает базовые методы:
# .call('текущий курс рубля в доллару'), result = .result()
# а реализация конкретная будет в GeminiProvider(LMMProvider),
# OpenAIProvider(LLMProvider) и т.д.

# git-hub-case когда все через тире (это еще javascript case)

# camel-case format
class PetAnimal:

    # СВОЙСТВА / ПОЛЯ / АТРИБУТЫ класса
    name: str = None
    age: int = None

    # self в Java - this
    # self ВСЕГДА передается первым параметров в функциях класса
    # именно поэтому они называются МЕТОДАМИ, потому что self говорит о
    # ПРИНАДЛЕЖНОСТИ к классу, в котором пишется функция.
    # поэтому функция в класси и называется МЕТОД КЛАССА

    # self - ОБЪЕКТА класса, а не класс. поэтому попытки обратиться к нему
    # не имея созданный объект вызовут ошибку
    # ЭТО КОНСТРУКТОР класса
    # создает INSTANCE объектов. но называется инициализация
    def __init__(self, name, age):
        # даже если нет свойств класса, записав в них первый раз что-то
        # Пайтон их автоматически (динамически) создаст
        self.name = name
        self.age = age

    # snake_case
    def make_sound(self):
        print("Звук Питомца")
    def sleep(self):
        print(self)
        print(f'{self.name} - zzz...')
    def wake_up(self):
        print('Проснулся')

    # dunder method - double underscore method
    # underscore - подчеркивание
    # их еще называют Магические методы
    def __str__(self):
        return f'Домашний Питомец: имя - {self.name}, возраст - {self.age}'

    # делает из класса функцию
    def __call__(self, *args, **kwargs):
        return 'call PetAnimal'

class Cat(PetAnimal):
    pass

# любой НАСЛЕДНИК создан для того чтоб КОНКРЕТИЗИРОВАТЬ
# свойства и функционал РОДИТЕЛЯ
# НАСЛЕДНИКИ совершенно не обязательны, если РОДИТЕЛЬ самодостаточен

# если б писали на JAVA:
# class Dog extends PetAnimal, ..., ...

class Dog(PetAnimal):
    # def __init__(self, name, age, breed):
    #     super().__init__(name, age)
    #     # порода (Русский Спаниель)
    #     self.breed = breed
    # override, переопределение
    def make_sound(self):
        print("Гав")
    def wake_up(self):
        print('и сделал ГАВ')
        super().wake_up()
        super().make_sound()

dog = Dog("Buddy", 3, "Golden Retriever")
dog.make_sound()
dog.sleep()
# print(dog.name)
# print(dog.age)
# ДИНАМИЧЕСКОЕ СОЗДАНИЕ СВОЙСТВ КЛАССА, лучше так не делать
# всегда лучше испольщзовать только те свойства и методы, что прописаны в классе
# dog.name_2 = 2
# print(dog.name_2)
# dog.wake_up()

# интерфейс - чертеж класса, где прописываются пустые функции
# и малое кол-во полей (ПУСТЫХ).
# в Java под это прям есть класс Intefrace. в питоне только ABC (Абстракный Класс)
class Car(ABC):
    def startup(self):
        """
        эта функция бла бла бла
        :return:
        """
        pass
    def drive(self):
        pass
    def stop(self):
        pass

# ячейки памяти и все такое
pet_1 = PetAnimal(name='Conos', age=3)
# print(pet_1)
# pet_2 = PetAnimal(name='Alice', age=6)
# print(pet_2)
# pet_3 = PetAnimal(name='Conos', age=3)
# print(pet_3)
# pet_4 = pet_3
# print(id(pet_3))
# print(pet_4)
# print(id(pet_4))

# вызов КОНСТРУКТОРа класса
# фигурные скобоки после имени класса вызывают КОНСТРУКТОР класса
# и создают ОБЪЕКТ класса
# ИНИЦИАЛИЗАЦИЯ / ИНСТАНЦИРОВАНИЕ, создание ЭКЗЕМПЛЯРА / ОБЪЕКТА класса
# pet_no_init = PetAnimal()
# print(pet_no_init)
# pet_no_init.make_sound()

# ПРОВЕРКА ТИПА ДАННЫХ
print(type(pet_1.name))
print(type(pet_1.age))
print(type(pet_1))


# ПРОВЕРКА ТИПА ДАННЫХ ЧТОБ ВЫЗЫВАТЬ ФУНКЦИЮ
if type(pet_1.name) == str:
    print(pet_1.name.upper())
