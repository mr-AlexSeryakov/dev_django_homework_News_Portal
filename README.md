# News Portal — учебный проект на Django

Разработка учебного проекта по домашнему заданию 
в рамках которого создается новостной портал News Portal

## Установка

Проект работает на Python Python 3.13.7

1. Настроить виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate # Linux/MacOS
    venv\Scripts\activate # Windows

2. Клонировать репозиторий:
    git clone https://github.com/mr-AlexSeryakov/dev_django_homework_News_Portal.git

3. Перейти в папку проекта:
    cd News_Portal

4. Установить расширения:
    pip install -r reguirements.txt

## Функционал

- Создание базы данных через models.py
- Учебные задания по разделу 9.1 (HW-03) и примеры в файле test_django.txt 
- Запуск многокодового скрипта в Django shell через scripts_np.py

## Изменения
### (2025-10-07) версия 1.01
- Добавлен фильтр цензуры слов из списка BAD_WORDS.
- Добавлена страница новостей (News) с переходом на отдельную новость

### (2025-10-08) версия 1.02
- Добавлена пагинация на страницу с новостями (News)

## Автор
- mr_Alex_Ser