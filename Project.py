from tkinter import *
import tkcalendar
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib
from dateutil.parser import parse
from matplotlib.backends.backend_tkagg import *
import matplotlib.pyplot as plt
from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure 
import seaborn as sns
from tkinter import filedialog
import requests 
from geopy.geocoders import Nominatim
from PIL import ImageTk
import time
import csv
from ttkwidgets.autocomplete import AutocompleteCombobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
from meteostat import Point, Daily

def monthf1(x):
    if x=="Jan":
        return "01"
    elif x=="Feb":
        return "02"
    elif x=="Mar":
        return "03"
    elif x=="Apr":
        return "04"
    elif x=="May":
        return "05"
    elif x=="Jun":
        return "06"
    elif x=="Jul":
        return "07"
    elif x=="Aug":
        return "08"
    elif x=="Sep":
        return "09"
    elif x=="Oct":
        return "10"
    elif x=="Nov":
        return "11"
    elif x=="Dec":
        return "12"

def dayf(x):
    if x==" 1":
        return str(int(monthf1(dtime[4:7]))-1),"18", "01"
    elif x==" 2":
        return str(int(monthf1(dtime[4:7]))-1),"19", "02"
    elif x==" 3":
        return str(int(monthf1(dtime[4:7]))-1),"20", "03"
    elif x==" 4":
        return str(int(monthf1(dtime[4:7]))-1),"21", "04"
    elif x==" 5":
        return str(int(monthf1(dtime[4:7]))-1),"22", "05"
    elif x==" 6":
        return str(int(monthf1(dtime[4:7]))-1),"23", "06"
    elif x==" 7":
        return str(int(monthf1(dtime[4:7]))-1),"24", "07"
    elif x==" 8":
        return str(int(monthf1(dtime[4:7]))-1),"25", "08"
    elif x==" 9":
        return str(int(monthf1(dtime[4:7]))-1),"26", "09"
    elif x=="10":
        return str(int(monthf1(dtime[4:7]))-1),"27", "10"
    elif x=="11":
        return str(int(monthf1(dtime[4:7]))-1),"28", "11"
    elif x=="12":
        return str(int(monthf1(dtime[4:7]))-1),"29", "12"
    elif x=="13":
        return str(int(monthf1(dtime[4:7]))-1),"30", "13"
    elif x>=14 and x<24:
        return monthf1(dtime[4:7]), str("0"+str(int(x)-14)), str(x)
    else:
        return monthf1(dtime[4:7]), str(int(x)-14), str(x)

def getdates():
    global dtime, q, neie1, neie2, neie3, neie4, neie6,neie7,neie8,neie9,neie5
    if q==1:
        neie1.destroy()
        neie2.destroy()
        neie3.destroy()
        neie4.destroy()
        neie5.destroy()
        neie6.destroy()
        neie7.destroy()
        neie8.destroy()
        neie9.destroy()
        
    dtime=time.ctime(time.time())
    kek=dayf(dtime[8:10])
    mont=monthf1(dtime[4:7])
    dayt=kek[2]
    startday=kek[1]
    mont1=kek[0]
    year=int(dtime[-4:-1]+dtime[-1])
    start = datetime(year, int(mont1), int(startday))
    end = datetime(year, int(mont), int(dayt))
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(citynamepre.get())
    location = Point(getLoc.latitude, getLoc.longitude)
    data = Daily(location, start, end)
    data = data.fetch()
    Data=data.values.tolist()
    data=[]
    for i in range(len(Data)):
        data.append([])
        data[i].append(i+1)
        data[i].append(int(Data[i][0]))
        data[i].append(int(Data[i][6]))
        data[i].append(int(Data[i][8]))
    Data=np.asarray(data)
    mean = np.arange(start=i+2, stop=i+5)
    fittempe = np.polyfit(Data[:,0], Data[:,1] ,1) 
    linetempe = np.poly1d(fittempe)
    postempe=linetempe(mean)
    fitwind = np.polyfit(Data[:,0], Data[:,2] ,1)
    linewind = np.poly1d(fitwind)
    poswind=linewind(mean)
    fitpres = np.polyfit(Data[:,0], Data[:,3] ,1)
    linepres = np.poly1d(fitpres)
    pospres=linepres(mean)
    for i in range(len(postempe)):
        postempe[i]=round(postempe[i],1)
    for i in range(len(poswind)):
        poswind[i]=round(poswind[i],1)
    for i in range(len(pospres)):
        pospres[i]=round(pospres[i],0)
    
    neie1=Label(Prediction, text=postempe[0], font=("Arial", 15))
    neie1.grid(row=0,column=0, sticky=N, pady=220)
    neie2=Label(Prediction, text=poswind[0], font=("Arial", 15))
    neie2.grid(row=0,column=1, sticky=N, pady=220)
    neie3=Label(Prediction, text=pospres[0], font=("Arial", 15))
    neie3.grid(row=0,column=2, sticky=N, pady=220)
    neie4=Label(Prediction, text=postempe[1], font=("Arial", 15))
    neie4.grid(row=0,column=0, sticky=S, pady=130)
    neie5=Label(Prediction, text=poswind[1], font=("Arial", 15))
    neie5.grid(row=0,column=1, sticky=S, pady=130)
    neie6=Label(Prediction, text=pospres[1], font=("Arial", 15))
    neie6.grid(row=0,column=2, sticky=S, pady=130)
    neie7=Label(Prediction, text=postempe[2], font=("Arial", 15))
    neie7.grid(row=0,column=0, sticky=S)
    neie8=Label(Prediction, text=poswind[2], font=("Arial", 15))
    neie8.grid(row=0,column=1, sticky=S)
    neie9=Label(Prediction, text=pospres[2], font=("Arial", 15))
    neie9.grid(row=0,column=2, sticky=S)
    neiel1=Label(Prediction, text="Через 1 день", font=("Arial", 18))
    neiel1.grid(row=0,column=1, sticky=N, pady=180)
    neiel2=Label(Prediction, text="Через 2 дня", font=("Arial", 18))
    neiel2.grid(row=0,column=1, sticky=S, pady=170)
    neiel4=Label(Prediction, text="Через 3 дня", font=("Arial", 18))
    neiel4.grid(row=0,column=1, sticky=S, pady=40)
    q=1
    
