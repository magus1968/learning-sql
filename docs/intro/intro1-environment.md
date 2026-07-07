# 1. Настройка рабочего пространства

- **Anaconda Navigator** должен быть закрыт:  
  *иначе Windows может выдать ошибку и прервать выполнение*.
- **Anaconda Prompt** запускаем _**БЕЗ**_ прав администратора:  
  *так как [Anaconda Distribution](https://www.anaconda.com/download) установлен по умолчанию для пользователя*.

## 1.1. Создание изолированного окружения
на базе [**Anaconda Metapackage**](https://www.anaconda.com/docs/getting-started/advanced-install/install-metapackage).

```{code} bash
# Anaconda Prompt: (base) C:\Users\Preinstalled>

# Создаем окружение с базовым набором Anaconda Metapackage
conda create --name ds-book anaconda

# Активируем его
conda activate ds-book
```

---
## 1.2. Настройка окружения
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

