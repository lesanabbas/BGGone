# BGGone

BGGone is a simple and efficient desktop application that removes the background from images. It processes all images in a folder and removes their backgrounds with a click of a button using a user-friendly GUI built with Tkinter.

## Overview

BGGone helps users remove image backgrounds automatically, saving time and effort. The application processes images in the `IMG` folder and saves the results with transparent backgrounds into an `output` folder. It is powered by the `rembg` library and features a responsive GUI that continues to work smoothly even during image processing, thanks to multi-threading.

## Project Setup / Installation

To get started with BGGone, follow these steps:

### Requirements:
- Python 3.x
- Required Python Libraries: `rembg`, `Pillow`, `tkinter`
- Optionally: `PyInstaller` to create an executable file

### Installation:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/BGGone.git
    cd BGGone
    ```

2. Create and activate a virtual environment:

    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Install the dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the `IMG` folder exists in the project directory and place the images you want to process in that folder.

5. Run the application:

    ```bash
    python BGGone.py
    ```

## Create a Build or .exe

To create an executable file for easy distribution, follow these steps:

1. Install `PyInstaller` inside the virtual environment:

    ```bash
    pip install pyinstaller
    ```

2. Run the following command to create an executable from the script:

    ```bash
    pyinstaller --onefile --windowed BGGone.py
    ```

3. After running the above command, you will find the executable in the `dist/` folder. Place the `IMG` folder in the same directory as the `.exe` file.

4. Double-click the `.exe` file to run the application.

## Open Source License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**BGGone** - Simplifying image background removal with just a click!
