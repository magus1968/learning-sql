---
title: GitVerse vs GitHub
subtitle: SQL Lab in JupyterLab
# license: CC-BY-4.0
github: https://github.com/magus1968/learning-sql
subject: Technical Portfolio
# subject: SQL Learning & Tooling
venue: GitHub & GitVerse Pages
abstract: |
  _**Еще на старте озадачился мыслью:**_
  - _Смогу ли использовать для проекта отечественный [GitVerse](https://gitverse.ru/home/) – аналог зарубежных сервисов GitHub и GitLab разработанный компанией СберТех?_
  - _Если да – как использовать GitHub и GitVerse в параллели с одним локальным репозиторием?_
authors:
  - name: Alex Smirnov
    email: a@smirnovs.pro
    corresponding: true
    affiliations: Data & BI Analyst
date: 2026-08-06
abbreviations:
    MyST: Markedly Structured Text
    Jupyter Book: Build static Web-books
    JupySQL: Run & highlight SQL in Jupyter
    Pandas: Библиотека Python для анализа и обработки данных
    Polars: Мощный аналог Pandas на Rust/Python
---

% :::{note} *Еще на старте озадачился мыслью:*
% :class: simple
% :open: true
% :icon: false
% - _Смогу ли использовать для проекта отечественный [GitVerse](https://gitverse.ru/home/) – аналог зарубежных сервисов GitHub и GitLab разработанный компанией СберТех?_
% - _Если да – как использовать GitHub и GitVerse в параллели с одним локальным репозиторием?_
% :::

---

Итак, настроен один удаленный репозиторий _origin_, который указывает на GitHub. Чтобы отправлять код **раздельно** на две платформы (GitHub и GitVerse), нужно добавить GitVerse как второй удаленный репозиторий.


:::{hint} Регистрация
:class: dropdown
:open: true
:icon: true

Так как СберID и GigaID у меня отсутствуют, то авторизовался в [GitVerse](https://gitverse.ru/signin) через бесплатный аккаунт в сервисе партнера [Cloud.ru](https://cloud.ru/) на который в свою очередь зарегистрировался уже с обычной google-почтой. 
:::

---

## 1. Настроить SSH-ключ в профиле GitVerse

_Применяем "паранойя-режим": изолированные ключи для каждого сервиса. Репозиторий с GitHub [связан по SSH-ключу](https://magus1968.github.io/learning-sql/intro4-git/#id-4-4-ssh) `id_ed25519`. Для GitVerse создаем отдельный новый ключ и объясняем компьютеру, в какой ситуации какой ключ использовать._

---

### Генерируем новый отдельный SSH ключ для GitVerse

Запускаем в Git Bash команду генерации. Чтобы не затереть старый ключ от GitHub – _явно_ укажем новое имя файла `id_ed25519_verse`:

```bash
# -- Здесь и далее команды выполняем в Git Bash --
#  Git Bash: <YOUR_USERNAME>@<COMPUTER> MINGW64 ~


ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519_verse

# Вместо `your_email@example.com` пишем почту, привязанную к GitVerse
# На оба вопроса про `passphrase` жмем Enter
```
::::{div}
:class: text-sm

:::{warning .simple .dropdown icon=false open=true} Флаг `-f` (от англ. _`file`_)
Задает путь и имя файла для сохраняемых ключей.

Если не указать этот флаг, утилита _ssh-keygen_ по умолчанию попытается сохранить ключ по стандартному пути. Для алгоритма `ed25519` это `~/.ssh/id_ed25519`.

Поскольку уже создан дефолтный ключ для GitHub с таким же именем, генерация без флага `-f` приведет к перезаписи старого ключа, из-за чего доступ к GitHub сломается.
:::
::::

В папке `~/.ssh/` появятся два файла:
- закрытый ключ `id_ed25519_verse`;
- и открытый `id_ed25519_verse.pub`.

---

### Добавляем новый ключ на GitVerse

Копируем содержимое публичного ключа в буфер обмена

```bash
cat ~/.ssh/id_ed25519_verse.pub | clip
```

Заходим на [gitverse.ru](https://gitverse.ru/) –> кликаем иконку профиля –> **Настройки** –> **Ключи SSH/GPG** –> **Добавить SSH ключ** и вставляем в соответствующее поле.

---

## 2. Настроить SSH-конфиг (Магия разделения)

Теперь нужно сделать так, чтобы при обращении к GitHub система брала старый ключ, а при обращении к GitVerse – новый. Для этого создадим файл конфигурации SSH.

Создать файл `~/.ssh/config` можно в любом текстовом редакторе (без расширения):

:::{code} text
:filename: config
# Конфигурация для GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

# Конфигурация для GitVerse
Host gitverse.ru
    HostName gitverse.ru
    User git
    IdentityFile ~/.ssh/id_ed25519_verse
    IdentitiesOnly yes
:::

Лучше использовать команду для терминала, которая создаст файл `config` сразу в правильном месте, без расширения и сразу запишет туда нужные настройки:

```bash
cat << 'EOF' > ~/.ssh/config
# Конфигурация для GitHub
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_ed25519
	IdentitiesOnly yes

# Конфигурация для GitVerse
Host gitverse.ru
	HostName gitverse.ru
	User git
	IdentityFile ~/.ssh/id_ed25519_verse
	IdentitiesOnly yes
EOF
```

:::{note} Если в будущем захотим добавить в *config* третий сервис
:class: dropdown
:open: true
:icon: true

Hапример, GitLab и решим воспользоваться этой же командой, символ `>` затрет настройки для GitHub и GitVerse. Для безопасного добавления (дозаписи) в конец существующего файла используем оператор `>>`:

```bash
cat << 'EOF' >> ~/.ssh/config
```
:::

Чтобы убедиться, что файл создался правильно: в том же окне Git Bash выполним команду для просмотра содержимого:

```bash
cat ~/.ssh/config

# Должны увидеть напечатанный текст конфигурации
```

Иногда Windows-версия SSH в Git Bash может _капризничать_, если у файла конфигурации слишком _свободные_ права. Чтобы этого избежать, выполним:

```bash
chmod 600 ~/.ssh/config
```

Когда создадим файл и добавим публичный ключ на сайт GitVerse, можем проверить связь одной короткой командой:

```bash
ssh -T git@gitverse.ru
```
_Если всё настроено верно, GitVerse узнает нас, поприветствует по имени (аккаунту) `Hi there, <your-account-name>! You've successfully authenticated...` и закроет соединение._

---

## 3. Подружить локальный репозиторий с GitVerse

Настроим GitVerse как **второй удаленный репозиторий**, чтобы отправлять код на обе платформы независимо друг от друга.

### Создаем пустой репозиторий на GitVerse

1. Заходим на [gitverse.ru](https://gitverse.ru/) в свой аккаунт.
2. Жмем кнопку **Создать** (знак плюса в верхнем меню) –> **Новый репозиторий**.
3. Вписываем имя проекта (лучше такое же, как на GitHub).
4. **Важно:** снять галочки с пунктов _Инициализировать репозиторий c README_ и _Добавить .gitignore_. Репозиторий должен быть абсолютно пустым.
5. Жмем **Создать репозиторий**.
6. На открывшейся странице копируем ссылку на репозиторий.

---

### Связываем локальный репозиторий с GitVerse

В стандартном шаблоне подсказки (_бойлерплейт_) для новых репозиториев GitVerse выведет сообщение, ориентируясь на _старый_ стандарт Git, в котором ветка по умолчанию называлась `master`:

```bash
Отправка существующего репозитория из командной строки

 git remote add origin git@gitverse.ru:alexey-sm/learning-sql.git
 git branch -M master
 git push -u origin master
 
# Чтобы наглядно показать далее вывод команды `git remote -v`
# умышленно использую реальные данные вместо <плейсхолдеров>
# `alexey-sm` вместо <your-username>
# `learning-sql` вместо <repo-name>
```

Полностью _**игнорируем**_ шаблонную инструкцию на сайте GitVerse и выполняем команды для нашей ветки `main`.

Открываем терминал в _**папке локального проекта**_ и добавляем удаленный репозиторий GitVerse по SSH под новым именем `verse`:

```bash
git remote add verse git@gitverse.ru:alexey-sm/learning-sql.git

# SSH-клиент автоматически подставит нужный ключ,
# как только увидит домен `gitverse.ru`
```

Чтобы проверить, что все привязалось правильно, вводим команду:

```bash
git remote -v

# origin  git@github.com:magus1968/learning-sql.git (fetch)
# origin  git@github.com:magus1968/learning-sql.git (push)
# verse   git@gitverse.ru:alexey-sm/learning-sql.git (fetch)
# verse   git@gitverse.ru:alexey-sm/learning-sql.git (push)
```

_Должны увидеть в списке и `origin` (GitHub), и `verse` (GitVerse)._

---

### Отправляем код на GitVerse

Отправляем нашу ветку `main` на GitVerse (вместо предложенной сайтом `master`):

```bash
git push -u verse main

# -- Увидим в терминале: --
# * [new branch]      main -> main
# branch 'main' set up to track 'verse/main'.
```

Так как репозиторий на GitVerse абсолютно пустой, у него нет предустановленной главной ветки.  Как только выполним первый пуш `git push -u verse main`, GitVerse примет нашу ветку `main`. Поскольку она окажется первой и единственной веткой в репозитории, **платформа автоматически сделает её главной (Default branch)**.

```bash
# Если в будущем планируем несколько веток, используем

git push -u verse --all
```

---

### Возвращаем основным сервисом GitHub

Из-за того, что в предыдущем шаге использовали флаг `-u`, наша локальная ветка `main` теперь считает своим основным (_дефолтным_) направлением GitVerse (`verse`):

```bash
# branch 'main' set up to track 'verse/main'.
```

Чтобы основным сервисом оставался **GitHub** (чтобы при вводе короткой команды `git push` без аргументов код улетал именно на GitHub), выполним в терминале одну простую команду, чтобы вернуть привязку обратно:

```bash
git push -u origin main

# branch 'main' set up to track 'origin/main'.
# Everything up-to-date
```

---

## 4. Daily Workflow

Работаем с кодом, делаем коммиты как обычно.

```bash
# Чтобы отправить изменения на `GitHub` (основной):
git push

# Чтобы отправить изменения на `GitVerse` (зеркало):
git push verse
```

_Если привычнее, вместо короткого `git push` можно отправить `git push origin`_

---

## 5. Параллельный автодеплой

Настроить параллельный автодеплой статического сайта (Jupyter Book) для GitHub Pages и GitVerse Pages можно через разделение конфигурационных файлов.

:::{note} Как разделить CI/CD для GitHub и GitVerse
:class: dropdown
:open: false

Для бесконфликтной работы двух систем развертывания нужно настроить изоляцию воркфлоу. Для этого отлично подходит настройка в интерфейсе GitVerse:

```text
Использовать конфигурацию из .gitverse/workflows.
При наличии .gitverse и .github, использовать .gitverse
```

**Логика разделения:**

- **GitHub** абсолютно ничего не знает про папку .gitverse и её содержимое. Он всегда обращается только к `.github/workflows/deploy.yml`.

- **GitVerse**, если включить указанную выше опцию, будет полностью игнорировать папку .github и выполнять только те инструкции, которые лежат в `.gitverse/workflows/`.

```text
# Cтруктура разделения 

Learning-SQL/
├── .github/               # деплой в GitHub: создается автоматически
│   └── workflows/         # командой `jupyter book init --gh-pages`
│       └── deploy.yml
├── .gitverse/             # деплой в GitVerse
│   └── workflows/
│       └── deploy.yml     # файл можно переименовать
...
```
:::

---

### Hастройка автодеплоя для GitVerse Pages

Настройка в веб-интерфейсе GitVerse:

1. Открыть созданный репозиторий _learning-sql_ на GitVerse.
2. Перейти в **Настройки** –> **Страницы** (в левом меню):
   - Включить тумблер **Включить функцию**.
   - В поле **Источник** выбрать значение **Воркфлоу** (Workflow).
3. Перейти в **Настройки** –> **Репозиторий** –> **CI/CD**:
   - Установить переключатель на опцию
   ```yaml
   Использовать конфигурацию из .gitverse/workflows.
   При наличии .gitverse и .github, использовать .gitverse
   ```

---

### Конфигурация файла сценария

В корне локального репозитория создаем новую директорию для GitVerse-экшенов:

```bash
# В корне проекта:
mkdir -p .gitverse/workflows

# Переходим в созданную папку
cd .gitverse/workflows

# Создаем файл сценария
touch deploy.yaml
```
% _Флаг `-p` (от англ. `parents` – родители) создает всю цепочку вложенных папок за один раз, а если они уже существуют пропустит создание и не выбросит ошибку `File exists`._

::::{div}
:class: text-sm

:::{note .simple .dropdown icon=false open=true} Флаг `-p` (от англ. _`parents`_)
Создает всю цепочку вложенных папок за один раз, а если они уже существуют пропустит создание и не выбросит ошибку `File exists`.

Это делает команду _идемпотентной_ (безопасной для повторного запуска в любых сценариях и скриптах).
:::
::::

---

В созданный файл `.gitverse/workflows/deploy.yml` добавляем конфигурацию, адаптированную под платформенные экшены GitVerse:

:::{code} yaml
:filename: deploy.yml
name: Deploy Jupyter Book to GitVerse Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

env:
  NODE_OPTIONS: --dns-result-order=ipv4first
  BASE_URL: /learning-sql

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18.x

      - name: Install Jupyter Book (via myst)
        run: npm install -g jupyter-book

      - name: Build HTML Assets
        run: jupyter-book build --html

      - name: Upload pages artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: './_build/html'

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitVerse Pages
        uses: actions/deploy-pages@v1
:::

---

### Отправка изменений на GitVerse

Осталось добавить сформированный `.gitverse/workflows/deploy.yml` в список отслеживаемых файлов, закоммитить и запушить на **оба** сервера.

:::{code} bash
git add .
git commit -m "chore: add gitverse actions deploy workflow"
git push               # отправляем изменения на `GitHub`
git push verse       # отправляем изменения на `GitVerse`
:::

Как только делаем `git push verse` в ветку `main`, сервера **GitVerse** перехватывают это событие, запускают виртуальную машину, собирают книгу и сами выкладывают её на [сайт-зеркало](https://alexey-sm.gitverse.site/learning-sql/).

---

## GitVerse vs GitHub: личный опыт

Месяц параллельного использования показал, что идея держать два независимых репозитория себя оправдала. Однако в роли веб-хостинга для статического сайта сервисы ведут себя по-разному.

### Плюсы: GitVerse как Git-зеркало

Как система контроля версий GitVerse работает стабильно. Команда `git push verse` синхронизирует репозиторий без сбоев, а раздельные SSH-ключи не конфликтуют. Благодаря этому проект получает независимый бэкап на случай проблем с доступом к зарубежным сервисам. В качестве зеркала платформа полностью выполняет свое назначение.

### Минусы: GitVerse Pages как хостинг

А вот со статическим сайтом пока не все гладко:
- **Скорость:** страницы на GitVerse открываются медленнее. Не критично, но ощутимо.
- **Стабильность деплоя:** сборка сайта в CI/CD на GitVerse падает чаще. На GitHub сбои тоже случаются, но значительно реже.
- **Не работает поиск (главный минус):** на GitVerse он не работает в принципе – окно поиска на секунду появляется и сразу схлопывается. А ведь именно ради быстрого поиска вся эта затея с сайтом и задумывалась (иначе можно было просто читать файлы в репозитории).

:::{dropdown} Можете оценить разницу самостоятельно:
:open: true

- **GitHub Pages:** [github.io/learning-sql](https://magus1968.github.io/learning-sql/) – быстрая загрузка и рабочий поиск (но из РФ может потребоваться тот самый _инструмент из трех букв_).
- **GitVerse Pages:** [gitverse.site/learning-sql](https://alexey-sm.gitverse.site/learning-sql/) – открывается неторопливо и без поиска, зато доступен без всяких _инструментов_.
:::

### Резюме
Рабочая связка на сегодня: **GitHub как основной удобный сайт** + **GitVerse как запасной аэродром с прямым доступом из РФ**.

:::{figure} media/gitverse-vs-github.png
% :align: left
% :width: 30%
:::

---