def prediction():
    global Prediction, citynamepre, q, pred, analy, moni, vis, visual, Analytics, monitoring
    q=0
    if vis == 1:
        visual.withdraw()
        vis = 0
    if moni == 1:
        monitoring.withdraw()
        moni = 0
    if analy==1:
        Analytics.withdraw()
        analy=0
    
    Prediction=Tk()
    Prediction.title("Прогноз")
    Prediction.geometry("800x600")
    for x in range(3): Prediction.columnconfigure(index=x, weight=1)
    for y in range(3):Prediction.rowconfigure(index=y, weight=1)
    citypre=Button(Prediction, text="Введите название города", font=("Arial", 14), height=1, command=getdates)
    citypre.grid(row=0,column=1, sticky=N, pady=20)
    citynamepre=Entry(Prediction, font=("Arial", 14))
    citynamepre.grid(row=0,column=1, sticky=N, pady=70)
    Pressura_praedictio=Label(Prediction, text="Давление", font=("Arial", 18))
    Pressura_praedictio.grid(row=0,column=2, sticky=N, pady=120)
    ventus_celeritate=Label(Prediction, text="Скорость ветра", font=("Arial", 18))
    ventus_celeritate.grid(row=0,column=1, sticky=N, pady=120)
    Temperatus=Label(Prediction, text="Температура", font=("Arial", 18))
    Temperatus.grid(row=0,column=0, sticky=N, pady=120)
    b1=Button(Prediction, width=2, height=1, bg='lightblue', command=predtoana)
    b1.grid(row=2,column=1, sticky=SW)
    b2=Button(Prediction, width=2, height=1, bg='lightgreen', command=predtovis)
    b2.grid(row=2,column=1, sticky=S)
    b3=Button(Prediction, width=2, height=1, bg='orange', command=predtomon)
    b3.grid(row=2,column=1, sticky=SE)
    
    Prediction.mainloop()


