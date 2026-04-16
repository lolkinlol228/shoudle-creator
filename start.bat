@echo off
:: Получаем путь к папке, где находится этот .bat (то есть project)
set "BASE_DIR=%~dp0"

:: Запускаем Python и main.py в подпапке "Новая папка"
start "" "%BASE_DIR%\Python\python.exe" "%BASE_DIR%\app.py"


:: Открываем браузер по умолчанию
start http://localhost:5000

pause
