# Webhook KeyLogger
This code is an educational keylogger that captures keyboard input and sends it to an external server every five minutes.

- **Keyboard Monitoring**: Uses pynput to log each key pressed, storing it in the content variable. Special keys (space, enter, etc.) are formatted or ignored.

- **Data Transmission**: Every five minutes, a background thread sends the captured text to a specified webhook URL via a POST request.

- **Listener**: Runs continuously until manually stopped, tracking all key presses in real time.

This tool is for educational purposes only, the author do not endorse or promote any illegal activity and are not responsible for any damage done henceforth.
## Installation
### Windows
```batch
.\build_env.bat
```
### Linux
```sh
./build_env.sh
```
## Launch the Application
### Windows
```batch
.\run.bat
```
### Linux
```sh
./run.sh
```
## Generate Executable
### Windows
```batch
.\tools\generate_executable.bat
```
### Linux
```sh
./tools/generate_executable.sh
```
## License
_This program is free software; you can redistribute it and/or modify it under the terms of the MIT License (MIT). See [LICENSE](LICENSE) for more details._