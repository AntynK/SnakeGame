# Гра Змійка
Класична гра змійка написана на мові Python з використанням [Pygame](https://www.pygame.org/docs/).

## Вимоги
Версія Python 3.9 або новіша. 

Версія pygame 2.1.0 або новіша.

## Запуск
Гру можна запустити 2 способами.

### Спосіб 1: Вихідний код
> [!IMPORTANT]
> У вас має бути встановлений [Python 3.9](https://www.python.org/downloads/release/python-390/) або новіший

1. Відкрийте сторінку [релізів](https://github.com/AntynK/SnakeGame/releases/latest).
2. Завантажте архів `SourceCode.zip`.
3. Розпакуйте його.
4. Інсталюйте залежності для цього відкрийте розпаковану папку і виконайте команду
Windows:
```bash
pip install -r requirements.txt
``` 
#### Linux та MacOs:
```bash
pip3 install -r requirements.txt
``` 
5. Запустіть файл `main.py`, двічі натиснувши по ньому або через команду:
#### Windows:
```bash
python main.py
``` 
#### Linux та MacOs:
```bash
python3 main.py
``` 

### Спосіб 2: Виконуваний файл (лише Windows)
> [!NOTE]
> Цей спосіб працює лише на Windows, для інших операційних систем довидеться використовувати спосіб 1, або емулятори.

> [!IMPORTANT]
> У папці з виконуваним файлом має бути папка `assets` зі всіма зображеннями та фрифтами.


1. Відкрийте сторінку [релізів](https://github.com/AntynK/SnakeGame/releases/latest).
2. Завантажте файл `Snake game.exe` та архів `assets.zip`.
3. Розпакуйте архів `assets.zip`.
4. Перемістить файл `Snake game.exe` у розпаковану папку.
5. Запустіть його, двічі натиснувши по ньому.

## Збирання (Windows)
Для збирання використовується модуль [Pyinstaller](https://pyinstaller.org/en/stable/index.html), який можна встановити за допомогою команди:

#### Windows
```bash
pip install pyinstaller
```

Збирання програми виконується цією командою:
#### Windows
```bash
pyinstaller main.spec
```
Після завершення процесу збирання у папці `dist` буде знаходитися виконуваний файл.

> [!IMPORTANT]
> У папці з виконуваним файлом має бути папка `assets` зі всіма зображеннями та фрифтами.
