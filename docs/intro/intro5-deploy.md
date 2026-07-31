---
title: 5. Публикация сайта
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  [Публикуем](https://jupyterbook.org/stable/get-started/publish/) книгу Jupyter на **GitHub Pages** с помощью **GitHub Actions**.
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
date: 2026-07-25
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Инструмент сборки статических сайтов
    JupySQL: Расширение для запуска и подсветки SQL в Jupyter
    GitHub Pages: Сервис бесплатного хостинга статических сайтов
    GitHub Actions: Платформа автоматизации рабочих процессов и CI/CD
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

Для этого необходимо включить [GitHub Pages](https://docs.github.com/ru/pages) и установить в качестве источника [GitHub Actions](https://docs.github.com/ru/actions):
1.  Открыть репозиторий на сайте **GitHub**.
2.  В верхнем горизонтальном меню репозитория перейти во вкладку **`Settings`**.
3.  В левой боковой панели найти раздел **`Code and automation`**.
4.  Выбрать пункт **`Pages`**.
5.  В центре экрана найти блок **`Build and deployment`**.
6.  Внутри этого блока найти выпадающий список под заголовком **`Source`**.  
   По умолчанию там обычно выбрано _`Deploy from a branch`_.

---

## 5.1. Создание файла автоматизации

Jupyter Book имеет под капотом [команду](https://jupyterbook.org/stable/get-started/publish/), которая сама создает файл автоматизации GitHub Actions `.github/workflows/deploy.yml` для развертывания сайта на GitHub Pages:

:::{code} bash
# > Git Bash: (ds-book)
# > YOUR_USERNAME@COMPUTER MINGW64 /d/GitHub/Books/Learning-SQL (main)

# Создаем автодеплой на GitHub Pages
jupyter book init --gh-pages

# Отвечаем на вопросы утилиты (ветка: main, имя экшена: deploy.yml)
# ? What branch would you like to deploy from? --> main
# ? What would you like to call the action? --> deploy.yml
:::

---

## 5.2. Отправка изменений на GitHub

Осталось добавить сгенерированный `.github/workflows/deploy.yml` в список отслеживаемых файлов, закоммитить и запушить на GitHub

:::{code} bash
# > Git Bash: (ds-book)
# > YOUR_USERNAME@COMPUTER MINGW64 /d/GitHub/Books/Learning-SQL (main)

git add .
git commit -m "chore: add github actions deploy workflow"
git push
:::

:::{hint} Как только делаем обычный `git push` в ветку `main`

Cервера **GitHub** перехватывают это событие, запускают виртуальную машину, собирают книгу и сами выкладывают её на сайт.
:::