def callmonth(town, timing):
    global ForSavep
    if yyy ==1:
        lamaxtempe.destroy(Analytics)
        laminhumiditas.destroy(Analytics)
        lamaxpressio.destroy(Analytics)
        lagravispluviam.destroy(Analytics)
        laminhumilispraecipitatio.destroy(Analytics)
        laMediocrisTemperatus.destroy(Analytics)
        laMediocrishumiditas.destroy(Analytics)
    if timing=="Январь":
        timing=1
    elif timing=="Февраль":
        timing=2
    elif timing=="Март":
        timing=3
    elif timing=="Апрель":
        timing=4
    elif timing=="Май":
        timing=5
    elif timing=="Июнь":
        timing=6
    elif timing=="Июль":
        timing=7
    elif timing=="Август":
        timing=8
    elif timing=="Сентябрь":
        timing=9
    elif timing=="Октябрь":
        timing=10
    elif timing=="Ноябрь":
        timing=11
    elif timing=="Декабрь":
        timing=12
    i = info11.index(town)
    if town=="Кастомные данные":
        data=CustomData
        Data=[]
        for i in range(len(data)):
            if data[i][1]==int(timing):
                Data.append(data[i])
    else:
        data = [j.strip() for j in open(str(Meteor1[i][1])+".dat").readlines()]
        Data=[]
        Count=0
        for i in range(len(data)):
            if int(data[i][25:27])==int(timing):
                Data.append([])
                Data[Count].append(int(data[i][20:24]))
                Data[Count].append(int(data[i][25:27]))
                Data[Count].append(int(data[i][28:30]))
                if data[i][118:120] == "  ":
                    a = 0
                else:
                    a = int(data[i][118:120])     
                Data[Count].append(a)
                if data[i][132:138] == "      ":
                    a = 0.0
                else:
                    a = float(data[i][132:138])
                Data[Count].append(a)
                if data[i][181:186] == "     ":
                    a = 0.0
                else:
                    a = float(data[i][181:186])     
                Data[Count].append(a)
                if data[i][241:244] == "   ":
                    a = 0
                else:
                    a = int(data[i][241:244])    
                Data[Count].append(a)
                if data[i][276:282] == "      ":
                    a = 0.0
                else:
                    a = float(data[i][276:282])    
                Data[Count].append(a)
                Count=Count+1
    temperatura=[]
    numerustempe=[]
    daymaxtempe=[]
    for i in range(len(Data)):
            temperatura.append(Data[i][5])
            numerustempe.append(Data[i][2])
    maxtempe=max(temperatura)
    MediocrisTemperatus=sum(temperatura)/len(temperatura)
    humiditas=[]
    for i in range(len(Data)):
        if Data[i][6]!=0:
            humiditas.append(Data[i][6])
    minhumiditas=min(humiditas)
    Mediocrishumiditas=sum(humiditas)/len(humiditas)
    humilispraecipitatio=[]
    for i in range(len(Data)):
        if Data[i][4] != 0:
            humilispraecipitatio.append(Data[i][4])
    minhumilispraecipitatio=min(humilispraecipitatio)
    gravispluviam=max(humilispraecipitatio)
    pressio=[]
    numeruspressio=[]
    daypressio=[]
    for i in range(len(Data)):
            pressio.append(Data[i][7])
    maxpressio=max(pressio)
    MediocrisTemperatus=round(MediocrisTemperatus, 1)
    Mediocrishumiditas=int(round(Mediocrishumiditas,0))
    lamaxtempe=Label(Analytics, text=maxtempe, font=("Arial", 16))
    lamaxtempe.grid(row=0,column=0, sticky=S,pady=50)
    laminhumiditas=Label(Analytics, text=minhumiditas, font=("Arial", 16))
    laminhumiditas.grid(row=0,column=2, sticky=S,pady=50)
    lamaxpressio=Label(Analytics, text=maxpressio, font=("Arial", 16))
    lamaxpressio.grid(row=1,column=1, sticky=N,pady=60)
    lagravispluviam=Label(Analytics, text=gravispluviam, font=("Arial", 16))
    lagravispluviam.grid(row=1,column=0, sticky=N,pady=60)
    laminhumilispraecipitatio=Label(Analytics, text=minhumilispraecipitatio, font=("Arial", 16))
    laminhumilispraecipitatio.grid(row=1,column=2, sticky=N,pady=60)
    laMediocrisTemperatus=Label(Analytics, text=MediocrisTemperatus, font=("Arial", 16))
    laMediocrisTemperatus.grid(row=2,column=0, sticky=N,pady=50)
    laMediocrishumiditas=Label(Analytics, text=Mediocrishumiditas, font=("Arial", 16))
    laMediocrishumiditas.grid(row=2,column=2, sticky=N,pady=50)
    y=1
    ForSave=[]
    ForSave.append(maxtempe)
    ForSave.append(minhumiditas)
    ForSave.append(maxpressio)
    ForSave.append(gravispluviam)
    ForSave.append(minhumilispraecipitatio)
    ForSave.append(MediocrisTemperatus)
    ForSave.append(Mediocrishumiditas)
    col1="Параметры"
    col2="Данные"
    list1 = ["Максимальная температура","Самая низкая влажность","Самое высокое атм. давление","Большее кол-во осадков","Меньшее кол-во осадков","Средняя температура","Средняя влажность"]
    ForSavep=pd.DataFrame({col1: list1, col2: ForSave})
    Saveinfo=Button(Analytics, text="Сохранить", command=loadd).grid(row=2,column=1, sticky=N,pady=20)
    

