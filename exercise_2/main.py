"""
Задание: Создать функцию validate_user_input(data), которая принимает словарь с данными пользователя. Функция
должна проверять наличие и корректность ключей name (строка) и age (положительное число). В случае некорректных
данных генерировать соответствующие исключения.

Пошаговая инструкция:
    Создайте функцию validate_user_input(data).
    Проверьте, что data является словарем. Если нет, вызовите TypeError.
    Проверьте, что ключ name присутствует в словаре и его значение является строкой. Если нет, вызовите ValueError.
    Проверьте, что ключ age присутствует в словаре и его значение является положительным числом. Если нет, вызовите ValueError.
    Используйте ключевое слово from, чтобы создать цепочку исключений, если это необходимо.

Проверка:
    Протестируйте функцию с корректными данными, например, {"name": "Alice", "age": 30}.
    Протестируйте функцию с отсутствующим ключом name.
    Протестируйте функцию с некорректным значением для age (например, строкой или отрицательнымчислом).
    Протестируйте функцию с некорректным типом входных данных (например, строкой вместо словаря).

"""

def validate_user_input(data):
    try:
        if not isinstance(data, (dict)):
            raise TypeError("Недопустимый тип данных: ожидается словарь")
        if not "name" in data.keys():
            raise ValueError("Отсутствует ключ 'name'")
        if not isinstance(data["name"], (str)):
            raise ValueError("Недопустимый тип значения по ключу 'name'")
        if not "age" in data.keys():
            raise ValueError("Отсутствует ключ 'age'")
        if not isinstance(data["age"], (int, float)):
            raise ValueError("Недопустимый тип значения по ключу 'age'")
        if not data["age"] > 0:
            raise ValueError("Недопустимое значение по ключу 'age'")
    
    except Exception as e:
        print(f"Данные некорректны: {e}")
    else:
        print("Данные корректны")
    finally:
        print("***** Проверка данных завершена")

if __name__ == "__main__":
    validate_user_input({"name": "Alice", "age": 30})
    validate_user_input({"age": 30})
    validate_user_input({"name": "Alice", "age": -30})
    validate_user_input({"name": "Alice", "age": "abc"})
    validate_user_input("abc")
