"""
Задание: Создать класс NegativeNumberError, который будет генерироваться, если переданное число
отрицательное. Использовать это исключение в функции check_positive_number.

Пошаговая инструкция:
    Создайте класс NegativeNumberError, наследующий от Exception.
    Переопределите конструктор, чтобы принимать значение числа и сообщение об ошибке.
    Переопределите метод __str__, чтобы возвращать информативное сообщение.
    Создайте функцию check_positive_number, которая проверяет, является ли число положительным. Если
    число отрицательное, функция должна вызывать исключение NegativeNumberError.

Проверка:
    Протестируйте функцию с отрицательным числом.
    Протестируйте функцию с положительным числом.
    Убедитесь, что исключение NegativeNumberError правильно обрабатывается и выводит информативное сообщение.

"""

class NegativeNumberError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.message = message
        self.value = value

    def __str__(self):
        return f"{self.message}: {self.value}. Аргумент должен быть положительным числом"
    
def check_positive_number(value: float | int):
    if value < 0: raise NegativeNumberError("Недопустимое значение аргумента", value)

if __name__ == "__main__":
    try:
        check_positive_number(-10)
    except NegativeNumberError as e:
        print(f"Ошибка выполнения функции: {e}")
    else:
        pass
    finally:
        pass

    try:
        check_positive_number(10)
    except NegativeNumberError as e:
        print(f"Ошибка выполнения функции: {e}")
    else:
        pass
    finally:
        pass
    