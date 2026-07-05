# Конспект книги Алана Болье Изучение SQL

## Задача

Для проработки базовых знаний по MySQL, полученных на курсе Аналитик данных в Skillbox, выбрал из обзора [Лучшие книги по SQL](https://rutube.ru/video/d1430088a4d553b543ded84a471c6a8b/) на Rutube топ обзора: Изучаем SQL. Генерация, выборка и обработка данных, 3-е изд. Алан Болье (O'Reilly) пер. 2021.

Возник вопрос – где делать практику? Чтобы была возможность вернуться: подсмотреть/вспомнить код (запрос) и увидеть вывод (результат запроса).
- В книге используется клиент командной строки mysql (MySQL 8.0 Command Line Client) – но тогда не сохранится ни код (запрос), ни вывод. Можно конечно использовать логирование в текстовый файл с помощью команды tee, но мне этот способ оказался менее удобен в сравнении с итоговым решением.
- Можно использовать графический IDE, например, DBeaver CE – код сохранится, но вывод нет. По крайней мере в версии Community инструмента SQL Notebook нет.

Подсказку нашел в книге SQL. Pocket guide, 4-е изд. Элис Жао (O'Reilly) пер. 2024. В Главе 2 описывается подключение Python к базе данных через драйвер [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/). Но в итоге выбор пал на PyMySQL и SQLAlchemy.

**Итоговое решение**: блокноты [Jupyter Notebook](https://jupyter.org/), [Python](https://www.python.org/) и [SQLAlchemy](https://www.sqlalchemy.org/) – из дистрибутива [Anaconda](https://www.anaconda.com/download); плюс драйвер-коннектор [PyMySQL](https://pypi.org/project/PyMySQL/) и [JupySQL](https://jupysql.readthedocs.io/en/latest/quick-start.html) для подсветки синтаксиса SQL.

Вопрос вроде бы был уже решен, но тут появилась "подкожная" мысль, которая и стала причиной этого гайда: что если для доступа к блокнотам использовать не просто GitHub, а создать статический сайт с функцией поиска?

Опыт с [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) у меня уже был, но он использует только файлы [Markdown](https://www.markdownguide.org/). И тут я вспомнил про книгу [Learning Data Science](https://learningds.org/intro.html), которая Powered by [Jupyter Book](https://jupyterbook.org/). И мое желание быстрее приступить к проработке SQL "пришлось" отложить на исследование нового инструмента и на составление гайда – потому что я не смог повторить сходу все установки/настройки и прочие манипуляции на втором компе.

А ещё потому что:
- Пришлось искать костыльное решение для отображения синтаксиса SQL на сайте: потому что JupySQL подсвечивает синтаксис в блокноте Jupyter, но не на созданном с помощью Jupyter Book сайте. _В этот момент идею с сайтом хотелось уже бросить в пользу обычного хранения на GitHub._
- Плюс у "подкожной мысли" появилось продолжение: а что если доступ к GitHub заблокируют? Смогу ли использовать отечественный [GitVerse](https://gitverse.ru/home/)? Если да – как использовать GitHub и GitVerse в параллели с одним локальным репозиторием?

На случай если кому-то пригодятся мои изыскания решил поделиться.

Оффтоп: для изучения/прокачки SQL много любопытных ресурсов:
- [Интерактивный онлайн курс по SQL](https://sql-academy.org/ru) от SQL Academy
- [Симулятор SQL](https://karpov.courses/simulator-sql) от karpov.courses
- [100-Year QA-Textbook 2026: Базы данных для тестировщиков](https://mentorpiece.ru/100/db/) от Mentorpiece Education
- [Интерактивный тренажер по SQL](https://stepik.org/course/63054/promo) на Stepik (автор Озерова Галина Павловна)
- [SQL с нуля до PRO](https://stepik.org/course/61247/promo) на Stepik (автор Shultais Education)
- [SQL практикум. Основы](https://stepik.org/course/212435/promo) на Stepik (автор Pragmatic Programmer)
- [Learn SQL](https://www.w3schools.com/sql/default.asp) от W3 schools

Просто на данном этапе я выбрал книгу, изредка подглядывая на эти ресурсы.

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
