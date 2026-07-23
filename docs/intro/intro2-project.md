---
title: 2. Создание проекта
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
# abstract: |
#   Забегая вперед отмечу, что чистый файл зависимостей `environment.yml` создать пришлось. Но, во-первых, на старте его не было, а во-вторых, это гайд как создать с нуля. Поехали.
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

## 2.1. Инициализация Jupyter Book

_[Инициализируем](https://jupyterbook.org/stable/get-started/init/) Jupyter Book **БЕЗ** запуска локального веб-сервера_

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter book init
# Would you like to run jupyter book start now?" – Отвечаем `n`
```

:::{note .simple .dropdown icon=false open=false} Команда `init` спросит, хотим ли запустить локальный веб-сервер для отображения проекта. Выходим из программы, нажав {kbd}`n` и {kbd}`Enter` поскольку контента для просмотра у нас пока нет!

```sh
(ds-book) D:\GitHub\Books\Learning-SQL>jupyter book init
building myst-cli session with API URL: https://api.mystmd.org

Welcome to the Jupyter Book (via myst) CLI! 🎉 🚀

jupyter book init walks you through creating a myst.yml file.

You can use Jupyter Book (via myst) to:
- create interactive websites from markdown and Jupyter Notebooks 📈
- build & export professional PDFs and Word documents 📄

Learn more about this CLI and MyST Markdown at: https://jupyterbook.org/stable

💾 Writing new project and site config file: myst.yml
? Would you like to run jupyter book start now? No

You can start the Jupyter Book (via myst) web server later with: jupyter book start
You can build all content with: jupyter book build --all
```
:::

---
## 2.2. Создание структуры проекта

Поскольку репозиторий ещё не инициализирован, по-прежнему можем использовать штатный Проводник Windows.

   ```text
   # Пример структуры
   
   Learning-SQL/
   ├── .github/               # деплой в GitHub: создается автоматически
   │   └── workflows/         # командой `jupyter book init --gh-pages`
   │       └── deploy.yml
   ├── docs/
   │   ├── ch/                # сюда из корня docs/ можно убрать главы
   │   ├── data/              # датасеты
   │   ├── intro/             # файлы Get Started
   │   ├── media/             # скриншоты
   │   ├── ch02.ipynb         # глава 2
   │   ├── ch03.ipynb         # глава 3
   │   └── index.md           # introduction
   ├── helpers/
   │   └── db_connect.py      # cюда можем написать логику подключения к БД
   ├── notebooks/             # папка для черновиков (игнорируется Git)
   ├── schemas/               # например для схем sakila: .mwb .pbix etc.
   ├── .gitignore
   ├── LICENSE                # MIT
   ├── myst.yml               # конфигурационный файл
   ├── README.md
   └── toc.yml                # файл содержания (table of contents)
   ```

---
       
## 2.3. Jupyter Lab
Для создания контента и настройки проекта будем использовать [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/#). Удобнее запустить сервер Jupyter Lab в корне диска `D:\` – таким образом будет возможность перемещаться между проектами.

Однако, чтобы не засорять корневую директорию диска временными файлами Jupyter, рекомендуется запускать Jupyter Lab в папке проекта

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter lab
```
По завершении сеанса Jupyter Lab обязательно закрываем через **Shut Down**.  
Если сервер в терминале сам не закрылся: {kbd}`Ctrl` + {kbd}`C` –> {kbd}`Y` –> {kbd}`Enter`.
                                                                     
---

## 2.4. Создание контента

Создаем обязательный [intro.md](https://jupyterbook.org/stable/get-started/create-content/). А может даже и первый блокнот `.ipynb` чтобы сразу визуально протестировать структуру  будущего сайта.

:::{code} markdown
:filename: intro.md
# Introduction

I am a book about ... something!
:::

---
## 2.5. Настройка проекта

- Конфигурационный файл [myst.yml](https://jupyterbook.org/stable/build-and-publish/website/)
- Файл содержания [toc.yml](https://jupyterbook.org/stable/authoring/table-of-contents/).

:::{note} Примечание
:class: dropdown
:open: true

Переписывать документацию смысла нет.

Если структура `toc.yml` в принципе понятна после раздела [Table of contents structure](https://jupyterbook.org/stable/authoring/table-of-contents/).

То настройка конфигурации `myst.yml` рассматривается во многих разделах: [Initialise a project](https://jupyterbook.org/stable/get-started/init/), [Build a website](https://jupyterbook.org/stable/get-started/build-websites/), [Get started with websites](https://jupyterbook.org/stable/build-and-publish/website/#configure-site-and-page-options), [Web Navigation, Structure, and Menus](https://mystmd.org/guide/website-navigation#website-layout), [Website Themes & Templates](https://mystmd.org/guide/website-templates#change-site-templates), [Content frontmatter options](https://mystmd.org/guide/frontmatter) и точно где-то ещё.

Но свои шаблоны-заготовки выложу.
:::

:::{code} yaml
:filename: myst.yml

# See docs at: https://mystmd.org/guide/frontmatter
version: 1
project:
  id: 4da9cb15-177c-41f5-8c4e-6a24b4e87eab
  # title: An example Jupyter Book
  # description: A collection of files that build up a book
  keywords:
    - jupyter-book
    - something-else
  authors:
    - name: Jo the Jovyan
    - name: Planet Jupyter
  github: captain-jupyter/my-book
  # plugins: []

  extends:                    # содержание в отдельный файл
  - toc.yml                   # файл содержания (table of contents)

site:
  # template: article-theme
  template: book-theme
  # title:
  # options:
  #   favicon: favicon.ico
  #   logo: site_logo.png     # или site-logo.svg
  nav:                        # навигация верхнего уровня
    - title: Internal page
      url: /website-metadata
  actions:                    # кнопки действий в заголовке сайта
    - title: Learn More
      url: https://mystmd.org/guide
  # domains: []
:::

:::{code} yaml
:filename: toc.yml

version: 1
project:
  toc:
    # Главная страница
    - file: docs/index.md
    # Get started
    - title: Быстрый старт
      children:
        - file: docs/intro/intro-source.md
        - file: docs/intro/intro1-environment.md
        - file: docs/intro/intro2-project.md
        - file: docs/intro/intro3-start.md
    # Глава 2
    - title: Глава 2. Создание и наполнение базы данных
      file: docs/ch02.ipynb
    # Глава 3
    - title: Глава 3. Запросы
      file: docs/ch03.ipynb
:::

---
