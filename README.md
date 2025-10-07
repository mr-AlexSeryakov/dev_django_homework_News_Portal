# News Portal — учебный проект на Django

Разработка учебного проекта по домашнему заданию 
в рамках которого создается новостной портал News Portal

## Установка

Проект работает на Python Python 3.13.7
1. Настроить виртуальное окружение:
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
- Добавлен фильтр, который цензурит слова из списка BAD_WORDS.
- Добавлена страница News которая выводит список всех новостей.
- Создан переход по названию новости на отдельную страницу с полной информацией по статье.

## 

- mr_Alex_Ser