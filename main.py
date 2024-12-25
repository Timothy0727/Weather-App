from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+30+200")    # tkinter window with dimensions 500x900
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    try:
        # Define a custom and descriptive user_agent
        geolocator = Nominatim(user_agent="WeatherApp_TimLam/1.0 (contact: timlam727@gmail.com)")
        location = geolocator.geocode(city, timeout=10)
        
        if not location:
            messagebox.showerror("Error", "City not found. Please try again.")
            return
        
        # Fetch timezone using latitude and longitude
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        # get searched city's current time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # get real time weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06676166a3be2954ae9e0cf9a96ff7bf"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        feels_like = int(json_data['main']['feels_like'] - 273.15)

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", feels_like, "°C"))
        p.config(text=(pressure, "mb"))
        h.config(text=(humidity, "%"))
        w.config(text=(wind, "m/s"))
        d.config(text=description)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# search box
search_image = PhotoImage(file="images/search_bar.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="images/search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
logo_image = PhotoImage(file="images/logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# bottom box
frame_image = PhotoImage(file="images/box.png")
myimage_frame = Label(image=frame_image)
myimage_frame.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


# labels
# wind
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
w = Label(text='...', font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

# humidity
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
h = Label(text='...', font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

# description
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
d = Label(text='...', font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

# pressure
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)
p = Label(text='...', font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)




root.mainloop()