
# SQL & SQLAlchemy vs Jupyter Book

Интерактивный учебный конспект и рабочая тетрадь по SQL (на базе книги Алана Болье _Изучаем SQL_, 3-е изд. 2021), оформленные в виде статического веб-сайта с функцией поиска.

- **GitHub Pages (Основной хостинг):** [magus1968.github.io/learning-sql](https://magus1968.github.io/learning-sql/)
- **GitVerse Pages (Резервное зеркало):** [alexey-sm.gitverse.site/learning-sql](https://alexey-sm.gitverse.site/learning-sql/)

---
## Архитектура проекта и стек технологий

При изучении SQL через стандартный CLI-клиент или традиционные графические IDE (DBeaver) код запроса и результат его выполнения не сохраняются в одном месте для быстрого повторного обращения.

Этот проект решает проблему за счет интеграции следующих инструментов:

- **Anaconda & Jupyter Lab** — интерактивная среда для ведения конспектов.
- **SQLAlchemy & PyMySQL** — программный слой для подключения Python к локальной СУБД MySQL.
- **JupySQL** — расширение для поддержки SQL-запросов и подсветки синтаксиса в ячейках блокнота.
- **Jupyter Book 2.x (MyST CLI)** — компилятор на базе Node.js, преобразующий Markdown-файлы и Jupyter-блокноты в структурированный статический сайт. На страницах сайта используется тег `remove-input` для автоматического скрытия Python-кода подключения, оставляя пользователю только читаемый SQL-запрос и результирующую таблицу.

---
## Отказоустойчивый параллельный CI/CD

Для обеспечения отказоустойчивости и независимости от возможных инфраструктурных сбоев реализован двойной автоматический деплой на две платформы: **GitHub** и **GitVerse**.

### 1. Изоляция SSH-доступов

На локальной машине настроен «паранойя-режим» для разделения ключей доступа. Конфигурация в `~/.ssh/config` предотвращает путаницу учетных записей:

```text
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host gitverse.ru
    HostName gitverse.ru
    User git
    IdentityFile ~/.ssh/id_ed25519_verse
    IdentitiesOnly yes
```

### 2. Разделение сценариев автоматизации (Workflows)

Поскольку GitHub и GitVerse используют разные API-интерфейсы для хостинга страниц, сценарии развертывания разнесены по разным каталогам:

- **GitHub Pages** настраивается через `.github/workflows/deploy.yml`. Шаг публикации использует экшены `actions/configure-pages` и `actions/deploy-pages@v4`.
- **GitVerse Pages** настраивается через `.gitverse/workflows/deploy.yml`. В настройках репозитория GitVerse указан приоритет использования папки `.gitverse/`. Шаг публикации использует экшены совместимости `actions/upload-pages-artifact@v1` и `actions/deploy-pages@v1`.
- **Среда сборки полностью идентична:** на обеих платформах компиляция выполняется в окружении **Node.js 18.x** через менеджер `npm` (`npm install -g jupyter-book`), что гарантирует стопроцентное совпадение верстки, шрифтов и стилей на обоих сайтах.
- **Обход сетевых ограничений контейнеров:** в GitVerse-сценарии настроена принудительная адресация по IPv4 (`NODE_OPTIONS: --dns-result-order=ipv4first`), что предотвращает падение внутреннего краулера MyST из-за отключенной поддержки IPv6-протокола в сетевых мостах Docker.

---
## Быстрый старт (Локальная установка)

Для развертывания проекта локально понадобится предустановленный дистрибутив [Anaconda Distribution](https://www.anaconda.com/download).

Выполните последовательно в терминале:

```bash
# 1. Клонируем репозиторий и переходим в папку проекта
git clone git@github.com:magus1968/learning-sql.git
cd learning-sql

# 2. Создаем окружение на базе стандартного Anaconda Metapackage
conda create --name ds-book anaconda
conda activate ds-book

# 3. Устанавливаем дополнительные пакеты для Jupyter Book и MySQL
conda install -c conda-forge jupyter-book mysql-connector-python pymysql jupysql jupyterlab-myst
```
_Пошаговое руководство по настройке рабочего пространства представлено на главной странице сайта._

---
## Daily Workflow

Ежедневный цикл работы с конспектами и автоматической публикацией изменений на оба зеркала:

```bash
conda info --envs        # Проверить текущее активное окружение
conda activate ds-book   # Перейти в целевое окружение, если требуется

jupyter lab              # Запуск среды разработки контента

jupyter book start       # Локальное тестирование и просмотр верстки сайта

# Фиксация изменений
git add .
git commit -m "Добавил упражнения по оконным функциям SQL"

# Публикация в облако
git push                 # Автоматический деплой на GitHub Pages (по умолчанию)
git push verse           # Автоматический деплой на GitVerse Pages (зеркало)
```
