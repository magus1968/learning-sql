---
title: Бенчмаркинг SQL-запросов
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  Как реализовать автоматический вывод времени выполнения SQL-запросов в JupyterLab, чтобы воспроизвести поведение консольного клиента MySQL CLI.
#  Реализация автоматического вывода времени выполнения SQL-запросов в интерфейсе Jupyter по аналогии с выводом консольного клиента MySQL CLI.
#  Интеграция плагина `jupyterlab_execute_time` для достижения функционального паритета (эмуляции поведения) интерактивной среды Jupyter с консольным клиентом MySQL CLI.
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
date: 2026-08-20
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Инструмент сборки статических сайтов
    JupySQL: Расширение для запуска и подсветки SQL в Jupyter
    GitHub: Платформа хостинга репозиториев и совместной разработки
    GitHub Pages: Сервис бесплатного хостинга статических сайтов
    GitHub Actions: Платформа автоматизации рабочих процессов и CI/CD
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

:::{dropdown} Бенчмаркинг в SQL
:open:
Это замер скорости выполнения запросов для оценки их эффективности. Мы фиксируем время работы каждой ячейки, чтобы наглядно сравнивать альтернативные варианты SQL-кода (например, работу `JOIN` против подзапроса).
:::

---

## Автозамер: JupyterLab Execute Time

В текущей версии JupySQL класс [`SqlMagic`](https://github.com/ploomber/jupysql/blob/master/doc/api/configuration.md) не содержит встроенного флага для логирования времени выполнения самой СУБД. Однако в [документации](https://jupysql.readthedocs.io/en/latest/howto/benchmarking-time.html) предлагается решение через официальное расширение **`jupyterlab_execute_time`**, которое автоматически отображает время выполнения внизу каждой ячейки.

В [репозитории](https://github.com/deshaw/jupyterlab-execute-time) расширения указано, что плагин можно установить через `conda`. В [истории релизов](https://pypi.org/project/jupyterlab-execute-time/#history) актуальная версия – 3.3.0 от 23 дек. 2025 г. ОК.

Однако при проверке доступных версий в канале `conda-forge` оказывается, что последняя доступная там сборка – 3.2.0 от 13 сен. 2024 г.:

```bash
conda search -c conda-forge --override-channels jupyterlab_execute_time

# Name                   Version  Build         Channel
jupyterlab_execute_time  2.0.1    pyhd8ed1ab_0  conda-forge
...                      ...      ...           ...
jupyterlab_execute_time  3.2.0    pyhd8ed1ab_1  conda-forge
```

То есть разработчики опубликовали версию 3.3.0 на `PyPI`, но до сих пор не обновили рецепт в `conda-forge`, где все еще лежит билд 3.2.0.

Чтобы установить актуальную версию, придется использовать менеджер `pip`

```bash
conda activate ds-book

pip install jupyterlab_execute_time
```

Так в итоговом файле [environment.yml](https://magus1968.github.io/learning-sql/intro1-environment/#id-1-4) появляется секция `pip`.

:::{dropdown} Весьма вероятно
:open:
что вам не потребуется постоянный вывод времени исполнения запроса. Тем более что можно точечно использовать встроенную магию `%%time`.

Однако **цель интеграции плагина в проект** – чтобы вывод ячеек в интерфейсе Jupyter максимально соответствовал по информативности выводу консольного клиента MySQL CLI со страниц книги Алана Болье.
:::

---

## Ручной замер: магия `%%time`

Поскольку JupySQL работает внутри Jupyter, мы можем комбинировать магические команды. Стандартная встроенная команда `%%time` замеряет время выполнения всей ячейки. Единственное условие: `%%time` всегда должна объявляться в ячейке **первой строкой**, перед `%%sql`.

В качестве примера команда `%%time` использована в подразделе [Условия неравенства](https://magus1968.github.io/learning-sql/ch04/#id-3) Главы 4:

```python
%%time
%%sql
SELECT c.email
FROM customer c
  INNER JOIN rental r
  ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14';
```

```bash
16 rows affected.
CPU times: total: 0 ns
Wall time: 45 ms
```

**Wall time** (астрономическое время) – это фактическое время от нажатия `Shift+Enter` до вывода результата в интерфейс.

---

## Особенности и выводы

1. Несмотря на возможность использования встроенной магии `%%time`, в проекте задействован плагин `jupyterlab_execute_time` – чтобы фиксация времени выполнения запроса происходила **автоматически**.

2. Единственный нюанс плагина `jupyterlab_execute_time` – время отображается в интерфейсе Jupyter, но не переносится в статическую верстку сайта Jupyter Book (в отличие от вывода команды `%%time`). \
   Этот момент аналогичен отсутствию на собранном сайте подсветки синтаксиса MySQL в ячейках `%%sql`, о чем упомянуто в разделе [Создание таблицы](https://magus1968.github.io/learning-sql/ch02/#id) Главы 2

3. Время, которое фиксируют `%%time` и `jupyterlab_execute_time` – это **полное время жизненного цикла ячейки**:
   - формирование и отправка запроса через Python и драйвер `PyMySQL` в базу данных;
   - исполнение запроса на стороне сервера MySQL;
   - передача результирующей выборки обратно в Python и ее преобразование в табличный вид.

   Для локальной учебной базы (Sakila) эти накладные расходы минимальны, однако чистое время исполнения на сервере (показываемое в MySQL CLI) всегда будет немного меньше общего времени выполнения ячейки.

---

