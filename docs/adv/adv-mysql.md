---
title: Установка MySQL
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  Для работы с базой данных установим на компьютер сервер базы данных MySQL и собственно саму базу данных Sakila.
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
date: 2026-10-09
abbreviations:
    MyST: Markedly Structured Text
    ПКМ: Правая Кнопка Мыши
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

Перед **первой** установкой MySQL рекомендую к просмотру три видео:
- [Установка MySQL](https://stepik.org/lesson/206803/step/2?unit=563745) от Shultais Education, Stepik;
- [Установка MySQL сервера](https://stepik.org/lesson/1413879/step/1?unit=1431702) от Pragmatic Programmer, Stepik;
- [How to install MySQL...](https://www.youtube.com/watch?v=fzd6-qcLzrE) от Amit Thinks, YouTube (выбрать в настройках звуковую дорожку с Русским языком).

Изучив первые два видеогайда (например, чтобы увидеть что делать в случае отсутствия в Windows необходимых для установки компонентов[^1]), за основу возьмем третий гайд, потому что автор рассматривает *кастомную* установку.

[^1]: В большинстве случаев в системе может отсутствовать пакет [Microsoft Visual C++ 2015–2022 Redistributable (x64)](https://learn.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist?view=msvc-170).
    
    Если инсталлятор на старте выдаст ошибку о нехватке библиотек Visual C++, сначала установите пакет Visual C++ Redistributable (x64) и перезапустите установщик.

Но сделаем точечную корректировку на этапе выбора устанавливаемых компонентов, поскольку нам нужна база данных Sakila.

---

## Скачивание инсталлятора

Для Windows воспользуемся инсталлятором [MySQL Installer](https://dev.mysql.com/downloads/installer/), на момент написания версией 8.0.46 (565.9M), чтобы за один раз установить совместимые версии:
- MySQL Server 8.0 version 8.0.46
- MySQL Shell 8.0 version 8.0.46
- MySQL Workbench 8.0 CE version 8.0.47
- Sample Databases 8.0 version 8.0.46, с базой данных Sakila

::::{note} MySQL Installer
:class: simple dropdown
:open: true
:icon: false

:::{figure} media/mysql-install-00-mysql-installer.png
:align: center
На момент скачивания версия может быть выше, поэтому выберите последнюю версию 8.0.хх из списка и адаптируйте установку к скачанной версии. Либо скачайте используемую в проекте версию 8.0.46 из [архива](https://downloads.mysql.com/archives/installer/)[^2].

[^2]: Если на момент скачивания версия 8.0.46 уже не будет последней актуальной.
:::
::::

Из видеогайдов уже знаем, что после нажатия **Download** будет предложено зарегистрироваться; мы предложение проигнорируем, выбрав ссылку **No thanks, just start my download**. После этого начнется загрузка файла mysql-installer-community-8.0.46.0.msi.

---

## Установка

Запускаем скачанный инсталлятор. Поскольку по видеогайдам с процессом установки уже знакомы, чтобы проще контролировать процесс установки, далее будут зафиксированы только **чек-боксы необходимых параметров**, а **скриншоты** скрыты в раскрывающихся блоках.

::::{note} Choosing a Setup Type
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-01-choosing-a-setup-type.png
:align: center
ПКМ по скрину –> Открыть картинку в новой вкладке
:::
::::

Выбираем тип установки Custom.

- [ ] Server only
- [ ] Client only
- [ ] Full
- [x] **Custom**

---

::::{note} Select Products
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-02-select-products.png
:align: center
:::

:::{figure} media/mysql-install-03-select-products.png
:align: center
:::
::::

Выбираем сервер баз данных, графическую среду (IDE) и консоль (CLI) – для работы с базами данных. А также **Samples and Examples** – для установки необходимой нам базы данных **Sakila**.

% **MySQL Servers**
- [x] **MySQL Server** –> MySQL Server 8.0.46 - X64 \
  *(сервер баз данных)*
% 
% **Applications**
- [x] **MySQL Workbench** –> MySQL Workbench 8.0.47 - X64 \
  *(IDE для открытия оригинального файла [sakila.mwb](https://dev.mysql.com/doc/sakila/en/sakila-installation.html) – для изучения структуры данных (схемы связей) исследуемой базы данных)*
- [x] **MySQL Shell** –> MySQL Shell 8.0.46 - X64 \
  *(консольная утилита)*
- [ ] **MySQL Router** *(НЕ нужен): это инструмент для распределения нагрузки между несколькими серверами. При обучении на одном компьютере он бесполезен и будет зря тратить ресурсы.*
% 
% **Documentation**
- [ ] **MySQL Documentation** –> MySQL Documentation 8.0.46 X86 \
  *(установить можно, но на практике 99% разработчиков используют официальный сайт [mysql.com](https://dev.mysql.com/doc/)).*
- [x] **Samples and Examples** –> Samples and Examples 8.0.46 - X86 \
  *(учебные базы `sakila` и `world`)*

:::{div}
:class: text-base

- [ ] Enable the Select Features page to customize product features – оставить пустым.
:::

---

::::{note} Installation
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-04-installation.png
:align: center
:::

:::{figure} media/mysql-install-05-installation.png
:align: center
:::
::::

Проверяем список выбранных для установки на предыдущем шаге компонентов, запускаем установку {kbd}`Execute` –> {kbd}`Next`.

---

::::{note} Product Configuration
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-06-product-configuration.png
:align: center
:::
::::

Сервер и демонстрационные базы данных готовы к настройке –> {kbd}`Next`.

---

::::{note} Type and Networking
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-07-type-and-networking.png
:align: center
:::
::::

Оставляем *дефолтные* параметры без изменений –> {kbd}`Next`.

- [x] Config Type: **Development Computer**
- [x] TCP/IP
- [x] Port: **3306** [^3]
- [x] X Protocol Port: **33060**
- [x] Open Windows Firewall ports for network access
- [ ] Named Pipe
- [ ] Shared Memory
- [ ] Show Advanced and Logging Options

[^3]: По умолчанию у mysql порт **3306**

Единственное на что следует обратить внимание – значение параметра **Port**, которое будет использоваться при подключении к серверу для работы с базой данных через внешние SQL-клиенты (DBeaver, Workbench или DataGrip) и среды разработки (**JupyterLab**[^4], VS Code или PyCharm).

[^4]: Проект в принципе *заточен* под **JupyterLab** (90%), но также используются DBeaver (7%) и Workbench (3%).

---

::::{note} Authentication Method
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-08-authentication-method.png
:align: center
:::
::::

Нам не требуется совместимость с версией 5.х, оставляем *дефолтный* выбор.

- [X] Use Strong Password Encryption for Authentication (RECOMMENDED)
- [ ] Use Legacy Authentication Method (Retain MySQL 5.x Compatibility)

---

::::{attention} Account and Roles
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-09-accounts-and-roles.png
:align: center
:::
::::

Введенный пароль нужно **запомнить**. Но если устанавливаете на личном компьютере – смысла изобретать сложный пароль нет никакого.

Дополнительные пользователи нам не нужны, будем пользоваться доступом через пользователя **root** –> {kbd}`Next`.

---

::::{note} Windows Service
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-10-windows-service.png
:align: center
:::
::::

Параметры настройки запуска MySQL в качестве системной службы не меняем.

- [x] Configure MySQL Server as Windows Service
- [x] Windows Service Name: **MySQL80**
- [x] Start the MySQL Server at System Startup \
  *(автоматический запуск базы данных при старте Windows.)*
- [x] Standard System Account
- [ ] Custom User

Поскольку параметр автоматического запуска базы данных при старте системы оставили отмеченным, будет полезным знать, как автозапуск при необходимости отключить, если вдруг поняли что не собираетесь работать с базой данных каждый день – чтобы сервер не висел в памяти компьютера вхолостую и не тратил ресурсы.

:::{card}
:header: **Как отключить автоматический запуск сервера**

1. Нажать комбинацию клавиш {kbd}`Win` + {kbd}`R`, ввести команду `services.msc` и нажать {kbd}`Enter` – откроется окно управления службами Windows.
2. Найти в списке службу **MySQL80** и дважды кликнуть по ней.
3. В открывшемся окне на вкладке **Общие** изменить значение параметра **Тип запуска** (Startup type) с *Автоматически* на **Вручную** (Manual) и нажать ОК.
:::

Теперь сервер больше не будет загружать систему при старте компьютера, но его всегда можно запустить вручную.

:::{card}
:header: **Как запустить службу вручную через Диспетчер задач**

1. Нажать {kbd}`Ctrl` + {kbd}`Shift` + {kbd}`Esc`, чтобы открыть **Диспетчер задач**.
2. Перейти на вкладку **Службы** (Services).
3. Найти в списке службу **MySQL80**.
4. Кликнуть по ней правой кнопкой мыши и выбрать **Запустить** (Start).
:::

---

::::{note} Server File Permissions
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-11-server-file-permissions.png
:align: center
Место сохранения баз данных: **C:\ProgramData\MySQL\MySQL Server 8.0\Data**
:::
::::

Права доступа к служебным файлам и базам данных MySQL на уровне операционной системы оставляем по умолчанию –> {kbd}`Next`.

- [x] Yes, grant full access to the user running the Windows Service (if applicable) and the administrators group only. Other users and groups will not have access.
- [ ] Yes, but let me review and configure the level of access.
- [ ] No, I will manage the permissions after the server configuration.

---

::::{note} Apply Configuration
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-12-apply-configuration.png
:align: center
:::

:::{figure} media/mysql-install-13-apply-configuration.png
:align: center
:::
::::

Запускаем процесс применения и сохранения всех выбранных настроек {kbd}`Execute` –> {kbd}`Finish`.

---

::::{note} Product Configuration
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-14-product-configuration.png
:align: center
:::
::::

После применения основных настроек инсталлятор вернется к **Product Configuration** чтобы приступить к настройке компонента **Samples and Examples** –> {kbd}`Next`.

---

::::{note} Connect To Server
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-15-connect-to-server.png
:align: center
:::

:::{figure} media/mysql-install-16-connect-to-server.png
:align: center
:::
::::

- [x] User name: **root**
- [x] Password: **ввести**

Вводим созданный пароль –> проверяем связь[^5] кнопкой {kbd}`Check` –> {kbd}`Next`.

[^5]: Окно **Connect To Server** – это важный технический шаг.
    
    Установщик MySQL не может просто так взять и скопировать демонстрационную базу данных `sakila` на компьютер. Ему нужно зайти внутрь только что созданного SQL-сервера, создать там пустую схему и выполнить SQL-скрипты.
    
    Для этого инсталлятору требуются права администратора базы данных (пользователя root). Кнопка **Check** имитирует реальное подключение к серверу. Если пароль введен верно, статус меняется на *Connection succeeded*, и установщик получает *зеленый свет* на создание таблиц.

---

::::{note} Apply Configuration
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-17-apply-configuration.png
:align: center
:::

:::{figure} media/mysql-install-18-apply-configuration.png
:align: center
:::
::::

Запускаем процесс развертывания демонстрационных баз данных –> {kbd}`Execute` –> {kbd}`Finish`.

---

::::{note} Product Configuration
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-19-product-configuration.png
:align: center
:::
::::

После успешного развертывания баз данных инсталлятор покажет финальный статус конфигурации компонентов –> {kbd}`Next`.

---

::::{note} Installation Complete
:class: simple dropdown
:open: false
:icon: false

:::{figure} media/mysql-install-20-installation-complete.png
:align: center
:::
::::

В последнем окне снимаем отметки автоматического запуска программ, запустим нужное по необходимости –> {kbd}`Finish`.

- [ ] Start MySQL Workbench after setup
- [ ] Start MySQL Shell after setup

---

## Что дальше

:::{seealso} Далее накидаю тезисно, возможно впоследствии распишу подробно.
:class: simple dropdown
:open: true
:icon: true

1. Отметка времени `4:44` из видео [How to install MySQL...](https://www.youtube.com/watch?v=fzd6-qcLzrE) от Amit Thinks, YouTube – добавление пути к папке `bin` сервера MySQL в системную переменную среды `Path` лично я сделал, хотя в других руководствах по установке не встречал. Добавление пути в переменную Path нужно для удобства: чтобы вызывать утилиту `mysql` напрямую из любой консоли (CMD, PowerShell, VS Code), а не только через стандартные ярлыки MySQL 8.0 Command Line Client или графические программы вроде DBeaver.

Большинство авторов этот шаг игнорируют.
- Стандартный путь: `C:\Program Files\MySQL\MySQL Server 8.0\bin`.
- Это дает возможность проверить статус базы или быстро накатить дамп командой `mysql -u root -p < dump.sql` прямо из консоли проекта без необходимости открытия внешних SQL-клиентов.

---

2. Проверка подключения к базе данных Sakila из консоли **MySQL 8.0 Command Line Client - Unicode**.

```sql
-- При запросе "Enter password:" вводим пароль пользователя root

-- Проверка установленных баз данных
show databases;

-- Переключение на учебную базу данных Sakila
use sakila;

-- Просмотр списка таблиц (должно быть 16 таблиц + представления)
show tables;

-- Выход из консольного клиента
quit
```

---

3. Запуск **MySQL Workbench** и открытие модели данных [sakila.mwb](https://dev.mysql.com/doc/sakila/en/sakila-installation.html) для изучения структуры данных (схемы связей) исследуемой базы данных.
    - Запустить MySQL Workbench и создать новое подключение к локальному серверу.
    - В верхнем меню выбрать **File** –> **Open Model** и указать путь к скачанному файлу `sakila.mwb`.
    - Дважды кликнуть по иконке схемы в блоке **EER Diagrams**[^6] чтобы открыть интерактивную визуальную карту таблиц.
    - Изучить связи (внешние ключи) между ключевыми сущностями: `actor`, `film`, `customer` и `rental`.

[^6]: **Enhanced Entity-Relationship Diagram** – расширенная диаграмма *сущность-связь*.

    MySQL Workbench устанавливаем только для одной конкретной задачи – открыть файл `sakila.mwb` и наглядно увидеть схему связей (EER-диаграмму) учебной базы данных.

---

4. [Скачивание](https://dev.mysql.com/doc/index-other.html) и [установка](https://dev.mysql.com/doc/sakila/en/sakila-installation.html) базы данных Sakila в случае, если сервер MySQL был установлен ранее без демонстрационной базы данных[^7].

[^7]: Правда нужно понять нужно ли это расписывать, т.к. Алан Болье повествует об этом в начале Главы 2.

```cmd
mysql -u root -p < sakila-schema.sql
mysql -u root -p < sakila-data.sql
```

:::

---

