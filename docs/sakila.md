---
title: База данных Sakila
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
# abstract: |
#   Расширение JupySQL подсвечивает синтаксис SQL в блокнотах Jupyter, но не на созданном в Jupyter Book сайте. Как обойти это недоразумение было показано в Главе 2. Здесь и далее подобным увлекаться не будем.
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
      # - Data Analyst
      # - BI Analyst
      # - Business Analyst
      # - Independent Researcher
date: 2026-07-19
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
---

- [ ] _Проверить `sakila.pbix` на соответствие `sakila.mwb`_

**Sakila** – это классическая учебная база данных, разработанная командой MySQL для демонстрации возможностей реляционных СУБД. Она имитирует реальные бизнес-процессы компании начала 2000-х годов, занимающейся прокатом DVD-дисков. 

Схема содержит **16 основных таблиц**, связанных внешними ключами, а также встроенные представления (Views) и триггеры.

```text
| Tables_in_sakila           | Table_type |
| -------------------------- | ---------- |
| actor                      | BASE TABLE |
| actor_info                 | VIEW       |
| address                    | BASE TABLE |
| category                   | BASE TABLE |
| city                       | BASE TABLE |
| country                    | BASE TABLE |
| customer                   | BASE TABLE |
| customer_list              | VIEW       |
| film                       | BASE TABLE |
| film_actor                 | BASE TABLE |
| film_category              | BASE TABLE |
| film_list                  | VIEW       |
| film_text                  | BASE TABLE |
| inventory                  | BASE TABLE |
| language                   | BASE TABLE |
| nicer_but_slower_film_list | VIEW       |
| payment                    | BASE TABLE |
| rental                     | BASE TABLE |
| sales_by_film_category     | VIEW       |
| sales_by_store             | VIEW       |
| staff                      | BASE TABLE |
| staff_list                 | VIEW       |
| store                      | BASE TABLE |
```

---

## Схема связей (ER-диаграмма)

Для визуального понимания структуры:
- можем использовать диаграмму модели данных из Приложения А;
- или открыть в MySQL Workbench исходный файл диаграммы `sakila.mwb`, который включен в [дистрибутив Sakila](https://dev.mysql.com/doc/index-other.html);
- лично мне для первого знакомства по душе пришлась диаграмма с [Exploring Sakila](https://cgerezmi.github.io/2017/08/25/introduction.html):

```{image} ./media/sakila-structure.png
:alt: ER-диаграмма базы данных Sakila
:align: center
```

---

## Описание таблиц по категориям

### 1. Прокат и инвентарь (Ядро бизнеса)
*   **`rental`** – факты выдачи дисков клиентам. Содержит даты выдачи, возврата, ID клиента и сотрудника.
*   **`inventory`** – физические копии фильмов. Связывает конкретный диск, находящийся в конкретном магазине, с фильмом.
*   **`payment`** – платежи клиентов. Фиксирует транзакции, суммы и даты оплат за аренду.

### 2. Клиенты и персонал
*   **`customer`** – личные данные постоянных клиентов (имя, email, статус активности, привязка к адресу).
*   **`staff`** – сотрудники магазинов (включая логины, пароли и фотографии).
*   **`store`** – информация о филиалах (магазинах). Связывает менеджера филиала с его адресом.

### 3. Каталог фильмов и медиа-данные
*   **`film`** – каталог кинокартин (название, описание, год выпуска, условия аренды, рейтинг MPAA).
*   **`actor`** – информация об актерах (имя, фамилия).
*   **`film_actor`** – таблица связей «многие-ко-многим», определяющая, какие актеры снимались в каких фильмах.
*   **`category`** – жанры фильмов (экшен, комедия, драма и т.д.).
*   **`film_category`** – связь «многие-ко-многим» между фильмами и их жанрами.
*   **`language`** – языки (аудиодорожки и субтитры).
*   **`film_text`** – упрощенная таблица с названиями и описаниями фильмов для быстрого полнотекстового поиска.

### 4. География (Географические справочники)
*   **`address`** – точные адреса, включая улицы, почтовые индексы и телефоны.
*   **`city`** – города мира.
*   **`country`** – страны мира.
