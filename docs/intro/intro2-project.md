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
    email: a9455440@gmail.com
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

(project-init)=
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

(project-structure)=
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
   │   └── intro.md           # introduction
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

(project-jupyterlab)=
## 2.3. Jupyter Lab
Для создания контента и настройки проекта будем использовать [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/#). Удобнее запустить сервер Jupyter Lab в корне диска `D:\` – таким образом будет возможность перемещаться между проектами.

Однако, чтобы не засорять корневую директорию диска временными файлами Jupyter, рекомендуется запускать **Jupyter Lab** в папке проекта

:::{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter lab
:::

:::{important} В открытом блокноте `.ipynb`
:class: dropdown
:open: true

В верхнем правом углу интерфейса **Jupyter Lab** убедиться, что выбран Kernel нужного окружения. В нашем примере `Python [conda env:ds-book] *`
:::

По завершении сеанса Jupyter Lab обязательно закрываем через **Shut Down**.  
Если сервер в терминале сам не закрылся: {kbd}`Ctrl` + {kbd}`C`.  \
Если не сработало: {kbd}`Ctrl` + {kbd}`Break`.
                                                                     
---

(project-content)=
## 2.4. Создание контента

Создаем [intro.md](https://jupyterbook.org/stable/get-started/create-content/) – корневой файл проекта, который станет **главной страницей** (**лендингом**) сайта. А может даже и первый блокнот `.ipynb` чтобы сразу визуально протестировать структуру  будущего сайта.

:::{code} text
:filename: intro.md
# Introduction

I am a book about ... something!
:::

---

(project-config)=
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
:label: project-myst-yml
:filename: myst.yml

# See docs at: https://mystmd.org/guide/frontmatter
version: 1
project:
  id: 4da9cb15-177c-41f5-8c4e-6a24b4e87eab
  title: SQL Lab в JupyterLab     # An example Jupyter Book
  # description: A collection of files that build up a book
  # keywords:   # убрал, чтобы не отображались в `abstract`
    # - jupyter-book
    # - data-science
    # - sql
    # - something-else
  authors:
    - name: Jo the Jovyan
    - name: Planet Jupyter
  github: captain-jupyter/my-book
  # plugins: []
  
  # Файл оглавления – внешний (отдельный)
  extends:
  - toc.yml                   # table of contents

site:
  # template: article-theme
  # template: book-theme
  # —— Шаблон темы: ——
  # 19.11.2026 после выпуска масштабного обновления `myst-theme 2.0.0` зафиксировал
  #    стабильную версию темы 1.4.1 (в репозитории соответствует слепку `23f2df5`):
  template: https://github.com/myst-templates/book-theme/archive/23f2df5.zip
  # Кнопка в верхней панели сайта
  # actions:
    # - title: Портфолио
      # url: https://magus1968.github.io/Portfolio/
  # title:
  options:
    favicon: assets/site_logo.png # favicon.ico
    logo: assets/site_logo.png
    logo_text: SQL Lab в JupyterLab
  # —— Навигация: ——
  #    ссылки – это веб-путь (URL-маршрут) внутри сгенерированного сайта
  #   `/website-metadata`, а не физический путь к файлу `/path/to/document`
  # nav:
    # - title: About
    #   url: /about
    # - title: Быстрый старт
    #   children:
    #   - title: Исходные данные
    #     url: /intro0-source
    #   - title: Настройка рабочего пространства
    #     url: /intro1-environment
  # domains: []
:::

:::{code} yaml
:label: project-toc-yml
:filename: toc.yml

version: 1
project:
  toc:
    # Главная страница
    - file: docs/intro.md
    # Get started
    - title: Быстрый старт
      file: docs/intro/intro-about.md
      children:
        - file: docs/intro/intro0-source.md
        - file: docs/intro/intro1-environment.md
        - file: docs/intro/intro2-project.md
        - file: docs/intro/intro3-start.md
        - file: docs/intro/intro4-git.md
        - file: docs/intro/intro5-deploy.md
        - file: docs/intro/daily-workflow.md
    # Advanced Setup
    - title: Advanced Setup
      file: docs/adv/adv-about.md
      children:
        - file: docs/adv/adv-mysql.md
        - file: docs/adv/adv-sqlalchemy-jupysql.ipynb
        - file: docs/adv/adv-execute-time.md
        - file: docs/adv/adv-vscode.ipynb
        - file: docs/adv/adv-gitverse.md
    # Chapters
    - title: Главы
      file: docs/chapters/ch-about.md
      children:
        - title: Глава 2. Создание и наполнение базы данных
          file: docs/chapters/ch02.ipynb
        - title: Глава 3. Запросы
          file: docs/chapters/ch03.ipynb
        - title: Глава 4. Фильтрация
          file: docs/chapters/ch04.ipynb
        - title: Глава 5. Запросы к нескольким таблицам
          file: docs/chapters/ch05.ipynb
        - title: Глава 6. Работа с множествами
          file: docs/chapters/ch06.ipynb
        - title: Глава 7. Генерация, обработка и преобразование данных
          file: docs/chapters/ch07.ipynb
        - title: Глава 8. Группировка и агрегация
          file: docs/chapters/ch08.ipynb
        - title: Глава 9. Подзапросы
          file: docs/chapters/ch09.ipynb
        - title: Глава 10. Соединения
          file: docs/chapters/ch10.ipynb
        - title: Глава 11. Условная логика
          file: docs/chapters/ch11.ipynb
        # Схема Sakila
        - title: Sakila
          file: docs/chapters/sakila.md
        # Предметный указатель
        - title: Index
          file: docs/chapters/index.ipynb
    # Appendix
    - title: Appendix
      file: docs/appx/appx-about.md
      children:
        - file: docs/appx/about.md
        - file: docs/appx/sandbox.ipynb
        - file: docs/appx/simulative.ipynb
:::

---
