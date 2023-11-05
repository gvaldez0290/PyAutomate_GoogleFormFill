"""
This code was adapted from https://automatetheboringstuff.com/2e/chapter20/ by Al Sweigart
https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
"""

import pyautogui, time
import pandas as pd
import webbrowser

# Open the link to the form in the default web browser
webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')

# Wait for the browser to open
time.sleep(5)  # Adjust this delay as needed


formData= pd.read_csv(
    r"C:\dataPath.csv",
    sep=","
)

print(formData.head())


pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')


for index, person in formData.iterrows():
    # Give the user a chance to kill the script.
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    
    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t', '\t', '\t'])  # Simulates pressing the Tab key four times


    # Fill out the Name field.
    pyautogui.write(person['name'] + '\t')


    # Fill out the Greatest Fear(s) field.
    pyautogui.write(person['fear'] + '\t')
    
    
     # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.write(['down', '\n','\t'] , 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\n','\t'] , 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\n','\t'] , 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\n','\t'] , 0.5)
    
         # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.write(['right', 'left', '\t', '\t'] , 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'] , 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'] , 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'] , 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'] , 0.5)
    
    # Fill out the Additional Comments field.
    pyautogui.write(person['comments'] + '\t')
    
    # "Click" Submit button by pressing Enter.
    time.sleep(0.5) # Wait for the button to activate.
    pyautogui.press('enter')
    time.sleep(5)
    
    pyautogui.write(['\t','\n'])
    
    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

#close the active browser
pyautogui.hotkey('alt', 'f4')
