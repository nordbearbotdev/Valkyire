<h1 align="center">📡 DDOS Tool (Layer 7) </h1> 
<div align="center">
<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> <img src="https://svgshare.com/i/ZhY.svg"> <img src="https://img.shields.io/github/forks/nordbearbotdev/Valkyire?style=social&label=Fork&maxAge=2592000"> <img src="https://img.shields.io/github/stars/nordbearbotdev/Valkyire?style=social&label=Star&maxAge=2592000"> <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"> 
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/nordbearbotdev/Valkyire/main/img/" width="200" height="200">
</p>

# :computer: Главное окно
<p align="center">
  <img src="https://raw.githubusercontent.com/tanjilk/Valkyire/main/img/imgshow.png">
</p>

# 🌙 Установка


<h2>Windows</h2> <img src="https://cdn.iconscout.com/icon/free/png-256/windows-221-1175066.png" width="50" height="50">  

  - Установите Python 3.8 [aqui](https://www.python.org/downloads/release/python-38)
  - Откроется установщик и нажмите на кнопку: `add python to PATH`
  - Скачайте архив Valkyire <a href="https://github.com/nordbearbotdev/Valkyire/archive/refs/heads/main.zip" target="blank">aqui</a>
  - Откройте cmd или PowerShell с Valkyire
  - Введите команду: `pip install -r requirements.txt`  


 

 <h2>Linux</h2><img src="https://raw.githubusercontent.com/8fn/Valkyire/main/img/linux-icon-28166.png" width="50" height="50">

```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/nordbearbotdev/Valkyire
cd Valkyire/
pip3 install -r requirements.txt or python -m pip install -r requirements.txt
```

<h2>Termux</h2><img src="https://brandslogos.com/wp-content/uploads/images/large/terminal-logo.png" width="50" height="50">  

```
pkg update
pkg install python3 python3-pip git -y
git clone https://github.com/nordbearbotdev/Valkyire
cd Valkyire/
pip3 install -r requirements.txt
```

## ❓ Как использовать?
Основная команда чтоб использовать.  

```
python3 Valkyire.py --time XXX --threads XXX --target [URL] --method HTTP
```

Пример: 

```
python3 Valkyire.py --time 5000 --threads 550 --target https://www.google.com/ --method HTTP
```
