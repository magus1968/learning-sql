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
    Jupyter Book: Инструмент сборки статических сайтов
    JupySQL: Расширение для запуска и подсветки SQL в Jupyter
    GitHub: Платформа хостинга репозиториев и совместной разработки
    GitHub Pages: Сервис бесплатного хостинга статических сайтов
    GitHub Actions: Платформа автоматизации рабочих процессов и CI/CD
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

Этот путь был выбран на старте, чтобы _не заморачиваться_ потом с доустановкой необходимых пакетов и исправлением возможных конфликтов зависимостей.

---

Однако, оказавшись за _стареньким_ дачным компом с нестабильным мобильным интернетом оказалось, что этот путь невозможен. Пришлось _почерепить_ что действительно может понадобиться и разбил задачу на три этапа.

## 1.1. Создание изолированного окружения

```{code} bash
# -- Этап 1 -- Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>
# Создание conda-окружения и установка базовых пакетов

conda create --name ds-book -c conda-forge python=3.12 jupyterlab=4.4.7 ^
  notebook=7.4.5 pandas numpy matplotlib seaborn scikit-learn ^
  python-dotenv cryptography sqlalchemy -y

# Python -- 3.12 стабильный релиз из сбалансированного Anaconda Distribution
# Jupyter Lab -- 4.4.7 для совместимости с расширением `jupyterlab_myst`
# Jupyter Notebook -- 7.4.5 синхронизирован с базой JupyterLab 4.

conda activate ds-book
```

% ::::{div}
% :class: text-sm

% :::{note .simple .dropdown icon=false open=true} Зафиксированные версии

% **Python** 3.12 – стабильный релиз из сбалансированного метапакета Anaconda Distribution \
% **Jupyter Lab** 4.4.7 – зафиксирован для совместимости с расширением **jupyterlab_myst** \
% **Jupyter Notebook** 7.4.5 – синхронизирован с базой JupyterLab 4
% :::
% ::::


| Пакет                  | Версия в проекте | Назначение                                                                     |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **`python=3.12`**      | 3.12.13          | Ядро языка программирования                                                    |
| **`jupyterlab=4.4.7`** | 4.4.7            | Интерактивная среда разработки                                                 |
| **`notebook=7.4.5`**   | 7.4.5            | Интерактивная среда разработки                                                 |
| **`pandas`**           | 3.0.5            | Классический анализ данных. Базовый инструмент обработки таблиц (DataFrames)   |
| **`numpy`**            | 2.5.1            | Математические вычисления                                                      |
| **`matplotlib`**       | 3.11.1           | Базовые графики                                                                |
| **`seaborn`**          | 0.13.2           | Статистическая визуализация                                                    |
| **`scikit-learn`**     | 1.9.0            | Машинное обучение                                                              |
| **`python-dotenv`**    | 1.2.2            | Управление секретами. Безопасное хранение паролей БД и токенов в файлах `.env` |
| **`cryptography`**     | 50.0.0           | Шифрование данных. На случай продвинутой работы с секретами внутри Python      |
| **`sqlalchemy`**       | 2.0.51           | Универсальный ORM-мост между Python и реляционными БД                          |

---
    
## 1.2. Установка инструментов верстки и коннекторов БД

```{code} bash
# -- Этап 2 -- Anaconda Prompt: (ds-book) C:\Users\YOUR_USERNAME>
# Установка в conda инструментов верстки и коннекторов БД

conda install -c conda-forge jupyter-book mysql-connector-python ^
  pymysql jupysql jupyterlab-myst
```

