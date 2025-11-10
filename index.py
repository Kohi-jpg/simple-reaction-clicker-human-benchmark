import pyautogui

print("script started\n rest your mouse over the colored part")

while True:
    x, y = pyautogui.position()
    if pyautogui.pixel(x, y) == (75, 219, 106):
        pyautogui.click()