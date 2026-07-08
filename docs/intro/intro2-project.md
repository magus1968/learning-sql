# 2. Создание проекта

## 2.1. Подготовка папки проекта

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
## 2.2. Инициализация Jupyter Book

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
## 2.3. Создание структуры проекта

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
## 2.4. Jupyter Lab
Для создания контента и настройки проекта будем использовать [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/#). Удобнее запустить сервер Jupyter Lab в корне диска D:\ – таким образом будет возможность перемещаться между проектами.

Однако, чтобы не засорять корневую директорию диска временными файлами Jupyter, рекомендуется запускать Jupyter Lab в папке проекта

```{code} bash
# Anaconda Prompt: (ds-book) D:\GitHub\Books\Learning-SQL>

jupyter lab
```
По завершении сеанса Jupyter Lab обязательно закрываем через **Shut Down**.
Если сервер в терминале сам не закрылся – в командной строке **Ctrl + C** –> подтвердить **Y** –> **Enter**.

---
## 2.5. [Создание контента](https://jupyterbook.org/stable/get-started/create-content/)
Создаем обязательный intro.md и может даже первый блокнот .ipynb: например, чтобы визуально проверить устраивает ли структура сайта.

---
## 2.6. Настройка проекта
В зависимости от выбранных предпочтений, настраиваем конфигурационный файл myst.yml и файл содержания [toc.yml](https://jupyterbook.org/stable/authoring/table-of-contents/).

---