# Vitaliy_Avdoshkin_HomeWork_4

# Домашняя работа в блоке "Объектно-ориентированное программирование"

## Описание

В рамках домашней работы будет работать над интернет-магазином.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/vitaliy_avdoshkin_HomeWork_4
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
```

5. Установите библиотеку pandas, для работы с табличными данными.
Также, для корректной работы с Excel-файлами в pandas необходимо
дополнительно установить библиотеку openpyxl.
 
```
poetry add pandas
poetry add openpyxl
```

6. Установите библиотеки requests и dotenv
````commandline
poetry add requests
poetry add python-dotenv
````

## Тестирование

1. Для тестирования кода установите Pytest
```
poetry add --group dev pytest
```
2. Установите Code coverage для расчета процента протестированного кода
```
poetry add --group dev pytest-cov
```
Запуск Code coverage
```commandline
pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, используйте следующую команду
```commandline
pytest --cov=src --cov-report=html
```
Отчет будет сгенерирован в папке
```
htmlcov
```
 и храниться в файле с названием 
```
index.html
```

3. Для тестирования вывода в консоль используйте специальную фикстуру
```
capsys
```

# Модули

## Модуль Main
В модуле реализована основная работа по созданию экземпляров классов

## Модуль classes

Модуль содержит два класса: Product и Category


