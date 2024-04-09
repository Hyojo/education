import csv
import json
import random
import shutil
from abc import ABC, abstractmethod
from io import StringIO

import pandas as pd
import yaml
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


def writeToFile(path, data):
    with open(path, 'a') as toFile:
        toFile.write(json.dumps(data))


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
        # return StringIO('\n'.join('\t'.join(map(str, row)) for row in data))
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    def write(self, data: list[list[int, str, float]]) -> StringIO:
        output = StringIO()
        json.dump(data, output)
        output.seek(0)
        return output


class CSVWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    def write(self, data: list[list[int, str, float]]) -> StringIO:
        output = StringIO()
        writer = csv.writer(output)
        writer.writerows(data)
        output.seek(0)
        return output


class YAMLWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    def write(self, data: list[list[int, str, float]]) -> StringIO:
        output = StringIO()
        yaml.dump(data, output)
        output.seek(0)
        return output


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []

        """Ваша реализация"""
        for i in range(matrix_size):
            data.append((random.randint(0, 9), "A:" + str(random.randint(0, 9)), random.randint(0, 9) + 0.5))

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """
        """Ваша реализация"""

        print(path)
        with open(path, 'w') as buffer:
            writer.seek(0)
            shutil.copyfileobj(writer, buffer)
        self.file_id = id(writer)
