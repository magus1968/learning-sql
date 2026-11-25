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
    email: a9455440@gmail.com
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

(deploy-automation)=
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

(deploy-github-push)=
## 5.2. Отправка изменений на GitHub

Осталось добавить сгенерированный `.github/workflows/deploy.yml` в список отслеживаемых файлов, закоммитить и запушить на GitHub.

:::{code} bash
# > Git Bash: (ds-book)
# > YOUR_USERNAME@COMPUTER MINGW64 /d/GitHub/Books/Learning-SQL (main)

git add .
git commit -m "chore: add github actions deploy workflow"
git push
:::

**Как только делаем обычный `git push` в ветку `main`**:  \
Сервера **GitHub** перехватывают это событие, запускают виртуальную машину, собирают книгу и сами выкладывают её на [сайт](https://magus1968.github.io/learning-sql/).

:::{warning} Если сборка в Actions завершилась ошибкой
Стандартный шаблон, который генерирует `jupyter book init --gh-pages`, периодически устаревает из-за обновлений GitHub и Node.js. С конца ноября 2026 года воркфлоу стал падать (ошибки вроде `--env-file` или отсутствия артефакта) – потребовалась ручная правка {ref}`deploy.yml <deploy-yml-updated>`.

Все изменения разобраны в разделе ниже.
:::

---

(deploy-yml-fix)=
## Корректировка `deploy.yml`

Стандартный файл воркфлоу, который автоматически генерирует команда `jupyter book init --gh-pages`, со временем устаревает и приводит к сбоям GitHub Actions. Для стабильного деплоя и удобства управления в него были внесены следующие изменения:

:::{card} 1. Актуализирована версия Node.js (`18.x` → `22.x`)

Генератор шаблона фиксирует устаревшую `node-version: 18.x`, однако шаг `npm install -g jupyter-book` при каждом запуске скачивает самую свежую версию движка (`myst`). Новые релизы `myst` используют флаги запуска (в частности `--env-file`), поддерживаемые только в Node.js 20+, из-за чего сборка падает с ошибкой `node: bad option: --env-file`. Переход на актуальную LTS-версию `22.x` полностью устраняет несовместимость.
:::

:::{card} 2. Процесс разделён на две независимые задачи (`build` и `deploy`)

В исходном шаблоне сборка сайта, выгрузка архива и публикация объединены в одну задачу (`job`). Из-за микрозадержек репликации API GitHub шаг публикации может запросить архив раньше, чем база данных успеет его проиндексировать, вызывая сбой `No artifacts named "github-pages" were found`. Вынесение публикации в отдельную задачу `deploy` с зависимостью `needs: build` гарантирует, что артефакт полностью зафиксирован на сервере до начала деплоя.
:::

:::{card} 3. Обновлены версии стандартных экшенов GitHub  

Устаревшие `actions/configure-pages@v3` и `actions/upload-pages-artifact@v3` обновлены до актуальных `@v5` и `@v4` для совместимости с современным API артефактов и раннерами GitHub.
:::

:::{card} 4. Добавлена возможность ручного запуска (`workflow_dispatch`)  

Опция `workflow_dispatch` в блоке `on:` добавляет кнопку **Run workflow** на вкладке **Actions** в репозитории GitHub. Это позволяет при необходимости пересобрать и задеплоить сайт вручную (например, после временного сбоя серверов GitHub) без создания *пустых* коммитов в терминале. Автоматический деплой при каждом `git push` в ветку `main` при этом полностью сохраняется.
:::

### Новый файл `deploy.yml`

:::{code} yaml
:label: deploy-yml-updated
:filename: .github/workflows/deploy.yml

# Воркфлоу деплоя (на базе шаблона `jupyter book init --gh-pages`)
# В настройках GitHub Pages выбрать источник публикации: GitHub Actions

name: Jupyter Book (via myst) GitHub Pages Deploy
on:
  push:
    # Запуск при отправке изменений в основную ветку
    branches: [main]
  workflow_dispatch: # Ручной запуск деплоя кнопкой на вкладке Actions

env:
  # Путь к сайту относительно корня домена (имя репозитория)
  BASE_URL: /${{ github.event.repository.name }}

# Права токена GITHUB_TOKEN для чтения кода и публикации на Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Один деплой за раз:
# лишние запуски в очереди пропускаются, но уже начатая публикация не отменяется
concurrency:
  group: 'pages'
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22.x
      - name: Install Jupyter Book (via myst)
        run: npm install -g jupyter-book
      - name: Build HTML Assets
        run: jupyter-book build --html
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: './_build/html'

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
:::

---
