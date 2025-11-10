md
# Simple Reaction Clicker - Human Benchmark

A simple Python script to automate clicks on the Human Benchmark reaction time test.

## Key Features & Benefits

*   **Automation:** Automates the clicking process for the Human Benchmark reaction time test.
*   **Simple:** Easy to use and understand.
*   **Efficiency:** Potentially achieves faster reaction times than manual clicking (results may vary).

## Prerequisites & Dependencies

*   **Python 3.x:**  Make sure you have Python 3 installed on your system.
*   **PyAutoGUI:** This library is required for controlling the mouse and keyboard.  Install it using pip:
    ```bash
    pip install pyautogui
    ```

## Installation & Setup Instructions

1.  **Clone the Repository:** Clone this repository to your local machine using Git:
    ```bash
    git clone git@github.com:Kohi-jpg/simple-reaction-clicker-human-benchmark.git
    ```
    (Replace `git@github.com:Kohi-jpg/simple-reaction-clicker-human-benchmark.git` with the actual URL of the repository, e.g., `https://github.com/Kohi-jpg/simple-reaction-clicker-human-benchmark.git`)

2.  **Navigate to the Directory:** Change your current directory to the cloned repository:
    ```bash
    cd simple-reaction-clicker-human-benchmark
    ```

3.  **Install Dependencies:** Although only pyautogui is required and was installed above, double-check that it is correctly installed. If necessary, re-install it.

## Usage Examples

1.  **Run the Script:** Execute the `index.py` script using Python:
    ```bash
    python index.py
    ```

2.  **Important Note:** **BEFORE** running the script, open the Human Benchmark reaction time test in your browser. Position your mouse cursor over the colored area where the test begins.

3.  **Start the Script:** After running the script and seeing the "script started" message, *do not move your mouse*. The script will automatically click when the colored area changes.

4.  **Stop the Script:** To stop the script, you may need to interrupt it manually using `Ctrl+C` in your terminal.

## Configuration Options

Currently, the script has no external configuration options. The critical parameter is the RGB color value `(75, 219, 106)` which represents the green color the script waits for. If the website changes this, you must modify the script accordingly.

To find the current RGB values, you can use pyautogui to identify the color under the cursor before starting the test manually with the following steps:

1. Run a python script with `print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))` after importing pyautogui.
2. Hover the mouse over the target area on the Human Benchmark website.
3. Run the script to get the current RGB values.
4. Update the `if pyautogui.pixel(x, y) == (75, 219, 106):` line in `index.py` with the new RGB values.

## Contributing Guidelines

Contributions are welcome! Here's how you can contribute:

1.  **Fork the Repository:** Fork this repository to your GitHub account.

2.  **Create a Branch:** Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  **Make Changes:** Implement your changes and ensure they are well-documented.

4.  **Commit Changes:** Commit your changes with descriptive messages:
    ```bash
    git commit -m "Add your descriptive message here"
    ```

5.  **Push to GitHub:** Push your changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```

6.  **Create a Pull Request:** Create a pull request from your branch to the `main` branch of this repository.

## License Information

No license is currently specified for this project. All rights are reserved by the owner.

## Acknowledgments

*   [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - For providing the necessary mouse control functionality.
