---
title: Предметный указатель
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  Решил попробовать создать персональный CheatSeet. Пока _не_ нравится. Либо пойму как переделать, либо удалю.
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
      # - Data Analyst
      # - BI Analyst
      # - Business Analyst
      # - Independent Researcher
date: 2026-07-28
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
---
## H2

### H3

:::{div}
#### CREATE TABLE
Создание таблицы `52`
```sql
CREATE TABLE person(
    person_id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(20),
    lname VARCHAR(20),
    -- ...
    postal_code VARCHAR(20)
);
```
:::

:::{div}
#### CREATE TEMPORARY TABLE
Создание вр*е*менной таблицы `77`
```sql
CREATE TEMPORARY TABLE actors_J (
    actor_id smallint(5),
    first_name varchar(45),
    last_name varchar(45)
);
```
:::

:::{div}
#### CREATE VIEW
Создание представления (виртуальной таблицы) `78`
```sql
CREATE VIEW cust_vw AS
SELECT customer_id, first_name, last_name, active
FROM customer;
```
:::

---
#### DELETE
`инструкция` удалить данные `61`
```sql
DELETE FROM person
WHERE person_id = 2;
```

---
#### DESC
`команда` (_describe_) посмотреть столбцы и определение таблицы `53`
```sql
DESC person;
```
`ключевое слово` для сортировки по убыванию `87`
```sql
ORDER BY last_name desc
```

---
#### DISTINCT
`ключевое слово` исключить из вывода дубликаты (оставить уникальные) `74`
```sql
SELECT DISTINCT actor_id
FROM film_actor
ORDER BY actor_id;
```

---
#### DROP TABLE
`команда` удалить таблицу `66`
```sql
DROP TABLE person;
```

---
#### IN
`369`
```sql
WHERE last_name IN ('WILLIAMS', 'DAVIS');
```

---
#### INSERT INTO
`инструкция` добавить данные `57`
```sql
INSERT INTO person
    (person_id, fname, lname, eye_color, birth_date)
VALUES (null, 'William', 'Turner', 'BR', '1972-05-27');
```

---
#### DATE

---
#### TIME

---
#### SHOW TABLE
`команда` посмотреть таблицы в базе `65`

---
#### SHOW FULL TABLE
`команда` посмотреть таблицы в базе c выводом типа

---
#### UPDATE
`инструкция` изменение (дополнение) данных `61`
```sql
UPDATE person
SET street = '1225 Tremont St.',
    city = 'Boston',
    state = 'MA',
    country = 'USA',
    postal_code = '02138'
WHERE person_id = 1;
```
