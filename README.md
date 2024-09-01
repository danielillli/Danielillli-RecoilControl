# Recoil Control Script

This is a Python-based anti-recoil script that simulates mouse movements to control weapon recoil in various games. The script provides a simple GUI for adjusting recoil strength and can be controlled via global hotkeys.

## Features

- **Adjustable Recoil Strength:** Easily adjust the recoil strength using a simple GUI.
- **Global Hotkeys:** Use F1-F4 keys to control the script without focusing on the GUI.
- **Smooth Recoil Control:** Ensures smooth and consistent downward cursor movement.
- **Minimalistic GUI:** Lightweight, always-on-top GUI that can be toggled on or off.

## Requirements

- Python 3.7+
- `pyautogui` library
- `pynput` library
- `keyboard` library
- `tkinter` (usually included with Python)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/recoil-control-script.git
    cd recoil-control-script
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script:**

    ```bash
    python Recoil.py
    ```

## Usage

- **F1:** Decrease recoil power.
- **F2:** Increase recoil power.
- **F3:** Toggle the GUI.
- **F4:** Exit the script.

The script starts controlling the recoil as soon as you press the left mouse button and stops when the button is released.

## Customization

You can adjust the default recoil strength range by modifying the `power` variable in the script.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this script at your own risk. The developer is not responsible for any consequences that may arise from the use of this script in online games.
