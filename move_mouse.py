import time
import pyautogui

# Ask user to input time in minutes
time_input = int(input("Enter time in minutes: "))
time_remaining = time_input * 60  # convert minutes to seconds
# Loop through the corners of the screen while time remains
while time_remaining > 0:
    time.sleep(5)
    # Move cursor to top-left corner
    pyautogui.moveTo(x=117, y=104, duration=0.5)

    # Move cursor to top-right corner
    pyautogui.moveTo(x=1784, y=115, duration=0.5)

    # Move cursor to bottom-right corner
    pyautogui.moveTo(x=1765, y=946, duration=0.5)
    spotify_button = pyautogui.locateOnScreen("./images/spotify.png", confidence=0.9)
    pyautogui.moveTo(spotify_button, duration=0.5)
    pyautogui.click(spotify_button)
    time.sleep(0.5)
    minimize_button = pyautogui.locateOnScreen("./images/minimize.png", confidence=0.8)
    pyautogui.moveTo(minimize_button, duration=0.5)
    pyautogui.click(minimize_button)

    # Move cursor to bottom-left corner
    pyautogui.moveTo(x=122, y=907, duration=0.5)
    pyautogui.click()

    # Update remaining time and print it
    time_remaining -= 10
    remaining_time = round(time_remaining)
    remaining_minutes, remaining_seconds = divmod(remaining_time, 60)
    print("Remaining time: {:02d}:{:02d}".format(remaining_minutes, remaining_seconds))

# Print end time in HH:MM:SS format
end_time = time.strftime("%H:%M:%S", time.localtime())
print("End time: ", end_time)
