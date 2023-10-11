@echo off
echo Instalando bibliotecas Python...

cls

pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org tk

cls

echo Primeira Instalação concluída.

cls

echo Fazendo a Proxima instalação.

cls

pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org pyautogui

cls

echo Segunda Instalação concluída.

cls

pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org time

cls

echo Todas bibliotecas instaladas, Execute agora o run.bat

pause
