import tkinter as tk
import requests
import time

#get data from api
def getWeather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=3e3478877717792204f0cfcd5fe207aa"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'] - 273.15)
    min_temp=int(json_data['main']['temp_min'] - 273.15)
    max_temp=int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info= condition + "\n" + str(temp) + "°C"
    final_data= "\n" + "Max Temp : " +str(max_temp) + "°C" + "\n" + "Min Temp : " +str(min_temp) + "°C" + "\n" + "Pressure : " +str(pressure) + "\n" + "Humidity : " +str(humidity) + "\n" + "Wind Speed : " +str(wind) + "\n" + "Sunrise : " +sunrise + "\n" + "Sunset : " +sunset
    label1.config(text=final_info)
    label2.config(text=final_data)
    
    
    
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("weather app")
canvas.configure(bg="#57adff")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)     #return value obtained from textfield to getWeather function.

label1=tk.Label(canvas,font=t)
label1.pack()
label1.configure(bg="#57adff")

label2=tk.Label(canvas,font=f)
label2.pack()
label2.configure(bg="#57adff")
canvas.mainloop()


