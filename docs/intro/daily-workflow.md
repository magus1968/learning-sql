---
title: Daily Workflow
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  Когда всё настроено, ежедневная работа сводится к простому циклу
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
date: 2026-07-23
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

:::{code} bash
# Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>
conda activate ds-book                   # перейти в целевое окружение

(ds-book) C:\Users\YOUR_USERNAME>D:          # перейти на диск проекта
(ds-book) D:\>cd GitHub\Books\Learning-SQL   # перейти в папку проекта

jupyter lab                                       # запуск Jupyter Lab


# Git Bash: YOUR_USERNAME@COMPUTER MINGW64 ~
$ conda activate ds-book
$ cd /d/GitHub/Books/Learning-SQL

$ jupyter book start                         # запуск локального сайта

$ git add .
$ git commit -m "docs: finished chapter 2"
$ git push                              # отправка изменений на GitHub
:::

Однако, если было произведено изменение структуры папок (потому что _вдруг_ поняли, что лучше иначе), то придется очистить кэш сборки и пересобрать сайт.

---

## Пересборка

:::{code} bash
# Находясь в корне репозитория

jupyter book clean --all   # Полностью удаляет папку _build и кэш
jupyter book build --all   # Пересобирает все страницы с нуля
jupyter book start         # Запускает локальный веб-сервер
:::

:::{note} Чуть подробней
:class: dropdown
:open: false
:icon: false

- `jupyter book clean --all` (полное форматирование памяти):  
    Стирает оба уровня памяти под корень. Полностью удаляет и папку `_build`, и скрытую базу данных кэша выполнения кода.  
    После выполнения `clean --all` Jupyter Book _забывает_ вообще всё.

---

- `jupyter book build --all` (режим строгой проверки):  
    Работает по принципу _всё или ничего_. Компилирует проект в максимально строгом режиме (именно так, как это будет делать сервер GitHub). Если в структуре или коде есть критическая ошибка, сборка сразу же _упадет_ (завершится с ошибкой). Это гарантирует выявление проблемы до отправки кода в репозиторий.

---

- `jupyter book start` (режим разработки):  
    Создана для комфортной работы. Если допустили ошибку (например, опечатались в имени файла в `toc.yml`, указали неверную ссылку на другую главу или сломали структуру MyST-блока), `start` **не остановит** работу. Утилита просто выведет предупреждение (Warning) в терминал, закроет глаза на ошибку и продолжит держать сервер запущенным, чтобы мы могли спокойно писать текст дальше.
:::

:::{card} Полное форматирование памяти
:header: `jupyter book clean --all`
Стирает оба уровня памяти под корень. Полностью удаляет и папку `_build`, и скрытую базу данных кэша выполнения кода. После выполнения `clean --all` Jupyter Book _забывает_ вообще всё.
:::

:::{card} Режим строгой проверки
:header: `jupyter book build --all`
Работает по принципу _всё или ничего_. Компилирует проект в максимально строгом режиме (именно так, как это будет делать сервер GitHub). Если в структуре или коде есть критическая ошибка, сборка сразу же _упадет_ (завершится с ошибкой). Это гарантирует выявление проблемы до отправки кода в репозиторий.
:::

:::{card} Режим разработки
:header: `jupyter book start`
Создана для комфортной работы. Если допустили ошибку (например, опечатались в имени файла в `toc.yml`, указали неверную ссылку на другую главу или сломали структуру MyST-блока), `start` **не остановит** работу. Утилита просто выведет предупреждение (Warning) в терминал, закроет глаза на ошибку и продолжит держать сервер запущенным, чтобы мы могли спокойно писать текст дальше.
:::
