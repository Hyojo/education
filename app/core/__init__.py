from abc import ABC, abstractmethod
from io import StringIO
import pandas as pd
import requests
from fastapi import HTTPException


def convert_arabic_to_roman(number: int) -> str:
    romanNum = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    result = ''
    for value, numeral in sorted(romanNum.items(), reverse=True):
        print(numeral, value)
        while number >= value:
            result += numeral
            number -= value
    return result


def convert_roman_to_arabic(number: str) -> int:
    try:
        romanNum = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        prevValue = 0
        for char in reversed(number):
            value = romanNum[char]
            if value < prevValue:
                result -= value
            else:
                result += value
            prevValue = value
        return result
    except Exception as e:
        e.message = str("Invalid input")


def average_age_by_position(file):
    try:
        pdFile = pd.read_csv(file, delimiter=',')

        requiredColumns = ["Имя", "Возраст", "Должность"]
        if not set(requiredColumns).issubset(pdFile.columns):
            raise ValueError("Неверный формат файла. Отсутствуют необходимые колонки.")

        posAndAvg = pdFile.groupby("Должность")["Возраст"].mean().to_dict()
        return posAndAvg
    except Exception:
        raise HTTPException(status_code=400, detail="Файл не найден")


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""


class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    pass


class CSVWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    pass


class YAMLWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""

        pass
