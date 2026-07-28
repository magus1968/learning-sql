# SQL & SQLAlchemy vs Jupyter Book

:::{figure} media/cover.png
:align: left
:width: 30%
:::

Для проработки базовых знаний по MySQL, полученных на курсе Аналитик данных в Skillbox, выбрал из обзора [Лучшие книги по SQL](https://rutube.ru/video/d1430088a4d553b543ded84a471c6a8b/) на Rutube топ обзора: [Изучаем SQL. Генерация, выборка и обработка данных, 3-е изд. Алан Болье](https://shultais.education/blog/sql-books/learn-sql) (O'Reilly) пер. 2021.

Возник вопрос: где делать практику? Чтобы была возможность вернуться: подсмотреть/вспомнить код (запрос) и увидеть вывод (результат запроса).
- В книге используется клиент командной строки mysql (MySQL 8.0 Command Line Client) – но тогда не сохранится ни код (запрос), ни вывод. Можно конечно использовать логирование в текстовый файл с помощью команды tee, но мне этот способ оказался менее удобен в сравнении с итоговым решением.
- Можно использовать графический IDE, например, DBeaver – код сохранится, но вывод нет. По крайней мере в версии Community инструмента SQL Notebook нет.

Подсказку нашел в книге [_SQL. Pocket guide, 4-е изд. Элис Жао_](https://www.piter.com/collection/bazy-dannyh/product/sql-pocket-guide-4-e-izd) (O'Reilly) пер. 2024. В Главе 2 описывается подключение Python к базе данных через драйвер [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/). Но в итоге выбор пал на PyMySQL и SQLAlchemy.

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

