import pygetwindow as jw
import win32gui
import time
import requests

windows = jw.getWindowsWithTitle('Google chrome')

while True:
    for window in windows:
        title = window.title
        print(title)
        sites = ['facebook', 'youtube', 'فيسببوك', 'يوتيوب', 'faceBook']
        
        for x in sites:
            if x in title.lower():
                hwnd = window._hWnd
                title = win32gui.GetWindowText(hwnd)
                message = f"انتبه الموظف يتصفح الموقع التالي:\n{title}"
                title = f'{x}'
                ID = 753181682
                token = '8029803315:AAGPMDI96390dcH4jzVkj6jJ1r9zbOFMP-4'
                sent = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={message}'
                response = requests.get(sent)
                print(response.json())  # طباعة استجابة API
                
            time.sleep(5)