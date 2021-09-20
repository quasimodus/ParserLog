# log_ip_parser

<H1>Сборка проекта с помощью Pyinstaller</H1>
<code> pip3 install pyinstaller </code>

<code> pyinstaller --version </code>

Наиболее часто используемые опции:
----------------------------------------------------------------------------------
--onefile — сборка в один файл, т.е. файлы .dll не пишутся.
--windowed -при запуске приложения, будет появляться консоль.
--noconsole — при запуске приложения, консоль появляться не будет.
--icon=app.ico — добавляем иконку в окно.
--paths — возможность вручную прописать путь к необходимым файлам, если pyinstaller
не может их найти(например: --paths D:\python35\Lib\site-packages\PyQt5\Qt\bin)

PyInstaller анализирует файл myscript.py и делает следующее:

Пишет файл myscript.spec в той же папке, где находится скрипт.
Создает папку build в той же папке, где находится скрипт.
Записывает некоторые логи и рабочие файлы в папку build.
Создает папку dist в той же папке, где находится скрипт.
Пишет исполняемый файл в папку dist.

В итоге наша команда будет выглядеть так:
-------------------------------------------------------------
<code> pyinstaller --onefile --icon=name.ico --noconsole myscript.py </code>

или в нашем случае:

<code> pyinstaller --onefile --noconsole --icon=src\detective.ico ParserLog.py </code>