def analysf():
    global pred, Analytics, info11, Meteor1, yyy, vis, moni, monitoring, visual, analy, Prediction
    analy=0
    if vis == 1:
        visual.withdraw()
        vis = 0
    if moni == 1:
        monitoring.withdraw()
        moni = 0
    if pred == 1:
        Prediction.withdraw()
        pred = 0
        
    Analytics=Tk()
    Analytics.geometry("800x600")
    Analytics.title("Анализ")
    yyy=0
    f = open("Vs.csv")
    Meteor1 = []
    info11 = []
    for x in f:
        x = x.split(";")
        Meteor1.append(x)
        info11.append(x[0])
    
    for x in range(3): Analytics.columnconfigure(index=x, weight=1)
    for y in range(3): Analytics.rowconfigure(index=y, weight=1)
    city=Label(Analytics, text="Город", font=("Arial", 14), height=1)
    city.grid(row=0,column=1, sticky=N, pady=5)
    info1=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
    combobox = ttk.Combobox(Analytics, values=info11)
    combobox.grid(row=0,column=1, sticky=N, pady=35)
    period=Label(Analytics, text="Промежуток времени", font=("Arial", 14), height=1)
    period.grid(row=0,column=1, sticky=N, pady=60)
    combobox1 = ttk.Combobox(Analytics, values=info1)
    combobox1.grid(row=0,column=1, sticky=N, pady=90)
    apply=Button(Analytics, text="Анализ", font=("Arial", 14), height=1,command=lambda: callmonth(combobox.get(),combobox1.get()))
    apply.grid(row=0,column=1, sticky=N, pady=120)
    temperature=Label(Analytics, text="Максимальная температура", font=("Arial", 12))
    temperature.grid(row=0,column=0, sticky=S,pady=80)
    speedwind=Label(Analytics, text="Самая низкая влажность", font=("Arial", 12))
    speedwind.grid(row=0,column=2, sticky=S,pady=80)
    description=Label(Analytics, text="Самое высокое атм. давление", font=("Arial", 12))
    description.grid(row=1,column=1, sticky=N,pady=30)
    humidity=Label(Analytics, text="Большее кол-во осадков", font=("Arial", 12))
    humidity.grid(row=1,column=0, sticky=N,pady=30)
    pressure=Label(Analytics, text="Меньшее кол-во осадков", font=("Arial", 12))
    pressure.grid(row=1,column=2, sticky=N,pady=30)
    humidity=Label(Analytics, text="Средняя температура", font=("Arial", 12))
    humidity.grid(row=2,column=0, sticky=N,pady=20)
    pressure=Label(Analytics, text="Средняя влажность", font=("Arial", 12))
    pressure.grid(row=2,column=2, sticky=N,pady=20)
    b1=Button(Analytics, width=2, height=1, bg='lightgreen', command=anatovis)
    b1.grid(row=2,column=1, sticky=SW)
    b2=Button(Analytics, width=2, height=1, bg='yellow', command=anatopred)
    b2.grid(row=2,column=1, sticky=S)
    b3=Button(Analytics, width=2, height=1, bg='orange', command=anatomon)
    b3.grid(row=2,column=1, sticky=SE)
    
    
    Analytics.mainloop()

