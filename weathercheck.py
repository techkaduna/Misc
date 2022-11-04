from tkinter import *
import requests
import json




root = Tk()
root.title("Weather app")
#root.iconbitmap("favicon.ico")
root.geometry("400x500")

def search():
    #zipd = Label(root,text =zip.get())
    #zipd.grid(row=2,column=0,columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(Zip.get())+"20002&distance=25&API_KEY=YOUR_API_KEY")
        api = json.loads(api_request.content)
        city = str(api[0]["Reporting Area"])
        quality = str(api[0]["Aqi"])
        category = str(api[0]["Category"]["Name"])
        if category == "Good":
            color = "green"
        elif category == "Moderate":
            color = "black"
        elif category == "USG":
            color = "cyan"
        elif category == "Unhealthy":
            color = "grey"
        elif category == "Very unhealthy":
            color = "blue"
        elif category == "Hazardous":
            color = "red"

        root.configure(background="green")

        lbl = Label(root,text="City: "+city+" Air Quality: "+quality+" Category: "+category,background=color)
        lbl.grid(row=0,column=0)

    except Exception as e:
        print(e)
        print(Zip.get())


Zip = Entry(root)
Zip.grid(row=1,column=0)
Zipp = Button(root,text="Search",command=search).grid(row=1,column=2)

    
root.mainloop()
