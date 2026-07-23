---
title: 3. Запуск локального вебсайта
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

На этом шаге нам потребуется второй терминал. Потому что один терминал **Anaconda Prompt** мы уже задействовали для запуска **Jupyter Lab**.

Можно конечно запустить второе окно **Anaconda Prompt**. Hо в качестве второго терминала мы подготовим **Git Bash** и будем использовать его.

---

## 3.1. Настройка Git Bash

Итак, **Git Bash** потребуется в качестве второго терминала для исполнения команд **Conda**. Настроим его.

Чтобы не вводить команду `source ~/anaconda3/etc/profile.d/conda.sh` вручную при каждом открытии терминала, этот процесс можно автоматизировать.

Чтобы подружить **Git Bash** c **Conda** раз и навсегда _(научить **Git Bash** понимать команды **Conda** без ручного ввода путей)_:

:::{code} bash
# Выполнить команду для интеграции conda с профилем bash
echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc

# Перезапустить терминал (закрыть Git Bash и открыть заново)
:::

Это запишет команду в конфигурационный файл `.bashrc`, который выполняется автоматически при каждом запуске **Git Bash**. Теперь при открытии терминала мы сможем сразу писать `conda activate envname`.

Если главного файла настроек профиля в системе ещё нет, **GitBash** создаст его сам:

:::{code} bash
WARNING: Found ~/.bashrc but no ~/.bash_profile, ~/.bash_login or ~/.profile.

This looks like an incorrect setup.
A ~/.bash_profile that loads ~/.bashrc will be created for you.
:::

---

## 3.2. Запуск локального вебсайта

[Запускаем локальный вебсайт](https://jupyterbook.org/stable/get-started/build-websites/), чтобы посмотреть как выглядит результат в браузере. По сути мы локально тестируем будущий сайт: смотрим, правим, сохраняем – при каждом сохранении сайт обновляется.

```{code} bash
# Git Bash: (ds-book) /d/GitHub/Books/Learning-SQL
jupyter book start

👉  http://localhost:3000  👈
# открываем эту ссылку в браузере
```
_Для остановки сервера в терминале нажать {kbd}`Ctrl` + {kbd}`C`_

---