def get_weather():
    global monitoring, tempera, feelsl, speedw, pres, humidi, desc, u
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(cityname.get())
    lat = getLoc.latitude
    lon = getLoc.longitude
    if u == 1:
        tempera.destroy()
        feelsl.destroy()
        speedw.destroy()
        pres.destroy()
        humidi.destroy()
        desc.destroy()
    params = { 
        'lat': lat, 
        'lon': lon, 
        'lang': 'ru_RU', 
        'limit': 7, 
        'hours': True, 
        'extra': True 
    } 
      
    api_key = 'f20b317e-2d69-4280-809e-3a1ea0494302' 
     
    url = 'https://api.weather.yandex.ru/v2/forecast' 
      
    response = requests.get(url, params=params, headers={'X-Yandex-API-Key': api_key}) 
      
    if response.status_code == 200:  
        data = response.json()  
        tempera=Label(monitoring,text=f'{data["fact"]["temp"]} °C', font=("Arial", 20))
        tempera.grid(row=1, column=0, sticky=N)
        feelsl=Label(monitoring,text=f'{data["fact"]["feels_like"]} °C', font=("Arial", 20))
        feelsl.grid(row=1, column=1, sticky=N) 
        speedw=Label(monitoring,text=f'{data["fact"]["wind_speed"]} м/с', font=("Arial", 20))
        speedw.grid(row=1, column=2, sticky=N) 
        pres=Label(monitoring,text=f'{data["fact"]["pressure_mm"]} мм рт. ст.', font=("Arial", 20))
        pres.grid(row=2, column=0, sticky=N) 
        humidi=Label(monitoring,text=f'{data["fact"]["humidity"]} %', font=("Arial", 20))
        humidi.grid(row=2, column=1, sticky=N) 
        desc=Label(monitoring,text=f'{data["fact"]["condition"]}', font=("Arial", 20))
        desc.grid(row=2, column=2, sticky=N)
        u = 1
    else: 
        print(f'Ошибка: {response.status_code}')

def OpenFile():
    global CustomData
    files = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.dat"),("XLSX", "XLSX"), ("CSV", "CSV"),("all files", "*.*")),
        multiple=True
        )
    
    lst = str(files)[2:-3]
    CustomData=[]
    data = [i.strip() for i in open(lst).readlines()]
    for i in range(len(data)):
        CustomData.append([])
        CustomData[i].append(int(data[i][20:24]))
        CustomData[i].append(int(data[i][25:27]))
        CustomData[i].append(int(data[i][28:30]))
        if data[i][118:120] == "  ":
            a = 0
        else:
            a = int(data[i][118:120])     
        CustomData[i].append(a)
        if data[i][132:138] == "      ":
            a = 0.0
        else:
            a = float(data[i][132:138])
        CustomData[i].append(a)
        if data[i][181:186] == "     ":
            a = 0.0
        else:
            a = float(data[i][181:186])     
        CustomData[i].append(a)
        if data[i][241:244] == "   ":
            a = 0
        else:
            a = int(data[i][241:244])    
        CustomData[i].append(a)
        if data[i][276:282] == "      ":
            a = 0.0
        else:
            a = float(data[i][276:282])    
        CustomData[i].append(a)
    Label(ws, text="Файл загружен").place(x=200, y=120, anchor="c", width=280, height=40)

def monthf(x):
    if x=="Jan":
        return "янв"
    elif x=="Feb":
        return "Фев"
    elif x=="Mar":
        return "мар"
    elif x=="Apr":
        return "апр"
    elif x=="May":
        return "май"
    elif x=="Jun":
        return "июн"
    elif x=="Jul":
        return "июл"
    elif x=="Aug":
        return "авг"
    elif x=="Sep":
        return "сен"
    elif x=="Oct":
        return "окт"
    elif x=="Nov":
        return "ноя"
    elif x=="Dec":
        return "дек"
    