| Пакет                                                                                            | Версия в проекте | Назначение                                                                          |
| ------------------------------------------------------------------------------------------------ | ---------------- | ----------------------------------------------------------------------------------- |
| [Jupyter Book](https://jupyterbook.org/)                                                         | 2.1.6            | Для верстки сайта из файлов Markdown и блокнотов Jupyter                            |
| [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)                       | 9.7.0            | Драйвер базы данных MySQL для Python                                                |
| [pymysql](https://pypi.org/project/PyMySQL/)                                                     | 1.2.0            | Драйвер-коннектор MySQL для SQLAlchemy                                              |
| [JupySQL](https://jupysql.readthedocs.io/en/latest/quick-start.html)                             | 0.11.1           | Расширение для работы с SQL в ячейках Jupyter c поддержкой подсветки синтаксиса     |
| [jupyterlab-execute-time](https://jupysql.readthedocs.io/en/latest/howto/benchmarking-time.html) | 3.3.0            | Плагин для вывода времени исполнения запроса в строке статуса ячейки Jupyter Lab    |
| [jupyterlab_myst](https://mystmd.org/guide/quickstart-jupyter-lab-myst)                          | 2.7.0            | Визуальный плагин разметки MyST для Lab. Рендерит внутри интерфейса во время работы |

:::{note} Примечание по плагину `jupyterlab_execute_time`
:class: dropdown
:open: true
:icon: true

Для автоматического вывода времени выполнения SQL-запросов в проекте используется интерфейсный плагин `jupyterlab_execute_time`. Из-за отставания версий в репозитории `conda-forge` плагин устанавливается через `pip`.

Подробный разбор причин такого решения, сравнение с магической командой `%%time` и особенности отображения таймингов в Jupyter Book вынес в отдельный раздел [Бенчмаркинг SQL-запросов](https://magus1968.github.io/learning-sql/adv-execute-time/).
:::

---

## 1.3.  Установка Polars

Чтобы _неожиданно_ не получить в Jupyter Lab `Kernel Died` (как произошло у меня на _старом_ компе), хорошо бы знать какой на ПК процессор (CPU): 
- современный – с поддержкой AVX2;
- или _старый_ – без поддержки AVX2.

:::{card}
Установка Polars вынесена в отдельный раздел, чтобы разобрать _грабли_ с архитектурой процессоров и показать, почему по умолчанию в `environment.yml` зафиксирован вариант через `pip`, но оставлена возможность _переключиться_ на чистую `conda` для современного железа.
:::

Из [официальной документации](https://docs.pola.rs/user-guide/installation/) установка производится через менеджер `pip`. 

```bash
# Anaconda Prompt: (ds-book) C:\Users\YOUR_USERNAME>

# На современных CPU с поддержкой AVX2
pip install polars

# На старых CPU без поддержки AVX2
pip install polars[rtcompat]
```

- Обычный `pip install polars` ставит **одну версию**, оптимизированную под современные CPU. Если запустить её на старом процессоре (без AVX2), она упадет с ошибкой `Illegal instruction`, что вызовет в Jupyter Lab падение ядра `Kernel Died`.  
- `polars[rtcompat]` (runtime compatibility) – _толстая_ установка. Она скачивает сразу **несколько версий** движка (скомпилированных под разные наборы инструкций) и во время импорта библиотеки выбирает нужный.
    
| Пакет                                                                        | Версия в проекте | Назначение                                                                                         |
| ---------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| [Polars](https://docs.pola.rs/user-guide/installation/)                      | 1.43.2           | Аналог Pandas. Мощный современный движок на Rust для _щупанья_ альтернатив (на современных CPU)    |
| [polars[rtcompat]](https://docs.pola.rs/user-guide/installation/#legacy-cpu) | 1.43.2           | На старых ПК: c автоматической поддержкой старых процессоров без AVX2 (через движок совместимости) |

:::{important} Универсальность `polars[rtcompat]`
:class: dropdown
:open: true
:icon: true

На самом деле, пакет `polars[rtcompat]` – **универсален**. В него включены сразу несколько движков. При запуске на современном ПК он определит наличие AVX2 и активирует быстрый движок, а на старом процессоре переключится на режим совместимости.

**Разница только в размере:** `polars[rtcompat]` занимает больше места на диске (порядка 100 МБ) так как скачивает несколько версий библиотек.
:::

Поскольку `polars[rtcompat]` оказался **универсальным**, то в `environment.yml` именно он зафиксирован для установки Polars по умолчанию. 


---
Окружение проекта строим на Conda. Чтобы выяснить возможность установки пакетов через `conda`, проверим их доступность в репозиториях.

```bash
# Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>

conda search -c conda-forge -c defaults polars
Loading channels: done
# Name                  Version  Build             Channel
...                     ...      ...               ...
polars                  1.43.1   pyh8da0edf_0      conda-forge
polars                  1.43.2   pyh8da0edf_0      conda-forge
polars                  1.44.0   pyh8da0edf_0      conda-forge
polars                  1.44.1   pyh8da0edf_0      conda-forge
polars                  1.44.2   pyh3138b34_0      conda-forge
```

Видим, что на современном ПК установить `polars` через `conda` можем:
- Префикс `pyh...` в колонке Build обозначает пакет типа `noarch: python` (метапакет-обертку), который не привязан к конкретной версии Python и одинаково успешно установится и на Python 3.10, и на наш 3.12.

А вот на _старом_ ПК (без AVX2) устанавливать `polars[rtcompat]` придется через `pip`.

```bash
# Anaconda Prompt: (base) C:\Users\YOUR_USERNAME>

conda search -c conda-forge -c defaults polars-runtime-compat
Loading channels: done
# Name                  Version  Build             Channel
...                     ...      ...               ...
polars-runtime-compat   1.41.2   py310haa95532_0   pkgs/main
polars-runtime-compat   1.41.2   py311haa95532_0   pkgs/main
polars-runtime-compat   1.41.2   py312haa95532_0   pkgs/main   # py312
polars-runtime-compat   1.41.2   py313haa95532_0   pkgs/main
polars-runtime-compat   1.41.2   py314haa95532_0   pkgs/main
...                     ...      ...               ...
polars-runtime-compat   1.44.1   py310h7f95213_0   conda-forge
polars-runtime-compat   1.44.1   py314h47234b9_0   conda-forge
polars-runtime-compat   1.44.2   py311hd8b5709_0   conda-forge
polars-runtime-compat   1.44.2   py314h47234b9_0   conda-forge
```
::::{div}
:class: text-sm
:::{warning} Для используемой в проекте версии Python 3.12:
:class: simple dropdown
:open: true
:icon: false

- Пакет совместимости (колонка Build версия `py312...`) есть только в канале `pkgs/main` (официальный репозиторий Anaconda: defaults). В канале `conda-forge` версии для Python 3.12 на данный момент вообще нет. _То есть если устанавливать через `conda`, то необходимо добавить в установку основной канал `-c defaults`._
- Доступная версия в `pkgs/main` сильно устарела – 1.41.2 (тогда как в PyPI уже доступна 1.44.2). Между версиями Polars 1.41 и 1.44 разработчики могли исправить баги интеграции с SQLAlchemy или оптимизировать чтение из MySQL. _Использовать старую версию пакета в проекте – это шаг назад (лишиться свежих исправлений и оптимизаций)._
- В экосистеме `pip` (на PyPI) такой проблемы нет – там всегда лежит актуальный универсальный wheel-пакет, который без проблем развернется в нашем окружении под Python 3.12.
:::
::::

Поскольку каналы Conda отстают от релизов и не имеют нужной сборки под Python 3.12, в `environment.yml` установка `polars[rtcompat]` зафиксирована именно через `pip`.

---
Наличие _точечно различающихся_ окружений в принципе нормальная практика в Data Science: на слабом железе используется совместимый рантайм `polars[rtcompat]`, а на современном – максимально оптимизированный `polars`. 

Поэтому при сборке окружения вручную, итоговый Этап 3 представляет на выбор два варианта:

```bash
# -- Этап 3 -- Установка Polars
# Anaconda Prompt: C:\Users\YOUR_USERNAME>

# Вариант 1: на любых CPU -- Универсальный установщик через `pip`
# (ds-book)
pip install polars[rtcompat]

# Вариант 2: только на современных CPU с AVX2 -- через `conda`
# (base)
conda install -n ds-book --override-channels -c conda-forge polars
```
::::{div}
:class: text-sm
:::{warning} Для установки в `conda` используем строгий и изолированный синтаксис:
:class: simple dropdown
:open: true
:icon: false

- `-n ds-book` – запускаем команду из (base), благодаря чему окружение (ds-book) остается _холодным_ и Windows не блокирует его файлы.
- `--override-channels` – указываем Conda игнорировать глобальные настройки каналов в файле `.condarc`, чтобы исключить любые конфликты конфигураций.
:::
::::

Работая над проектом на двух разных машинах, я использую оба сценария:
- на ПК с современным CPU работает чистый `polars` из `conda`;
- на старом ПК – универсальный `polars[rtcompat]` из `pip`.

Чтобы убедиться, что ядро видит библиотеку и не падает:

```bash
# Проверить импорт внутри терминала Python
python
>>> import polars as pl
>>> print(pl.__version__)
1.43.2
>>> exit()
```

```python
# Проверить импорт в ячейке Jupyter Lab
import polars as pl
print(pl.__version__)
# 1.43.2
```

:::{important} Вердикт

1. Базовую инфраструктуру (Python, JupyterLab, SQLAlchemy) разворачиваем через чистый `conda-forge`.
2. Самый свежий рантайм Polars ставим через `pip`, так как официальные каналы Conda не успевают за релизами PyPI под Python 3.12.
:::

Зачем понадобятся Pandas и Polars продемонстрировал в [Главе 3](https://magus1968.github.io/learning-sql/ch03/#id-2).

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
  - python=3.12
  - pip
  # Среда разработки
  - jupyterlab=4.4.7
  - notebook=7.4.5
  - jupyter-book=2.1.6
  - jupyterlab-myst=2.7.0
  # Анализ данных и визуализация
  - pandas>=3.0.5
  # - polars>=1.43.2                    # на современных CPU с поддержкой AVX2
  - numpy>=2.5.1
  - matplotlib>=3.11.1
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
      - "polars[rtcompat]>=1.43.2"         # и на старых и на современных CPU
      - "jupyterlab_execute_time>=3.3.0"

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
# Практически НЕ используется:
# так как деактивация происходит при закрытии терминала
conda deactivate


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


# -- Просмотреть состав текущего окружения --
conda list
# Eсли в `Channel` написано `pypi`: значит пакет установлен через `pip`
# Если пусто: пакет установлен менеджером Conda из основного канала `defaults`
# Если `conda-forge`: значит пакет взят из этого сообщества


# -- Посмотреть список всех окружений --
conda env list


# -- Удалить созданное окружение --
#    находясь в базовом `(base)`
conda env remove -n ds-test
# флаг `-n` – это сокращение от слова `--name`


# -- Проверка наличия обновлений в `pip` --
# Нас интересует `Polars` – ищем его в списке
pip list --outdated

# Обновление `Polars`
pip install --upgrade polars[rtcompat]

# Проверить импорт внутри Python
python
>>> import polars as pl
>>> print(pl.__version__)
1.43.2
>>> exit()
:::
::::

---