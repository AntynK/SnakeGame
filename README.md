# Snake game
Popular game 'snake' written in Python.

## Requirements
Python version 3.9 or later.
Pygame version 2.1.0 or later.

## Run
The game can be run in two ways

### 1. Using the source code
> [!IMPORTANT]
> [Python 3.9](https://www.python.org/downloads/release/python-390/) or later must be installed

1. Open [releases](https://github.com/AntynK/SnakeGame/releases/latest) page.
2. Download the `SourceCode.zip` archive.
3. Unzip the archive.
4. Install the required modules using the command:

#### Windows:
```bash
pip install -r requirements.txt
``` 
#### Linux and MacOs:
```bash
pip3 install -r requirements.txt
``` 
5. Run the `main.py` file by double-clicking it or using the command:
#### Windows:
```bash
python main.py
``` 
#### Linux and MacOs:
```bash
python3 main.py
``` 

### 2. Using the executable file (Windows only)
> [!NOTE]
> This method is only for Windows. For other operating systems, use Method 1 or an emulator.

> [!IMPORTANT]
> The folder containing the executable must also include an `assets` folder with all images and fonts.

1. Open [releases](https://github.com/AntynK/SnakeGame/releases/latest) page.
2. Download the `Snake game.exe` file and the `assets.zip` archive.
3. Unzip the `assets.zip` archive.
4. Move the `Snake game.exe` file to the unpacked folder.
5. Run the executable file by double-clicking it.

## Building (Windows only)
[Pyinstaller](https://pyinstaller.org/en/stable/index.html) is used for building the game. It can be installed using the following command:

#### Windows
```bash
pip install pyinstaller
```

To build the game, use the following command:
#### Windows
```bash
pyinstaller main.spec
```

After building, a `dist` folder will be created, which contains the executable file.

> [!IMPORTANT]
> The folder containing the executable must also include an `assets` folder with all images and fonts.