def monitoringf():
    global pred, monitoring, cityname, u, tempera, feelsl, speedw, pres, humidi, desc, moni, vis, analy, Analytics, Prediction
    monitoring=Tk()
    monitoring.title("Мониторинг")
    monitoring.geometry("800x600")
    u = 0 ### в get_weather понадобится
    if vis == 1:
        visual.withdraw()
        vis = 0
    if analy == 1:
        Analytics.withdraw()
        analy = 0
    if pred == 1:
        Prediction.withdraw()
        pred = 0
    
    for x in range(3): monitoring.columnconfigure(index=x, weight=1)
    for y in range(3):monitoring.rowconfigure(index=y, weight=1)
    city=Button(monitoring, text="Введите название города", font=("Arial", 14), height=1, command=get_weather)
    city.grid(row=0,column=1, sticky=N, pady=20)
    cityname=Entry(monitoring)
    cityname.grid(row=0,column=1, sticky=N, pady=70)
    ltime=time.ctime(time.time())
    month=monthf(ltime[4:7])
    date=Label(monitoring,text="Дата: "+ltime[8:10]+" "+month+" "+ltime[-4:]+" Время: "+ltime[-13:-5], font=("Arial", 16)).grid(row=0, column=1)
    temperature=Label(monitoring, text="Температура воздуха", font=("Arial", 12))
    temperature.grid(row=1,column=0, sticky=N, pady=53)
    feelslike=Label(monitoring, text="Ощущается как", font=("Arial", 12))
    feelslike.grid(row=1,column=1, sticky=N, pady=53)
    speedwind=Label(monitoring, text="Скорость ветра", font=("Arial", 12))
    speedwind.grid(row=1,column=2, sticky=N, pady=53)
    description=Label(monitoring, text="Погодное описание", font=("Arial", 12))
    description.grid(row=2,column=2, sticky=N, pady=53)
    humidity=Label(monitoring, text="Влажность", font=("Arial", 12))
    humidity.grid(row=2,column=1, sticky=N, pady=53)
    pressure=Label(monitoring, text="Давление", font=("Arial", 12))
    pressure.grid(row=2,column=0, sticky=N, pady=53)
    b1=Button(monitoring, width=2, height=1, bg='lightblue', command=montoana)
    b1.grid(row=2,column=1, sticky=SW)
    b2=Button(monitoring, width=2, height=1, bg='lightgreen', command=montovis)
    b2.grid(row=2,column=1, sticky=S)
    b3=Button(monitoring, width=2, height=1, bg='yellow', command=montopred)
    b3.grid(row=2,column=1, sticky=SE)

    monitoring.mainloop() 
    
    

def SaveFile():
    filename = filedialog.asksaveasfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Save file", 
        filetypes=(("XLSX", "XLSX"), ("CSV", "CSV")))
    ForSavep.to_excel(str(filename)+".xlsx", sheet_name="Info")
    
def loadd():
    global ws
    ws = Tk()
    ws.title("Загрузить данные")
    ws.geometry("400x250")
    Button(ws, text="Открыть файл", command=OpenFile).place(x=200, y=80, anchor="c", width=280, height=40)
    
    Button(ws, text="Сохранить файл", command=SaveFile).place(x=200, y=160, anchor="c", width=280, height=40)
    
    ws.mainloop()    


def vistomon():
    global vis
    vis = 1
    monitoringf()
def montovis():
    global moni
    moni = 1
    visualf()
def vistoana():
    global vis
    vis = 1
    analysf()
def montoana():
    global moni
    moni = 1
    analysf()
def anatomon():
    global analy
    analy = 1
    monitoringf()
def anatovis():
    global analy
    analy = 1
    visualf()
def vistopred():
    global vis
    vis=1
    prediction()
def montopred():
    global moni
    moni=1
    prediction()
def anatopred():
    global analy
    analy=1
    prediction()
def predtovis():
    global pred
    pred=1
    visualf()
def predtomon():
    global pred
    pred=1
    monitoringf()
def predtoana():
    global pred
    pred=1
    analysf()

def convert_to_datetime(input_str, parserinfo=None):
    return parse(input_str, parserinfo=parserinfo)
def date_range(start,stop,value):
    global Meteor
    f2 = open("Info.csv")
    A = f2.readlines()
    for i in range(len(A)):
        A[i] = A[i].strip()
        
    y = A.index(combobo.get())  
    i = info.index(value)
    f1 = open(str(Meteor[i][1])+".dat")
    C = {}
    fig, ax = plt.subplots()
    for i in f1:
        i = i.split()
        d = str(i[1]) + "-" + str(int(i[2])//10) + str(int(i[2])%10) + "-" + str(int(i[3])//10) + str(int(i[3])%10)
        d = convert_to_datetime(d)
        if start <= d.date() <= stop:
            if d.date() in C:
                C[d.date()] += [float(i[y])]
            else:
                C[d.date()] = [float(i[y])]
        if d.date() > stop:
            break
    for x in C:
        C[x] = sum(C[x]) // len(C[x])
    a = list(C.keys())
    for i in range(len(a)):
        a[i] = a[i].day
    a = tuple(a)    
    b = list(C.values())
    ax.set_xlabel("Даты")
    ax.set_ylabel("Значения")  
    ax.pie( b, labels=a, autopct='%1.1f%%')
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=visual)
    canvas.draw()
    canvas.get_tk_widget().place(x=300, y=300, anchor="c", width=500, height=600)  

