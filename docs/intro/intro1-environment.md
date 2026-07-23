---
title: 1. Настройка рабочего пространства
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

Забегая вперед отмечу, что чистый файл зависимостей `environment.yml` создать пришлось. Но, во-первых, на старте его не было, а во-вторых, это гайд как создать с нуля. Поехали.

:::{attention} Внимание
:class: simple
- **Anaconda Navigator** должен быть закрыт:  
  *иначе Windows может выдать ошибку и прервать выполнение*.
- **Anaconda Prompt** запускаем _**БЕЗ**_ прав администратора:  
  *так как [Anaconda Distribution](https://www.anaconda.com/download) установлен по умолчанию для пользователя*.
:::

Простое решение: создать новое окружение на базе [Anaconda Metapackage](https://www.anaconda.com/docs/getting-started/advanced-install/install-metapackage) – готового набора популярных библиотек для Data Science, Data Analysis и Machine Learning с идеальной совместимостью версий.

```{code} bash
# Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>

# Создаем окружение с базовым набором Anaconda Metapackage
conda create --name ds-book anaconda

# Активируем его
conda activate ds-book
```

Этот путь был выбран на старте, чтобы не заморачиваться потом с доустановкой необходимых пакетов и исправлением возможных конфликтов зависимостей.

---

Однако, оказавшись за _стареньким_ дачным компом с нестабильным мобильным интернетом оказалось, что этот путь невозможен. Пришлось почерепить что мне действительно может понадобиться и разбил задачу на три этапа.

## 1.1. Создание изолированного окружения

```{code} bash
# -- Этап 1 -- Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>
# Создание conda-окружения и установка базовых пакетов

conda create --name ds-book -c conda-forge python=3.12 jupyterlab=4.4.7 ^
  notebook=7.4.5 pandas numpy matplotlib seaborn scikit-learn ^
  python-dotenv cryptography sqlalchemy -y

# Jupyter Lab -- конкретно версии 4.4.7 чтобы работал jupyterlab_myst
# Jupyter Notebook -- 7.4.5 (по той же причине)
# Python -- 3.12.12 именно эта версия входит в сбалансированный
#  Anaconda Metapackage (Distribution) – решил не экспериментировать 

conda activate ds-book
```

| Пакет                  | Версия в проекте | Назначение                                                                     |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **`python=3.12.12`**   | 3.12.12          | Ядро языка программирования                                                    |
| **`jupyterlab=4.4.7`** | 4.4.7            | Интерактивная среда разработки                                                 |
| **`notebook=7.4.5`**   | 7.4.5            | Интерактивная среда разработки                                                 |
| **`pandas`**           | 3.0.3            | Классический анализ данных. Базовый инструмент обработки таблиц (DataFrames)   |
| **`numpy`**            | 2.5.1            | Математические вычисления                                                      |
| **`matplotlib`**       | 3.11.0           | Базовые графики                                                                |
| **`seaborn`**          | 0.13.2           | Статистическая визуализация                                                    |
| **`scikit-learn`**     | 1.9.0            | Машинное обучение                                                              |
| **`python-dotenv`**    | 1.2.2            | Управление секретами. Безопасное хранение паролей БД и токенов в файлах `.env` |
| **`cryptography`**     | 49.0.0           | Шифрование данных. На случай продвинутой работы с секретами внутри Python      |
| **`sqlalchemy`**       | 2.0.51           | Универсальный ORM-мост между Python и реляционными БД                          |

---
    
## 1.2. Установка инструментов верстки и коннекторов БД

```{code} bash
# -- Этап 2 -- Anaconda Prompt: (ds-book) C:\Users\YOUR_USERNAME>
# Установка в conda инструментов верстки и коннекторов БД

conda install -c conda-forge jupyter-book mysql-connector-python ^
  pymysql jupysql jupyterlab-myst
```


| Пакет                                                                      | Версия в проекте | Назначение                                                                          |
| -------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------- |
| [Jupyter Book](https://jupyterbook.org/)                                   | 2.1.6            | Для верстки сайта из файлов Markdown и блокнотов Jupyter                            |
| [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) | 9.7.0            | Драйвер базы данных MySQL для Python                                                |
| [pymysql](https://pypi.org/project/PyMySQL/)                               | 1.2.0            | Драйвер-коннектор MySQL для SQLAlchemy                                              |
| [JupySQL](https://jupysql.readthedocs.io/en/latest/quick-start.html#)      | 0.11.1           | Расширение для работы с SQL в ячейках Jupyter c поддержкой подсветки синтаксиса     |
| [jupyterlab_myst](https://mystmd.org/guide/quickstart-jupyter-lab-myst)    | 2.7.0            | Визуальный плагин разметки MyST для Lab. Рендерит внутри интерфейса во время работы |

---

## 1.3.  Установка Polars

Из [официальной документации](https://docs.pola.rs/user-guide/installation/) установка производится только через менеджер `pip`. Причем для старых процессоров (без поддержки [AVG](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)) команда установки отличается.

```{code} bash
# -- Этап 3 -- Anaconda Prompt: (ds-book) C:\Users\YOUR_USERNAME>
# Установка Polars через менеджер `pip`

# Универсальный установщик -- на любых PC
pip install polars[rtcompat]

# На современных PC с поддержкой AVX2
pip install polars
```

| Пакет                                                   | Версия в проекте | Назначение                                                                                     |
| ------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------- |
| [Polars](https://docs.pola.rs/user-guide/installation/) | 1.43.0           | Аналог Pandas. Мощный современный движок на Rust для _щупанья_ альтернатив (на домашнем компе) |
| **`polars[rtcompat]`**                                  | 1.42.1           | На дачном компе: c автоматической поддержкой старых процессоров (через движок совместимости)   |

::::{tip} Чуть подробнее
:class: dropdown
:open: false

- Обычный `pip install polars` ставит одну версию, оптимизированную под современные CPU. Если запустить её на старом процессоре (без AVX2), она упадет с ошибкой `Illegal instruction`, что вызовет в Jupyter Lab `Kernel Died`.  
- `polars[rtcompat]` (runtime compatibility) – _толстая_ установка. Она скачивает сразу несколько версий движка (скомпилированных под разные наборы инструкций) и во время импорта выбирает нужный.

:::{note} Универсальность `rtcompat`:
:class: simple
:icon: false
- На самом деле, пакет `polars[rtcompat]` – **универсальный**. В него включены сразу несколько движков. При запуске на современном компе он _увидит_, что процессор поддерживает AVX2, и включит быстрый движок. При запуске на _стареньком_ (дачном) компе он _увидит_ старый процессор и включит совместимый движок.
- **Разница только в размере:** `polars[rtcompat]` занимает больше места на диске порядка 100Мб (так как качает несколько версий библиотек), но работает и там, и там.
:::

:::{tip} Решение:
:icon: false
- Наличие разных окружений в принципе нормальная практика в Data Science: на слабом/старом железе может стоять `polars[rtcompat]`, а на мощном/современном просто `polars`.
- Но поскольку `polars[rtcompat]` _оказался_ **универсальным**, то в итоговый `environment.yml` вошел именно он. 
:::

:::{note} Примечание:
:class: simple
:icon: false
- Работая над этим проектом на двух разных машинах, я позволил себе в качестве эксперимента установить на основном компе с современным CPU `pip install polars`. Поэтому в таблице присутствует строка с версией `1.43.0`.
- Код будет идентичен. `import polars as pl` работает одинаково в обоих случаях.

```{code} bash
# Проверить импорт внутри Python (пример на современном PC)
python
>>> import polars as pl
>>> print(pl.__version__)
1.43.0
>>> exit()

# Проверить импорт в ячейке Jupyter Lab (пример на старом PC)
import polars as pl
print(pl.__version__)
# 1.42.1
```
:::

::::

Зачем понадобятся Pandas и Polars наглядно продемонстрировал в [Главе 3](https://magus1968.github.io/learning-sql/ch03/#id-2).

---

## 1.4. Фиксация окружения

Окружение создано, все требуемые пакеты установлены – на этом можно было бы настройку рабочего пространства завершить.

Но это не наш метод. Потому что может сложиться ситуация, когда нам понадобится созданное окружение воссоздать. Поэтому потратим ещё какое-то количество времени и сохраним (зафиксируем) нашу работу в специальный файл зависимостей `environment.yml`.

- С одной стороны, поскольку `conda` создает окружения в своей системной папке `C:\Users\YOUR_USERNAME\anaconda3\envs`, нам не обязательно сейчас находиться в корне проекта. То есть можем создать файл зависимостей в любом месте, а уже потом перенести в папку проекта.
- Однако по уму создавать `environment.yml` лучше все-таки сразу в корне проекта. Поэтому папку проекта создадим сразу.

::::{note} Олдскульная привычка – отделять мух от котлет:
:class: dropdown
:open: true
- Системный диск `C:\` – для программ;
- Для данных (проектов) – диск `D:\`
:::{div}
:class: text-xs
Понятно, что второго диска может не быть: значит работаем с чем есть – меняем в гайде `D:\` на `C:\`
:::
::::

Поскольку мы в Windows, папку проекта можем создать через штатный Проводник. Или продолжить в терминале:

```bash
# Anaconda Prompt: (ds-book) C:\Users\YOUR_USERNAME>

C:\Users\YOUR_USERNAME>D:   # перейти на датадиск
D:\>cd GitHub\Books         # перейти в родительскую папку проекта

# создать папку проекта и (&&) перейти в нее
mkdir Learning-SQL && cd Learning-SQL
```

Наконец, готовы создать _волшебный_ файл, в котором будут зафиксированы все зависимости созданного нами окружения. Создадим его, находясь в нашем окружении _(об этом подсказывает в скобках имя окружения (ds-book) перед текстом командной строки)_:

```bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

conda env export --no-builds > environment.yml
```

После создания открываем `environment.yml` (например, в [VS Code](https://code.visualstudio.com/thank-you?dv=win64user)) и ... вручную убираем лишнее, корректируем, добавляем комментарии, чтобы получить чистый понятный завершенный вариант, готовый к развертыванию на любом компе

:::{code} yaml
:filename: environment.yml
name: ds-book
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12.12
  - pip
  # Среда разработки
  - jupyterlab=4.4.7
  - notebook=7.4.5
  - jupyter-book=2.1.6
  - jupyterlab-myst=2.7.0
  # Анализ данных и визуализация
  - pandas>=3.0.3
  - numpy>=2.5.1
  - matplotlib>=3.11.0
  - seaborn>=0.13.2
  - scikit-learn>=1.9.0
  # Работа с БД
  - sqlalchemy>=2.0.51
  - mysql-connector-python>=9.7.0
  - pymysql=1.2.0
  - jupysql=0.11.1
  # Утилиты
  - python-dotenv
  - cryptography
  - pip:
      - "polars[rtcompat]>=1.42.1"

:::

---

## 1.5. Воспроизведение окружения 

При наличии файла `environment.yml` создание окружения на другом компе сводится к одной простой команде

:::{code} bash
# Находясь в корне планируемого проекта в базовом окружении
# Anaconda Prompt: (base) D:\GitHub\Books\Learning-SQL>

conda env create -f environment.yml
:::

## 1.6. Краткий чек-лист

:::{code} bash
# Этап 1: создание conda-окружения и установка базовых пакетов
conda create --name ds-book -c conda-forge python=3.12 jupyterlab=4.4.7 ^
  notebook=7.4.5 pandas numpy matplotlib seaborn scikit-learn ^
  python-dotenv cryptography sqlalchemy -y

# Активация окружения
conda activate ds-book

# Этап 2: установка в conda инструментов верстки и коннекторов БД
conda install -c conda-forge jupyter-book mysql-connector-python ^
  pymysql jupysql jupyterlab-myst

# Этап 3: Установка Polars через менеджер `pip`
pip install polars[rtcompat]

# Фиксация окружения
conda env export --no-builds > environment.yml

# Воспроизведение окружения
conda env create -f environment.yml
:::

::::{seealso} Сопутствующий СheatSheet
:class: dropdown

:::{div}
:class: text-xs
_Команды которые пригодятся / могут пригодиться при настройке / тестировании окружения_
:::

:::{code} bash
# Полностью перезаписать `environment.yml` 
conda env export --no-builds > environment.yml
# знак `>` полностью перезаписывает файл


# -- Обновить текущее окружение-- 
# (подтянуть до состояния актуального)
conda env update -f environment.yml --prune
# `update` – добавит недостающее
# `--prune` – удалит то, чего больше нет в файле


# -- Создать окружение с другим именем --
# отличным от указанного в environment.yml
conda env create -f environment.yml -n ds-test
# флаг `-n` перекрывает имя окружения, написанное внутри файла
# `ds-test` – задать имя тестируемого окружения


# -- Просмотреть состав окружения --
conda list
# Eсли в `Channel` написано `pypi`: значит пакет установлен через `pip`
# Если пусто: пакет установлен менеджером Conda из основного канала `defaults`
# Если `conda-forge`: значит пакет взят из этого сообщества


# -- Удалить созданное окружение --
conda env remove -n ds-test
# флаг `-n` – это сокращение от слова `--name`
:::
::::

---