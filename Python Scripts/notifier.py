from plyer import notification # pip install plyer
import time

if __name__ == "__main__":
    while True:
        notification.notify(title="Health Break", message="Take a break from your pc. Go and drink water. Move your head a little bit. Do some quick exercise, it will help you keep yourself fit. Give rest to your fingers.", timeout=10, app_name="PyHealth", app_icon="icon.ico") # put icon.ico in the same folder as the script
        time.sleep(1200) # sleeps and notifies every 1200 seconds
