---
title: 4. Инициализация Git
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
date: 2026-07-25
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

::::{attention} Anaconda Prompt vs Git Bash
:class: dropdown
:open: true

Используем самую надежную и проверенную временем связку на Windows:
- **Anaconda Prompt** (без админ-прав) – для **Conda**;
- **Git Bash** – для **Git**.

:::{div}
:class: text-xs
Помним, что в предыдущем разделе [настроили **Git Bash**](https://magus1968.github.io/learning-sql/intro3-start/#id-3-1-git-bash) в качестве второго терминала для исполнения команд **Conda**
:::
::::

---

## 4.1. Создание .gitignore

Чтобы не отправлять на GitHub временные файлы, кэш сборки и т.д. создаем в корне локального проекта файл `.gitignore` :

:::{code} text
:filename: .gitignore

# ====================================================================
# ИСКЛЮЧЕНИЯ ДЛЯ ПРОЕКТА JUPYTER BOOK 2.x (MyST CLI), ANACONDA & PYTHON
# ====================================================================

# --- Системные файлы операционных систем ---
# Временные файлы проводника Windows (кэш эскизов изображений)
Thumbs.db
ehthumbs.db

# --- Кэш компиляции Python ---
# Временный кэш компиляции скриптов Python (из папки helpers)
__pycache__/
*.pyc
*.pyo
*.pyd

# --- Инструменты Jupyter ---
# Временные автосохранения блокнотов (.ipynb)
.ipynb_checkpoints/

# Кэш расширений JupyterLab (например, Variable Inspector)
.virtual_documents/

# --- Сборка книги Jupyter Book / MyST ---
# Каталог компиляции книги (готовый HTML-сайт)
_build/

# Внутренний кэш парсера разметки MyST Markdown
.myst/

# --- Окружения и виртуальные среды ---
# Конфигурации проектов Anaconda
anaconda_projects/

# Локальные секреты с паролями к БД
# Файлы секретов и переменных окружения (пароль к базе данных)
.env
.envrc

# --- Настройки сред разработки (IDE) ---
# Персональные настройки VS Code
.vscode/

# Настройки среды PyCharm
.idea/

# --- Черновики и эксперименты ---
# Папка для черновиков и экспериментов
notebooks/
:::

---

## 4.2. Инициализация локального репозитория

:::{code} bash
# Git Bash: YOUR_USERNAME@COMPUTER MINGW64 ~

# 1. Переходим в папку проекта (синтаксис Git Bash!)
cd /d/GitHub/Books/Learning-SQL
# или в папке проекта в Проводнике Windows: ПКМ –> Open Git Bash here

# 2. Инициализируем пустой локальный Git-репозиторий
git init

# 3. Добавляем все файлы проекта в индекс
git add .

# 4. Фиксируем изменения
git commit -m "Initial commit: environment and project structure"
:::

---

## 4.3. Создание репозитория на GitHub

Создаем на [GitHub](https://github.com) **пустой** репозиторий: **Сreate New ...** –> **New repository** –> **Create a new repository** (без _README.md_ и без _.gitignore_ которые мы создадим локально) –> **Create repository**.

---

## 4.4. Связываем репозитории по SSH

Поскольку у нас уже создан локальный репозиторий, выбираем на GitHub второй вариант подсказки `...or push an existing repository from the command line`:

:::{code} bash
# Git Bash:
# YOUR_USERNAME@COMPUTER MINGW64 /d/GitHub/Books/Learning-SQL (master)

# Привязываем репозиторий по SSH
git remote add origin git@github.com:magus1968/learning-sql.git
# это реальная ссылка моего проекта, у вас будет другая (похожая)

# Переименовываем master в main
git branch -M main

# Отправляем файлы в облако
git push -u origin main

# Git Bash:
# YOUR_USERNAME@COMPUTER MINGW64 /d/GitHub/Books/Learning-SQL (main)
:::

:::{div}
:class: text-xs

Инсайт: В этом варианте название созданной локальной папки не совпадает с названием созданного репозитория на GitHub. И не обязано.
:::

::::{hint} Git _vs_ Conda
:class: dropdown
:open: true

**Git** и **Conda** – _не_ взаимосвязаны.  
То есть запускать команды `git` можно как из базового окружения _`(base)`_, так и из рабочего _`(ds-book)`_.

:::{div}
:class: text-xs
То есть когда в [ежедневной работе](https://magus1968.github.io/learning-sql/daily-workflow/) будем в **Git Bash** выключать сервер, то выходить из _`(ds-book)`_ перед фиксацией изменений и отправкой их в **GitHub** – _не_ требуется .
:::
::::

::::{tip} Кратко по SSH
:class: dropdown
:open: false
**GitHub** в своей документации рекомендует:

1. Генерировать SSH-ключ **ed25519**  
[Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"`
```
---

2. Перед генерацией проверить наличие ключа в системе  
[Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)  
```bash
$ ls -al ~/.ssh
```
---
                                                                    
3. Добавить новый SSH-ключ в аккаунт GitHub  
[Adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

:::{div}
:class: text-xs
Чтобы не ошибиться, что именно копировать, лучше _катануть_ содержимое публичного ключа в буфер обмена непосредственно в терминале **Git Bash**
:::

```bash
cat id_ed25519.pub | clip
```

:::{div}
:class: text-xs
А то помню открыл ключ в **VS Code** и скопировал сначала без почты, потом без первой записи ssh-ed25519 и только на третий раз сообразил, что копировать нужно **всё** содержимое.
:::
::::

---

## 4.5 Кратко по SSH

**GitHub** в своей документации рекомендует:

:::{card} [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)
:header: Генерировать SSH-ключ **ed25519**

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"`
```
:::

:::{card} [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
:header: Перед генерацией проверить наличие ключа в системе

```bash
$ ls -al ~/.ssh
```
:::

:::{card} [Adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
:header: Добавить новый SSH-ключ в аккаунт **GitHub**

```bash
cat id_ed25519.pub | clip
```
:::



