# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['nirma']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def getweather(city):
    result = requests.get(url.format(city, api_key))
      
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = round(temp_kelvin-273.15,3)
        temp_feels_kelvin = json['main']['feels_like']
        temp_feels_celsius =  round(temp_feels_kelvin - 273.15,3)
        temp_min_k = json['main']['temp_min']
        temp_min_c =  round(temp_min_k - 273.15,3)
        temp_max_k = json['main']['temp_max']
        temp_max_c =  round(temp_max_k - 273.15,3)
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_celsius,temp_feels_celsius ,temp_min_c,temp_max_c,weather1]
        return final
    else:
        print("No Results Found For The City You Entered")


def search():
    city = city_entered.get()
    weather = getweather(city)
      
    if weather:
        loc['text'] = 'City: {} , Country: {}'.format(weather[0], weather[1]['country'])
        loc['borderwidth'] = 2
        loc['relief'] = 'solid'
        tempLab['text'] =  'Current Temperature: {}, But Feels Like: {} (All temperatures in degree celsius)'.format(weather[2],weather[3])
        tempLab['borderwidth'] = 2
        tempLab['relief'] = 'solid'
        temp_maxmin['text'] = 'Maximum Temperature:{} ; Minimum Temperature: {}'.format(weather[5],weather[4])
        temp_maxmin['borderwidth'] = 2
        temp_maxmin['relief'] = 'solid'
        weather_desc['text'] = 'Today\' weather : {}'.format(weather[6])
        weather_desc['borderwidth'] = 2
        weather_desc['relief'] = 'solid'
          
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

app = Tk()
app.title("Nirmalya's Weather App")

app.geometry("2000x2000")
  
# add labels, buttons and text
city_entered = StringVar()
city_wid = Entry(app, textvariable=city_entered)
city_wid.pack(padx=5, pady=5)#padx=20, pady=40)
  
button = Button(app, text="Search Weather",width=12, command=search)
button.pack()#padx=20, pady=40)
  
loc = Label(app, text="Enter Location Here", font={'bold', 20})#,borderwidth=2, relief="solid")
loc.pack(padx=10, pady=10)
  
tempLab = Label(app, text="", font={'bold', 20})#,borderwidth=2, relief="solid")
tempLab.pack(padx=10, pady=10)
#tempLab.grid(padx=20, pady=40)

temp_maxmin = Label(app, text="", font={'bold', 20})#,borderwidth=2, relief="solid")
temp_maxmin.pack(padx=10, pady=10)
#temp_maxmin.grid(padx=20, pady=40)
  
weather_desc = Label(app, text="", font={'bold', 20})#,borderwidth=2, relief="solid")
weather_desc.pack(padx=10, pady=10)
#weather_desc.grid(padx=20, pady=40)

canvas = Canvas(app, width = 1200, height = 1200)      
canvas.pack()      
img = PhotoImage(file="img.png")      
canvas.create_image(20,20, anchor=NW, image=img)  

app.mainloop()


