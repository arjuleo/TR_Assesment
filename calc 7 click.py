import pyautogui
x=29
y=876
pyautogui.moveTo(x, y, duration=1)
pyautogui.click(x, y)
a=287
b=645
pyautogui.moveTo(a, b, duration=1)
pyautogui.click(a, b)
pyautogui.moveTo(377, 731)
pyautogui.click(377, 731)
pyautogui.hotkey('left', 'home', interval=0.25)
pyautogui.hotkey('shift', 'end', interval=0.25)
pyautogui.press('delete')
pyautogui.typewrite('calc')
pyautogui.press('enter', interval=0.25)
list(pyautogui.locateAllOnScreen(r'C:\Users\carj\Documents\calc7key.png'))
n7n=pyautogui.locateOnScreen(r'C:\Users\carj\Documents\calc7key.png')
b7x, b7y = pyautogui.center(n7n)
pyautogui.click(b7x, b7y)