def date_range2(start,stop,value):
    global Meteor
    f2 = open("Info.csv")
    A = f2.readlines()
    for i in range(len(A)):
        A[i] = A[i].strip()
        
    y = A.index(combobo.get())  
    i = info.index(value)
    f1 = open(str(Meteor[i][1])+".dat")
    C = {}
    fig, ax = plt.subplots()
    for i in f1:
        i = i.split()
        d = str(i[1]) + "-" + str(int(i[2])//10) + str(int(i[2])%10) + "-" + str(int(i[3])//10) + str(int(i[3])%10)
        d = convert_to_datetime(d)
        if start <= d.date() <= stop:
            if d.date() in C:
                C[d.date()] += [float(i[y])]
            else:
                C[d.date()] = [float(i[y])]
        if d.date() > stop:
            break
    for x in C:
        C[x] = sum(C[x]) / len(C[x])
    a = list(C.keys())
    for i in range(len(a)):
        a[i] = a[i].day
    a = tuple(a)
    b = list(C.values())
    fig, ax = plt.subplots()
    df2 = pd.DataFrame(b, index=a)
    ax= sns.lineplot(data=df2, markers= True)
    ax.set(xlabel='Даты', ylabel='Значения', title=value) 
    canvas = FigureCanvasTkAgg(fig, master=visual)
    canvas.draw()
    canvas.get_tk_widget().place(x=300, y=300, anchor="c", width=500, height=600)    
    
def visualf():
    global pred, visual, date1, date2, info, combobox, monitoring, moni, vis, combobo, Meteor, info, analy, Analytics, Prediction
    if moni == 1:
        monitoring.withdraw()
        moni = 0
    if analy == 1:
        Analytics.withdraw()
        analy = 0
    if pred == 1:
        Prediction.withdraw()
        pred = 0
    
    f = open("Vs.csv")
    Meteor = []
    info = []
    for x in f:
        x = x.split(";")
        Meteor.append(x)
        info.append(x[0])
    visual = Tk()
    visual.title("Визуализация")
    visual.geometry("800x600")
    
    
    combobox = ttk.Combobox(visual,values=info)
    combobox.place(x=640, y=230, anchor="c", width=120, height=30)
    
    date1 = tkcalendar.DateEntry(visual)
    date1.place(x=640, y=80, anchor="c", width=120, height=40)
    
    date2 = tkcalendar.DateEntry(visual)
    date2.place(x=640, y=150, anchor="c", width=120, height=40)
    
    
    Button(visual,text='Линейная',command=lambda: date_range2(date1.get_date(),date2.get_date(),combobox.get())).place(x=640, y=440, anchor="c", width=120, height=50)
    Button(visual,text='Круговая',command=lambda: date_range(date1.get_date(),date2.get_date(),combobox.get())).place(x=640, y=370, anchor="c", width=120, height=50)    
    info1=["Температура воздуха по спирту минимального термометра","Средняя скорость ветра","Сумма осадков за период между сроками","Относительная влажность воздуха","Атмосферное давление на уровне моря"]
    filew=Label(visual, text="Параметр")
    filew.place(x=640, y=270, anchor="c")  
    combobo = ttk.Combobox(visual,values=info1)
    combobo.place(x=640, y=300, anchor="c", width=120, height=30)
    
    filewo=Label(visual, text="Город")
    filewo.place(x=640, y=200, anchor="c")  
    b1=Button(visual, width=2, height=1, bg='lightblue', command=vistoana)
    b1.place(x=750, y=180)
    b2=Button(visual, width=2, height=1, bg='yellow', command=vistopred)
    b2.place(x=750, y=230)
    b3=Button(visual, width=2, height=1, bg='orange', command=vistomon)
    b3.place(x=750, y=280)
    
    visual.mainloop()


def mainmenuf():
    global exitf, mainmenu, login
    login.withdraw()
    mainmenu=Tk()
    mainmenu.geometry('1920x1080')
    mainmenu.title("Главное меню")

    im1 = ImageTk.PhotoImage(master=mainmenu, file="analysis.png")
    im2 = ImageTk.PhotoImage(master=mainmenu, file="visual.png")
    im3 = ImageTk.PhotoImage(master=mainmenu, file="forecast.png")
    im4 = ImageTk.PhotoImage(master=mainmenu, file="mon.png")
    im5 = ImageTk.PhotoImage(master=mainmenu, file="files.png")
    exit=Button(mainmenu, text="Выход", width=10, height=2, bg='red', command=exitf)
    exit.pack(side=BOTTOM, anchor=SE, padx=40, pady=20)
    filework=Button(mainmenu, text="Загрузить данные", image=im5, command=loadd)
    filework.pack(side=TOP, anchor=NW, padx=40, pady=20)
    but1=Button(mainmenu, image=im1, command=analysf)
    but1.pack(side=LEFT,padx=[620, 15])
    but2=Button(mainmenu, image=im2, command=visualf)
    but2.pack(side=LEFT,padx=[0, 15])
    but3=Button(mainmenu, image=im3, command=prediction)
    but3.pack(side=LEFT,padx=[0, 15])
    but4=Button(mainmenu, image=im4, command=monitoringf)
    but4.pack(side=LEFT,padx=[0, 0])
    sim=Button(mainmenu, text="Симуляция", width=15, height=2, bg='purple', command=simulation)
    sim.pack(side=BOTTOM, anchor=SE, padx=40)

    mainmenu.mainloop()

def exitf():
    mainmenu.withdraw()

def upload():
    global tt2, t, CustomData
    if t==0:
        CustomData=[]
    CustomData.append([])
    CustomData[tt2].append(int(e1.get()))
    CustomData[tt2].append(int(e2.get()))
    CustomData[tt2].append(int(e3.get()))
    CustomData[tt2].append(int(e4.get()))
    CustomData[tt2].append(float(e5.get()))
    CustomData[tt2].append(float(e6.get()))
    CustomData[tt2].append(int(e7.get()))
    CustomData[tt2].append(float(e8.get()))
    tt2=tt2+1
    if t ==0:
        Label(Simulation,text="Сохранено", font=("Arial", 7)).pack()
    t=1
    
def simulation():
    global e1, e2, e3, e4, e5, e6, e7, e8, Simulation
    Simulation=Tk()
    Simulation.title("Симуляция")
    Simulation.geometry("250x530")

    Label(Simulation,text="Год", font=("Arial", 12)).pack()
    e1=Entry(Simulation, font=("Arial", 12))
    e1.pack()
    Label(Simulation,text="Месяц", font=("Arial", 12)).pack(pady=[10,0])
    e2=Entry(Simulation, font=("Arial", 12))
    e2.pack()
    Label(Simulation,text="День", font=("Arial", 12)).pack(pady=[10,0])
    e3=Entry(Simulation, font=("Arial", 12))
    e3.pack()
    Label(Simulation,text="Скорость ветра", font=("Arial", 12)).pack(pady=[10,0])
    e4=Entry(Simulation, font=("Arial", 12))
    e4.pack()
    Label(Simulation,text="Сумма осадков", font=("Arial", 12)).pack(pady=[10,0])
    e5=Entry(Simulation, font=("Arial", 12))
    e5.pack()
    Label(Simulation,text="Температура", font=("Arial", 12)).pack(pady=[10,0])
    e6=Entry(Simulation, font=("Arial", 12))
    e6.pack()
    Label(Simulation,text="Влажность", font=("Arial", 12)).pack(pady=[10,0])
    e7=Entry(Simulation, font=("Arial", 12))
    e7.pack()
    Label(Simulation,text="Атмосферное давление", font=("Arial", 12)).pack(pady=[10,0])
    e8=Entry(Simulation, font=("Arial", 12))
    e8.pack()
    Button(Simulation,text="Загрузить", font=("Arial", 15),command=upload).pack(pady=[20,10])
    Simulation.mainloop()

def check():
    global v, fals
    LOG=open("Vs.csv")
    log = []
    for x in LOG:
        x = x.split(";")
        log.append(x)
    for i in range(len(log)):
        if logine.get()==log[i][7] and passwe.get()==log[i][8]:
            mainmenuf()
            break
    if v==1:
        fals.destroy()
    fals=Label(login,text="Неправильный логин или пароль",fg="red")
    fals.pack(pady=5)
    v=1

    
login=Tk()
login.geometry('1920x1080')
login.title("Вход")
loginl=Label(login, text="Логин", font=("Arial", 14)).pack(pady=[300,5])
logine=Entry(login)
logine.pack(pady=[0,5])
passwl=Label(login, text="Пароль", font=("Arial", 14)).pack(pady=[0,5])
passwe=Entry(login)
passwe.pack(pady=[0,5])
loginb=Button(login, text="Войти", width=10, height=1, command=check, font=("Arial", 14))
loginb.pack(pady=[0,0])
vis = 0
moni = 0
pred=0
analy=0
col1="Параметры"
col2="Данные"
list1 = []
list2 = []
ForSavep=pd.DataFrame({col1: list1, col2: list2})
t=0
tt2=0
v=0

login.mainloop()


