# SQL & SQLAlchemy vs Jupyter Book

:::{figure} media/cover.png
:align: left
:width: 30%
:::

Для проработки базовых знаний по MySQL, полученных на курсе Аналитик данных в Skillbox, выбрал из обзора [Лучшие книги по SQL](https://rutube.ru/video/d1430088a4d553b543ded84a471c6a8b/) на Rutube топ обзора: Изучаем SQL. Генерация, выборка и обработка данных, 3-е изд. Алан Болье пер. 2021.

Возник вопрос: где делать практику? Чтобы была возможность вернуться: подсмотреть/вспомнить код (запрос) и увидеть вывод (результат запроса).
- В книге используется клиент командной строки mysql (MySQL 8.0 Command Line Client) – но тогда не сохранится ни код (запрос), ни вывод. Можно конечно использовать логирование в текстовый файл с помощью команды tee, но мне этот способ оказался менее удобен в сравнении с итоговым решением.
- Можно использовать графический IDE, например, DBeaver CE – код сохранится, но вывод нет. По крайней мере в версии Community инструмента SQL Notebook нет.

Подсказку нашел в книге SQL. Pocket guide, 4-е изд. Элис Жао (O'Reilly) пер. 2024. В Главе 2 описывается подключение Python к базе данных через драйвер [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/). Но в итоге выбор пал на PyMySQL и SQLAlchemy.

% An admonition containing a note
:::{important} Итоговое решение
Блокноты [Jupyter Notebook](https://jupyter.org/), [Python](https://www.python.org/) и [SQLAlchemy](https://www.sqlalchemy.org/) – из дистрибутива [Anaconda](https://www.anaconda.com/download); плюс драйвер-коннектор [PyMySQL](https://pypi.org/project/PyMySQL/) и [JupySQL](https://jupysql.readthedocs.io/en/latest/quick-start.html) для подсветки синтаксиса SQL.
:::

Вопрос вроде бы был уже решен, но тут появилась "подкожная" мысль, которая и стала причиной этого гайда: что если для доступа к блокнотам использовать не просто GitHub, а создать статический сайт с функцией поиска?

Опыт с [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) у меня уже был, но он использует только файлы [Markdown](https://www.markdownguide.org/). И тут я вспомнил про книгу [Learning Data Science](https://learningds.org/intro.html), которая Powered by [Jupyter Book](https://jupyterbook.org/). И мое желание быстрее приступить к проработке SQL _пришлось_ отложить на исследование нового инструмента и на составление гайда – потому что я не смог повторить сходу все установки/настройки и прочие манипуляции на втором компе.

А ещё потому что:
- Пришлось искать костыльное решение для отображения синтаксиса SQL на сайте: потому что JupySQL подсвечивает синтаксис в блокноте Jupyter, но не на созданном с помощью Jupyter Book сайте. _В этот момент идею с сайтом хотелось уже бросить в пользу обычного хранения на GitHub._
- Плюс у "подкожной мысли" появилось продолжение: а что если доступ к GitHub заблокируют? Смогу ли использовать отечественный [GitVerse](https://gitverse.ru/home/)? Если да – как использовать GitHub и GitVerse в параллели с одним локальным репозиторием?

На случай если кому-то пригодятся мои изыскания решил поделиться.

:::{note .simple .dropdown icon=false open=false} Оффтоп
Для изучения/прокачки SQL много любопытных ресурсов:
- [Интерактивный онлайн курс по SQL](https://sql-academy.org/ru) от SQL Academy
- [Симулятор SQL](https://karpov.courses/simulator-sql) от karpov.courses
- [100-Year QA-Textbook 2026: Базы данных для тестировщиков](https://mentorpiece.ru/100/db/) от Mentorpiece Education
- [Интерактивный тренажер по SQL](https://stepik.org/course/63054/promo) на Stepik (автор Озерова Г.П.)
- [SQL с нуля до PRO](https://stepik.org/course/61247/promo) на Stepik (автор Shultais Education)
- [SQL практикум. Основы](https://stepik.org/course/212435/promo) на Stepik (автор Pragmatic Programmer)
- [Learn SQL](https://www.w3schools.com/sql/default.asp) от W3 schools

**Просто на данном этапе я выбрал книгу, изредка подглядывая на эти ресурсы**.
:::

---
## Исходные данные

| Product                                   | Describe                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OC                                        | Windows 10 Корпоративная LTSC версия 21H2 сборка19044.7417                                                                                                                                                                                                                                                                                                                                                                  |
| ПК                                        | Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz <br>16GB RAM \| SSD 2x512GB \| Intel(R) UHD Graphics 630 (128MB)                                                                                                                                                                                                                                                                                                                   |
| Anaconda                                  | [Anaconda Distribution](https://www.anaconda.com/download) version 2024.10-1 <br>Anaconda Navigator version 2.7.1 <br>conda version : 26.5.3 <br>python version : 3.12.13.final.0 <br>**Jupyter Lab** version 4.4.7<br>Jupyter Notebook version 7.4.5                                                                                                                                                                       |
| ENV                                       | Conda environments: <br>(base) – anaconda metapackage included in an Anaconda Distribution installer<br>(ds-book) – для верстки в [Jupyter Book](https://jupyterbook.org/) (на базе [anaconda metapackage](https://www.anaconda.com/docs/getting-started/advanced-install/install-metapackage)) <br>(mmkdocs) – для верстки портфолио в [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) |
| [MySQL](https://dev.mysql.com/downloads/) | _Установлены через [MySQL Installer 8.0.46](https://dev.mysql.com/downloads/installer/)_ :<br>MySQL Server 8.0 version 8.0.46 <br>MySQL Shell version 8.0.46 <br>MySQL Workbench 8.0 CE version 8.0.47                                                                                                                                                                                                                      |
| DBeaver                                   | [DBeaver](https://dbeaver.io/download/) Community version 26.1.1 (current user) Released on June 21st, 2026                                                                                                                                                                                                                                                                                                                 |
| Git                                       | [Git for Windows](https://git-scm.com/install/windows) version 2.55.0.windows.2 (64-bit)                                                                                                                                                                                                                                                                                                                                    |
| GitHub                                    | Profile : https://github.com/magus1968                                                                                                                                                                                                                                                                                                                                                                                      |
| VS Code                                   | [Visual Studio Code](https://code.visualstudio.com/thank-you?dv=win64user) version 1.126.0 (user setup) <br>Терминал по умолчанию Git Bash <br>Python 3.12.13 (base) ~ \anaconda3\python.exe                                                                                                                                                                                                                                |

---
## 1. Настройка рабочего пространства

- **Anaconda Navigator** должен быть закрыт:  
  *иначе Windows может выдать ошибку и прервать выполнение*.
- **Anaconda Prompt** запускаем _**БЕЗ**_ прав администратора:  
  *так как [Anaconda Distribution](https://www.anaconda.com/download) установлен по умолчанию для пользователя*.

### 1.1. Создание изолированного окружения
на базе [**Anaconda Metapackage**](https://www.anaconda.com/docs/getting-started/advanced-install/install-metapackage).

```{code} bash
# Anaconda Prompt: (base) C:\Users\Preinstalled>

# Создаем окружение с базовым набором Anaconda Metapackage
conda create --name ds-book anaconda

# Активируем его
conda activate ds-book
```

---
### 1.2. Настройка окружения
Установка инструментов верстки и коннекторов БД

| Package                                                                    | Describe                                                                                                              |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [Jupyter Book](https://jupyterbook.org/)                                   | Для верстки сайта                                                                                                     |
| [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) | Драйвер базы данных MySQL для Python                                                                                  |
| [pymysql](https://pypi.org/project/PyMySQL/)                               | Драйвер-коннектор MySQL для SQLAlchemy                                                                                |
| [JupySQL](https://jupysql.readthedocs.io/en/latest/quick-start.html#)      | Для подсветки синтаксиса SQL                                                                                          |
| [jupyterlab_myst](https://mystmd.org/guide/quickstart-jupyter-lab-myst)    | Визуализирует MyST-разметку (предупреждения, вкладки, панели) прямо внутри интерфейса **Jupyter Lab** во время работы |

```{code} bash
# Anaconda Prompt: (ds-book) C:\Users\Preinstalled>

# 1. Установка Jupyter Book для компиляции сайта
conda install -c conda-forge jupyter-book

# 2. Установка драйвера MySQL для работы из Python
conda install -c conda-forge mysql-connector-python

# 3. Установка драйвера-коннектора MySQL для SQLAlchemy
conda install -c conda-forge pymysql

# 4. Установка JupySQL для поддержки SQL-запросов в ячейках
conda install -c conda-forge jupysql

# 5. Установка плагина визуализации MyST для Jupyter Lab
conda install -c conda-forge jupyterlab-myst
```

---
## 2. Создание проекта

### 2.1. Подготовка папки проекта

_Олдскульная привычка – отделять мух от котлет:
системный диск `C:\` – для программ; для данных (проектов) – диск `D:\`_

Поскольку мы в Windows, папку проекта можем создать через штатный Проводник. Или продолжить в терминале:

```{code} bash
# Anaconda Prompt: (ds-book) C:\Users\Preinstalled>

C:\Users\Preinstalled>D:   # перейти на датадиск
D:\>dir                    # просмотреть содержимое родителя
D:\>cd GitHub\Books        # перейти в родительскую папку проекта

# создать папку проекта и (&&) перейти в нее
mkdir Learning-SQL && cd Learning-SQL
```

---
### 2.2. Инициализация Jupyter Book

_[Инициализируем](https://jupyterbook.org/stable/get-started/init/) Jupyter Book **БЕЗ** запуска локального веб-сервера_

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter book init
# На вопрос: Would you like to run jupyter book start now?" отвечаем `n`
```

:::{note .simple .dropdown icon=false open=false} Команда `init` спросит, хотим ли мы запустить команду `start`, которая запускает локальный веб-сервер для отображения нашего проекта. Мы выйдем из программы, нажав клавиши `n` и `Enter`, поскольку у нас пока нет контента для просмотра!

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
### 2.3. Создание структуры проекта

Поскольку репозиторий ещё не инициализирован, по-прежнему можем использовать штатный Проводник Windows.

   ```text
   # Пример структуры
   
   Learning-SQL/
   ├── .github/            # деплой в GitHub: создается автоматически
   │   └── workflows/      # командой `jupyter book init --gh-pages`
   │       └── deploy.yml
   ├── .gitverse/          # деплой в GitVerse
   │   └── workflows/
   │       └── deploy.yml
   ├── docs/
   │   ├── ch/             # сюда из корня docs/ можно убрать главы
   │   ├── data/           # датасеты
   │   ├── intro/          # файлы Get Started
   │   ├── media/          # скриншоты
   │   ├── ch02.ipynb      # глава 2
   │   ├── ch03.ipynb      # глава 3
   │   └── index.md        # introduction
   ├── helpers/
   │   └── db_connect.py   # cюда можем написать логику подключения к БД
   ├── notebooks/          # папка для черновиков (игнорируется Git)
   ├── schemas/            # можно положить структуру репозитория
   ├── .gitignore
   ├── LICENSE
   ├── myst.yml            # конфигурационный файл
   ├── README.md
   └── toc.yml             # table of contents
   ```

---
### 2.4. Jupyter Lab
Для создания контента и настройки проекта будем использовать [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/#). Удобнее запустить сервер Jupyter Lab в корне диска D:\ – таким образом будет возможность перемещаться между проектами.

Однако, чтобы не засорять корневую директорию диска временными файлами Jupyter, рекомендуется запускать Jupyter Lab в папке проекта

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter lab
```
По завершении сеанса Jupyter Lab обязательно закрываем через **Shut Down**.
Если сервер в терминале сам не закрылся – в командной строке **Ctrl + C** –> подтвердить **Y** –> **Enter**.

---
### 2.5. [Создание контента](https://jupyterbook.org/stable/get-started/create-content/)
Создаем обязательный intro.md и может даже первый блокнот .ipynb: например, чтобы визуально проверить устраивает ли структура сайта.

---
### 2.6. Настройка проекта
В зависимости от выбранных предпочтений, настраиваем конфигурационный файл myst.yml и файл содержания [toc.yml](https://jupyterbook.org/stable/authoring/table-of-contents/).

---
## 3. Локальное тестирование сайта

[Запускаем локальный веб-сервер](https://jupyterbook.org/stable/get-started/build-websites/), чтобы посмотреть как выглядит результат в браузере.

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter book start
```
*Для остановки сервера в терминале нажать `Ctrl + C` (в Git Bash может потребоваться нажать два раза).*
