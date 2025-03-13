import json
import sys


def load_values(values_path):
    """
    Загружает значения тестов из JSON-файла.

    Args:
        values_path (str): Путь к JSON-файлу со значениями тестов.

    Returns:
        dict: Словарь, где ключом является id теста, а значением - его результат.
              Возвращает пустой словарь в случае ошибки чтения файла.
    """
    try:
        with open(values_path, 'r') as f:
            data = json.load(f)
        return {item['id']: item['value'] for item in data['values']}
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {values_path}")
        return {}  # Возвращаем пустой словарь, чтобы программа не упала
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный JSON в файле: {values_path}")
        return {}
    except KeyError:
        print(f"Ошибка: Отсутствует ключ 'id' или 'value' в файле: {values_path}")
        return {}


def update_test(test, value_map):
    """
    Рекурсивно обновляет поле 'value' в структуре теста на основе словаря value_map.

    Args:
        test (dict):  Словарь, представляющий структуру теста.
        value_map (dict): Словарь, содержащий соответствия id теста и его значения.

    Returns:
        dict: Обновленная структура теста.
    """
    if 'id' in test and test['id'] in value_map:
        test['value'] = value_map[test['id']]  # Обновляем значение, если id найден
    if 'values' in test:
        for item in test['values']:  # Рекурсивно обрабатываем вложенные тесты
            update_test(item, value_map)
    return test


def main():
    """
    Основная функция программы.
    Обрабатывает аргументы командной строки, загружает данные, обновляет структуру тестов и сохраняет результат.
    """
    if len(sys.argv) != 4:
        print("Использование: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_path, tests_path, report_path = sys.argv[1:4]

    # Загрузка данных
    value_map = load_values(values_path)  # Получаем словарь с результатами тестов
    if not value_map:
        print("Завершение работы из-за ошибки при загрузке values.json")
        sys.exit(1)

    try:
        with open(tests_path, 'r') as f:
            tests_data = json.load(f)  # Загружаем структуру тестов
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {tests_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный JSON в файле: {tests_path}")
        sys.exit(1)

    # Обновление структуры тестов
    updated_tests = [update_test(test, value_map) for test in tests_data['tests']]  # Обновляем значения тестов

    # Сохранение отчета
    try:
        with open(report_path, 'w') as f:
            json.dump({'tests': updated_tests}, f, indent=2)  # Сохраняем результаты в report.json
        print(f"Отчет успешно создан: {report_path}")  # Сообщаем об успехе
    except FileNotFoundError:
        print(f"Ошибка: Невозможно создать файл: {report_path}")
        sys.exit(1)
    except IOError:
        print(f"Ошибка ввода/вывода при записи в файл: {report_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
