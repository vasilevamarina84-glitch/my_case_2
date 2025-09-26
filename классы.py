# Базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Животное издаёт звук."

    def info(self):
        return f"Это {self.name}."


# Производный класс (наследует от Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызов конструктора базового класса
        self.breed = breed

    # Переопределение метода speak
    def speak(self):
        return "Гав-гав!"

    # Новый метод, специфичный для Dog
    def fetch(self):
        return "Собака приносит палку."

    # Переопределение метода info с расширением функциональности
    def info(self):
        base_info = super().info()  # вызов метода базового класса
        return f"{base_info} Порода: {self.breed}."


# Тестовая часть программы
if __name__ == "__main__":
    # Создание объекта базового класса
    animal = Animal("Неизвестное существо")
    print("=== Базовый класс Animal ===")
    print(animal.info())
    print(animal.speak())

    print("\n=== Производный класс Dog ===")
    # Создание объекта производного класса
    dog = Dog("Бобик", "Овчарка")
    print(dog.info())
    print(dog.speak())
    print(dog.fetch())

input("\nДемонстрация завершенв. Нажмите Enter для выхода...")