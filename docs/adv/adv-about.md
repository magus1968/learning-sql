---
title: Создание инфраструктуры
# subtitle: SQL Lab in JupyterLab
# github: https://github.com/magus1968/learning-sql
# subject: Technical Portfolio
# venue: GitHub & GitVerse Pages
# abstract: |
#   Разворачиваем инфраструктуру и выбираем инструменты.
# authors:
#   - name: Alex Smirnov
#     email: a9455440@gmail.com
#     corresponding: true
#     affiliations: Data & BI Analyst
# date: 2026-08-11
# abbreviations:
#     MyST: Markedly Structured Text
#     Jupyter Book: Build static Web-books
#     JupySQL: Run & highlight SQL in Jupyter
#     Pandas: Библиотека Python для анализа и обработки данных
#     Polars: Мощный аналог Pandas на Rust/Python
---

::::{note .simple .dropdown icon=false open=true} Разворачиваем инфраструктуру и настраиваем инструменты
:::{div}
:class: text-xs
- _Как установить на комп базу данных **sakila** и подключиться к ней?_
- _Как сделать чтобы вывод 5462 строк отображался как на страницах книги – в усеченном виде через многоточие?_

В этом разделе ответы на эти и другие вопросы, которые помогут развернуть целостную инфраструктуру и настроить используемые инструменты.
:::
::::

| Раздел [^1]                                             | Описание                                                                       |
| ------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [Установка MySQL](adv-mysql.md)                         | Разворачиваем локальную базу данных                                            |
| Установка DBeaver                                       |                                                                                |
| [Запуск SQL в JupyterLab](adv-sqlalchemy-jupysql.ipynb) | Подключение к базе данных Sakila и выполнение SQL-запросов в JupyterLab        |
| [Бенчмаркинг SQL-запросов](adv-execute-time.md)         | Реализация автоматического вывода времени выполнения SQL-запросов в JupyterLab |
| [VS Code vs JupyterLab](adv-vscode.ipynb)               | Для каких задач удобнее VS Code, настройка VS Code под проект                  |
| Pandas vs Polars                                        | Зачем они в проекте, нюансы использования                                      |
| [GitVerse vs GitHub](adv-gitverse.md)                   | GitVerse как резервное зеркало для основного хостинга, опыт использования      |

[^1]: Разделы без ссылки в статусе **черновик** в личном Obsidian

    Возможно целесообразно добавить разделы по установке [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install/windows-gui-install), [Git](https://selectel.ru/blog/tutorials/how-to-install-git-to-windows/) и что-нибудь еще. Но это не точно.
