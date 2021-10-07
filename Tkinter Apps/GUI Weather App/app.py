import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

# api.openweathermap.org/data/2.5/weather?id={city id}&appid={your api key}


def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']

        final_str='City: %s \nConditions: %s\n Temprature(°C): %s'%(name,desc,temp)
    except:
        final_str='No data retrieved'
    return final_str

def get_weather(city):
    weather_key='b32a57ee6c5e5e535f6cc6bafbc0af8a'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units': 'metric'}
    response=requests.get(url,params=params)
    weather=response.json()
    print(weather)
    label['text']=format_response(weather)

root=tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

back_img=tk.PhotoImage(file='Landscape.png')
back_label=tk.Label(root,image=back_img)
back_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text='Get Weather',font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,font=40)
label.place(relwidth=1,relheight=1)


root.mainloop()
