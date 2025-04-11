import pandas as pd
from tkinter import *
import tkinter as tk
import tkinter
from tkinter import *

import webbrowser
#from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import matplotlib.pyplot as plt
#import cv2
from PIL import ImageTk,Image
#import geopandas as gpd
import csv
import pandas as pd
##from shapely.geometry import Point
##from shapely.geometry import Polygon
##from shapely.geometry import Point, Polygon
import numpy as np
#import shapefile as shp
from itertools import islice
import pyttsx3
import requests
import time
from datetime import datetime, date, timedelta
from PIL import Image
import os
import subprocess
#import cv2
#from skimage import io
import shutil
import winsound
from winsound import Beep
from mpldatacursor import datacursor
from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl
import xlwt as xw
from xlwt import Workbook
import tkinter.font as tkFont
import numpy as np
import pyodbc
import sys
from matplotlib.widgets import Slider#, Button
from matplotlib.dates import DateFormatter
from datetime import datetime
import mplcursors
from matplotlib import image as img
import scipy.interpolate as interp
import matplotlib.ticker as ticker
import datetime
import math
import ee
import seaborn as sns
import geopandas as gpd
from bng_latlon import OSGB36toWGS84
from folium.plugins import MarkerCluster
MarkerCluster()
#import geemap

root = Tk()
root.title(" APLICACIÓN COMPUTACIONAL BASADA EN BIG DATA PARA EL USO Y ANÁLISIS DEL AGUA EN CUENCAS ACUAC)")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
#root.geometry("1500x1000")
my_canvas= Canvas(root, width = 3900, height=1000)
my_canvas.pack(fill ="both", expand= True)

##bgARIDH=PhotoImage(file='ESTADOS_RH\RH36.png')
bgARIDH=PhotoImage(file='IMAGEN_ENTRADA.png')
#bgARIDH=PhotoImage(file='ANIMATION_WATERSHED.gif')
LALO2=my_canvas.create_image(400,300,anchor=NW,image=bgARIDH)
NDVI_Q=PhotoImage(file='NDVI_Q.png')
INIFAP=PhotoImage(file="LOGO_INIFAP.png")
LALO=my_canvas.create_image(10,10,anchor=NW,image=INIFAP)
#my_canvas.configure(bg='light blue')
t=my_canvas.create_text(630,200, text="APLICACION COMPUTACIONAL PARA EL USO Y ANALISIS DEL AGUA EN CUENCAS (ACUAC)",fill="blue", font='sans 20 bold')
for m in range (36):
        time.sleep(0.1)
        my_canvas.move(LALO,36,20)
        my_canvas.update()
my_canvas.delete(LALO)
my_canvas.delete(t)

##converter = pyttsx3.init()
##converter.setProperty('rate', 150)
##converter.say("BUEN DÍA Y BIENVENIDO AL PORTAL INTERACTIVO HIDROLÓGICO DEL INIFAP")
##converter.runAndWait()

IMGN_INICIO=PhotoImage(file='IMAGEN_INICIO.png', master=root)
INIFAP=PhotoImage(file="LOGO_INIFAP.png")
bg2=PhotoImage(file="RH.png")
#bgARIDH=PhotoImage(file='RH36.png', master=root)
bgARIDH=PhotoImage(file='ESTADOS_RH\RH36.png', master=root)
#bgARIDH2=PhotoImage(file='RH24.png', master=root)
bgARIDH2=PhotoImage(file='ESTADOS_RH\RH24.png', master=root)
#bgARIDH3=PhotoImage(file='RH20.png', master=root)
bgARIDH3=PhotoImage(file='ESTADOS_RH\RH20.png', master=root)
#bgARIDH4=PhotoImage(file='RH37.png', master=root)
bgARIDH4=PhotoImage(file='ESTADOS_RH\RH37.png', master=root)
#bgARIDH5=PhotoImage(file='RH26.png', master=root)
bgARIDH5=PhotoImage(file='ESTADOS_RH\RH26.png', master=root)
bgARIDH6=PhotoImage(file='ESTADOS_RH\RH35.png', master=root)
bgARIDH7=PhotoImage(file='ESTADOS_RH\RH17.png', master=root)
bgARIDH8=PhotoImage(file='ESTADOS_RH\RH21.png', master=root)
bgARIDH9=PhotoImage(file='ESTADOS_RH\RH10.png', master=root)
bgARIDH10=PhotoImage(file='ESTADOS_RH\RH8.png', master=root)
bgARIDH11=PhotoImage(file='ESTADOS_RH\RH9.png', master=root)
bgARIDH12=PhotoImage(file='ESTADOS_RH\RH34.png', master=root)
bgARIDH13=PhotoImage(file='ESTADOS_RH\RH4.png', master=root)
bgARIDH14=PhotoImage(file='ESTADOS_RH\RH25.png', master=root)
bgARIDH15=PhotoImage(file='ESTADOS_RH\RH18.png', master=root)
bgARIDH16=PhotoImage(file='ESTADOS_RH\RH12.png', master=root)
bgARIDH17=PhotoImage(file='ESTADOS_RH\RH27.png', master=root)
bgARIDH18=PhotoImage(file='ESTADOS_RH\RH28.png', master=root)
bgARIDH19=PhotoImage(file='ESTADOS_RH\RH29.png', master=root)
bgARIDH20=PhotoImage(file='ESTADOS_RH\RH30.png', master=root)
bgARIDH21=PhotoImage(file='ESTADOS_RH\RH5.png', master=root)
bgARIDH22=PhotoImage(file='ESTADOS_RH\RH6.png', master=root)
bgARIDH23=PhotoImage(file='ESTADOS_RH\RH7.png', master=root)
bgARIDH24=PhotoImage(file='ESTADOS_RH\RH11.png', master=root)
bgARIDH25=PhotoImage(file='ESTADOS_RH\RH13.png', master=root)
bgARIDH26=PhotoImage(file='ESTADOS_RH\RH14.png', master=root)
bgARIDH27=PhotoImage(file='ESTADOS_RH\RH15.png', master=root)
bgARIDH28=PhotoImage(file='ESTADOS_RH\RH16.png', master=root)
bgARIDH29=PhotoImage(file='ESTADOS_RH\RH19.png', master=root)
bgARIDH30=PhotoImage(file='ESTADOS_RH\RH22.png', master=root)
bgARIDH31=PhotoImage(file='ESTADOS_RH\RH23.png', master=root)
bgARIDH32=PhotoImage(file='ESTADOS_RH\RH31.png', master=root)
bgARIDH33=PhotoImage(file='ESTADOS_RH\RH32.png', master=root)
bgARIDH34=PhotoImage(file='ESTADOS_RH\RH33.png', master=root)
bgARIDH35=PhotoImage(file='ESTADOS_RH\RH1.png', master=root)
bgARIDH36=PhotoImage(file='ESTADOS_RH\RH2.png', master=root)
bgARIDH37=PhotoImage(file='ESTADOS_RH\RH3.png', master=root)

suelo=ImageTk.PhotoImage(Image.open("CUENCA2.png"))

#######################################################
#BOTONES DE LAS APLICACIONES DEL PROGRAMA
#######################################################
REG_HYDR_IMG=PhotoImage(file='REG_HYDR_BUTTON.png', master=root)
HYDR_IMG=PhotoImage(file='HIDROLOGIA_BUTTON.png', master=root)
CLIMA_IMG=PhotoImage(file='WEATHER_BUTTON.png', master=root)
INICIO_IMG= PhotoImage(file='INICIO.png', master=root)
COMPLE_IMG = PhotoImage(file='COMPLE_BUTTON.png', master=root)
MSJ2=PhotoImage(file='FI.png', master=root)
GEE_IMG=PhotoImage(file='GEE_BUTTON.png', master=root)
EROSION_IMG=PhotoImage(file='EROSION_BUTTON.png', master=root)
CAMBIO_IMG=PhotoImage(file='CC_BUTTON.png', master=root)
AGRIC_IMG =PhotoImage(file='AGR_BUTTON.png', master=root)
DISTRITOS_IMG=PhotoImage(file='DR_IMG.png', master=root)
CUENCA2= my_canvas.create_image(600,250, image= IMGN_INICIO)
INI=my_canvas.create_image(1100,40,image=INIFAP)
#DSS1= PhotoImage(file='DSS.png', master=root)
BALANCE_S= PhotoImage(file='SWB.png', master=root)
LIBRO=PhotoImage(file='BOOK.png', master=root)
COMPUTER=PhotoImage(file='COMPU.png', master=root)
AQUIFER=PhotoImage(file='ACUIFERO.png', master=root)
QHISTORICO=PhotoImage(file='QHIST.png', master=root)
QESTOCASTICO=PhotoImage(file='QEST.png', master=root)
PELIGRO=PhotoImage(file='WARNING.png', master=root)
APARATOSN=PhotoImage(file='APARATO.png', master=root)
TIME=PhotoImage(file='REAL_TIME.png', master=root)
FACILITATOR= PhotoImage(file='DEC.png', master=root)
CURVA_NORMAL= PhotoImage(file='NORMAL.png', master=root)
INFORMACION= PhotoImage(file='INFORMATION.png', master=root)
EFECTOS_TEMP= PhotoImage(file='EFECTOS.png', master=root)
PRONOSTICO_CLIMA =PhotoImage(file='PRONOS.png', master=root)
IRRIGATION= PhotoImage(file='RIEGO.png', master=root)
REALTIME= PhotoImage(file='BAL_HIDRICO.png', master=root)
AYUDA_BH=PhotoImage(file='FI.png', master=root)
WEATHER=PhotoImage(file='WEATHER_BUTTON.png', master=root)
Credito=PhotoImage(file="Creditosn.png", master=root)
FORZA =PhotoImage(file='Forcings.png')#, master=root2)
ARTIFICIAL = PhotoImage(file="ART_INT.png")
GEE1_IMG = PhotoImage(file="GEE_CUENCAS.png")
GEE2_IMG = PhotoImage(file="GEE_ET.png")
SOC_ASPECT= PhotoImage(file="SOCIAL.png")
BODIES= PhotoImage(file="CUERPOS.png")
BODIES2=PhotoImage(file="CUERPOS2.png")

Font_tuple2=("Comic Sans MS", 10, "bold")
Font_tuple1=("Comic Sans MS", 7, "bold")
Font_tuple3=("Comic Sans MS", 12, "bold")
Font_tuple4=("Comic Sans MS", 14, "bold")
def read():
    global NAME
    global ESTADO
    print(NUM_CUENC.get())
    CUENCA=NUM_CUENC.get()
    NAME=NUM_CUENC.get()#"Presa Lazaro Cardenas"
    my_canvas.delete(ibis30)
    SUBC['state'] = "normal"
    
def func():
    global ESTADO
    ESTADO="dgo"
    
    webbrowser.open_new("http://189.194.30.186:8081/MuestraImagen.aspx?ID=35&PA=OT")
def func2():
    global ESTADO
    ESTADO="zac" 
def func3():
    global ESTADO
    ESTADO="gro"
def func4():
    global ESTADO
    ESTADO="coah"
def func5():
    global ESTADO
    ESTADO="slp"
def func6():
    global ESTADO
    ESTADO="chih"
def func7():
    global ESTADO
    ESTADO="mich"
def func8():
    global ESTADO
    ESTADO="oax"
def func9():
    global ESTADO
    ESTADO="nl"
def func10():
    global ESTADO
    ESTADO="tams"
def func11():
    global ESTADO
    ESTADO="sin"
def func12():
    global ESTADO
    ESTADO="son"
def func13():
    global ESTADO
    ESTADO="nl"
def func14():
    global ESTADO
    ESTADO="bc"
    print(ESTADO)
def func15():
    global ESTADO
    ESTADO="mex"
def func16():
    global ESTADO
    ESTADO="gto"
def func17():
    global ESTADO
    ESTADO="jal"
def func18():
    global ESTADO
    ESTADO="ags"
def func19():
    global ESTADO
    ESTADO="pue"
def func20():
    global ESTADO
    ESTADO="df"
def func21():
    global ESTADO
    ESTADO="ver"
def func22():
    global ESTADO
    ESTADO="hgo"
def func23():
    global ESTADO
    ESTADO="tab"
def func24():
    global ESTADO
    ESTADO="camp"
def func25():
    global ESTADO
    ESTADO="bcs"
def func26():
    global ESTADO
    ESTADO="nay"
def func27():
    global ESTADO
    ESTADO="col"
def func28():
    global ESTADO
    ESTADO="chis"
def func29():
    global ESTADO
    ESTADO = "yuc"
def func30():
    global ESTADO
    ESTADO = "qroo"

def borrar_balncehidrico():
         #LONGI=LONGI_1
         HELP_BH.destroy()
         HELP_BH_LBL.destroy()
         LATI.destroy()
         LATI_LBL.destroy()
         ANUNCIO.destroy()
         #LONGI_LBL.destroy()
         INICIO.destroy()
         INICIO_LBL.destroy()
         FIN.destroy()
         FIN_LBL.destroy()
         CALC_BALANCE.destroy()
         BORRA_BALANCE.destroy()
         UBICLON.destroy()
         UBICLON_LBL.destroy()
         PRONOSTICOS.destroy()
         PRONOSTICOS_LBL.destroy()
         #LONGI.destroy()
##         LONGI.delete(0,END)
def pronostica():
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.say("SE PRESENTA LA VARIACIÓN HORARIA DE LA EVAPOTRANSPIRACIÓN ACTUAL Y EL CONTENIDO DE HUMEDAD DEL SUELO PARA LOS PRÓXIMOS SIETE DÍAS PARA LA CUENCA SELECCIONADA.\n\
        POSTERIORMENTE, SE PRESENTA LA VARIACIÓN DIARIA")
        
        converter.runAndWait()
        #x2=("https://api.open-meteo.com/v1/forecast?latitude=16.5&longitude=93&hourly=temperature_2m&daily=temperature_2m_max,rain_sum,precipitation_probability_max,et0_fao_evapotranspiration&timezone=auto")
        #x2=("https://api.open-meteo.com/v1/forecast?latitude=16.5&longitude=93&daily=temperature_2m_max,temperature_2m_min,rain_sum,et0_fao_evapotranspiration&timezone=auto")
        x2=("https://api.open-meteo.com/v1/dwd-icon?latitude=25&longitude=103&daily=temperature_2m_max,temperature_2m_min,rain_sum,et0_fao_evapotranspiration&timezone=auto")

        x3=("https://api.open-meteo.com/v1/dwd-icon?latitude=23&longitude=105&hourly=evapotranspiration,soil_moisture_9_to_27cm&timezone=auto")
##        response3=requests.get(x3)
##        clima3=response3.json()

        
        new_x3= x3.replace("23",LATIT)
        new_x3_x3= new_x3.replace("105",LONGI)
        response3 =requests.get(new_x3_x3)
        clima3=response3.json()
        print('URL PARA HORAS',new_x3_x3)

        
        EVT= (clima3["hourly"]["evapotranspiration"])
        MOISTURE= (clima3["hourly"]["soil_moisture_9_to_27cm"])
        TIEMPO2 =(clima3["hourly"]["time"])
        fig,ax=plt.subplots(figsize=(10,10))
        ax2=ax.twinx()
        #ax.grid(which='both')
        ax2.tick_params('y',  color='black')#,direction="in")
        ax2.set_ylabel('HUMEDAD SUELO, (cm3.cm3)', color='blue')
        ax.set_ylabel("ETa mm.hr", color ="green")
        #tick_spacing = 2
        ax.xaxis.set_major_locator(plt.MultipleLocator(1.5))
        n = 5  # Keeps every 7th label
        [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]
        labels = TIEMPO2
        ax.set_xticklabels(labels, rotation=90)#, ha='right')
        ax.tick_params(axis='both', which='major', labelsize=5)
        GRAF1=ax.plot(TIEMPO2,EVT, color="green", label = "ETa")
        ax.legend()
        GRAF2=ax2.plot(TIEMPO2,MOISTURE, color ="blue", label ="HUMEDAD DEL SUELO")
        ax2.legend()
        
        mplcursors.cursor(GRAF1)
        mplcursors.cursor(GRAF2)
        plt.title("VARIACIÓN HORARIA DE LA EVAPOTRANSPIRACIÓN ACTUAL Y EL CONTENIDO DE HUMEDAD DEL SUELO")
        #ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.show()
        
        NEW_URL3=x2.replace("25",LATIT)
        NEW_URL4=NEW_URL3.replace("103",LONGI)
        response2 =requests.get(NEW_URL4)
        clima2 = response2.json()
        print(NEW_URL4)

        TEMPMAX= (clima2["daily"]["temperature_2m_max"])
        TEMPMIN= (clima2["daily"]["temperature_2m_min"])
        LLUVIA = (clima2["daily"]["rain_sum"])
        #PP_PROB =(clima2["daily"]["precipitation_probability_max"])
        ETO = (clima2["daily"]["et0_fao_evapotranspiration"])
        TIEMPO= (clima2["daily"]["time"])
        print(TIEMPO)
        column1=["TEMPMAX"]#,"LLUVIA",'ETO',"TEMPMIN", "TEMPMAX","TIEMPO"]
        column2=["LLUVIA"]
        column4=["ETO"]
        column5=["TEMPMIN"]
        column6=["TIEMPO"]
        df1=pd.DataFrame(TEMPMAX,columns=column1)
        df2=pd.DataFrame(LLUVIA,columns=column2)
        #df3=pd.DataFrame(PP_PROB)
        df4=pd.DataFrame(ETO,columns=column4)
        df5=pd.DataFrame(TEMPMIN,columns=column5)
        df6=pd.DataFrame(TIEMPO,columns=column6)
        

        with pd.ExcelWriter("PRONOSTICO.xlsx", engine = "openpyxl")as writer:
            #df.to_excel(writer)
            df1.to_excel(writer,startcol=1, startrow=1, header=True,index=False)#TEMPMAX
            df2.to_excel(writer,startcol=2, startrow=1, header=True,index=False)#8 LLUVIA
            #df3.to_excel(writer,startcol=3, startrow=1, header=True,index=False)#5 PP_PROB
            df4.to_excel(writer,startcol=4, startrow=1, header=True,index=False)#5 ETO
            df5.to_excel(writer,startcol=5, startrow=1, header=True,index=False)#5 #TEMPMIN
            df6.to_excel(writer,startcol=6, startrow=1, header=True,index=False)#5 #TIEMPO
            
        
        df3= pd.read_excel('PRONOSTICO.xlsx',engine='openpyxl', header =None)
##        plt.plot(TIEMPO, ETO)
##        plt.plot(TIEMPO, TEMPMIN)
##        plt.plot(TIEMPO, TEMPMAX)
##        plt.plot(TIEMPO, LLUVIA)
##        plt.xticks(rotation=90)
##        plt.show()

        
        fig,ax=plt.subplots(figsize=(10,10))
        ax2=ax.twinx()
        ax.grid(which='both')
        ax2.tick_params('y',  color='black')#,direction="in")
        ax2.set_ylabel('ETo, (mm)', color='black')
##        ax3.tick_params('y', labelsize=7, pad= -18, colors='blue',direction="in")
##        ax3.set_ylabel('PRECIPITACION (mm)',color='blue')
        plt.title("PRONÓSTICO DE VARIABLES DE BALANCE PARA LOS PRÓXIMOS SIETE DÍAS")
        plt.suptitle("DE CLICK EN CUALQUIER LÍNEA PARA DESPLEGAR EL DATO")

        #date_form = DateFormatter("%Y-%m-%b")
        
        #date_form = DateFormatter("%m")
        #ax.xaxis.set_major_formatter(date_form)
        index1 = ['DIA 1','DIA 2','DIA 3','DIA 4','DIA 5','DIA 6', 'DIA 7']
        GRAFICA1= ax.plot(TIEMPO,TEMPMAX,label = "TEMPMAX (°C)", color ='green')
        GRAFICA4= ax.plot(TIEMPO,TEMPMIN,label = "TEMPMIN (°C)", color ='red')
        ax.set_ylabel("TEMPERATURA °C\n PRECIPITACION (mm)",color ='green')
        ax.set_xlabel("FECHA POSTERIOR AL DÍA ACTUAL")
        GRAFICA2=ax.bar(TIEMPO,LLUVIA,label ="PRECIPITACION (mm)")
        ##plt.plot(df3,label="PROBABILIDAD LLUVIA")
        GRAFICA3=ax.plot(df4, color ='black', label ="ETo")
        #GRAFICA6 =ax2.plot(df6,df4, color ='black', label ="ETo")
        
        MINIMO1 =df5.min()
        MINIMO =MINIMO1.to_string(index=False)
        MAXIMO1 =df1.max()
        MAXIMO =MAXIMO1.to_string(index=False)
        PRECIP1 = df2.sum()
        PRECIP = PRECIP1.to_string(index=False)
        ax.legend()
        #plt.legend()
        #ax2.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5))
        #ax3.legend(bbox_to_anchor =(0.35, 1.15), ncol = 5)
        mplcursors.cursor(GRAFICA1)
        mplcursors.cursor(GRAFICA2)
        mplcursors.cursor(GRAFICA3)
        mplcursors.cursor(GRAFICA4)
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.say("EL VALOR MAXIMO DE TEMPERATURA ES "+str(MAXIMO)+str('EL VALOR MÍNIMO ES '+str(MINIMO))+str("GRADOS CENTÍGRADOS")+str('LA PRECIPITACION TOTAL ES'+str(PRECIP)+str("MILÍMETROS")))
        converter.runAndWait()
        plt.show()
        
def CALC_BALANCE_HIDR():
    global LONGI
    global LATI
    global FI_1
    global FF
    global FF_1
    global LATIT
    global LATIT_1
    global LONGI_1
    global UBICLON
    global PRONOSTICOS
    global PRONOSTICOS_LBL
    global clima
    
    PRONOSTICOS = Button(top, command= pronostica,image =WEATHER)
    PRONOSTICOS.place(x= 590, y=390)
    PRONOSTICOS_LBL =Label(top, text= "PRONOSTICO",font= Font_tuple1,fg="blue")
    PRONOSTICOS_LBL.place( x=580, y=370)
    FI_1 = INICIO.get()
    FI = str(FI_1)
    FF_1 = FIN.get()
    FF = str(FF_1)
    LATIT_1 = LATI.get()
    LATIT =str(LATIT_1)
    LONGI_1 =UBICLON.get()
    LONGI = str(LONGI_1)
##    LONGI_1 = LONGI.get()
##    LONGI =str(LONGI_1)
    
    #print(LONGI)
   
    #x =("https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=1950-01-01&end_date=2050-12-31&models=MRI_AGCM3_2_S&daily=temperature_2m_mean,precipitation_sum,et0_fao_evapotranspiration_sum")
    x =("https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=1950-01-01&end_date=2050-12-31&models=MRI_AGCM3_2_S&disable_bias_correction=false&daily=temperature_2m_mean,precipitation_sum,soil_moisture_0_to_10cm_mean,et0_fao_evapotranspiration_sum")
    #x=("https://api.open-meteo.com/v1/forecast?latitude=23&longitude=125&hourly=temperature_2m&daily=temperature_2m_max,rain_sum,precipitation_probability_max,et0_fao_evapotranspiration&timezone=auto")

    

    
    NEW_URL =x.replace("1950-01-01",FI)
    NEW_URL2=NEW_URL.replace("2050-12-31",FF)
    
    NEW_URL3=NEW_URL2.replace("52.52",LATIT)
   
    NEW_URL4=NEW_URL3.replace("13.41",LONGI)

    #print(NEW_URL4)
    response =requests.get(NEW_URL4)
    clima = response.json()
    #print(clima)
    LLUVIA= (clima["daily"]["precipitation_sum"])
    TIEMPO= (clima["daily"]["time"])
    ETO=(clima["daily"]["et0_fao_evapotranspiration_sum"])#et0_fao_evapotranspiration_sum
    TEMP=(clima["daily"]["temperature_2m_mean"])
    #TEMP=(clima["daily"]["temperature_2m_max"])
    SOIL=(clima["daily"]["soil_moisture_0_to_10cm_mean"])#soil_moisture_0_to_10cm_mean
    print(SOIL)
    df=pd.DataFrame(LLUVIA)
    df2=pd.DataFrame(TIEMPO)
    df4=pd.DataFrame(ETO)
    df5=pd.DataFrame(TEMP)
    df6BAL=df-df4#df+(df-df4)
    print("balance -->",df6BAL)
    #df8()
    column4=["TIEMPO"]
    #df2=pd.DataFrame(TIEMPO,columns=column4)
    #df7=pd.DataFrame(SOIL)
    #colnames=['PP','FECHA','ETO', 'TMED', 'BALANCE']
    with pd.ExcelWriter("output.xlsx", engine = "openpyxl")as writer:
            df.to_excel(writer,startcol=1, startrow=1, header=True,index=False)
            df.to_excel(writer,startcol=3, startrow=1, header=True,index=False)#PRECIPITACION
            df2.to_excel(writer,startcol=4, startrow=1, header=True,index=False)#8 FECHA
            df4.to_excel(writer,startcol=5, startrow=1, header=True,index=False)#5 ETO
            df5.to_excel(writer,startcol=6, startrow=1, header=True,index=False)#10 TEMPERATURA
            df6BAL.to_excel(writer,startcol=7, startrow=1, header=True,index=False)#11 BALANCE df6BAL
            #df7.to_excel(writer,startcol=12, startrow=1, header=True,index=False)
    df3= pd.read_excel('output.xlsx',engine='openpyxl', header =None)

    
            
##    with pd.ExcelWriter("output3.xlsx", engine = "openpyxl")as writer:
##            #df.to_excel(writer)
##            df2.to_excel(writer,startcol=3, startrow=1, header=True,index=False)#TIEMPO
##            df.to_excel(writer,startcol=4, startrow=1, header=True,index=False)#PP
##    df15=pd.read_excel('output3.xlsx',engine='openpyxl', header =None)
##    pd.to_datetime(df[df15[3],df15[4]],format='ISO 8601')
##    plt.plot(df[df15[3],df15[4]])
##    plt.show()
   ######################################
    balance = 0
    LULA=df3.iloc[:,3]
    LULA2 = LULA.astype(float)
    LULA_BIS=df3.iloc[:,7]
    LULA_BIS_2 =LULA_BIS.astype(float)
    LULAETO=df3.iloc[:,5]
    LULAETO2 = LULAETO.astype(float)
    cont=1
    k=1
    j=1
    balance1 =0
    balance2 = 0
##    print('lula', LULA)
##    for i in df3.index:
##            balance = ((LULA_BIS_2[cont-1])+(LULA2[cont]-LULAETO2[cont]))
##            cont = cont +1
##            df9=pd.DataFrame(df3)
##            with pd.ExcelWriter("output3.xlsx", engine = "openpyxl")as writer:
##                    aula =df9.to_excel(writer,startcol=1, startrow=1, header=True,index=False)
                    
##                    print(aula)
##                    balance2= df8
##            df8= pd.read_excel('output2.xlsx',engine='openpyxl', header =None)
            #print(LULA_BIS_2[cont-1], LULA2[cont],LULAETO2[cont], balance)
    
    for i in range,(len (df3)):
            for j in range,(len(LULA_BIS)):
                            balance = balance2
                            for k in range,(len(LULAETO2)):
                                    balance=((LULA_BIS_2[cont-1])+(LULA2-LULAETO2))
                                    
                                    cont=cont+1
                                    print('cont ',cont)
                                    df8=pd.DataFrame(balance)
                                    with pd.ExcelWriter("output2.xlsx", engine = "openpyxl")as writer:
                                            df8.to_excel(writer,startcol=11, startrow=0, header=True,index=False)
                                            #cont=cont+1
                                           
                                            balance2= df8      
                                    df8= pd.read_excel('output2.xlsx',engine='openpyxl', header =None)
                            
   ########################################         
    fig,ax=plt.subplots(figsize=(15,10))
    ax2=ax.twinx()
    ax.grid(which='both')
    ax3=ax.twinx()
##    datos2=pd.DataFrame(df3[1],df3[9])
##    res=(df3[9].pct_change()*100)
##    print(res)
##    datos =df3[1]
##    df20=pd.DataFrame(datos)
##    print(df20.sub(15))
    
    
    #date_form = DateFormatter("%Y-%m")#-%b")
    #date_form = DateFormatter("%m")
    #ax.xaxis.set_major_formatter(date_form)
    ax.set_ylabel("ETO -- TMED")
    ax.set_xlabel("DIA")
    ax.set_ylabel("PRECIPITACION mm", color ="blue")
    ax3.set_ylabel("BALANCE mm (Q = PP-ETo)", color="brown")
    #ax.xaxis.set_major_locator(mdates.DayLocator(interval=20))

    print(df3.columns.values)
    #column6=["TEMPMAX"]#,"LLUVIA",'ETO',"TEMPMIN", "TEMPMAX","TIEMPO"]
    column3=["LLUVIA"]
    column5=["ETO"]
    column6=["TEMP"]
    column4=["TIEMPO"]
    
    x1=df3[4]#FECHA 4
    y1=df3[1]#LLUVIA 1
    y2=df3[5]#ETO 5
    y3=df3[6]#TEMPERATURA 6
    y5=df8[11]#HUMEDAD
    y4=df6BAL#BALANCE

    sumapp=df3[[1]].sum()
    sumapp2=sumapp.astype(float)
    media1 = df3[[1]].mean()
    media=media1.to_string(index=False)#para evitar que escriba el data type
    maximo1 =df3[[5]].max()
    maximo =maximo1.to_string(index=False)
    DESVIACION1 = df3[[1]].std()
    DESVIACION=DESVIACION1.to_string(index=False)
    suel_min1=df8[[11]].min(axis=0, skipna=True, numeric_only=False)
    #suel_min1=df6BAL[[7]].min
    
    SUELO_MIN = suel_min1.to_string(index=False)
    if float(SUELO_MIN) < float (0):
            SUELO_MIN=0
    suel_max1=df8[[11]].max()
    #suel_max1=df6BAL[[7]].max
    SUELO_MAX=suel_max1.to_string(index=False)
    TOTAL1= df3[[1]].sum()
    TOTAL = TOTAL1.to_string(index=False)
    TOTAL_BALANCE=df3[[7]].sum()
    
    TOTAL_ETo= df3[[5]].sum()
    TOTAL_ETo2=TOTAL_ETo.astype(float)
    BAL_GLOBAL= sumapp - TOTAL_ETo
    print("el balance total es  ", BAL_GLOBAL)
    
    #plt.plot(df, linewidth=0.1,color='red')
##    ax = bar_plot.set_index(bar_plot.dt.map(lambda s: s.strftime('%y-%m-%b')))\
##    .plot.bar(x1,y1, legend=False, title='Open & Close Rates', rot=0,
##    color=['orange', 'green']) 

    
    tick_spacing = 1
    line4=ax.bar(x1.index.values,y1,linewidth=0.3,color='blue',label = "PRECIPITACION (mm)")#x1.index.values,
    ax.set_ylabel("PRECIPITACION mm")
    ax.tick_params('y', labelsize=7, pad= 18, colors='blue')
    
    line1=ax2.plot(y2,linewidth=0.15,color='red',label = "ETO (mm)")
    ax2.tick_params('y', labelsize=7, pad= -18, colors='red', direction="in")
    ax2.set_ylabel('ETO (mm)',color='brown')
    ax2.legend()
    line3=ax.plot(y3,linewidth=0.3,color='black',label = "TEMPERATURA MED(°C)")
    line2=ax3.plot(y5, linewidth=0.8, color='brown', label ="PRECIPITACION EN EXCESO (mm)")#,location="inside")
    ax3.tick_params('y', labelsize=7, pad= 18, colors='red')#, direction="in")
    plt.title("BALANCE HÍDRICO EN CUENCAS")
    plt.suptitle("DATOS ALMACENADOS EN EL ARCHIVO: OUTPUT.xlsx")
##    ax3.plot(y4, linewidth=0.8, color='black', label ="BALANCE (mm)")#,location="inside")
##    ax.plot(x1.index.values,y5,linewidth=0.5, color='black', label ="HUMEDAD SUELO (mm)")
##    ax.tick_params('y', labelsize=9, pad= 14, colors='black')#, direction="in")
    #ax.legend(bbox_to_anchor =(0.75, 1.15), ncol = 2)
    mplcursors.cursor(line2)
    mplcursors.cursor(line1)
    mplcursors.cursor(line4)
    mplcursors.cursor(line3)
    #datacursor(hover=True, point_labels=df['E'])
    ax.bar = pd.to_datetime(x1,  format='mixed')
    #plt.xticks(bar_width/2, ax.bar[x1].dt.strftime('%by-%m-%d'))
    #plt.show()
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("LA MEDIA DE PRECIPITACION DIARIA ES ,"+str((media))+str('milimetros'))#+str("LA DESVIACIONESTANDAR ES "+str((DESVIACION)))+str("milimetros"))
    #converter.say("EL TOTAL DE LA PRECIPITACION EN EL PERIODO SEÑALADO ES, "+str(TOTAL)+str("MILÍMETROS"))
    converter.say("EL MÁXIMO VALOR DE EVAPOTRANSPIRACIÓN POTENCIAL ES,"+str(maximo)+str("milímetros"))
    converter.say("LA PRECIPITACION EN EXCESO OSCILA ENTRE" +str(SUELO_MIN) +str("y,")+str(SUELO_MAX)+str("milímetros"))
    converter.say("DE CLICK CON EL MOUSE SOBRE CUALQUIER LÍNEA DE LA GRÁFICA PARA DESPLEGAR EL DATO")
    converter.runAndWait()
    ax.legend()
    plt.show()
    
def HELPIOSA_BH():
    
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("LA PRESENTE APLICACIÓN HACE USO DE MODELOS CON DATOS REESCALADOS PARA PROVEER INFORMACIÓN CLIMÁTICA A PARTIR DE 1950 Y HASTA EL 2050.\n\
    LOS DATOS SON PROVEÍDOS A TRAVES DE UNA API, (INTERFASE DE PROGRAMACIÓN AVANZADA).\n\
    DEBE ENTENDERSE QUE EL MODELO NO PREDICE, SOLO PROVÉ DE PROYECCIONES POSIBLES.\n\
    CON LOS DATOS DE PRECIPITACIÓN Y EVAPOTRANSPIRACIÓN, SE REALIZA EL BALANCE HÍDRICO DIARIO PARA LA CUENCA DE INTERÉS.\n\
    AUXÍLIESE DE LA GRÁFICA PARA UBICAR LA CUENCA.\n\
    AL TÉRMINO DE DESPLIEGUE DE LA GRÁFICA DEL BALANCE, SE ACTIVA UN BOTÓN PARA REALIZAR UN PRONÓSTICO CLIMÁTICO BÁSICO PARA LOS PRÓXIMOS SIETE DÍAS")
    converter.runAndWait()
    #webbrowser.open("https://smn.conagua.gob.mx/es/climatologia/temperaturas-y-lluvias/mapas-diarios-de-temperatura-y-lluvia", new=1)
    
    image = img.imread("MAP2_METEO.JPG")
    plt.imshow(image)
    plt.show()

def TIEMPO_REAL():
            global UBICLON
            global UBICLON_LBL
            global LATI
            global LATI_LBL
            global LONGI
            global LONGI_LBL
            global INICIO
            global INICIO_LBL
            global FIN
            global FIN_LBL
            global CALC_BALANCE
            global BORRA_BALANCE
            global ANUNCIO
            global HELP_BH
            global HELP_BH_LBL
            
##            from matplotlib import image as img
##            image = img.imread("MAPA_CUENC_METEO.png")
##            plt.imshow(image)
##            plt.show()
            
            LATI=DoubleVar()
            LATI=Entry(top, textvariable=LATI, width=10)
            LATI.place(x=400, y=400)
            LATI_LBL=Label(top, text="LATITUD",font= Font_tuple1,fg="blue")
            LATI_LBL.place(x=400,y=370)

            UBICLON=DoubleVar()
            UBICLON=Entry(top, textvariable=UBICLON, width=10)
            UBICLON.place(x=500, y=400)
            UBICLON_LBL=Label(top, text="LONGITUD",font= Font_tuple1,fg="blue")
            UBICLON_LBL.place(x=500,y=370)

            INICIO=StringVar()
            INICIO=Entry(top, textvariable=INICIO, width=10)
            INICIO.place(x=400, y=460)
            INICIO_LBL = Label(top, text="FECHA INICIO\n (AAAA-MM-DD)",font= Font_tuple1,fg="blue")
            INICIO_LBL.place(x=390, y=425)                            

            FIN=StringVar()
            FIN=Entry(top, textvariable=FIN, width=10)
            FIN.place(x=500, y=460)
            FIN_LBL = Label(top, text="FECHA FIN\n (AAAA-MM-DD)",font= Font_tuple1,fg="blue")
            FIN_LBL.place(x=490, y=425)

            CALC_BALANCE = Button(top, text="CALCULAR" , command =CALC_BALANCE_HIDR, font= Font_tuple1,fg="blue")
            CALC_BALANCE.place(x=400, y=490)

            BORRA_BALANCE = Button(top, text= "SALIR", command =borrar_balncehidrico, font= Font_tuple1,fg="blue")
            BORRA_BALANCE.place(x=510, y=490)

            ANUNCIO=Label(top,text="INFORMACION PARA PROYECTAR EL BALANCE HIDRICO\n\
            (ELIJA UN PERIODO ENTRE 1950 - 2050)\n\
            PARA MEJOR APRECIACIÓN, ELIJA UN PERIODO MINIMO DE 5 AÑOS",font= Font_tuple1,fg="blue")
            ANUNCIO.place(x=300, y=310)

            HELP_BH = Button(top, command=HELPIOSA_BH, image=AYUDA_BH)
            HELP_BH.place(x= 470, y=270)
            HELP_BH_LBL = Label(top, text="AYUDA",font= Font_tuple1,fg="blue") 
            HELP_BH_LBL.place(x=470, y=250)
            #os.startfile("CLIMA_APLICACION\CLIMA2.exe")
def GUARDA_DATOS():
        from tkinter import filedialog, Tk
        import xlsxwriter
        import tkinter as tk
        global guardado
        global EXPLICA
        
        guardado= Label(root, text="GUARDADO EN CARPETA: CONSULTA_ESTACIONES",font= Font_tuple1,fg="blue")
        guardado.place(x=480, y=370)

        EXPLICA = Label(root, text ="\n\
                  EN LA CARPETA GUARDADA APARECEN DOS PESTAÑAS\n\
                  UNA CON LA DESCRIPCION DE LOS DATOS EN BASE DIARIA\n\
                  Y LA OTRA CON LA DE LOS DATOS EN BASE MENSUAL.\n\
                  LA INFORMACIÓN PROVIENE DEL SMN Y SE ACTUALIZAN \n\
                  CONFORME LO HAGA ESA DEPENDENCIA.",font= Font_tuple1,fg="blue")
        EXPLICA.place(x= 700, y=390)
        
        root.after(7000, lambda: EXPLICA.destroy())
        root.after(7000, lambda: guardado.destroy())
        NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios/"+str(ESTADO)+str("/")+str("dia")+str(NUM_EST.get())+str(".txt")
        New_Url3="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Mensuales/"+str(ESTADO)+str("/")+str("mes")+str(NUM_EST.get())+str(".txt")
        #Url="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/"+str("000")+str(NUM_EST.get())+ str(".TXT")
##        current_url = Url.replace("/dgo/", "/"+str(ESTADO)+str("/"))
##        #webbrowser.open_new(current_url)
##        df5 = pd.read_csv(current_url, skiprows=4,  sep='\s+',encoding='latin-1')
##        dff5=df5.reset_index(drop = True)
##        print(df5)
        
        df = pd.read_csv(NewUrl, skiprows=22,  sep='\s+',encoding='latin-1')#,index_col=0)#,header=None)
        dff=df.reset_index(drop=False)
        df=pd.DataFrame(dff,columns=['index','PRECIP','EVAP','TMAX','TMIN'])
        df = df.rename({'index': 'FECHA'},axis='columns')
        df['PRECIP'].replace({'NULO': ''}, inplace=True)
        df['EVAP'].replace({'NULO': ''}, inplace=True)
        df['TMAX'].replace({'NULO': ''}, inplace=True)
        df['TMIN'].replace({'NULO': ''}, inplace=True)
        df2 = df.drop(df[df['PRECIP'] == '(MM)'].index)
        df3= df.drop(df[df['TMAX'] == '(°C)'].index)
        df = df2.dropna()
##        df.to_excel(" "+str(NUM_EST.get())+str('.xlsx'), index=False)
        
        #ESTE=df.to_excel((NUM_EST.get())+str(".xlsx"), index=False)
        nombre=NUM_EST.get()+str(".xlsx")
        print (nombre)
        df22 = pd.read_csv(New_Url3, skiprows=22,  sep='\s+',encoding='latin-1')
##        df_22=df22.reset_index(drop=False)
##        dfff=pd.DataFrame(df_22,columns=['index','ENE','FEB','MAR','ABR'])
##        dfff['ENE'].replace({'': '0'}, inplace=True)
        
##        df22['ENE'].replace({'': '0'}, inplace=True)
##        df22['FEB'].replace({'': '0'}, inplace=True)
##        df22['MAR'].replace({'': '0'}, inplace=True)
##        df22['ABR'].replace({'': '0'}, inplace=True)
##        df22['MAY'].replace({'': '0'}, inplace=True)
##        df22['JUN'].replace({'': '0'}, inplace=True)
##        df22['JUL'].replace({'': '0'}, inplace=True)
##        df22['AGO'].replace({'': '0'}, inplace=True)
##        df22['SEP'].replace({'': '0'}, inplace=True)
##        df22['OCT'].replace({'': '0'}, inplace=True)
##        df22['NOV'].replace({'': '0'}, inplace=True)
##        df22['DIC'].replace({'': '0'}, inplace=True)
##        df22['EVAP'].replace({'NULO': ''}, inplace=True)
##        df22['TMAX'].replace({'NULO': ''}, inplace=True)
##        df22['TMIN'].replace({'NULO': ''}, inplace=True)
        
        #df.to_excel((NUM_EST.get())+str(".xlsx"), index=False)#LO GUARDA DIRECTAMENTE EN LA RAIZ
        #df.to_excel(r'CONSULTA_ESTACIONES\(NUM_EST.get()).xlsx')#+str(".xlsx"), index=False)
        with pd.ExcelWriter(r"CONSULTA_ESTACIONES/"+str(NUM_EST.get())+str(".xlsx")) as writer:
                df.to_excel(writer,sheet_name='DATOS DIARIOS')
                df22.to_excel(writer,sheet_name='DATOS MENSUALES',engine='xlsxwriter')
                #df.to_excel(r'CONSULTA_ESTACIONES/'+str(NUM_EST.get())+str('.xlsx'),writer,sheet_name='DATOS DIARIOS')#+str(NUM_CUENC.get()))#+str(".xlsx"), index=False)
                #df5.to_excel(r'CONSULTA_ESTACIONES/'+str(NUM_EST.get())+str('.xlsx'),writer,sheet_name='DATOS MENSUALES')
                #df.to_excel(writer,sheet_name='DATOS DIARIOS')#+str(NUM_CUENC.get()))#+str(".xlsx"), index=False)
                #df5.to_excel(writer,sheet_name='DATOS MENSUALES')

        
        
##        writer.close()
        
##        name =NUM_EST.get()+str(".xlsx")
##        print(name)
##        root = Tk()
##        root.withdraw()
##        
##        types =[("Excel Files", "*.xlsx"),
##                ("All Files", "*.*")]      
##        file = tkinter.filedialog.asksaveasfilename(title = "ACUAC",filetypes=types)
##        df.to_excel=file=(str(NUM_EST.get()+".xlsx"))
        
        
        
        
def PRONO():
        global df
        NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios/"+str(ESTADO)+str("/")+str("dia")+str(NUM_EST.get())+str(".txt")
        New_Url3="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Mensuales/"+str(ESTADO)+str("/")+str("mes")+str(NUM_EST.get())+str(".txt")
        df = pd.read_csv(NewUrl, skiprows=22,  sep='\s+',encoding='latin-1')#,index_col=0)#,header=None)
        print(df)
        dff=df.reset_index(drop=True)
        
        df=pd.DataFrame(dff,columns=['PRECIP','EVAP','TMAX','TMIN'])
        
        df['PRECIP'].replace({'NULO': '0'}, inplace=True)
        df['EVAP'].replace({'NULO': '0'}, inplace=True)
        df['TMAX'].replace({'NULO': '0'}, inplace=True)
        df['TMIN'].replace({'NULO': '0'}, inplace=True)
        df2 = df.drop(df[df['PRECIP'] == '(mm)'].index)
        df3= df.drop(df[df['TMAX'] == '(°C)'].index)
        
        df = df2.dropna()
        df = df.replace([np.nan, -np.inf], 0)
        df3=df.astype(float)
        plt.figure(figsize = (10,10))
        x=df3['PRECIP'].mean(axis = 0)
        print('este es',x)
        xx= df3['PRECIP'].std(axis=0)
        y = df3['TMAX'].mean(axis = 0)
        yy=df3['TMAX'].std(axis=0)
        z=df3['TMIN'].mean(axis = 0)
        zz=df3['TMIN'].std(axis=0)

        
        plt.suptitle('FUNCIONES DE DENSIDAD \n '+str('MEDIA TMAX= ')+str(round(y,2))+str('°C ')\
        +str(' STD = ')+str(round(yy,2))+str('° C\n')+str('MEDIA TMIN = ')+str(round(z,2))+str('°C ')\
        +str(' STD = ')+str(round(zz,2))+str('° C\n')+str('MEDIA PRECIP = ')+str(round(x,2))+str('mm ')\
        +str(' STD = ')+str(round(xx,2))+str(' mm'),fontsize = 10)
        sns.histplot(df3["TMAX"] ,  fill = True,color='blue',label="TMAX")#era kdeplot
        plt.xlabel("Tmax (°C)")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.show()
        sns.histplot(df3["TMIN"] , fill = True,label="TMIN")
        plt.xlabel("Tmin (°C)")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.show()
        sns.histplot(df3["PRECIP"] , fill = True,label="PRECIP")
        plt.xlabel("Precipitacion (mm)")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.show()
##        plt.xlabel("Tmax (°C), Tmin (°C), Pp (mm)")
##        plt.ylabel("Funcion de densidad")
##        plt.legend()
##        plt.show()
        
        fig, axs = plt.subplots(3)
        fig.suptitle('SERIES DE TIEMPO'+str(' PARA ESTACION ')+str(NUM_EST.get())+str(" ")+str(NUM_CUENC.get()))
        axs[0].plot(df3["TMAX"],linewidth=0.3,color="red")
        axs[1].plot(df3['TMIN'],linewidth=0.3,color="green")
        axs[2].plot(df3['PRECIP'],linewidth=0.3,color="blue")
        axs[0].set_title('TMAX °C')
        axs[1].set_title('TMIN °C')
        axs[2].set_title('PRECIP mm')
        fig.tight_layout() 
        fig.set_figwidth(15)
        fig.set_figheight(13)
        
        plt.xlabel('Numero de observaciones')
        plt.show()

        
        from scipy.stats import zscore
        import matplotlib.dates as mdates
        import calendar, locale
        #fig, axs = plt.subplots(3)
        locale.setlocale(locale.LC_ALL, 'es-ES')
        df = pd.read_csv(NewUrl, skiprows=24,  sep='\s+',encoding='latin-1',index_col=0)#,header=None)
        index = df.index#("%d-%m-%Y")
        #print(index)
        s1 = str(index)
        print(type(s1))
        s2=s1.replace("/","-")
        print(s2)
##        s3=datetime.datetime(s2)
##        print(s3)
##        fig, ax = plt.subplots()
##        ax1 = ax.twinx()
##        #ax1=ax.secondary_yaxis('right')
##        locator=mdates.AutoDateLocator()
##        formatter=mdates.AutoDateFormatter(locator)
##        ax.xaxis.set_major_locator(locator)
##        ax.xaxis.set_major_formatter(formatter)
##        fig.autofmt_xdate()
##        ax.plot(df3["TMAX"],linewidth=0.1,color="red",label="TMAX")
##        ax.plot(df3['TMIN'],linewidth=0.1,color="green",label="TMIN")
##        ax1.plot(df3['PRECIP'],color="blue",label="PRECIP",linewidth=1)
##        fig.set_figwidth(15)
##        fig.set_figheight(13)
##        ax.legend()
##        ax1.legend()
##        plt.xlabel("TIEMPO")
##        plt.suptitle("UTILIZANDO LOS BOTONES DE ABAJO, REALIZE ZOOM SOBRE LA GRÁFICA PARA VISUALIZAR EL DETALLE DE LA FECHA")
##        ax.set_ylabel("Tmax (°C), Tmin (°C)")
##        ax1.set_ylabel("Precipitación (mm)")

        
        
##        z=zscore(df3['PRECIP'])
##        z2=zscore(df3['TMAX'])
##        z3=zscore(df3['TMIN'])
##        fig.suptitle('CURVAS DE Z'+str(' PARA ESTACION ')+str(NUM_EST.get())+str(" ")+str(NUM_CUENC.get()))
        
##        axs[0].plot(df3["TMAX"],linewidth=0.3,color="red")
##        axs[0]=df3['TMAX'].plot(x=z2, y='FreqDist', kind='kde', figsize=(10, 6))
##        axs[1]=df3['TMIN'].plot(x=z3, y='FreqDist', kind='kde', figsize=(10, 6))
##        axs[2]=df3['PRECIP'].plot(x=z, y='FreqDist', kind='kde', figsize=(10, 6))

        
##        z=zscore(df3['PRECIP'])
##        ax = df3['PRECIP'].plot(x=z, y='FreqDist', kind='kde', figsize=(10, 6))
##        ax = df3['TMAX'].plot(x=z2, y='FreqDist', kind='kde', figsize=(10, 6))
##        ax = df3['TMIN'].plot(x=z3, y='FreqDist', kind='kde', figsize=(10, 6))
##        arr = ax.get_children()[0]._x
##        plt.xticks(np.linspace(arr[0], arr[-1]), rotation=90)
##        plt.plot(z)
        plt.show()
        print(z)


def Eli():
            IRSE.config(background="red")
##            root.after(5000, IRSE.flash)
##            for iterator in range(0, 50, 2):
##                    root.after(1000, IRSE.flash)
                    
            global ESTADO
            global totstr
            global REAL_TIME
            global REAL_TIME_LBL
            global PRONOMET
            global GUARDAMOS
            global PRONOMET_LBL
            global NewUrl
            global Num
            
##            REAL_TIME= Button(root, command=TIEMPO_REAL, image= TIME, bd=7)
##            REAL_TIME.place(x= 200,y=380)
##            REAL_TIME_LBL= Label(root, text="TIEMPO REAL")
##            REAL_TIME_LBL.place(x= 230, y=360)

            
            Num=NUM_EST.get()
            string=Num
            first=string[0:2]
            first2=string[0:1]
            print('este es first2',first)   
            totstr=len(Num)
            print('numero_caracteres',len(Num))    
            if first ==str("10") and totstr==5:         
                func()
            elif first==str("32"):
                func2()
            elif first==str("12"):
                func3()
            elif first==str("50")or first==str("51"):
                func4() 
            elif first==str("24"):
                func5()
            elif first==str("83")or first==str("80")or first==str("82")or first==str("80"):
                func6()
            elif first==str("16"):
                func7()
            elif first==str("20")and totstr==5:
                func8()
            elif first==str("20")and totstr==4:
                func14()
                
            elif first==str("19"):
                func9()
            elif first==str("28"):
                func10()
            elif first==str("25"):
                func11()
            elif first==str("26"):
                func12()
            elif first==str("19"):
                func13()
##            elif first==str("20")and totstr==4:
##                print("si paso")
##                func14()
            elif first==str("15"):
                func15()
            elif first==str("11"):
                func16()
            elif first==str("14"):
                func17()
            elif first==str("21")and totstr==5:
                func19()
            elif first==str("21")and totstr==4:
                func14()
            elif first==str("10")and totstr==4:
                func18()
            elif first==str("90")and totstr==4:
                func20()
            elif first==str("30")and totstr==5:
                func21()
            elif first==str("30") and totstr==4:
                func25()
            elif first==str("13"):
                func22()
            elif first==str("27"):
                func23()
            elif first==str("40"):
                func24()
            elif first==str("31")and totstr==4:
                func25()
            elif first==str("31") and totstr==5:
                func29()
            elif first==str("18"):
                func26()
            elif first==str("60"):
                func27()
            elif first==str("70")or first==str("72") or first ==("73"):
                func28()
            elif first==str("23"):
                func30()
            
        
##            if first2==str("1"):
##                func18()
            
##            if first==str("20")and totstr==4:
##                print("este es tostado",totstr)
##                func14()
                
            

            NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios/"+str(ESTADO)+str("/")+str("dia")+str(NUM_EST.get())+str(".txt")
            New_Url3="https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Mensuales/"+str(ESTADO)+str("/")+str("mes")+str(NUM_EST.get())+str(".txt")
            webbrowser.open_new(NewUrl)
            webbrowser.open_new(New_Url3)

##            Url="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/"+str("000")+str(NUM_EST.get())+ str(".TXT")
##            current_url = Url.replace("/dgo/", "/"+str(ESTADO)+str("/"))
            
            if ESTADO =="chih" or ESTADO=="mich" or  ESTADO == "coah" or ESTADO =="ags" or ESTADO =="bc" or ESTADO=="df" or ESTADO =="camp" or ESTADO =="bcs" or ESTADO == "col" or ESTADO=="chis":
                Url="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/"+str("0000")+str(NUM_EST.get())+ str(".TXT")
                current_url = Url.replace("/dgo/", "/"+str(ESTADO)+str("/"))
                webbrowser.open_new(current_url)
                
##            if ESTADO=="bc":# and totstr==4:
##                print('dentro de la url',ESTADO)
##                Url="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/"+str("0000")+str(NUM_EST.get())+ str(".txt")
##                current_url = Url.replace("/dgo/", "/"+str(ESTADO)+str("/"))
##                webbrowser.open_new(current_url)
                    
            

            
                    
            #NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/current_url/"+str("000")+str(NUM_EST.get())+ str(".TXT")
            #NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Diarios/"+str(NUM_EST.get())+str(".txt")
            #webbrowser.open_new(current_url)
            
            PRONOMET=Button(root,  command = PRONO, image = CURVA_NORMAL,bd=5)
            PRONOMET.place(x= 280,y=400)
            PRONOMET_LBL = Label(root, text ="SERIES DE TIEMPO Y FUNCION DE DENSIDAD",font= Font_tuple1)
            PRONOMET_LBL.place(x= 240, y=370)

            GUARDAMOS= Button(root, command = GUARDA_DATOS, text='GUARDAR\nESTACIONES',bd=5)
            GUARDAMOS.place(x=540, y=405)
            

##            REAL_TIME = Button(root, command =TIEMPO_REAL, image =REALTIME, bd=5)#, state="disabled") 
##            REAL_TIME.place (x= 400, y=400)
##            REAL_TIME_LBL = Label(root, text= "CLIMA ACTUAL", font=Font_tuple1)
##            REAL_TIME_LBL.place(x= 440, y=370)
            
            
            #webbrowser.open_new(NewUrl)
def empty():
        my_texti.destroy()
        NUM_CUENC.delete(0,END)
        NUM_EST.destroy()
        Elige.destroy()
        my_canvas.delete(INTR)
        root.after(2000, lambda: VACIO.destroy())
def SUBCU():
    global TEMPORAL5
    global TEMPORAL4
    global NUM_EST
    global EST1
    global EST2
    global EST3
    global NUM_EST
    global my_texti
    global Elige
    global INTR
    global ESTADO
    global canvas
    global df
    global VACIO
    AGR["state"]="active"
    Datos2 = pd.read_csv(Archivo2,encoding='latin-1')
    
##    VACIO = Button(root, text="BORRA_FRAME", command = empty,font= Font_tuple1,fg="blue")
##    VACIO.place(x= 240, y=320)

    
    
    canvas=Canvas(root, width = 390, height=100)
    canvas.pack(fill ="both", expand= True)
    TEMPORAL4=Datos2[Datos2["CUENCA"]==str(NAME)]#"Presa Lazaro Cardenas"]  
    #EST1 = TEMPORAL5=TEMPORAL4[["ID","ESTACION","ESTADO","CUENCA"]]#,"MUNICIPIO"]]
    EST1 = TEMPORAL5=TEMPORAL4[["ID","ESTACION","ESTADO","MUNICIPIO"]]
    df=pd.DataFrame(EST1)
    nada =df.empty
    print(nada)
    if nada==True:
            print("siiii")
            VACIO = Button(root, text="BORRA_FRAME_VACIO", command = empty,font= Font_tuple1,fg="blue")
            VACIO.place(x= 240, y=320)
            
    #EST2 = my_canvas.create_text(1000,400, text=" " +str(TEMPORAL5))
    #EST3 = my_canvas.create_text(540,500, text="ESTACIONES CLIMATICAS EN CUENCA ELEGIDA")

    my_texti=Text(root, height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
    my_texti.place(x= 200, y=30)
    #my_texti.insert(END, TEMPORAL5)#+'\n')
    my_texti.insert(1.0,TEMPORAL5)
    
    
    #fin= open("ESTACIONES_CLIMATICAS/RESULTADOS" , "a")
    fin= open("ACUAC_CONSULTAS/ESTACIONES CLIMATICAS" , "w")# si ponemos "a" no sobreescribe,va haciendo el cumulo de consultas
    fin.write("\n-----------------------------------------------------------------\n")
    fin.write("\n")
    fin.write("FECHA "+str(datetime.datetime.now())+str("\n"))
    fin.write("CUENCAS EN LA REGION HIDROLOGICA ELEGIDA "+str(clickrRH.get())+str("\n")+str(TEMPORAL3)+str("\n"))
    fin.write("_________________________________________________________________"+str("\n"))
    fin.write("_________________________________________________________________"+str("\n"))
    fin.write("ESTACIONES DE LA CUENCA "+str(NAME)+str(" de la ")+str(" ")+str(clickrRH.get()+str("\n")+str(TEMPORAL5)))
    fin.close()
    
    
    
    
    #plt.savefig("./GRAFICAS/")
    
    #Num_Est=10149
    NUM_EST=IntVar()
    NUM_EST=Entry(root, textvariable=NUM_CUENC, width=10)
    NUM_EST.place(x=60, y=400)
    INTR=my_canvas.create_text(110,380, text="INTRODUZCA ID DE ESTACION CLIMÁTICA",font= Font_tuple1)
    Elige= Button(root, text= "LEE DATOS", command= Eli,font= Font_tuple1,fg="blue")
    Elige.place(x= 60, y=430)
##    Url=("https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/00010119.TXT")
##    NewUrl="https://smn.conagua.gob.mx/tools/RESOURCES/Mensuales/dgo/"+str("000")+str(NUM_EST.get())+ str(".TXT")
##    webbrowser.open_new(NewUrl)
def SUBCUENCA(event):
    global IDCUENCA
    global Datos
    global NUM_CUENC
    global ID
    global NUMERO
    global TEMPORAL3
    global Archivo2
    global ibis30
    global ibis30_2
    global CUENC
    global CUENC_O
    global NUM_CUENC
    global SUBC
    global clickrRH
    global ESTADO
    global NUM_CUENC_lbl
    global my_texti2
    global LEE
    global ALMACENA_DATOS
    global clickTEMAS
    global option11
    global drop4

    option11 =[
              
              "TEMAS DE CONSULTA PARA LA "+str(clickrRH.get()),
              "CAPTACION DE AGUA DE LLUVIA",
              "DISTRITOS DE RIEGO",
              "POTENCIAL PRODUCTIVO",
              "HIDROLOGÍA",
              "ALTERNATIVAS CONSERVACION",
              "AGENDAS TECNOLOGICAS",
              "INIFAP EN LA REGION ",
              "ASPECTOS SOCIALES"
              
            ]
    clickTEMAS =StringVar()
    clickTEMAS.set(option11[0])
    drop4=OptionMenu(root,clickTEMAS, *option11, command= KNOWLEDGE_BASE)
    drop4["menu"].config(bg="light BLUE")
    drop4.place(x=30, y=200)
    my_canvas.delete(CUENCA)

    
    if clickrRH.get()=="RH036":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUEC_ESTCLIM.csv"
        ibis30= my_canvas.create_image(500,350, image= bgARIDH)
    if clickrRH.get()=="RH024":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH024.csv"
        ibis30= my_canvas.create_image(550,320, image= bgARIDH2)
    if clickrRH.get()=="RH020":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH020.csv"       
        ibis30= my_canvas.create_image(600,370, image= bgARIDH3)
    if clickrRH.get()=="RH037":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH037.csv"       
        ibis30= my_canvas.create_image(450,280, image= bgARIDH4)     
    if clickrRH.get()=="RH026":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH026.csv"       
        ibis30= my_canvas.create_image(450,310, image= bgARIDH5)
    if clickrRH.get()=="RH035":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH035.csv"       
        ibis30= my_canvas.create_image(520,300, image= bgARIDH6)
    if clickrRH.get()=="RH017":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH017.csv"       
        ibis30= my_canvas.create_image(570,350, image= bgARIDH7)
    if clickrRH.get()=="RH021":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH021.csv"       
        ibis30= my_canvas.create_image(570,350, image= bgARIDH8)
    if clickrRH.get()=="RH010":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH010.csv"       
        ibis30= my_canvas.create_image(500,340, image= bgARIDH9)
    if clickrRH.get()=="RH008":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH008.csv"       
        ibis30= my_canvas.create_image(570,330, image= bgARIDH10)
    if clickrRH.get()=="RH009":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH009.csv"       
        ibis30= my_canvas.create_image(510,330, image= bgARIDH11)
    if clickrRH.get()=="RH034":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH034.csv"       
        ibis30= my_canvas.create_image(520,330, image= bgARIDH12)
    if clickrRH.get()=="RH004":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH004.csv"       
        ibis30= my_canvas.create_image(570,320, image= bgARIDH13)
    if clickrRH.get()=="RH025":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH025.csv"       
        ibis30= my_canvas.create_image(410,310, image= bgARIDH14)
    if clickrRH.get()=="RH018":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH018.csv"       
        ibis30= my_canvas.create_image(570,370, image= bgARIDH15)
    if clickrRH.get()=="RH012":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH012.csv"       
        ibis30= my_canvas.create_image(520,300, image= bgARIDH16)
    if clickrRH.get()=="RH027":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH027.csv"       
        ibis30= my_canvas.create_image(520,250, image= bgARIDH17)
    if clickrRH.get()=="RH028":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH028.csv"       
        ibis30= my_canvas.create_image(520,250, image= bgARIDH18)
    if clickrRH.get()=="RH029":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH029.csv"       
        ibis30= my_canvas.create_image(470,350, image= bgARIDH19)
    if clickrRH.get()=="RH030":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH030.csv"       
        ibis30= my_canvas.create_image(470,350, image= bgARIDH20)
    if clickrRH.get()=="RH005":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH005.csv"       
        ibis30= my_canvas.create_image(470,300, image= bgARIDH21)
    if clickrRH.get()=="RH006":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH006.csv"       
        ibis30= my_canvas.create_image(470,300, image= bgARIDH22)
    if clickrRH.get()=="RH007":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH007.csv"       
        ibis30= my_canvas.create_image(470,300, image= bgARIDH23)
    if clickrRH.get()=="RH011":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH011.csv"       
        ibis30= my_canvas.create_image(470,300, image= bgARIDH24)
    if clickrRH.get()=="RH013":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH013.csv"       
        ibis30= my_canvas.create_image(470,300, image= bgARIDH25)
    if clickrRH.get()=="RH014":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH014.csv"       
        ibis30= my_canvas.create_image(500,330, image= bgARIDH26)
    if clickrRH.get()=="RH015":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH015.csv"       
        ibis30= my_canvas.create_image(500,330, image= bgARIDH27)
    if clickrRH.get()=="RH016":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH016.csv"       
        ibis30= my_canvas.create_image(500,330, image= bgARIDH28)
    if clickrRH.get()=="RH019":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH019.csv"       
        ibis30= my_canvas.create_image(550,300, image= bgARIDH29)
    if clickrRH.get()=="RH022":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH022.csv"       
        ibis30= my_canvas.create_image(680,320, image= bgARIDH30)
    if clickrRH.get()=="RH023":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH023.csv"       
        ibis30= my_canvas.create_image(530,300, image= bgARIDH31)
    if clickrRH.get()=="RH031":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH031.csv"       
        ibis30= my_canvas.create_image(400,300, image= bgARIDH32)
    if clickrRH.get()=="RH032":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH032.csv"       
        ibis30= my_canvas.create_image(500,350, image= bgARIDH33)
    if clickrRH.get()=="RH033":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH033.csv"       
        ibis30= my_canvas.create_image(500,350, image= bgARIDH34)
    if clickrRH.get()=="RH001":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH001.csv"       
        ibis30= my_canvas.create_image(460,280, image= bgARIDH35)
    if clickrRH.get()=="RH002":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH002.csv"       
        ibis30= my_canvas.create_image(510,280, image= bgARIDH36)
    if clickrRH.get()=="RH003":
        Archivo="NO_CUENCAS.csv"
        Archivo2="CUENC_ESTCLIM_RH003.csv"       
        ibis30= my_canvas.create_image(510,280, image= bgARIDH37)
        
    ALMACENA_DATOS = Label(root, text="LOS DATOS CONSULTADOS SERÁN GUARDADOS EN LA CARPETA ACUAC_CONSULTAS",fg="blue",font=('Helvetica','8','bold'))
    ALMACENA_DATOS.place(x=550, y=10)
        
    Datos = pd.read_csv(Archivo,encoding='latin-1')
    TEMPORAL2 = Datos[Datos["ID_RH"]==(clickrRH.get())]
    TEMPORAL3=TEMPORAL2[["IDCUENCA","REGION","CUENCA","AREA"]]

    fin= open("ACUAC_CONSULTAS/CUENCAS" , "w")# si ponemos "a" no sobreescribe,va haciendo el cumulo de consultas
    
    fin.write("\n-----------------------------------------------------------------\n")
    fin.write("\n")
    fin.write("FECHA "+str(datetime.datetime.now())+str("\n"))
    fin.write("CUENCAS EN LA REGION HIDROLOGICA ELEGIDA "+str(clickrRH.get())+str("\n")+str(TEMPORAL3))
    fin.close()
    
    
##    CUENC_O=my_canvas.create_text(800,100, text=" " +str(TEMPORAL3))
##    CUENC=my_canvas.create_text(500,40, text="CUENCAS EN RH "+str(clickrRH.get()))

    my_texti2=Text(root, height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
    my_texti2.place(x= 600, y=30)
##    my_texti2.insert(END, TEMPORAL3)#+'\n')
##    my_texti2.insert(1.0, TEMPORAL3)
    Datos2 = pd.read_csv(Archivo2,encoding='latin-1')
    df=pd.DataFrame(TEMPORAL3)
    CONVERTIDO=df.to_string()
    my_texti2.insert(1.0, CONVERTIDO)
    print("AQUI")
    SUBC=Button(root, text="PRESIONE PARA ELEGIR \n ESTACION CLIMÁTICA ", command=SUBCU, state="disabled",font= Font_tuple1,fg="blue" )
    SUBC.place(x=70, y=320)
    NUMERO=TEMPORAL3["IDCUENCA"]
    NUM_CUENC=StringVar()
    NUM_CUENC=Entry(root, textvariable=NUM_CUENC, width=20)
    NUM_CUENC.place(x=60, y=280)
    NUM_CUENC_lbl=Label(root, text="INTRODUZCA NOMBRE DE LA CUENCA",font= Font_tuple1,fg="blue")
    NUM_CUENC_lbl.place(x=40, y=260)
    LEE=Button(root, text="LEER", command = read)
    LEE.place(x=20, y=320)

##    option11 =[
##              
##              "TEMAS DE CONSULTA",
##              "CAPTACION DE AGUA DE LLUVIA",
##              "DISTRITOS DE RIEGO",
##              "POTENCIAL PRODUCTIVO",
##              "HIDROLOGÍA",
##              "ALTERNATIVAS CONSERVACION"
##              
##            ]
##    clickTEMAS =StringVar()
##    clickTEMAS.set(option11[0])
##    drop4=OptionMenu(root,clickTEMAS, *option11, command= KNOWLEDGE_BASE)
##    drop4["menu"].config(bg="light BLUE")
##    drop4.place(x=40, y=220)
        
##        TEMPORAL4=Datos2[Datos2["CUENCA"]=="Presa Lazaro Cardenas"]  
##        TEMPORAL5=TEMPORAL4[["ESTACION","ESTADO","CUENCA"]]
##        my_canvas.create_text(500,300, text=" " +str(TEMPORAL5))
##        my_canvas.create_text(500,240, text="ESTACIONES CLIMATICAS EN CUENCA ELEGIDA")

def borras():
    
    my_canvas.delete(CUENC)
    my_canvas.delete(CUENC_O)
    my_canvas.delete(EST1)
    my_canvas.delete(EST2)
    my_canvas.delete(EST3)
    clickrRH.set(option[0])
    NUM_EST.delete(0,END)
    NUM_CUENC.delete(0,END)
    TEMPORAL4.destroy()
    my_texti.destroy()
    
    
    
    
    
def MENSAJE():
    
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    
    converter.say("EN EL PAIS EXISTEN 37 REGIONES HIDROLÓGICAS. SU SITUACIÓN BIO CLIMÁTICA ES SUSTANCIALMENTE DIFERENTE.\n\
    DE AHÍ QUE, LOS PROCESOS HIDROLÓGICOS PRESENTAN DIFERENTES MAGNITUDES ACORDE AL ESTADO QUE GUARDE SU SUPERFICIE.\n\
    AL PRESIONAR EL BOTÓN, SELECCIONE RH, PODRÁ ELEGIR LA RH DE INTERÉS. EL RESULTADO MOSTRARÁ EL NOMBRE DE LA RH, LAS CUENCAS QUE COMPRENDE, Y EL ÁREA DE ÉSTAS.\n\
    ESTA INFORMACIÓN, ES ACORDE A LA NUEVA REGIONALIZACIÓN PUBLICADA EL 18 DE SEPTIEMBRE DEL 2023. EL BOTÓN, INTRODUZCA NOMBRE DE LA CUENCA, DESPLIEGA LAS ESTACIONES CLIMÁTICAS DE LA CUENCA ELEGIDA, EL ESTADO Y EL MUNICIPIO.\n\
    EL BOTÓN, ELEGIR ESTACIÓN CLIMÁTICA, LE SOLICITARÁ INTRODUCIR EL NÚMERO DE LA ESTACIÓN MARCADO COMO I D.\n\
    AL PRESIONAR, LEE DATOS, APARECERÁN LAS ESTADÍSTICAS MENSUALES DE LA ESTACIÓN ELEGIDA ASÍ COMO LOS DATOS DIARIOS.\n\
    ESTOS DATOS, PUEDEN SER GUARDADOS COMO TEXTO EN SU COMPUTADORA PARA USO POSTERIOR, SOLO PRESIONANDO EL BOTON DERECHO DEL MOUSE Y ELEGIR, GUARDAR COMO.\n\
    EN CASO DE NO DESPLEGAR NADA, SOLO CIERRE LAS PESTAÑAS PARA REGRESAR AL PROGRAMA.\n\
    PARA EL ÓPTIMO USO DE LA APLICACIÓN, ES NECESARIO CONTAR CON ACCESO A INTERNET")
    converter.runAndWait()
    MSJ.destroy()
    MSJlbl.destroy()
def irse2():
##    REAL_TIME.destroy()
##    REAL_TIME_LBL.destroy()
    drop4.destroy()
    drop.destroy()
    
    
    ALMACENA_DATOS.destroy()
    
    NUM_EST.delete(0,END)
    my_texti.destroy()
    my_texti2.destroy()
    #my_canvas.delete(CUENC_O)
    my_canvas.delete(ibis30)
    #my_canvas.delete(CUENC)
    NUM_CUENC_lbl.destroy()
    #my_canvas.delete(EST3)
    #my_canvas.delete(EST2)
    NUM_CUENC.destroy()
    NUM_CUENC_lbl.destroy()
    SUBC.destroy()
    NUM_CUENC.destroy()
    NUM_CUENC_lbl.destroy()
    LEE.destroy()
    NUM_EST.destroy()
    Elige.destroy()
    my_canvas.delete(INTR)
    #IRSE.destroy()
    PRONOMET.destroy()
    PRONOMET_LBL.destroy()
    GUARDAMOS.destroy()
    #REAL_TIME.destroy()
    #REAL_TIME_LBL.destroy()
    #SALIR2.destroy()
    drop.destroy()
    Hydr["state"]="active"
    CC["state"]="active"
    EROSION["state"]="active"
    #CLIMA["state"]="active"
    DR["state"]="active"
    GEE["state"]="active"
    BALANCE["state"]="active"
    ANUNCIO=Label(root, text="PRESIONE CUALQUIERA DE LOS BOTONES ABAJO PARA DESPLEGAR EL TEMA",font= Font_tuple4,fg="blue")
    ANUNCIO.place(x=250, y=300)
    root.after(2000, ANUNCIO.destroy)
##    VACIO.destroy()
##    guardado.destroy()
##    EXPLICA.destroy()
    #NUM_CUENC.delete(0, END)
    
    
    
   
def REG_HYDR():
    global clickrRH
    global CUENCA
    global option
    global MSJ2
    global MSJ
    global MSJlbl
    global SALIR2
    global IRSE
    global drop
    CREDITOS.destroy()
    CREDITOS_lbl.destroy()
    
    CUENCA= my_canvas.create_image(270,490, image= bg2, anchor="sw")
    my_canvas.delete(CUENCA2)
    MSJ = Button(root, text= "MENSAJE DE VOZ", command=MENSAJE, image=MSJ2)
    MSJ.place(x= 220,y=60)
    MSJlbl= Label(root, text="INTRODUCCION",  font= Font_tuple1,fg="blue")
    MSJlbl.place(x= 200, y=30)
    
    option =[
              "SELECCIONE RH",
              "RH001",
              "RH002",
              "RH003",
              "RH004",
              "RH005",
              "RH006",
              "RH007",
              "RH008",
              "RH009",
              "RH010",
              "RH011",
              "RH012",
              "RH013",
              "RH014",
              "RH015",
              "RH016",
              "RH017",
              "RH018",
              "RH019",
              "RH020",
              "RH021",
              "RH022",
              "RH023",
              "RH024",
              "RH025",
              "RH026",
              "RH027",
              "RH028",
              "RH029",
              "RH030",
              "RH031",
              "RH032",
              "RH033",
              "RH034",
              "RH035",
              "RH036",
              "RH037"
            ]
    clickrRH =StringVar()
    clickrRH.set(option[0])
    drop=OptionMenu(root,clickrRH, *option, command=SUBCUENCA)
    drop["menu"].config(bg="light BLUE")
    drop.place(x=40, y=150)

    

    IRSE= Button(root, text= "BORRAR", command = irse2,bd=5,font= Font_tuple1,fg="blue")#BORRA CONSULTA CLIMATICA
    IRSE.place(x= 60, y=455)
    SALIR2= Button (root, text = "SALIR", command = SALGAMOS, bd=5,font= Font_tuple1,fg="blue")
    SALIR2.place(x=60, y=490)

def calcular2(event):
    global PP
    global LONG
    global CN
    global PEND
    global CE
    global AREA
    global convert
    global CN_POND
    global PP_POND
    global PEND_POND
    global AREA_TOT
    global LONGITUD
    global LONGITUD_lbl
    global AVISO_POND
    global CALC_POND
    global VAMONOS
    global CAPTURA_LONG
    
    if clickAREA.get()==str("AREA3"):#or clickAREA.get()==str("AREA2")or  clickAREA.get()==str("AREA3") :
        PP= AREA3_PP.get()
        LONG=LONG_PEND3_S.get()
        CN=AREA3_CN.get()
        PEND= AREA3_PEND.get()
        CE=CE3.get()
        AREA=AREA3.get()
        S=((25400)/float(CN))-254
        convert=float(S)
        print('PP',PP, 'LONG', LONG, 'CN', CN, 'PEND', PEND, 'CE', CE, 'AREA', AREA)
        
    if clickAREA.get()==str("AREA2"):#or clickAREA.get()==str("AREA2")or  clickAREA.get()==str("AREA3") :
        PP= AREA2_PP.get()
        LONG=LONG_PEND2_S.get()
        CN=AREA2_CN.get()
        PEND= AREA2_PEND.get()
        CE=CE2.get()
        AREA=AREA2.get()
        S=((25400)/float(CN))-254
        convert=float(S)
        print('PP',PP, 'LONG', LONG, 'CN', CN, 'PEND', PEND, 'CE', CE, 'AREA', AREA,'S',S)

    if clickAREA.get()==str("AREA1"):#or clickAREA.get()==str("AREA2")or  clickAREA.get()==str("AREA3") :
        PP= AREA1_PP.get()
        LONG=LONG_PEND1_S.get()
        CN=AREA1_CN.get()
        PEND= AREA1_PEND.get()
        CE=CE1.get()
        AREA=AREA1.get()
        S=((25400)/float(CN))-254
        convert=float(S)
        print('PP',PP, 'LONG', LONG, 'CN', CN, 'PEND', PEND, 'CE', CE, 'AREA', AREA,'S',S)

    if clickAREA.get()==str("PONDERADO"):
        CALC_POND= Button(top, text="PONDERADO", command = calcular_pond,font=('Times New Roman',6,'bold'),bg="light blue")
        CALC_POND.place(x=500, y=440)
        VAMONOS = Button(top, text = "SALIR", command=salir_pond)
        VAMONOS.place (x=500, y=380)
        

        AREA_TOT= int(AREA1.get())+int(AREA2.get())+int(AREA3.get())
        CN_POND1= int(AREA1_CN.get())*int(AREA1.get())
        CN_POND2= int(AREA2_CN.get())*int(AREA2.get())
        CN_POND3= int(AREA3_CN.get())*int(AREA3.get())
        CN_POND = (CN_POND1+CN_POND2+CN_POND3)/AREA_TOT

        PP_POND1=int(AREA1_PP.get())*int(AREA1.get())
        PP_POND2=int(AREA2_PP.get())*int(AREA2.get())
        PP_POND3=int(AREA3_PP.get())*int(AREA3.get())
        PP_POND= (PP_POND1+PP_POND2+PP_POND3)/AREA_TOT

        PEND_POND1 =float(AREA1_PEND.get())*int(AREA1.get())
        PEND_POND2 =float(AREA2_PEND.get())*int(AREA2.get())
        PEND_POND3 =float(AREA3_PEND.get())*int(AREA3.get())
        PEND_POND = (PEND_POND1+PEND_POND2+PEND_POND3)/AREA_TOT

        LONGITUD=IntVar()
        LONGITUD =Entry(top, textvariable= LONGITUD, width=10)
        LONGITUD.place(x=500, y=470)
        LONGITUD_lbl = Label (top, text="LONGITUD TRIBUTARIO\n PRINCIPAL",font= Font_tuple1,fg="blue")
        LONGITUD_lbl.place(x=470,y=490)

        AVISO_POND = Label(top, text="REQUIERE DATOS DE LAS OTRAS CUENCAS", font= Font_tuple1,fg="blue")
        AVISO_POND.place(x=419, y=410)

        CAPTURA_LONG= Button(top, text ="LEE",command =captura_longitud, font=Font_tuple1,fg="blue")
        CAPTURA_LONG.place(x=450, y=470)
                 
    print("CN_POND", CN_POND, "PP_POND ",PP_POND, "PEND_POND ", PEND_POND)
def salir_pond():
        LONGITUD.destroy()
        LONGITUD_lbl.destroy()
        CAPTURA_LONG.destroy()
        AVISO_POND.destroy()
        CALC_POND.destroy()
        VAMONOS.destroy()
def captura_longitud():
    global LARGO
    LARGO =int(LONGITUD.get())
def calcular_pond():
    global LONG
    

    #LONG=1000
    LONG =LONGITUD.get()
    print('LONG ',LONG)
    S=(25400/CN_POND)-254
    convert=float(S)
    Q= ((float(PP_POND)-float(0.2*(convert)))**2)/((float(PP_POND)+float(0.8*convert)))
    TcSCS1=float((LONG))**0.8
    TcSCS2=(1000/(float(CN_POND)-9)**0.7)
    TcSCS3=(4407*float(int(PEND_POND))**0.5)
    TcSCS=(TcSCS1*TcSCS2)/TcSCS3
    q=0.0028*float(CE)*float(PP)*float(AREA_TOT)
    print("QPOND ",Q, "q ", q)

    df= pd.read_excel('HIDRO.xlsx',engine='openpyxl')#, usecols = cols)
    fig,ax=plt.subplots()
    ax.set_xlabel("Tiempo (min)")
    ax.set_ylabel("q m3.seg Hidrograma Actual", color='green')
    #Q=4.8
    u = Q/2620
    w= q/100
    k=167*(u/w)
    qus=df['t']
    qus2=df['q']
    x1=df['t']*k
    y1=df['q']*w
    y3=df['PUNTO']*Q
    df['kt']=x1
    df['wq']=y1
    accum=0
    suma=0
    row=1
    ax2=ax.twinx()
    ax.grid(which='both')
    ax.plot(x1,y1,color='green')#, label= 'Hidrograma\n Actual')
    ax2.plot(x1,y3, color ="brown")#, label='Lamina\n acumulada')
    leg=ax.legend()
    leg=ax2.legend()
    ax2.set_ylabel('Lamina Acumulada (mm)',color='brown')
    plt.title("HIDROGRAMA ADIMENSIONAL PARA LA CUENCA ELEGIDA DE LA RH")#+str(clickrRH.get()))
    df.to_excel('RESULTADOS.xlsx',engine='openpyxl')
    maximo = df['wq'].max()
    print('maximo',maximo)
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("EL MAXIMO VALOR DE ESCURRIMIENTO EN EL HIDROGRAMA PONDERADO, GASTO PICO ES"+str(round(maximo,2))+str('metros cúbicos por segundo'))
    converter.runAndWait()
    plt.show()
def calcular():
    global Q
    global q
    global maximo
    
    #S= float((25400/CN))-float(254)
    #S=55
    ia=0.2*(convert)
    print('ia =',ia)
    if float(PP)<=ia:
        print ('no hay escurrimiento')
        converter = pyttsx3.init()
        
        converter.setProperty('rate', 150)
        converter.say("NO OCURRE ESCURRIMIENTO CON LOS PARÁMETROS PROVEÍDOS DE LA CUENCA. ESQO SE DEBE A UNA CURVA NUMÉRICA BAJA\n\
        O A UNA ESCASA PRECIPITACIÓN. SE RECOMIENDA VERIFICAR LOS PARÁMETROS A SABIENDAS QUE, LA CURVA NUMÉRICA, ES FUNCIÓN\n\
        DE LA CUBIERTA VEGETAL DE LA CUENCA, EL ESTADO QUE ÉSTA GUARDA Y DEL GRUPO HIDROLÓGICO DE SUELO.\n\
        VER LA AYUDA PROVEÍDA EN EL APARTADO CORRESPONDIENTE")
        converter.runAndWait()
    else:
        
        Q= ((float(PP)-float(0.2*(convert)))**2)/((float(PP)+float(0.8*convert)))
        
        print("este es Q ", Q)
        TcSCS1=float((LONG))**0.8
        TcSCS2=(1000/(float(CN)-9)**0.7)
        TcSCS3=(4407*float((PEND))**0.5)
        TcSCS=(TcSCS1*TcSCS2)/TcSCS3
        q=0.0028*float(CE)*float(PP)*float(AREA)
        print("CE=",CE, "PP=",PP, "AREA=",AREA)
        print(Q, " ", q)

        
        
        df= pd.read_excel('HIDRO.xlsx',engine='openpyxl')#, usecols = cols)
        fig,ax=plt.subplots()
        ax.set_xlabel("Tiempo (min)")
        ax.set_ylabel("q m3.seg Hidrograma Actual", color='green')
        #Q=4.8
        u = Q/2620
        w= q/100
        k=167*(u/w)
    ##    u2=Q100/2620
    ##    w2=q100/100
    ##    k2=167*(u2/w2)

        qus=df['t']
        qus2=df['q']
        #qus3=df['GASTO']

        x1=df['t']*k
        y1=df['q']*w
    ##    x2=df['t']*k2
    ##    y2=df['q']*w2
        y3=df['PUNTO']*Q
    ##    print(y3)
    ##    y4=df['PUNTO']*Q100n

        df['kt']=x1
        df['wq']=y1
        #df['PUNTO']=y3
        accum=0
        suma=0
        row=1
##        NUM_CUENC=str(nombre)
        ax2=ax.twinx()
        #ax3=ax.twinx()
        #plt.plot(x1, dato5)
        ax.grid(which='both')
        ax.plot(x1,y1,color='green')#, label= 'Hidrograma\n Actual')
        ax2.plot(x1,y3, color ="brown")#, label='Lamina\n acumulada')
        #ax3.plot(x1,y4)
        #plt.figure(figsize=[15,14])
        leg=ax.legend()
        leg=ax2.legend()
        ax2.set_ylabel('Lamina Acumulada (mm)',color='brown')
        plt.title("HIDROGRAMA ADIMENSIONAL PARA LA CUENCA ELEGIDA DE LA RH")#+str(clickrRH.get()))
    ##    ax2=ax.twiny()
    ##    ax2.set_ylabel("q m3.seg Hidrograma Tr 100")
        #ax2.set_xlabel("Tiempo (min) Hidrograma Tr 100")
        df.to_excel('RESULTADOS.xlsx',engine='openpyxl')
        maximo = df['wq'].max()
        print('maximo',maximo)
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.say("EL MAXIMO VALOR DE ESCURRIMIENTO, GASTO PICO, ES"+str(round(maximo,2))+str('metros cúbicos por segundo'))
        #converter.say("EL MAXIMO VALOR DE ESCURRIMIENTO PARA LA CUENCA"+str(str(NUM_CUENC)))#+str("ES")+str(round(maximo,2))+str('metros cúbicos por segundo')))
        converter.runAndWait()
        plt.show()

def BORRAR_INDEX():
    FI_1.destroy()
    PLACE_AREA.destroy()
    FI_2.destroy()
    FI_3.destroy()
    FI_4.destroy()
    FI_5.destroy()
    FI_6.destroy()
    FI_7.destroy()
    BT_AREA.destroy()
    AT_AREA.destroy()
    AB_AREA.destroy()
    PP_AN.destroy()
    SUE_A.destroy()
    SUE_D.destroy()
    FLOW_INDEX_CALC.destroy()
    BORRA_INDEX.destroy()
    RES_IF.destroy()
    
def CALC_FI():
    global RES_IF
    AREA_MOD=float(PLACE_AREA.get())*0.00386102
    PP_MOD=float(PP_AN.get())*0.03937
    print(AREA_MOD,"",PP_MOD)
##    IF=float(PLACE_AREA.get())*(-0.55077+(-0.0014132*float(BT_AREA.get()))+(0.0019883*float(AT_AREA.get()))+(0.0039675*float(AB_AREA.get())\
##        +(0.02408*float(PP_AN.get()))+(0.0023171*float(SUE_A.get()))+(0.001534*float(SUE_D.get()))))**2

    IF=AREA_MOD*(-0.55077+(-0.0014132*float(BT_AREA.get()))+(0.0019883*float(AT_AREA.get()))+(0.0039675*float(AB_AREA.get())\
        +(0.02408*PP_MOD+(0.0023171*float(SUE_A.get()))+(0.001534*float(SUE_D.get())))))**2
    IF2=IF*0.0283168
    print(IF,"",IF2)
    RES_IF= Label(top, text="EL INDICE DE SEGURIDAD DE LA CUENCA ES \n"+str(round(IF2,4))+str(" M3.seg")+str(" PARA SEGURIDAD EN LA CONSERVACION DE LA CUENCA\n\
    DE LOS TRIBUTARIOS Y DEL ACUÍFERO,\n DEBERÁ EXTRAERSE SOLO UN PORCENTAJE DE ESTE VALOR"),font= Font_tuple1,fg="blue")
    RES_IF.place(x=900, y=180)
def FI():
    global PLACE_AREA
    global FI_1
    global FI_2
    global BT_AREA
    global FI_3
    global AT_AREA
    global FI_4
    global AB_AREA
    global FI_5
    global PP_AN
    global FI_6
    global SUE_A
    global FI_7
    global SUE_D
    global FLOW_INDEX_CALC
    global BORRA_INDEX

    AYUDA_INDEX= Label(top, text="AYUDA", font= Font_tuple1,fg="blue")
    AYUDA_INDEX.place(x=1100, y=10)
    
    FI_1=Label(top, text="AREA TOTAL(Ha)",font= Font_tuple1,fg="blue")
    FI_1.place(x=725,y=100)
    PLACE_AREA=IntVar()
    PLACE_AREA=Entry(top, textvariable= PLACE_AREA, width=7)
    PLACE_AREA.place(x=750, y=130)

    FI_2=Label(top, text="% AREA CUENCA\n DE BAJA\n TRANSMISIVIDAD",font= Font_tuple1,fg="blue")
    FI_2.place(x=810,y=75)
    BT_AREA=DoubleVar()
    BT_AREA=Entry(top, textvariable= BT_AREA, width=7)
    BT_AREA.place(x=840, y=130)

    FI_3=Label(top, text="% AREA CUENCA\n DE ALTA\n TRANSMISIVIDAD",font= Font_tuple1,fg="blue")
    FI_3.place(x=905,y=75)
    AT_AREA=DoubleVar()
    AT_AREA=Entry(top, textvariable= AT_AREA, width=7)
    AT_AREA.place(x=930, y=130)

    FI_4=Label(top, text="% AREA \n DE BOSQUE",font= Font_tuple1,fg="blue")
    FI_4.place(x=995,y=75)
    AB_AREA=DoubleVar()
    AB_AREA=Entry(top, textvariable= AB_AREA, width=7)
    AB_AREA.place(x=1010, y=130)

    FI_5=Label(top, text="PRECIPITACION\n ANUAL (mm)",font= Font_tuple1,fg="blue")
    FI_5.place(x=1060,y=75)
    PP_AN=IntVar()
    PP_AN=Entry(top, textvariable= PP_AN, width=7)
    PP_AN.place(x=1080, y=130)

    FI_6=Label(top, text="% SUELO\nTIPO A",font= Font_tuple1,fg="blue")
    FI_6.place(x=1145,y=75)
    SUE_A=DoubleVar()
    SUE_A=Entry(top, textvariable= SUE_A, width=7)
    SUE_A.place(x=1150, y=130)

    FI_7=Label(top, text="% SUELO\nTIPO D",font= Font_tuple1,fg="blue")
    FI_7.place(x=1215,y=75)
    SUE_D=DoubleVar()
    SUE_D=Entry(top, textvariable= SUE_D, width=7)
    SUE_D.place(x=1220, y=130)

    FLOW_INDEX_CALC= Button(top, text="CALCULAR INDICE DE\n SEGURIDAD", command=CALC_FI, font= Font_tuple1,fg="blue")
    FLOW_INDEX_CALC.place(x=750, y=180)
    FLOW_INDEX2= Button(top, text= "AYUDA EN VOZ", command=HELP_HIDROLOGIA2, image=MSJ2)
    FLOW_INDEX2.place(x= 1100,y=30)

    BORRA_INDEX= Button(top, text= "BORRAR", command=BORRAR_INDEX, font= Font_tuple1,fg="blue")
    BORRA_INDEX.place( x= 770, y=230)
    
    
    pass
def BYBY_HYDR():
    top.destroy()
def HELP_CNN():
    subprocess.Popen("AYUDA_CN2.pdf", shell=True)
    
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("LA CURVA NUMÉRICA ES UN VALOR QUE INDICA LA PORCIÓN DE LA PRECIPITACIÓN QUE SE CONVIERTE EN ESCURRIMIENTO.\n\
    SU VALOR DEPENDE DE LA VEGETACIÓN, EL ESTADO QUE GUARDA ÉSTA Y DEL GRUPO HIDROLÓGICO DE SUELO.\n\
    LA CARACTERÍSTICA ESCENCIAL DEL GRUPO HIDROLÓGICO DE SUELO, ES LA CONDUCTIVIDAD HIDRÁULICA A SATURACIÓN.\n\
    ")
    converter.runAndWait()
    
##def HELP_WSH():
##    subprocess.Popen("AYUDA_WHS.pdf", shell=True)
def HELP_HIDROLOGIA2():
         
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.say("EL ÍNDICE DE SEGURIDAD ES UN VALOR QUE INDICA EL ESCURRIMIENTO AL TRIBUTARIO PRINCIPAL.\n\
        ES EL VALOR CON EL QUE SE DEBE DE COMPARAR LOS PLANES DE USO DEL AGUA DE LA CUENCA O TRIBUTARIO.\n\
        SE RECOMIENDA OBTENER ESTE ÍNDICE PARA LOS MESES DE MENOR PRECIPITACIÓN YA QUE SE OBTENDRÍA EL FLUJO BASE CRÍTICO.\n\
        EN EL BOTÓN, DISPONIBILIDAD DE ACUÍFEROS, APARECE UN DOCUMENTO EN PDF QUE DESCRIBE LAS CARACTERÍSITCAS HIDRÁULICAS DEL ACUÍFERO DE INTERÉS\n\
        CONSIDERA VARIABLES COMO LA TRANSMISIVIDAD DEL ACUÍFERO,LA CONDUCTIVIDAD HIDRÁULICA Y EL ÁREA DE DRENAJE.\n\
        LA TRANSMISIVIDAD ES EL PRODUCTO DE LA CONDUCTIVIDAD HIDRÁULICA Y EL ESPESOR DEL ACUÍFERO O ZONA ZATURADA.\n\
        PARA LOS TIPOS DE SUELO, CONSULTE LA AYUDA DE CURVA NUMÉRICA")
        converter.runAndWait()
        

        image = mpimg.imread("TRANSMISIVIDAD.png")
        plt.imshow(image)
        plt.show()
        
##        im = Image.open(r"TRANSMISIVIDAD.png")
##        im.show()
        
def HELP_HIDROLOGIA():
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.say("EN ESTE APARTADO, SE PODRÁ OBTENER EL HIDROGRAMA ADIMENSIONAL PARA LAS SUBCUENCAS EN QUE SE DIVIDA LA CUENCA.\n\
        ES NECESARIO INTRODUCIR TODOS LOS PARÁMETROS EN LOS ESPACIOS PROVEÍDOS EN CADA CUENCA. POSTERIORMENTE, SELECCIONAR EL ÁREA DEL COMBO\n\
        Y FINALMENTE PRESIONAR EL BOTÓN, CALCULAR, EN LA IMÁGEN DE LA CUENCA QUE SE TRATE.\n\
        EL BOTÓN ESCURRIMIENTO HISTÓRICO, GRAFICA EL ESCURRIMIENTO REGISTRADO EN EL PORTAL DEL BANCO DE AGUAS NACIONALES PARA LA RH ELEGIDA.\n\
        FINALMENTE, EL BOTON DISPONIBILIDAD DE ACUÍFEROS, LO LLEVARÁ AL PORTAL DE LA CONAGUA DONDE SE DESPLIEGAN VARIABLES DEL ACUÍFERO PARA EL ESTADO ELEGIDO.\n\
        ")
        converter.runAndWait()
def Q_EST():
    os.startfile("CUENCAS_GENERADOR\GENERADOR.exe") 

def Q_HIST():
    
    os.startfile("PLOT_DBASE\PLOT_BANDAS.exe")
    BANDASN = Button (top, text="BANDAS",command = BAND,image=APARATOSN)
    BANDASN.place(x=260, y=550)

##    converter = pyttsx3.init()
##    converter.setProperty('rate', 150)
##    converter.say("AL ELEGIR LA ESTACIÓN HIDROMÉTRICA,LA CLAVE DE ÉSTA DEBE SER DE CINCO DÍGITOS. SI EL NÚMERO ES SOLO DE CUATRO, AÑADIR UN CERO AL INICIO.\n\
##    DE HECHO EL SISTEMA AÑADE POR DEFAULT EL CERO AL INICIO. POR OTRO LADO, SI LA CLAVE ES DE CINCO DÍGITOS\n\
##    QUITAR EL CERO E INTRODUCIER LA CLAVE DE CINCO DÍGITOS.")
##    converter.runAndWait()
    

    BANDASN_LBL=Label(top, text="GEOGRAFIA BANDAS", font= Font_tuple2,fg="blue")
    BANDASN_LBL.place(x= 255, y=520)
    # os.startfile("READ_HYDR_2.exe")
def BAL_HIDRICO():
        pass
def lee_edo():
    
##    ESTADO = EDO.get()
    #ACTUAL=https://sigagis.conagua.gob.mx/gas1/sections/Edos/coahuila/coahuila.html
    
    EDO.get().lower()
    if EDO.get()=="BajaCalifornia":
        CURRENT_URL2=webbrowser.open_new(r'https://sigagis.conagua.gob.mx/gas1/sections/Edos/'+str(EDO.get())+str('/')+str('bc')+str('.html'))
    elif EDO.get()=="BajaCaliforniaSur":
        CURRENT_URL2=webbrowser.open_new(r'https://sigagis.conagua.gob.mx/gas1/sections/Edos/'+str(EDO.get())+str('/')+str('bcs')+str('.html'))
    else:
         
        CURRENT_URL2=webbrowser.open_new(r'https://sigagis.conagua.gob.mx/gas1/sections/Edos/'+str(EDO.get())+str('/')+str(EDO.get())+str('.html'))
        #CURRENT_URL2=webbrowser.open_new(r'https://sigagis.conagua.gob.mx/gas1/sections/Edos/'+str(EDO.get())+str('/')+str('son.html'))
def cierra():
    my_text.destroy()
    CIERRA_TEXT.destroy()

def LETS_GO():
        top20.destroy()
        EDO.destroy()
        NOMBRE_EDO.destroy()
        LEE_EDO.destroy()
        CIERRA.destroy()
def ACUIFERO():
    VISOR = webbrowser.open_new(r'https://sigagis.conagua.gob.mx/dma230911/')    
def CUENCA_ACUIF():
        
        os.startfile('ACUIFEROS.exe')
    
def ESTADO():
    global my_text
    global CIERRA_TEXT
    global EDO
    global CIERRA
    global EDO
    global NOMBRE_EDO
    global LEE_EDO
    global POR_ESTADO
    global POR_CUENCA
    global POR_ACUIFERO
    global top20
##    POR_ESTADO.destroy()

    top20=Toplevel()
    top20.geometry("650x500+0+0")
    EDO=StringVar()
    EDO=Entry(top20, textvariable= EDO, width=25)
    EDO.place(x=290,y=110)
    NOMBRE_EDO=Label(top20, text="INTRODUZCA EL ESTADO MAYUSCULAS O MINUSCULAS PEGADO\nEJEMPLO: quintanaroo, QUINTANAROO, sanluispotosi, SANLUISPOTOSI, zacatecas, ZACATECAS \n\
    EXCEPCIONES: BajaCalifornia, BajaCaliforniaSur",font= Font_tuple1,fg="blue")
    NOMBRE_EDO.place(x=150, y=40)

    LEE_EDO=Button(top20, text="LEER ESTADO", command=lee_edo)
    LEE_EDO.place(x= 330, y=150)

    CIERRA = Button(top20, text="CERRAR", command=LETS_GO)
    CIERRA.place(x= 335, y=190)
##    POR_CUENCA.destroy()
##    POR_ACUIFERO.destroy()
def pozo_by():
        ventana.destroy()
def POZOS_STAT():
        import pandas as pd
        import matplotlib.pyplot as plt
        import folium
        from bng_latlon import OSGB36toWGS84
        from folium.plugins import MarkerCluster
        import webbrowser
        global ventana
        global folium
        
        MarkerCluster()

        ventana = Tk()
        ventana.title(" ACUAC POZOS")
        width, height = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
        ventana.geometry("650x500+0+0")

        ANUNCIO = Label(ventana, text="SELECCIONE LA REGIÓN HIDROLÓGICA PARA\nDESPLEGAR LOS POZOS", fg="darkblue")
        ANUNCIO.place(x=200, y=30)
        
        SELECCIONE = Button(ventana, text="SELECCIONE RH", command = RH_SELEC, bd=5)
        SELECCIONE.place(x=50, y=100)

        SALIR= Button(ventana, text= "SALIR", command = pozo_by, bd=5)
        SALIR.place(x= 50, y=250)
        
def ELEGISTE(event):
            region=clickREGION.get()
            print(region)

            df = pd.read_csv('DATOS.csv', index_col=0, encoding='latin-1')
            df2 = pd.read_csv('C:\DATOS_POZOS_NAL\POZOS_GEO.csv', index_col=0, encoding='latin-1')
            ##row1 = df.iloc[[2, 3, 5, 6]]
            ##dato=df.iloc[1,15],df.iloc[1,16],df.iloc[1,17],df.iloc[1,18]
            ##datos=1,2,3,4
            ##plt.plot(datos,dato)
            ##plt.show()
            #region="Rio Ameca"
            #region2="RH010"
            TEMPORAL8=df[df["nom_rh"]==region]
            TEMPORAL9=TEMPORAL8.to_excel("TEMPORAL9.xlsx")

            TEMPORAL10=df2[df2["nom_rh"]==region]
            lat=TEMPORAL10['y']
            lon=TEMPORAL10['x']
            print(lat)
            df4=pd.read_excel('TEMPORAL9.xlsx')
            
            m = folium.Map(location=[lat,lon], tiles="Stamen Terrain", zoom_start=10)
            #m = folium.Map(location=[lat,lon], tiles="Mapbox", zoom_start=10)
            mcluster=MarkerCluster(name="cale").add_to(m)
            folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                                name='HIDROLOGIA',
                                attr='OpenTopoMap').add_to(m)
            for _, r in df4.iterrows():

            ##            html = df4.loc[_,['CLAVE_SITIO','NOMBRE DEL SITIO','MUNICIPIO','LATITUD','LONGITUD']].to_frame().T.to_html(
            ##            )
                        html = df4.loc[_,['nom_pozo','nom_acuif','nom_edo','nom_rh', 'LATITUD', 'LONGITUD','elev_ne']].to_frame().T.to_html(
                        )
                        classes="table table-striped table-hover table-condensed table-responsive"
                        folium.Marker(
                         location=[df4.iloc[_]['LATITUD'], df4.iloc[_]['LONGITUD']],
                         
                         popup = folium.Popup(html, max_width=500),icon=folium.Icon(color='red',icon='info-sign'),
                         ).add_to(mcluster)

                                 

            map_title = "Pozos en la región "+str(clickREGION.get())
            title_html = f'<h1 style="position:absolute;z-index:150000;left:40vw" >{map_title}</h1>'
            m.get_root().html.add_child(folium.Element(title_html))    
            m.save("map.html")
            webbrowser.open("map.html")
    
def RH_SELEC():
                
                global clickREGION
                option =[
                              "REGIONES HIDROLOGICAS",
                              "Armeria-Coahuayana",
                              "B.C. Centro Este",
                              "B.C. Centro Oeste",
                              "B.C. Suroeste",
                              "B.C. Noreste",
                              "Balsas",
                              "Bravo-Conchos",
                              "Coatzacoalcos",
                              "Costa Chica de Guerrero",
                              "Costa de Chiapas",
                              "Costa de Jalisco",
                              "Costa de Michoacan",
                              "Costa de Oaxaca",
                              "Costa Grande de Guerrero",
                              "Cuencas Cerradas del Norte",
                              "El Salado",
                              "Grijalva-Usumacinta",
                              "Lerma-Santiago",
                              "Mapimi",
                              "Nazas Aguanaval",
                              "Norte de Veracruz",
                              "Panuco",
                              "Papaloapan",
                              "Presidio-San Pedro",
                              "Rio Ameca",
                              "Rio Colorado",       
                              "Rio Huicicila",
                              "San Fernando-Soto la Marina",
                              "Sinaloa",
                              "Sonora Norte",
                              "Sonora Sur",
                              "Tehuantepec",
                              "Yucatan Este",
                              "Yucatan Norte",
                              "Yucatan Oeste"
              
                        ]
                clickREGION =StringVar()
                clickREGION.set(option[0])
                drop4=OptionMenu(ventana,clickREGION, *option,command= ELEGISTE)
                drop4["menu"].config(bg="light BLUE")
                drop4.place(x=40, y=200)
                    
                



def BY_ACUIF():
        POR_ACUIFERO.destroy()
        POR_CUENCA.destroy()
        POR_ESTADO.destroy()
        POR_POZO.destroy()
        BORRA_ACUIF.destroy()
        BAL_HIDR = Button(top, image = REALTIME,command = TIEMPO_REAL)
        BAL_HIDR.place(x= 400,y=550)
        BAL_HIDR_LBL = Label(top, text= "BALANCE HIDRICO",font= Font_tuple2,fg="blue")
        BAL_HIDR_LBL.place(x=415, y=520)
def DISP_ACUI():
    global my_text
    global CIERRA_TEXT
    global EDO
    global CIERRA
    global EDO
    global NOMBRE_EDO
    global LEE_EDO
    global POR_ESTADO
    global POR_CUENCA
    global POR_ACUIFERO
    global BORRA_ACUIF
    global POR_POZO
    
    POR_ACUIFERO = Button(top, text="CONSULTA POR ACUIFERO", command=ACUIFERO, bd=5)
    POR_ACUIFERO.place(x=340, y=360)
    
    POR_ESTADO = Button(top, text="CONSULTA POR ESTADO", command=ESTADO,bd=5)
    POR_ESTADO.place(x= 340, y=460)

    POR_CUENCA = Button(top, text="CONSULTA POR CUENCA", command=CUENCA_ACUIF,bd=5)
    POR_CUENCA.place(x=340, y=410)

    POR_POZO = Button(top, text="CONSULTA POZOS", command = POZOS_STAT, bd=5)
    POR_POZO.place( x= 500, y=460)

    BORRA_ACUIF = Button(top, text="BORRAR ACUIFEROS", command = BY_ACUIF, bd=5)
    BORRA_ACUIF.place(x=340, y=300)
    
##    my_text=Text(top, height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
##    my_text.place(x= 590, y=380)
##    
##    my_text.insert(END, "INTRODUZCA EL ESTADO Y PRESIONE LEER ESTADO. YA EN LA PÁGINA, PUEDE CONSULTAR EL ACUÍFERO DE INTERÉS.\n\
##    AHI ENCONTRARÁ LA INFORMACIÓN DE LOS ACUÍFEROS DEL ESTADO. PARA MEJOR VISUALIZACIÓN, DESPLÁCESE HASTA EL FINAL DE LA PÁGINA DONDE APARECE EL LOGO DE LA CONAGUA Y CIÉRRELO PRESIONANDO OKAY.\n\
##    ABAJO, PRESIONE AMPLIAR MAPA. POSICIÓNESE CON EL MOUSE EN EL ACUÍFERO DE INTERÉS PARA DESPLEGAR EL ESTADO ACUTAL DEL ACUÍFERO\n\
##    PUEDE USAR LOS BOTONES A LA IZQUIERDA DEL MAPA PARA CONTROL DE VISUALIZACIÓN")
##    CIERRA_TEXT=Button(top, text="CERRAR", command=cierra)
##    CIERRA_TEXT.place(x=600, y=500)
    
##    EDO=StringVar()
##    EDO=Entry(top, textvariable= EDO, width=25)
##    EDO.place(x=340,y=410)
##    NOMBRE_EDO=Label(top, text="INTRODUZCA EL ESTADO MAYUSCULAS O MINUSCULAS PEGADO\nEJEMPLO: quintanaroo, QUINTANAROO, sanluispotosi, SANLUISPOTOSI, zacatecas, ZACATECAS \n\
##    EXCEPCIONES: BajaCalifornia, BajaCaliforniaSur",font= Font_tuple1,fg="blue")
##    NOMBRE_EDO.place(x=200, y=340)
##
##    LEE_EDO=Button(top, text="LEER ESTADO", command=lee_edo)
##    LEE_EDO.place(x= 380, y=450)
##
##    CIERRA = Button(top, text="CERRAR", command=LETS_GO)
##    CIERRA.place(x= 385, y=490)
##    pass
def REGRESION():
      os.startfile("IA_CN.exe")
def RED():
      os.startfile("RED_NEUR.exe")
def AI_ALGORITHM():
      REGR = Button(top, text= "IA_REGR", command = REGRESION, bd=5)
      REGR.place(x=1040,y=440)

      NEURAL = Button(top, text= "IA_RED NEURAL", command = RED, bd=5)
      NEURAL.place(x= 1125, y=440)
      #os.startfile("IA_CN.exe")
def adios():
    top3.destroy()    
def cuencas():
##    nombre2="R. del Carmen"
##    shape2 = gpd.read_file("C:\CUENCAS_NAL\ACUAC_SUBCUENC.SHP")#.decode('utf-8', errors='ignore'))
##    df2 = pd.DataFrame(data=shape2)
##    TEMPORAL22 = df2[df2["SUBCUENCA"]==(nombre2)]
##    TEMPORAL22 =shape2[shape2["SUBCUENCA"].isin([nombre2])]
##    TEMPORAL44= TEMPORAL22[["AREA_KM2"]]
##    f=TEMPORAL22.plot("AREA_KM2")#, cmap="Set1")
##    plt.suptitle('EL AREA DE LA CUENCA '+str(nombre2)+str(' es =')+str(TEMPORAL44)+str(' Ha'))
##    plt.xlabel("LONGITUD")
##    plt.ylabel("LATITUD")
##    TEMPORAL33=TEMPORAL22[["area","rh","rha","descripcio"]]
##    plt.show()

    global LA
    global LO
    nombre=CUENC.get()
    TEMPORAL2 = df[df["cuenca"]==(nombre)]
    TEMPORAL2 =shape[shape["cuenca"].isin([nombre])]
    TEMPORAL4= TEMPORAL2[["area"]]
    f=TEMPORAL2.plot("area")#, cmap="Set1")
    plt.suptitle('EL AREA DE LA CUENCA '+str(nombre)+str(' es =')+str(TEMPORAL4)+str(' Ha'))
    plt.xlabel("LONGITUD")
    plt.ylabel("LATITUD")
    TEMPORAL3=TEMPORAL2[["area","rh","rha","descripcio"]]
    plt.show()
    TEXTO2=Label(top3, text=",\n\
        DEBE NOTARSE QUE. EN MUCHOS CASOS\n\
        NO TODA LA SUBCUENCA DRENA A LA PARCELA.\n\
        EL ALGORITMO SIRVE PARA DIMENSIONAR\n\
        EL AREA PARCIAL CONOCIENDO EL AREA TOTAL.", fg="blue", font = ('Helvetica','8','bold'))
    TEXTO2.place(x=290, y=250)
    text = nombre
    GRANDE = text.upper()

    UBICACION=Label(top3, text="ENTRE COORDENADAS DE LA PARCELA")
    UBICACION.place(x=330, y=325)

    LA=IntVar()
    LA=Entry(top3, textvariable=LA, width=10,bd=3, bg="white",fg="black",font=("arial", "10"))
    LA.place(x=400, y=350)
    LATL=Label(top3, text="LAT", fg="blue",font=("arial", "10"))
    LATL.place(x= 370, y=350)

    LO=IntVar()
    LO=Entry(top3, textvariable=LO, width=10,bd=3, bg="white",fg="black",font=("arial", "10"))
    LO.place(x=400, y=380)
    LOTL=Label(top3, text="LON", fg="blue",font=("arial", "10"))
    LOTL.place(x= 370, y=380)
    
    ELIGE_SUBCUENCA= Button(top3, text="SUBCUENCAS DE LA CUENCA: "+str(GRANDE), command=subcuencas,bd=6,bg="dark blue",fg="white")
    ELIGE_SUBCUENCA.place(x=330, y=440)
    

    
   
def subcuencas():
    
##    SUBCUENC=StringVar()
##    SUBCUENC=Entry(top3, textvariable=SUBCUENC, width=20,bd=3, bg="white",fg="black",font=("arial", "10"))
##    SUBCUENC.place(x=400, y=400)
##    SUB=Label(top3, text="NOMBRE\nSUBCUENCA", fg="blue",font=("arial", "10"))
##    SUB.place(x= 270, y=390)
    
    global TEMPORAL6
    shape2 = gpd.read_file("C:\CUENCAS_NAL\ACUAC_SUBCUENC.SHP")#.decode('utf-8', errors='ignore'))
    
    df3 = pd.DataFrame(data=shape2)
    nombre3=CUENC.get()
    print(nombre3)
    TEMPORAL8 =df3[df3["cuenca"]==nombre3]
    TEMPORAL8 =shape2[shape2["cuenca"].isin([nombre3])]
    TEMPORAL6= TEMPORAL8[["AREA2","SUBCUENCA"]]
    TEMPORAL8.plot("AREA2", cmap="coolwarm")
    df9=pd.DataFrame(TEMPORAL6)
    ax = TEMPORAL8.plot(
        figsize=(16,10),
        column="SUBCUENCA",
        legend=True,
        cmap="tab20",
        legend_kwds=dict(bbox_to_anchor=(1.05, 1.15), loc='upper left',fontsize="7"),
        ax=plt.gca(),
        missing_kwds={"color":"white"},)

    
    #plt.suptitle('AREA DE SUBCUENCAS '+str(TEMPORAL6)+str(' Ha'))
    
    
    ROLLO= "\n\
        LA GRAFICA MUESTRA AREAS TOTALES\n\
        DE LAS SUBCUENCAS\n\
        AUNQUE SOLO SE TRASLAPE\n\
        UNA PEQUEÑA PORCIÓN \n\
        EN LA CUENCA\n\
        ELEGIDA"
    text2 = nombre3
    GRANDE2 = text2.upper()
    plt.title("SUBCUENCAS DE LA CUENCA: "+str(GRANDE2))
    plt.figtext(0.01,0.1,''+str(ROLLO))
    plt.figtext(0.05, 0.5, ''+str(TEMPORAL6))
    plt.xlabel("LONGITUD")
    plt.ylabel("LATITUD")
    
    
    
    
    from matplotlib.patches import Arrow, Circle
    from matplotlib.widgets import Button
    
    def add(val):
            plt.figtext(0.8,0.6,"ARCHIVO GUARDADO\nEN LA CARPETA SUBC")
            SUBCLBL = Label(top3, text= "ARCHIVO GUARDADO EN CARPETA SUBC",bg="yellow",fg="black")
            SUBCLBL.place(x= 300,y=415)
            TEMPORAL8.to_file("SUBC\SUBCUENCAS.shp")
            plt.plot(LO.get(),LA.get(), "og", markersize=15) 
            
    axes = plt.axes([0.81, 0.000001, 0.10, 0.075])
    bnext = Button(axes, 'GUARDAR',color="yellow")
    bnext.on_clicked(add)
        
    TEMPORAL8.to_file("TEMPORAL8.shp")
    TEMPORAL8.to_file("C:\CUENCAS_NAL\TEMPORAL8.SHP")
    x=LO.get()
    y=LA.get()
    print(x,y)
    plt.plot(x,y, "og", markersize=8)
    plt.show()
    
    import folium
    
    
    tooltip="UBICACION DE PARCELA "+str("LAT ")+str(y)+str(" ")+str("LON ") +str(x)
    LDN_COORDINATES = (y, x)#(value,value2)#26.533, -107.517
    m= folium.Map(location=LDN_COORDINATES, zoom_start=8)#,tiles="Stamen Terrain")

    uno= folium.map.Marker(location=[y,x], popup="name",icon=folium.Icon( icon='cloud',color ='blue'),tooltip=tooltip).add_to(m)
    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                    name='HIDROLOGIA',
                    attr='OpenTopoMap').add_to(m)
    loc = 'UBICACION DE LA PARCELA A DONDE DRENA LA SUBCUENCA.DE CLICK EN EL ICONO PARA CONOCER AREAS DE LAS SUBCUENCAS '#+str('  SELECCIONE LA VISTA DESEADA EN LA ESQUINA SUPERIOR DERECHA')
    title_html = '''
         <h3 align="center" style="font-size:16px"><b>{}</b></h3>
         '''.format(loc)
    m.get_root().html.add_child(folium.Element(title_html))

    
    
    html = '<img src="data:image/png;base64,{}">'.format
    popup = folium.Popup( ""+str(TEMPORAL6),max_width=800, min_width=800)
    #popup="  "+str("AREAS")+str(" ")+str(TEMPORAL6)
    folium.Marker(location=[y,x], tooltip=tooltip, popup = popup, 
    icon=folium.Icon(color = 'blue')).add_to(m)

    geopath= TEMPORAL8.geometry.to_json()
    
    poligonos= folium.features.GeoJson(geopath)
    m.add_child(poligonos)

    print(df9)
    df=gpd.read_file(geopath)
    df = df.to_crs(epsg=2263)

# Access the centroid attribute of each polygon
    df["centroid"] = df.centroid
    df = df.to_crs(epsg=2263)
    df["centroid"] = df.centroid
    df = df.to_crs(epsg=4326)
    df["centroid"] = df["centroid"].to_crs(epsg=4326)
    i=0
    shape5 = gpd.read_file("C:\CUENCAS_NAL\TEMPORAL8.SHP")
    df5 = pd.DataFrame(data=shape5)
    for _, r in df.iterrows():
    
            lat = r["centroid"].y
            lon = r["centroid"].x
            
            folium.Marker(
                location=[lat, lon],
                popup=(df5.loc[_,['AREA2','SUBCUENCA']])
                ).add_to(m)
            
##            for l in range(0,len(df)):
##                    html = df.loc[l,['id']].to_frame().T.to_html(
##                    classes="table table-striped table-hover table-condensed table-responsive"
##                    )
##                    folium.Marker(
##                    location=[lat,lon],
##                    popup = folium.Popup(html, max_width=500),
##                    ).add_to(m)
##            m.save("map.html")
##            webbrowser.open("map.html")
                    
##            for _,k in df9.iterrows():
##                           folium.Marker(
##                           location=[lat,lon],
##                           popup="AREA (has): {} <br> NOMBRE SUBCUENCA: {}".format(k["AREA2"], k["SUBCUENCA"]),# <br> NOMBRE SUBCUENCA: {}".format(r,k["AREA2"],r,k["SUBCUENCA"]),                            
##                            
##                           ).add_to(m)
##                    
##                    
##                    
##            i=i+1

    
##    for _,k in df9.iterrows():
##    
##            
##            folium.Marker(
##                    location=[lat,lon],
##                        popup="AREA (has): {} <br> NOMBRE SUBCUENCA: {}".format(k["AREA2"],k["SUBCUENCA"]),
##                         
##                        ).add_to(m)
##            
##            print("este es",k)
            
     
    icon_1 = "SUBC\SUBCUENCAS.shp"
    icon = folium.features.CustomIcon(icon_1,icon_size=(40, 40))
    folium.Marker([y,x],icon=icon).add_to(m)
    
    folium.LayerControl().add_to(m)
    m.save('map-with-title.html')
    webbrowser.open("map-with-title.html")
    
    
    
def REGIONES():
    global CUENC
    
    nombre2=RH.get()
    TEMPORAL3 =df[df["clvrh"]==nombre2]
    TEMPORAL3 =shape[shape["clvrh"].isin([nombre2])]
    TEMPORAL5= TEMPORAL3[["rha"]]
    TEMPORAL3.plot("rha", cmap="coolwarm")
    
    TEMPORAL6=TEMPORAL3[["cuenca"]]
    plt.rcParams["figure.figsize"] = (28, 10)
    
    #plt.show()
    ax = TEMPORAL3.plot(
        figsize=(16,10),
        column="cuenca",
        legend=True,
        cmap="tab20",
        legend_kwds=dict(bbox_to_anchor=(1.05, 1.15), loc='upper left',fontsize="7"),
        ax=plt.gca(),
        missing_kwds={"color":"white"},)
    
    leg1 = ax.get_legend()
    for ea in leg1.legend_handles:
            ea.set_marker('s')
            ea.set_markeredgewidth(0.02)
            
    df2=pd.DataFrame(TEMPORAL6)
    CONVERTIDO=df2.to_string()
    my_texti2=Text(top3, height=15, width=40, wrap=WORD, bd=3,relief='solid',bg="pink",fg="blue",font=('Helvetica','7','bold'))
    my_texti2.place(x= 420, y=30)
    my_texti2.insert(END, TEMPORAL6,"\n")
    plt.title("CUENCAS EN LA "+str(nombre2))
    plt.xlabel("LONGITUD")
    plt.ylabel("LATITUD")
    plt.show()

    CUENC=StringVar()
    CUENC=Entry(top3, textvariable=CUENC, width=20,bd=3, bg="white",fg="black",font=("arial", "10"))
    CUENC.place(x=100, y=300)
    RHL=Label(top3, text="NOMBRE\nCUENCA", fg="blue",font=("arial", "10"))
    RHL.place(x= 30, y=290)

    
    ELIGE_CUENCA= Button(top3, text="ELIGE CUENCA", command=cuencas)
    ELIGE_CUENCA.place(x=100, y=340)

##    shape2 = gpd.read_file("C:\CUENCAS_NAL\ACUAC_SUBCUENC.SHP")#.decode('utf-8', errors='ignore'))
##    df3 = pd.DataFrame(data=shape2)
##    nombre3=CUENC.get()
##    print(nombre3)
##    TEMPORAL8 =df3[df3["cuenca"]==nombre3]
##    
##    TEMPORAL8 =shape2[shape2["cuenca"].isin([nombre3])]
##    TEMPORAL6= TEMPORAL8[["cuenca"]]
##    TEMPORAL8.plot("cuenca", cmap="coolwarm")
##    ax = TEMPORAL8.plot(
##        figsize=(16,10),
##        column="SUBCUENCA",
##        legend=True,
##        cmap="tab20",
##        legend_kwds=dict(bbox_to_anchor=(1.05, 1.15), loc='upper left',fontsize="7"),
##        ax=plt.gca(),
##        missing_kwds={"color":"white"},)
##    plt.show()

    
    

    
    
    
    
def area_help():
        import geopandas as gpd
        global RH
        global df
        global shape
        global top3

        top3=Toplevel()
        top3.geometry("650x500+0+0")

        TEXTO2= Label(top3, text="AYUDA PARA DIMENSIONAR EL ÁREA DE SUBCUENCA\n\
        QUE DRENA A LA PARCELA",fg="blue", font = ('Helvetica','10','bold'))
        TEXTO2.place(x=2, y=10)
        TEXTO= Label(top3, text=",\n\
        INTRODUZCA EL NOMBRE DE LA REGION HIDROLÓGICA\n\
        COMO SE INDICA EN EL EJEMPLO. POSTERIORMENTE\n\
        INTRODUZCA EL NOMBRE DE LA CUENCA DONDE SE \n\
        ENCUENTRA LA PARCELA. CIERRE LOS MAPAS COMO\n\
        VAYAN APARECIENDO PARA QUE SE ACTIVEN \n\
        LOS BOTONES. EL NOMBRE DE LA REGION HIDROLÓGICA\n\
        ES RH + 3 DÍGITOS; EJEMPLO: RH001, RH010, RH036, ETC.", fg="blue", font = ('Helvetica','8','bold'))
        TEXTO.place(x=2, y=50)
        
        shape = gpd.read_file("C:\CUENCAS_NAL\ACUAC_CUENCAS.SHP")#.decode('utf-8', errors='ignore'))
        df = pd.DataFrame(data=shape)
        
        RH=StringVar()
        RH=Entry(top3, textvariable=RH, width=10,bd=3, bg="white",fg="black",font=("arial", "10"))
        RH.place(x=100, y=220)
        RHL=Label(top3, text="CLAVE RH", fg="blue",font=("arial", "10"))
        RHL.place(x= 20, y=220)

        RHL2= Label(top3, text="EJEMPLO: RH036")
        RHL2.place(x= 100, y=190)

        ELIGERH= Button(top3, text="RH", command=REGIONES)
        ELIGERH.place(x= 100, y=250)

##        ELIGECUENC=Button(top3, text="CUENCAS")#, command=REGIONES)
##        ELIGECUENC.place(x= 300, y=300) 

        SALE= Button(top3, text="SALIR", command =adios)
        SALE.place(x= 100, y=450)
        
        pass
def MANUAL_HYDR():
        #subprocess.Popen('E:\PROGRAMAR_PAITON\CUENCAS\AYUDAS_ACUAC\HIDROLOGÍA.PDF',shell=True)
        subprocess.Popen('HIDROLOGÍA.PDF',shell=True)
       
def calculos():
    #IRSE.destroy()    
    global AREA3_PP
    global LONG_PEND3_S
    global AREA3_CN
    global AREA3
    global CE3
    global AREA3_PEND
    global top
    global clickAREA
    global PEND_S

    global AREA2_PP
    global LONG_PEND2_S
    global AREA2_CN
    global AREA2
    global AREA2_PEND
    global CE2
    global AREA2_2

    global AREA1_PP
    global LONG_PEND1_S
    global AREA1_CN
    global AREA1
    global AREA1_PEND
    global CE1
    global AREA1_1
    global clickTEMAS
    global top
    global drop4
    global option11
    global top

    
    top=Toplevel()
    top.geometry("1500x1100+0+0")
    suelo_label=Label(top, image=suelo)
    suelo_label.place(x=550,y=320)
    INSTRUCCIONES= Label(top, text="ES RECOMENDABLE DIVIDIR LA CUENCA EN SUB AREAS\n PARA EL CÁLCULO DEL ESCURRIMIENTO",font= Font_tuple2,fg="blue")
    INSTRUCCIONES.place(x= 720, y= 280)

    HELP_HIDRO= Button(top, text= "AYUDA EN VOZ", command=HELP_HIDROLOGIA,image=MSJ2)
    HELP_HIDRO.place(x= 90,y=15)
    HELP_HIDRO_lbl= Label (top, text= "AYUDA ",font= Font_tuple1,fg="blue")
    HELP_HIDRO_lbl.place(x=90,y=0)

    HELP_CN= Button(top, text= "AYUDA CN", command =HELP_CNN, font= Font_tuple1,fg="blue")
    HELP_CN.place(x=40, y=100)

    INTELLIGENCE = Button(top, image=ARTIFICIAL, bd=7, command = AI_ALGORITHM)
    INTELLIGENCE.place(x= 1030, y=525)
    INTELLIGENCE_lbl =Label(top, text= "MACHINE LEARNING\n ESTIMACIÓN RELACION P_Q", font=Font_tuple1,fg="blue")
    INTELLIGENCE_lbl.place(x=1030, y =490)
    

##    HELP_CUENCA = Button(top, text= "FIGURA DE AYUDA", command =HELP_WSH, font= Font_tuple1,fg="blue")
##    HELP_CUENCA.place(x=740, y=100)

    FLOW_INDEX= Button(top,  command=FI, font= Font_tuple1,fg="blue",image=PELIGRO)
    FLOW_INDEX.place(x=950, y=5)

    FLOW_INDEX_LABEL =Label(top, text="INDICE DE SEGURIDAD",font= Font_tuple1,fg="blue")
    FLOW_INDEX_LABEL.place(x=820, y=35)

            
    BYBY= Button(top, text="SALIR", command= BYBY_HYDR,font= Font_tuple1,fg="blue")
    BYBY.place(x=110, y=650)

    PRESENTACION_HOJA= Label(top, text= "INTRODUCIR EN LOS ESPACIOS INDICADOS LAS CARACTERÍSITCAS DE LAS ÁREAS DE LA CUENCA ",font= Font_tuple2,fg="blue")
    PRESENTACION_HOJA.place(x=40, y=50)
    option10 =[
              "SELECCIONE AREA",
              "AREA1",
              "AREA2",
              "AREA3",
              "PONDERADO"
              
            ]
    clickAREA =StringVar()
    clickAREA.set(option10[0])
    drop3=OptionMenu(top,clickAREA, *option10, command= calcular2)
    drop3["menu"].config(bg="light BLUE")
    drop3.place(x=100, y=280)
                   

    TEXT1=Label(top, text="CN")
    TEXT1.place(x=160,y=100)
    TEXT1_1=Label(top, text="AREA (ha)")
    TEXT1_1.place(x= 250, y=100)
    AREA_HELP= Button(top, text="AYUDA_AREA", command=area_help)
    AREA_HELP.place(x=240, y=240)
    AREA1_LBL= Label(top, text= "AREA 1")
    AREA1_LBL.place(x=50, y=130)
    
    AREA1_CN=DoubleVar()
    AREA1_CN=Entry(top, textvariable= AREA1_CN, width=10)
    AREA1_CN.place(x=140, y=130)
    
    AREA1_PP=DoubleVar()
    AREA1_PP= Entry(top, textvariable=AREA1_PP, width =10)
    AREA1_PP.place(x= 360, y=130)
    AREA1_LBL2= Label(top, text="PP (mm)")
    AREA1_LBL2.place(x= 370, y=100)

    AREA1=DoubleVar()
    AREA1=Entry(top, textvariable= AREA1, width=10)
    AREA1.place(x=250, y=130)

    AREA2_LBL= Label(top, text= "AREA 2")
    AREA2_LBL.place(x=50, y=170)
    
    AREA1=DoubleVar()
    AREA1=Entry(top, textvariable= AREA1, width=10)
    AREA1.place(x=250, y=130)
    
    AREA2=DoubleVar()
    AREA2=Entry(top, textvariable= AREA2, width=10)
    AREA2.place(x= 250, y=170)

    AREA2_PP=DoubleVar()
    AREA2_PP=Entry(top, textvariable= AREA2_PP, width=10)
    AREA2_PP.place(x= 360, y=170)

    AREA2_CN=DoubleVar()
    AREA2_CN=Entry(top, textvariable= AREA2_CN, width=10)
    AREA2_CN.place(x= 140, y=170)

    AREA3_LBL= Label(top, text= "AREA 3")
    AREA3_LBL.place(x=50, y=210)

    AREA3_CN=DoubleVar()
    AREA3_CN=Entry(top, textvariable= AREA3_CN, width=10)
    AREA3_CN.place(x= 140, y=210)

    AREA3=DoubleVar()
    AREA3=Entry(top, textvariable= AREA3, width=10)
    AREA3.place(x=250, y=210)

    AREA3_PP=DoubleVar()
    AREA3_PP=Entry(top, textvariable= AREA3_PP, width=10)
    AREA3_PP.place(x= 360, y=210)

    PEND1=Label(top, text="PENDIENTE (%)")
    PEND1.place(x=450,y=100)
    
    AREA1_PEND=IntVar()
    AREA1_PEND = Entry(top, textvariable= AREA1_PEND, width=10)
    AREA1_PEND.place(x=460, y=130)

    AREA2_PEND=DoubleVar()
    AREA2_PEND=Entry(top, textvariable= AREA2_PEND, width=10)
    AREA2_PEND.place(x=460,y=170)

    AREA3_PEND=DoubleVar()
    AREA3_PEND=Entry(top, textvariable= AREA3_PEND, width=10)
    AREA3_PEND.place(x=460,y=210)

    LONG_PEND1=Label(top, text="LONGITUD\n PENDIENTE (m)")
    LONG_PEND1.place(x=540,y=90)

    LONG_PEND1_S=DoubleVar()
    LONG_PEND1_S = Entry(top, textvariable= LONG_PEND1_S, width=10)
    LONG_PEND1_S.place(x=550, y=130)

    LONG_PEND2_S=DoubleVar()
    LONG_PEND2_S = Entry(top, textvariable= LONG_PEND2_S, width=10)
    LONG_PEND2_S.place(x=550, y=170)

    LONG_PEND3_S=DoubleVar()
    LONG_PEND3_S = Entry(top, textvariable= LONG_PEND3_S, width=10)
    LONG_PEND3_S.place(x=550, y=210)

    CE =Label(top, text="CE")
    CE.place(x=660,y=100)

    CE1=DoubleVar()
    CE1 = Entry(top, textvariable= CE1, width=10)
    CE1.place(x=640, y=130)

    CE2=DoubleVar()
    CE2 =Entry(top, textvariable= CE2, width=10)
    CE2.place(x=640, y=170)

    CE3=DoubleVar() 
    CE3 = Entry(top, textvariable= CE3, width=10)
    CE3.place(x=640, y=210)

    CALCULAR1= Button(top, text="CALCULAR 1", command = calcular,font=('Times New Roman',6,'bold'),bg="light blue")
    CALCULAR1.place(x=830, y=390)

    CALCULAR2= Button(top, text="CALCULAR 2", command = calcular, font=('Times New Roman',6,'bold'),bg="light blue")
    CALCULAR2.place(x=700, y=460) 
    
    CALCULAR3= Button(top, text="CALCULAR 3", command = calcular,font=('Times New Roman',6,'bold'),bg="light blue")
    CALCULAR3.place(x=940, y=440)

    USER_MANUALHYDR = Button(top, text="MANUAL USUARIO\nHIDROLOGIA", bd=5,command=MANUAL_HYDR, font=('Times New Roman',6,'bold'),fg="blue")
    USER_MANUALHYDR.place(x=500, y=10)

   
  
##    ESCURRIMIENTO=Button(top,  command=Q_EST, image=QESTOCASTICO,font=('Times New Roman',6,'bold'),bd=10)
##    ESCURRIMIENTO.place(x=60,y=410)
##
##    ESCURRIMIENTO_LBL= Label(top,text="ESCURRIMIENTO ESTOCASTICO", font= Font_tuple2,fg="blue")
##    ESCURRIMIENTO_LBL.place(x=40, y=380)
                            
    BANDAS=Button(top,  image=QHISTORICO,command=Q_HIST, font=('Times New Roman',6,'bold'),bd=10)
    BANDAS.place(x=60,y=550)
    BANDAS_LBL=Label(top, text="ESCURRIMIENTO HISTÓRICO",font= Font_tuple2,fg="blue")
    BANDAS_LBL.place(x=40, y=520)

##    BAL_HIDR = Button(top, image = REALTIME,command = TIEMPO_REAL)
##    BAL_HIDR.place(x= 400,y=550)
##    BAL_HIDR_LBL = Label(top, text= "BALANCE HIDRICO",font= Font_tuple2,fg="blue")
##    BAL_HIDR_LBL.place(x=415, y=520)

    ACUIFEROS= Button(top, image =AQUIFER,command=DISP_ACUI,bd=5)
    ACUIFEROS.place(x=60, y=410)
    ACUIFEROS_LBL= Label(top, text= "DISPONIBILIDAD ACUIFEROS", font= Font_tuple2,fg="blue")
    ACUIFEROS_LBL.place(x= 40, y=380)

    
##    option11 =[
##              
##              "TEMAS DE CONSULTA",
##              "CAPTACION DE AGUA DE LLUVIA",
##              "DISTRITOS DE RIEGO",
##              "POTENCIAL PRODUCTIVO",
##              "HIDROLOGÍA",
##              "ALTERNATIVAS CONSERVACION",
##              "AGENDAS TECNOLOGICAS"
##              
##            ]
##    clickTEMAS =StringVar()
##    clickTEMAS.set(option11[0])
##    drop4=OptionMenu(root,clickTEMAS, *option11, command= KNOWLEDGE_BASE)
##    drop4["menu"].config(bg="light BLUE")
##    drop4.place(x=150, y=220)
def NASAIN():
    
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("AQUÍ, INGRESARÁ A UN PORTAL QUE PRESENTA DIVERSAS VARIABLES CLIMÁTICAS Y DEL AMBIENTE\n\
    PUEDE REALIZAR ZOOM PARA ACERCARSE A ALGUN LUGAR, PUEDE BUSCAR LUGARES POR NOMBRE.\n\
    TAMBIÉN, PUEDE PROYECTAR EL ESCENARIO EN EL TIEMÓ CERCANO UTILIZANDO LA BARRA DE ABAJO")
    converter.runAndWait()
    
    NASA1=PhotoImage(file='NASA.png', master=root)
    webbrowser.open("https://www.windy.com/es/-Temperatura-temp?temp,24.645,-103.021,8,m:ecnade7")#"https://www.nnvl.noaa.gov/view/globaldata.html",new=2, autoraise=True)
def weather():
    Font_tuple1=("Comic Sans MS", 7, "bold")
    def borrar():
        pass
        ciudad.destroy()
        desc.delete(0,END)
        press.destroy()
        hum.destroy()

    def mostrar_respuesta (clima):
        global press
        global presion
        global ciudad
        global desc
        global press
        global hum
        try:
                nombre_ciudad = clima["name"]
                desc = clima["weather"] [0] ["description"]
                temp =clima["main"] ["temp"]
                press=clima["main"]["pressure"]
                hum=clima["main"]["humidity"]
               
                ciudad ["text"] = nombre_ciudad
                temperatura ["text"] = str(int(temp))+"°C"
                descripcion ["text"] = desc
                presion ["text"]=press#str(int(temp_max))+"°C"
                humedad["text"]=hum
                press =Label (text = "Presion Atmósferica (mb)")
                press.place (x= 120, y=360)
                humi=Label(text= "Humedad (%) ")
                humi.place(x= 140, y= 400)
                pronos=Label(text="Si presión\n < a 1009 mb\n probable lluvia",  font = ("Courier", 8, "bold"))
                pronos.place(x = 0, y=290)
                
        except:
                 ciudad["text"] = "Intenta nuevamente"
    def clima_JSON(ciudad):
        global MORE
        try: 
            API_key = "f899f03f42a4083566a57ae215f4043c"
            URL = " https://api.openweathermap.org/data/2.5/weather"
            parametros ={"APPID" : API_key, "q":ciudad, "units": "metric", "lang":  "es"}
            response =requests.get(URL, params = parametros)
            print(response)
            clima = response.json()
            mostrar_respuesta (clima)
            print(response.json())
        except:
                print("Error")
        INFO1= Label(ventana, text= "Nombre:", font= Font_tuple2,fg="blue")
        INFO1.place(x=60,y=300)
        clim= Label (ventana, text= (clima["name"]),font= Font_tuple2,fg="blue")
        clim.place(x=150, y=300)

        INFO2= Label (ventana, text="Cielo:", font= Font_tuple2,fg="blue")
        INFO2.place(x=60, y=320)
        desc= Label(ventana, text =(clima["weather"] [0] ["description"]),font= Font_tuple2,fg="blue")
        desc.place(x=150, y=320)

        INFO3 = Label (ventana, text="Temperatura°C:", font= Font_tuple2,fg="blue")
        INFO3.place(x=40, y=340)
        temper = Label (ventana, text= (clima["main"] ["temp"]),font= Font_tuple2,fg="blue")
        temper.place(x=150, y=340)

        INFO4 = Label(ventana, text= "Presión:",font= Font_tuple2,fg="blue")
        INFO4.place(x=60, y=360)
        presion = Label (ventana, text= (clima["main"]["pressure"]),font= Font_tuple2,fg="blue")
        presion.place( x=150, y=360)

        INFO5 = Label(ventana, text="Vel. Viento m/seg:", font= Font_tuple2,fg="blue")
        INFO5.place(x=30, y=380)
        velocidad = Label(ventana, text= (clima["wind"]["speed"]),font= Font_tuple2,fg="blue")
        velocidad.place (x= 150, y=380)


        

    ventana = Tk()
    ventana.title ("CLIMA EN LAS REGIONES HIDROLOGICAS EN TIEMPO REAL")
    ventana.geometry("350x450")
##    CONICO=ImageTk.PhotoImage(Image.open("INIFAP_CLIMA.gif"))
##    CONICO_label=Label (image= CONICO, width=95, height=55)
##    CONICO_label.place(x= 10, y=380)
##    CONICO_label.image=CONICO

    def vamonos():
        ventana.destroy()
        
    def who ():
        global localtime
        global timing
        localtime = time.asctime( time.localtime(time.time()) )
        print (ventana,  "El tiempo Local es :", localtime)
        timing=Label(ventana, text="HORA LOCAL:  "+str(localtime), font = ("Courier", 11, "bold"),bg="blue",fg="white")
        timing.place(x= 5, y=220)
        
    texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
    texto_ciudad.pack(padx = 30, pady =100)

    obtener_clima = Button (ventana, text = "INTRODUZCA MUNICIPIO DE LA CUENCA\n PARA OBTENER EL CLIMA  \n DAR CLICK AQUI",font= Font_tuple2,fg="blue", bg= "light green", bd=8, command = lambda: clima_JSON(texto_ciudad.get()))#font = ("Courier", 8, "bold")
    obtener_clima.place(x=35, y=15)
    texto_info= Button (ventana, text = "TIEMPO EN SU LOCALIDAD", command = who, bd=8, font= Font_tuple2,fg="blue",bg= "light green")
    texto_info.place(x= 90, y=160)#pack(padx=30, pady=20)

    ciudad = Label (font = ("courier", 12, "bold" ))
    ciudad.pack(padx =10, pady=5)


    temperatura = Label ( font =("Courier", 20, "bold" ), fg = "red")
    temperatura.pack(padx =10, pady=10)

    descripcion = Label (font = ("courier", 10, "bold" ))
    descripcion.pack(padx =10, pady=10)



    presion=Label( font =("Courier", 12, "bold" ), fg = "red")
    presion.pack(padx=10, pady=10)



    humedad=Label( font =("Courier", 12, "bold" ), fg = "red")
    humedad.pack(padx=10, pady=10)


    vamonos=Button(ventana, text="CERRAR", command = vamonos, bd=6, bg="yellow")
    vamonos.place(x= 260, y= 380)
    
    NASA_IMG=PhotoImage(file='NASA.png',  master=ventana)
    MORE= Button(ventana,text="NASA",command=NASAIN,image=NASA_IMG, bd=6)
    MORE.place(x=250, y=280)
    NASA_lbl=Label(ventana, text="CLICK INFO ADICIONAL",font= Font_tuple1,fg="blue")
    NASA_lbl.place(x= 230, y=260)

    ventana.mainloop()
def byby_texti2():
        my_texti2.destroy()
        SALIR_TEXTI2.destroy()
        
def start():
    global my_texti2
    global SALIR_TEXTI2
    my_canvas.delete(CUENCA2)
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("BIENVENIDOS AL SISTEMA EXPERTO PARA EL CONOCIMIENTO Y ANÁLISIS DE INFORMACIÓN DEL AGUA EN CUENCAS HIDROLÓGICAS.\n\
    EL SISTEMA ESTA DIVIDIDO EN VARIAS SECCIONES DONDE PODRÁ ENCONTRAR BASES DE DATOS Y PROGRAMAS EJECUTABLES PARA EL ANÁLISIS DE VARIABLES HIDROLÓGICAS.\n\
    EN CADA ELEMENTO ENCONTRARÁ AYUDAS QUE LO GUIARÁN PARA EL ADECUADO USO DE LA APLICACIÓN.\n\
    SOY LUISA, Y ESTARÉ GUIÁNDOLOS EN EL USO DE ESTE SISTEMA.\n\
    ESTE ÍCONO Y MENSAJE SE DESTRUIRÁ EN DOS SEGUNDOS PERO AL REINICIAR EL PROGRAMA APARECERÁ DE NUEVO\n\
    SUERTE")
    converter.runAndWait()
    BEGINING.destroy()
    BEGINING_lbl.destroy()
    ADVERTENCIA_lbl.destroy()
   
    #my_texti2=Text(root, height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
    my_texti2=Text(root, height=30, width=100, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','12','bold'))
    #my_texti2.place(x= 600, y=200)
    my_texti2.place(x= 160, y=70)
    my_texti2.insert(END, "  \n\
                             \n\
                                                                        ¿QUE OFRECE LA APLICACION?\n\
                            \n\
                            ACCESO A INFORMACIÓN DE DIFERENTES FUENTES EN UNA SOLA PLATAFORMA\n\
                            \n\
                            MODELOS DE SIMULACIÓN PARA EL COMPUTO DE VARIABLES COMO ESCURRIMIENTO Y EROSIÓN\n\
                            \n\
                            ACCESO A BASES DE DATOS QUE SE PUEDEN DESCARGAR PARA POSTERIOR USO\n\
                            \n\
                                    - CLIMATICOS\n\
                                    - HIDROLÓGICOS\n\
                                    - ESTADÍSTICAS\n\
                                    - SERIES DE TIEMPO\n\
                            \n\
                            MODELOS DE OPTIMIZACIÓN, PRONÓSTICO DE RIEGO, CAPTACIÓN DE AGUA\n\
                            \n\
                            MODELO PARA TOMA DE DECISIONES\n\
                            \n\
                            ACCESO A UNA BASE DE CONOCIMIENTO PARA OBTENER TECNOLOGÍA \n\
                            \n\
                            OBTENCIÓN DE ÍNDICES EN TIEMPO CUASI - REAL PARA CUALQUIER CUENCA DEL PAIS \n\
                            \n\
                            CUANTIFICACIÓN DEL EFECTO EN TEMPERATURA POR GASES EN LA ATMÓSFERA\n\
                            \n\
                            PROYECCIÓN DEL CALENTAMIENTO EN CUALQUIER CUENCA\n\
                            \n\
                            MODELO DE BALANCE HÍDRICO EN EL SUELO VINCULADO A SISTEMA EXPERTO\n\
                            \n\
                            ALGORITMOS DE INTELIGENCIA ARTIFICIAL PARA VARIABLES HIDROLÓGICAS")
                                                   
                     
    
    SALIR_TEXTI2 = Button(root, text="SALIR", command = byby_texti2)
    SALIR_TEXTI2.place(x= 900, y=610)

def KNOWLEDGE_BASE (event):
##    SHORT_CUT = Label(top, text="PARA DESPLEGAR LOS TEMAS \n\
##                ELIJA REGION HIDROLOGICA Y CUENCA\n\
##                EN LA VENTANA ANTERIOR EN EL APARTADO DE CLIMATOLOGIA",fg="blue")
##    SHORT_CUT.place(x=300,y=300)
##    clickTEMAS.set(option11[0])
##    top.after(4000, SHORT_CUT.destroy)
    
                       
    buttonClicked=False
    
    if not buttonClicked:
        buttonClicked=True
        print("HOLA_si")
        
    if buttonClicked:
            print("HOLA_no")       
    #CURRENT_URL=webbrowser.open_new(r'http://189.194.30.186:8081/Ver.aspx?Nombre_Estado=RH36&Nombre_Cultivo='+str(clickTEMAS.get()))#+str(clickrRH.get()))
    CAMBIO ='clickrRH.get()'
    
    CURRENT_URL=webbrowser.open_new(r'http://189.194.30.186:8081/Ver.aspx?Nombre_Estado='+str(clickrRH.get())+str('&Nombre_Cultivo=')+str(clickTEMAS.get()))
    clickTEMAS.set(option11[0])
def KNOWLEDGE_BASE2():
    CURRENT_URL=webbrowser.open_new(r'http://189.194.30.186:8081/Ver.aspx?Nombre_Estado='+str('RH')+str(clickrRH.get())+str('&Nombre_Cultivo=')+str(clickTEMAS.get()))

    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("LA BASE DEL CONOCIMIENTO, ES UNA BASE DE DATOS QUE SE ENCUENTRA EN UN SERVIDOR COMPUTACIONAL.\n\
    PODRÁ ACCEDER A ELLA EN EL APARTADO DE HIDROLOGÍA. AHI PODRA ENCONTRAR INFORMACIÓN DE LA CUENCA DE INTERÉS\n\
    EXISTEN DIVERSOS TEMAS PARA CONSULTAR: HIDROLOGÍA, POTENCIAL PRODUCTIVO, CLIMATOLOGÍA, DISTRITOS DE RIEGO,\n\
    TAMBIÉN, PODRÁ ENVIAR COMENTARIOS O SUGERENCIAS A LA ADMINISTRACIÓN DEL SISTEMA.")
    converter.runAndWait()
def SAVE_FILE():
    global DESPLIEGA
    
    text_file = open(NAME +str(".txt"), "w")
    text_file.write(my_text.get(1.0, END +'\n'))
    text_file.close()
    
    DESPLIEGA= Label(root, text="GUARDADO COMO:\CONSULTAS\MUNICIPIO(S) "+str(NAME),font=('Helvetica','8','bold'),fg="red")
    DESPLIEGA.place(x=850, y=500)
    
    shutil.move(NAME +str(".txt"), r"CONSULTAS\MUNICIPIO(S).txt")
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("MUNICIPIO ENCONTRADO Y GUARDADO EN LA CARPETA CONSULTAS")
    converter.runAndWait()
    

##    folder ='\CONSULTAS'
##    file_name='NAME.txt'
##    file_path= os.path.join(folder,file_name)
def BYBY_SIAP():
    DESPLIEGA.destroy()
    my_text.destroy()
    BY_SIAP.destroy()
    e.destroy()
    e_año.destroy()
    SIAP.destroy()
    SIAP_CROP.destroy()
    MUNI_CUENC.destroy()
    e_label.destroy()
    e_año_label.destroy()
    AGRIC_HELP.destroy()
    GUARDAR.destroy()
    my_texti.destroy()
    DESPLIEGA.destroy()
    my_texti.destroy()
    
def misma():
    global my_texti
    Datos2 = pd.read_csv(Archivo2,encoding='latin-1')
    
    
    canvas=Canvas(root, width = 390, height=100)
    canvas.pack(fill ="both", expand= True)
    TEMPORAL4=Datos2[Datos2["CUENCA"]==str(NAME)]  
    EST1 = TEMPORAL5=TEMPORAL4[["MUNICIPIO","CUENCA"]]
    

    my_texti=Text(root, height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
    my_texti.place(x= 450, y=230)
    my_texti.insert(END, TEMPORAL5)#+'\n')

def Siap_cult():
    global my_text
    global BY_SIAP
    global dato
    global NAME
    global GUARDAR

 
    dato =e.get()
    año= e_año.get()
    print(año)
    
    dato=str(dato)
    NAME=dato.title()
    
    este_año=2023
    #año=2018
    Datos=pd.read_csv('http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_'+str(año)+str('.csv'), encoding='latin-1')
    TEMPORAL2 = Datos[Datos["Nommunicipio"]==NAME]
    TEMPORAL3=TEMPORAL2[["Nommodalidad","Nomcicloproductivo", "Nomcultivo Sin Um","Rendimiento"]]
    CA=año

    pd.set_option("min_rows", 100)
    pd.set_option("max_colwidth", 15)
    #TEMPORAL3[["Nommodalidad","Nommunicipio","Nomcultivo","Rendimiento"]].head()
    with pd.option_context("display.max_rows",None, "display.max_columns",None):
        print(([TEMPORAL3]))
    
    my_text=Text(height=15, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','7','bold'))
    my_text.place(x= 860, y=230)
    my_text.insert(END,año)
    my_text.insert(END,e.get())
    my_text.insert(END,TEMPORAL3)
    
    GUARDAR= Button(root, text="¿GUARDAR?", command = SAVE_FILE)
    GUARDAR.place(x=1150, y=350)
    
    BY_SIAP=Button(root, text="CERRAR", command=BYBY_SIAP)
    BY_SIAP.place(x=1150, y=300)
    
def Siap():  
    lilo=webbrowser.open_new("https://cmgs.gob.mx/siapdsg/apps/webappviewer/index.html?id=f2a0fc332f24421095d11cfe6ffc2824")
    pass
def AGR_HELP():
    global ROLLO
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("AQUÍ ENCONTRARÁ INFORMACIÓN DE LOS CICLOS DE SIEMBRA EN EL MUNICIPIO DE LA CUENCA Y AÑO ELEGIDO\n\
    INTRODUZCA EL MUNICIPIO Y EL AÑO DE INTERÉS Y OPRIMA EL BOTÓN SIAP_CULT. EL SISTEMA DESPLEGARÁ LOS CULTIVOS SEMBRADOS, \n\
    LA MODALIDAD Y EL RENDIMIENTO OBTENIDO. LOS DATOS SE GUARDARÁN EN UN ARCHIVO DE TEXTO CON EL NOMBRE DEL MUNICIPIO ELEGIDO.\n\
    EL BOTÓN, SIAP_MAP, DESPLEGARÁ LAS PARCELAS DEL MUNICIPIO QUE SE ELIJA PARA EL AÑO DESEADO.\n\
    USANDO LAS HERRAMIENTAS DE LA PÁGINA, SE PUEDE DIBUJAR UN POLÍGONO PARA OBTENER EL ÁREA, UNA LÍNEA PARA MEDIR DISTANCIA, ETCÉTERA.\n\
    EL BOTÓN, MISMA CUENCA, DESPLEGARÁ LOS MUNICIPIOS DE LA CUENCA ELEGIDA AL INICIO DE LA APLICACIÓN")
    converter.runAndWait()
def BYBY_SIAP2():
        SIAP.destroy()
        SIAP_CROP.destroy()
        MUNI_CUENC.destroy()
        e.destroy()
        e_label.destroy()
        e_año.destroy()
        e_año_label.destroy()
        AGRIC_HELP.destroy()
        BY_SIAP.destroy()
def cerrar_agric():
        SIAP.destroy()
        SIAP_CROP.destroy()
        MUNI_CUENC.destroy()
        e.destroy()
        e_label.destroy()
        e_año.destroy()
        e_año_label.destroy()
        AGRIC_HELP.destroy()
##        BY_SIAP.destroy()
        CERRAR_AGRIC.destroy()
        POTENCIAL.destroy()
def PRODUCTIVO():
##        os.startfile("POTENCIAL_PROD\POTENCIAL_PROD.exe")
        global ventana3
        global top8
##        ventana3 = Tk()
##        ventana3.title(" ACUAC POZOS")
##        width, height = ventana3.winfo_screenwidth(), ventana3.winfo_screenheight()
##        ventana3.geometry("800x900+0+0")
        top8=Toplevel()
        top8.geometry("650x500+0+0")
        Font_tuple1=("Comic Sans MS", 10, "bold")
        INTROD= Label(top8, text="OBTENCIÓN DEL POTENCIAL PRODUCTIVO DE CULTIVOS EN CUENCAS\n\
        INTRODUZCA LA RH DE INTERES. 001<=RH<=037", font= Font_tuple1,fg="blue")
        INTROD.place(x=50,y=10)
        POT= Button(top8, text="INICIA", command = ARRANCA, bd=5)
        POT.place(x= 100, y=60)

        DESTRUYE = Button(top8, text="SALIR", command = byby,bd=5)
        DESTRUYE.place(x= 100, y=110)

##        GUARDAR= Button(top8, text="GUARDAR SHP", bd=5, command=GUARDA)
##        GUARDAR. place(x= 100, y=160)
        #ventana.mainloop()
        #top8.mainloop()
def READ_CULTI():
    global CROP
    option =[
              "ELIGE CULTIVO",
              "MAIZ",
              "FRIJOL",
              "AVENA",
              "SORGO",
              "TRIGO",
              "SOYA",
              "PASTO",
              "PAPA",
              "HIGUERILLA",
              "OLIVO",
              "AJO",
              "TOMATE_VERDE",
              "NOGAL",
              "CANOLA"
            ]
    CROP =StringVar()
    CROP.set(option[0])
    drop=OptionMenu(top8,CROP, *option, command=READ)# SELECT_CROP)
    drop["menu"].config(bg="light BLUE")
    drop.place(x=440, y=100)
def READ(event):
    global lat
    global lon
    global plt
    RH = REGION.get()
    CULTIVO=CROP.get()
    
    if CULTIVO=='MAIZ':
        NOMBRE2="maiz_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\MAIZ_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\MAIZ_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='FRIJOL':
        NOMBRE2 ="frijol_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\FRIJOL_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\FRIJOL_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='AVENA':
        NOMBRE2 ="avena_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\AVENA_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\AVENA_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='SORGO':
        NOMBRE2 ="sorgo_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\SORGO_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\SORGO_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='TRIGO':
        NOMBRE2 ="trigo_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\TRIGO_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\TRIGO_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='SOYA':
        NOMBRE2 ="soya_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\SOYA_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\SOYA_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='PASTO':
        NOMBRE2 ="pasto_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\PASTO_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\PASTO_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='PAPA':
        NOMBRE2 ="papa_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\PAPA_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\PAPA_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='HIGUERILLA':
        NOMBRE2 ="higuerilla_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\HIGUERILLA_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\HIGUERILLA_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='OLIVO':
        NOMBRE2 ="olivo_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\OLIVO_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\OLIVO_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='AJO':
        NOMBRE2 ="pot_prod_ajo"
        shape2=gpd.read_file("POTENCIAL_PROD\AJO_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\AJO_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='TOMATE_VERDE':
        NOMBRE2 ="pot_prod_tomate_verde"
        shape2=gpd.read_file("POTENCIAL_PROD\TOMATE_VERDE_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\TOMATE_VERDE_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='NOGAL':
        NOMBRE2 ="nogal_temporal" 
        shape2=gpd.read_file("POTENCIAL_PROD\\NOGAL_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\\NOGAL_TEMPORAL.xlsx', sheet_name=NOMBRE2)
    elif CULTIVO=='CANOLA':
        NOMBRE2 ="canola_temporal"
        shape2=gpd.read_file("POTENCIAL_PROD\CANOLA_TEMPORAL.SHP")
        df4=pd.read_excel('POTENCIAL_PROD\CANOLA_TEMPORAL.xlsx', sheet_name=NOMBRE2)

        
    df3 = pd.DataFrame(data=shape2)
    nombre3=RH
    ddf = df4[df4['clvrh'] == RH]['SUM_HECTAR']
    ddf2 = df4[df4['clvrh'] == RH]['POTPROD']
    RESULTADO=("POTENCIAL "+str(ddf2)+str(" ")+str(ddf))
    df22=[RESULTADO]
    TEMPORAL8 =df3[df3["clvrh"]==nombre3]
    TEMPORAL8 =shape2[shape2["clvrh"].isin([nombre3])]
    TEMPORAL6= TEMPORAL8[["clvrh","SUM_HECTAR"]]
    TEMPORAL8.plot("clvrh", cmap="prism")#coolwarm
    df9=pd.DataFrame(TEMPORAL6)
    df10=pd.DataFrame(TEMPORAL8)
    df10.to_excel("output.xlsx") 
    data=pd.read_excel("output.xlsx",usecols="L:M")
    print("Original DataFrame:\n",data,"\n\n")
    SUMA=data.loc[data['POTPROD']=="Medio", 'SUM_HECTAR'].sum()#POTPROD MEDIO
    SUMA2= data.loc[data['POTPROD']=="Alto", 'SUM_HECTAR'].sum()#POTPROD ALTO
    SUMA1=(f"{SUMA:,}")#PARA SEPARAR LOS NUMEROS CON COMAS
    SUMA22=(f"{SUMA2:,}")

    ax = TEMPORAL8.plot(
        figsize=(20,10),
        column="POTPROD",       
        legend=True,
        cmap="PiYG",
        legend_kwds=dict(bbox_to_anchor=(0.98, 1.00), loc='upper left',fontsize="7"),
        ax=plt.gca(),
        missing_kwds={"color":"white"},
        edgecolor='black',)
    
    
    plt.title("POTENCIAL PRODUCTIVO DEL " +str(CROP.get())+str(" ")+str(RH)+str(" TEMPORAL SOLAMENTE"))
    plt.suptitle("POTENCIAL MEDIO"+str('= ')+str(SUMA1)+str(' Has')+str(' POTENCIAL ALTO'+str('= ')+str(SUMA22)+str( 'Has')),fontsize=9)
    ax.set_xlabel("LONGITUD")
    ax.set_ylabel("LATITUD")
    plt.savefig('cale.png', dpi=80,transparent=True)
    plt.show()


    def GUARDA():
             
        TEMPORAL8.to_file("POTENCIAL_PROD\SHAPE_POTPROD.shp")#("SUBC\SUBCUENCAS.shp")
        AVISA = Label(top8, text="ARCHIVO SHP GUARDADO EN LA CARPETA:\nP0TENCIAL_PROD, COMO:SHAPE_POTPROD.SHP", font= Font_tuple4,fg="blue")
        AVISA.place(x=70, y=310)      
##        photo = tk.PhotoImage(file="cale.png")
##        IMAGEN = tk.Label(image=photo)
##        IMAGEN.place(x=50,y=290)
##        top8.mainloop()
    GUARDAR= Button(top8, text="GUARDAR SHP", bd=5, command=GUARDA)
    GUARDAR. place(x= 100, y=160)
    #ventana3.mainloop()
 
def byby():
    top8.destroy()
    
def ARRANCA():
    global REGION
    REGION=StringVar()
    REGION=Entry(top8, textvariable= REGION, width=25)
    REGION.place(x=340,y=60)
    REGION_LBL=Label(top8, text="ENTRE RH",font= Font_tuple1,fg="blue")
    REGION_LBL.place(x=200, y=60)
    LEE_CROP = Button(top8, text="CULTIVO", command=READ_CULTI, bd=5)
    LEE_CROP.place(x=340, y=100)
    
    

        
def AGR_CONECTION():
    global e
    global e_año
    global e_label
    global e_año_label
    global SIAP
    global SIAP_CROP
    global MUNI_CUENC
    global AGRIC_HELP
    global my_texti
    global BY_SIAP
    global BYBY_SIAP2
    global CERRAR_AGRIC
    global POTENCIAL

   # winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    POTENCIAL= Button(root, text="POT_PROD", command= PRODUCTIVO)
    POTENCIAL.place(x=860, y=350)
    
    SIAP=Button(root, text="SIAP_MAP", command=Siap)
    SIAP.place(x=990,y=470)

    SIAP_CROP= Button(root, text="SIAP_CULT", command = Siap_cult)
    SIAP_CROP.place(x=1070,y=470)

    MUNI_CUENC= Button(root, text="¿MISMA_CUENCA?", command=misma)
    MUNI_CUENC.place(x= 860, y=470)
                       
    
    e = Entry(root, width=20)
    e.place(x=880, y=430)
    e_label=Label(root, text="ENTRE MUNICIPIO",font=('Helvetica','7','bold'),fg="blue")
    e_label.place(x=890, y=400)

    e_año = Entry(root, width=10)
    e_año.place(x=1050, y=430)
    e_año_label=Label(root, text="ENTRE AÑO",font=('Helvetica','7','bold'),fg="blue")
    e_año_label.place(x=1050, y=400)

    AGRIC_HELP=Button(root, text="AYUDA", command =AGR_HELP)
    AGRIC_HELP.place(x=950,y=350)

    CERRAR_AGRIC = Button(root, text="CERRAR", command = cerrar_agric)
    CERRAR_AGRIC.place(x=1020, y=350)

    AGRIC_HELP.config(background="red")
    root.after(1000, AGRIC_HELP.flash)

##    BY_SIAP=Button(root, text="CERRAR", command=BYBY_SIAP2)
##    BY_SIAP.place(x=1150, y=430)
##    for iterator in range(0, 80, 1):
##                    root.after(2000, IRSE.flash)
def erease_DR():
    EMBALSES.destroy()
    EMBALSES_LBL.destroy()
    INFO.destroy()
    INFO_LBL.destroy()
    JUIMONOS.destroy()
    CALENDARIO.destroy()
    CALENDARIO_LBL.destroy()
    
def probabilidad():
    os.startfile("PRESAS_AQUA_MODEL.exe")
def informacion():
    webbrowser.open_new(r'https://sinav30.conagua.gob.mx:8080/SINA/?opcion=distritosr')
def RIEGOS():
    webbrowser.open_new("http://riego.inifap.gob.mx/mobile/")
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("CON ESTE PROGRAMA SE PUEDE OBTENER EL CALENDARIO DE RIEGO DE VARIOS CULTIVOS EN TIEMPO CUASI REAL.\n\
    SE PUEDE UTILIZAR EN LOS DISTRITOS DE RIEGO,PARCELAS, UNIDADES DE RIEGO.\n\
    EL PROGRAMA HACE USO DE INFORMACION CLIMÁTICA DE LAS ESTACIONES AUTOMATIZADAS LOCALIZADAS EN LAS PLANICIES DE LAS CUENCAS.\n\
    CONTIENE UNA SEGUNDA OPCIÓN DE OPTIMIZACIÓN.\n\
    EN LA OPCIÓN DE RIEGO,SE DEBE REQUISITAR LA INFORMACIÓN DE LOS CINCO PASOS LISTADOS EN LAS PESTAÑAS DE LA EZQUINA SUPERIOR DERECHA\n\
    EL LOS RESULTADOS SE OBTIENEN VARIAS GRÁFICAS DE LAS VARIABLES INVOLUCRADAS ASÍ COMO EL CALENDARIO DE RIEGO.")           
    converter.runAndWait()
def DRS():
    global EMBALSES
    global EMBALSES_LBL
    global INFO
    global INFO_LBL
    global JUIMONOS
    global CALENDARIO
    global CALENDARIO_LBL
    
    
    EMBALSES= Button(root, text= "EXCEDENCE", command =probabilidad, image= CURVA_NORMAL)
    EMBALSES.place(x= 820, y=420)

    EMBALSES_LBL = Label(root, text = "PROBABILIDAD PRESAS",font= Font_tuple2,fg="blue")
    EMBALSES_LBL.place(x= 790, y=390)

    INFO = Button(root, text="INFORMACION GENERAL", command = informacion, image = INFORMACION)
    INFO.place( x= 670, y=420)
    INFO_LBL = Label(root, text= "INFORMACION GENERAL", font= Font_tuple2,fg="blue")
    INFO_LBL.place(x=600, y=390)

    CALENDARIO = Button(root, image=IRRIGATION, command=RIEGOS)
    CALENDARIO.place(x=1000, y=420)
    CALENDARIO_LBL = Label(root, text="CALENDARIZACION",font= Font_tuple2,fg="blue")
    CALENDARIO_LBL.place(x= 980, y=390)

    JUIMONOS = Button (root, text="SALIR", command = erease_DR)
    JUIMONOS.place(x=750, y=430)
    
    
##    converter = pyttsx3.init()
##    converter.setProperty('rate', 150)
##    converter.say("EN ESTE APARTADO SE PUEDE CONSULTAR INFORMACIÓN DE LOS DISTRITOS DE RIEGO EN LAS CUENCAS DEL PAIS.\n\
##    EN LA PÁGINA, SELECCIONE EL AÑO AGRÍCOLA Y EL CULTIVO PARA QUE DESPLIEGUE INFORMACIÓN SOBRE SUPERFICIE SEMBRADA, REGADA, VOLÚMENES ETC.\n\
##    LA INFORMACIÓN SOLICITADA SE REFLEJARÁ EN EL MAPA, SOLO DE CLICK EN EL DISTRITO DE RIEGO DE INTERÉS PARA VISUALIZAR LA INFORMACIÓN REQUEDIDA.\n\
##    EN EL PENÚLTIMO BOTÓN DEL EXTREMO IZQUIERDO DEL MAPA, PUEDE DESCARGAR EL ARCHIVO CHEIP y OTROS FORMATOS, ASÍ COMO LA TABLA EN FORMATO EXCEL.")
##    converter.runAndWait()
    
def FOTG():
    SWAPA_LABEL.destroy()
    SWAPA.destroy()
    
def SALIR_EROS_2():
    MANUAL_EROS.destroy()
    MANUAL_EROS_LBL.destroy()
    MODELO_EROS.destroy()
    MODELO_EROS_LBL.destroy()

    MODELO_SILICO.destroy()
    MODELO_SILICO_LBL.destroy()
    MANUAL_USER.destroy()
    SALIR_EROS.destroy()
    
def USER_MANUAL_EROS():

    os.startfile("SWAPAS\PLANNING_TOOL_SISTEMA_EXPERTO.xlsm")
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("'ESTE PROGRAMA AUXILIA AL CONSERVACIONISTA A IDENTIFICAR PRÁCTICAS DE CONSERVACIÓN QUE TIENEN UN EFECTO POSITIVO SUSTANCIAL EN DISMINUIR LOS PROBELMAS DE DETERIORO.\n\
    ADEMÁS, ENLISTA LOS EFECTOS NEGATIVOS QUE PUDIERA TENER LA PRÁCTICA ELEGIDA.\n\
    EL PROGRAMA TIENE VARIAS PESTAÑAS E INCIA CON INSTRUCCIONES. EN LA PESTAÑA SELECT CONCERNS, SELECCIONE LOS PROBLEMAS EVIDENTES EN CAMPO.\n\
    PARA INCIAR, INTRODUZCA SU NOMBRE, LOCALIDAD, ASÍ COMO CUALQUIER COMENTARIO QUE SEA PERTINENTE.\n\
    COLOQUE UNA “X” EN LA HILERA CONTIGUA AL USO DEL SUELO DE INTERÉS.\n\
    COLOQUE UNA “X” EN LA HILERA CONTIGUA AL PROBLEMA ENCONTRADO PARA CADA RECURSO Y PRESIONE LA TECLA ENTER.\n\
    USE LAS FLECHAS O EL MOUSE PARA NAVEGAR POR LA HOJA EXCELL")           
    converter.runAndWait()
def MODEL_EROS():
    os.startfile(r"MODELO_EROSION\UH_BIS_3.exe")    
def MODEL_SILICO():
    os.startfile(r"Prod_soil\Perdida_productividad.exe")
    #os.startfile(r"E:\PROGRAMAR_PAITON\CUENCAS\Prod_soil\Perdida_productividad.exe")
def USER_SILICO():
    os.system("Prod_soil\MANUAL_SILICO.pdf")
def EROSION_CALC():
    global SWAPA_LABEL
    global SWAPA
    global MANUAL_EROS
    global MANUAL_EROS_LBL
    global MODELO_EROS
    global MODELO_EROS_LBL
    global SALIR_EROS
    global MODELO_SILICO
    global MODELO_SILICO_LBL
    global MANUAL_USER
    
    MANUAL_EROS= Button(root, text= "MATRIZ EFECTOS", command = USER_MANUAL_EROS,image=LIBRO)
    MANUAL_EROS.place(x= 180, y=420)
    MANUAL_EROS_LBL = Label(root, text= "MATRIZ EFECTOS", font= Font_tuple2,fg="blue")
    MANUAL_EROS_LBL.place(x= 160, y=390)

    MODELO_EROS= Button(root, command = MODEL_EROS,image=COMPUTER)
    MODELO_EROS.place(x= 350, y=420)
    MODELO_EROS_LBL = Label(root, text= "MODELO SIMULACION", font= Font_tuple2,fg="blue")
    MODELO_EROS_LBL.place(x= 310, y=390)

    MODELO_SILICO= Button(root, command = MODEL_SILICO,image=COMPUTER)
    MODELO_SILICO.place(x= 540, y=420)
    MODELO_SILICO_LBL = Label(root, text= "PROYECCION IN SILICO", font= Font_tuple2,fg="blue")
    MODELO_SILICO_LBL.place(x= 500, y=390)

    MANUAL_USER= Button(root, command = USER_SILICO, text= "MANUAL USUARIO")
    MANUAL_USER.place(x= 650, y=430)

    SALIR_EROS = Button(root, text="SALIR", command =SALIR_EROS_2)
    SALIR_EROS.place(x= 280, y=430)

def SALIR_GEE():
        GGE1.destroy()
        GGE2.destroy()
        SALIRS.destroy()
        INDEX.destroy()
        ETO.destroy()
        SOCIAL_BUTT.destroy()
        SOC_LBL.destroy()
        USR_MAN.destroy()
        WATER.destroy()
        WATERLBL.destroy()
        NDVI_QQ.destroy()
        NDVII_Q_LBL.destroy()
def NDVII_RUNOFF():
        lilo2=webbrowser.open_new("https://tatiyoma85.users.earthengine.app/view/ndviqlag")
def ASPECTOS():
        os.startfile("MARG_CUENC.exe")
        pass
def GEE_HYDR():
        lilo2=webbrowser.open_new("https://inifapcenidraspa.users.earthengine.app/view/gee-acuac")
def GEE2_ETo():
        #lilo2=webbrowser.open_new("http://etocalculator.com")
        lilo2=webbrowser.open_new("https://inifapcenidraspa.users.earthengine.app/view/vical")
def CARACT_USR():
        pass
def agua():
        #AGUA=webbrowser.open_new("https://ee-inifapcenidraspa.projects.earthengine.app/view/watergee")
        AGUA=webbrowser.open_new("https://tatiyoma85.users.earthengine.app/view/balance-cuencas2")
def GEE_CONECTION():
        global GGE1
        global GGE2
        global SALIRS
        global INDEX
        global ETO
        global SOCIAL_BUTT
        global SOC_LBL
        global USR_MAN
        global WATER
        global WATERLBL
        global NDVI_QQ
        global NDVII_Q_LBL
        GGE1= Button(root, text="GEE_HYDR", command =GEE_HYDR, bd=5, image=GEE1_IMG, state="active")
        GGE1.place(x= 520, y=420)

        INDEX = Label(root, text="INDICES\nCUENCAS",font= Font_tuple2,fg="blue")
        INDEX.place(x=450, y=440)

        ETO = Label (root, text= "VICAL\nGLOBAL", font= Font_tuple2,fg="blue")
        ETO.place(x= 820, y=435)

        SALIRS = Button(root, text= "SALIR", command = SALIR_GEE,bd=5)
        SALIRS.place(x= 635, y=440)

        GGE2= Button(root, text="GEE_ET", command =GEE2_ETo, bd=5, image=GEE2_IMG, state="active")
        GGE2.place(x= 700, y=420)

        WATER= Button(root, text= "WATER", command = agua,bd=5, image=BODIES2)
        WATER.place(x=900, y=420)
        WATERLBL = Label(root, text="<--BALANCE\n    HIDRICO",font= Font_tuple2,fg="blue")
        WATERLBL.place(x= 1020, y=440)

        #WATER="https://ee-inifapcenidraspa.projects.earthengine.app/view/watergee"
        NDVI_QQ = Button(root,command=NDVII_RUNOFF, bd=5, image=NDVI_Q)
        NDVI_QQ.place(x=125, y=420)
        NDVII_Q_LBL= Label(root, text= "NDVI_Q", font=Font_tuple2, fg="blue")
        NDVII_Q_LBL.place(x=50, y=440)
        SOCIAL_BUTT= Button(root, text="ASPECTOS/nSOCIALES", command =ASPECTOS, bd=5, image=SOC_ASPECT, state="active")
        SOCIAL_BUTT.place(x=310, y=420)
        SOC_LBL=Label(root, text="ASPECTOS\nSOCIALES",font= Font_tuple2,fg="blue")
        SOC_LBL.place(x=230, y=440)

        USR_MAN= Button(root, text= "MANUAL USUARIO", command = CARACT_USR, bd=5)
        USR_MAN.place(x=1130, y=440)

    
    #lilo2=webbrowser.open_new("https://inifapcenidraspa.users.earthengine.app/view/vical")
        #lilo2=webbrowser.open_new("https://inifapcenidraspa.users.earthengine.app/view/gee-acuac")
##    converter = pyttsx3.init()
##    converter.setProperty('rate', 150)
##    converter.say("Esta opción esta diseñada para obtener información de la cuenca de interés en tiempo cuasi-real.\n\
##    Utiliza la plataforma de GOOGLE EARTH ENYIN. Para inciar, Localizar la Cuenca de interés en el mapa base y dibujar el polígono utilizando la herramienta para tal efecto.\n\
##    Posteriormente, seleccionar la fecha inicial y final de la serie de tiempo en el formato indicado en la porción izquierda de su pantalla.\n\
##    Seleccione los satélites de las opciones proveídas y posteriormente, seleccione el índice de interés.\n\
##    Al presionar el botón calcular, aparecerán los resultados del índice elegido.\n\
##    El sistema muestra la primera imagen de la serie de tiempo pero puede seleccionar cualquier fecha en el rango especificado.\n\
##    Posteriormente, de click dentro del polígono para que se despliegue la gráfica de la serie de tiempo del índice.\n\
##    Esta información puede bajarse en diferentes formatos.\n\
##    Al dar click en la opción “polígono nuevo”, se podrá repetir el proceso con otro índice.\n\
##    Se puede editar la geometría del polígono. Finalmente, puede bajar el archivo en formato cheip o la imagen si se desea.")
##    converter.runAndWait()
def SALIR_CC():
        TEMP_VAR.destroy()
        TEMP_VAR_LBL.destroy()
        SLIDES.destroy()
        SLIDES_LBL.destroy()
        LETS_GO.destroy()
def HELP_SLIDE():
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    
    converter.say("EN ESTE APARTADO,SE PUEDE OBTENER LA PROYECCIÓN DEL INCREMENTO EN TEMPERATURA AL VARIAR LA CONCENTRACIÓN DE LOS GASES EFECTO DE INVERNADERO,\n\
    EN LA REGIÓN HIDROLÓGICA O CUENCA DE INTERÉS. UTILIZE LAS BARRAS DESLIZANTES PARA INDICAR EL NIVEL DESEADO DE GASES EN CADA CASO.\n\
    PULSAR EL BOTON CALCULAR PARA QUE SE DESPLIEGUEN LOS FORZAMIENTOS RADIATIVOS Y LA TEMPERATURA.\n\
    LOS RESULTADOS SE REPORTAN EN TÉRMINOS DE DIÓXIDO DE CARBONO EQUIVALENTE.\n\
    EL PROGRAMA UTILIZA LAS ECUACIONES DEL PÁNEL INTERGUBERNAMENTAL DEL CAMBIO CLIMÁTICO PARA LOS CÁLCULOS.\n\
    SE RECOMIENDA VER LA EXPLICACIÓN EN EL BOTÓN GASES EFECTO DE INVERNADERO, CUANDO ÉSTE APAREZCA")
    converter.runAndWait()
def juimonos():
    root2.destroy()
def borrar():
    
    slider1.set(nitroso_min)
    slider2.set(amonio_min)
    slider3.set(dioxido_min)
    slider4.set(dioxido_actual)
    my_canvas2.delete(rollo5)
    my_canvas2.delete(rollo6)
    my_canvas2.delete(rollo7)
    my_canvas2.delete(rollo8)
    my_canvas2.delete(rollo9)
    CC.destroy()
def bySALIR_CC():
        SALIR_CC.destroy()
        text2.destroy()
    
def calculate():
    
    global rollo5
    global rollo6
    global rollo7
    global rollo8
    global rollo9
    global id1
    global NO2_actual
    global CC
    global SALIR_CC
    global text2
    #my_canvas.delete(INGR)
    my_canvas2.delete(FORZAM)
    EXPLICA.destroy()
    INFO.destroy()
    
    def gases():
        webbrowser.open_new(r'GASES.pdf')
       
    CC=Button(root2, text="Gases efecto\n de invernadero", command= gases, bd=8, bg="yellow")
    CC.place(x= 230, y =500)

    val1 = slider1.get()
    val2 = slider2.get()
    sigma=4*(0.0000000567)
    val3=((1-val1)*val2/(sigma))**0.25
    temp= val3-273.15
    temp2=temp*1.2
    temp3=-18 + 33
    Co1=slider3.get()
    Co2= slider4.get()
    Co=5.35*(math.log(Co1/Co2))
    CoT=Co*0.8

    rollo6=my_canvas2.create_text(300, 410, text="El forzamiento por CO2 es=  " +str(round(Co,2)) + str("   ")+str ("Wm2"),fill = "blue", font = 'sans 11 bold')
    
    rollo7=my_canvas2.create_text(300, 480, text= "Incremento en temperatura en la cuenca es =  " +str(round(CoT,2)) + str("   ") + str("°C"), fill = "red", font = 'sans 11 bold')
    try:print("Number 1 : {} \nNumber 2 : {} \nsigma:{}\n".format(val1, val2, val3))
    except ZeroDivisionError:
        print("Can not divide by zero. Try another number")
    pass
    a2= -0.000008
    b2= 0.0000042
    c2= -0.0000049
    C0= 250
    NO= 330
    MO= 1859
    #calculo del N2O
    NO1= a2*((250 + slider3.get())*0.5)
    NO2= b2*((330+slider1.get())*0.5)
    NO3= c2*((1859+ slider2.get())*0.5)
    CTE= 0.117
    NO4= (slider1.get()**0.5) - 18.16
    NOT= (NO1+NO2+NO3+CTE)*(NO4)
##    NO2_actual=my_canvas.create_text(570, 40, text="La concentracion\n actual es = 330 ppb")
    
    rollo5= my_canvas2.create_text(300, 340, text= " El forzamiento por NO2 es=  "+str(round(NOT,2))+str("   ")+str ("Wm2"),fill = "blue", font = 'sans 11 bold')
    a3=-0.0000013
    b3=-0.0000082
    NH1= a3*((slider2.get()+1859)*0.5)
    NH2= b3*((slider1.get()+ 330)*0.5)
    CTE2=0.043
    NH3=((slider2.get())**0.5)-43.11
    NH4T=(NH1+NH2+CTE2)*NH3
    
    rollo8= my_canvas2.create_text(300,370, text="El forzamiento por NH4 es =  " +str(round (NH4T,2))+str("   ")+str ("Wm2"),fill = "blue", font = 'sans 11 bold')
    #TORAL NET FORCING AND DERIVED TEMPERATURE
    TOTNF= Co+NOT+NH4T
    rollo9= my_canvas2.create_text(300, 450, text="El forzamiento total es =  " +str(round(TOTNF,2))+str("   ") + str("Wm2"), fill="blue", font='sans 11 bold')

    fig,ax=plt.subplots(figsize=(10,7))
    ax2=ax.twinx()
    x='FORZ.TOTAL'
    x2='NH4'
    x3 = 'NO2'
    x4='CO2'
    x5='TEMP'
    y=TOTNF
    y2=NH4T
    y3=NOT
    y4=Co
    y5=CoT
    ax.bar(x,TOTNF, color ='orange')
    ax.bar(x2,NH4T, color ='green')
    ax.bar(x3,NOT, color ='grey')
    ax.bar(x4, Co, color ='yellow')
    ax2.bar(x5,CoT,color='red',edgecolor = "black", linestyle ="--", linewidth = 2)
    plt.title("FORZAMIENTOS RADIATIVOS PARA LA CUENCA")
    plt.suptitle("CON LOS PARAMETROS PROVEÍDOS ACORDE AL IPCC EL CALENTAMIENTO EN LA CUENCA ELEGIDA SERÁ COMO LO MUESTRA LA FIGURA",fontsize = 10)
    ax.set_xlabel("GASES")
    ax.set_ylabel("Forzamientos radiativos, Wm2")
    ax2.set_ylabel('Incremento temperatura (°C)', color='red')
    plt.show()
    text2=Text(root2, height=20, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','9','bold'))
    text2.place(x= 200, y=140)
    text2.insert(1.0," \n\
                        EL EFECTO DEL INCREMENTO EN TEMPERATURAS EN UNA CUENCA\n\
                        ES VARIADO:\n\
                        - Incremento en evaporación: El aire caliente puede retener\n\
                        mas humedad provocando mas evaporación.\n\
                        - Incremento en intensidad de precipitación: Derivado de lo \n\
                        anterior, la atmósfera tiene que liberar la humedad \n\
                        lo que provocaría precipitaciónes de alta intensidad\n\
                        con consecuencias en flujos o escurrimientos elevados.\n\
                        - Cambios en patrones de lluvia: El cambio de temperatura\n\
                        afecta los patrones de circulación provocando areas mas secas\n\
                        o mas húmedas lo que ocaciona eventos extremos.\n\
                        - Aparición de plagas y enfermedades no solo con efectos\n\
                        en las plantas, sino que también en humanos.\n\
                        - Prolongadas sequías producen vegetación seca (combustible)\n\
                        que puede provocar incendios de bosques")
    SALIR_CC = Button(root2, text="SALIR", command = bySALIR_CC)
    SALIR_CC.place(x= 400, y=400)
def SLI():
        global root2
        global slider1
        global slider2
        global slider3
        global slider4
        global my_canvas2
        global nitroso_min
        global amonio_min
        global dioxido_min
        global dioxido_actual
        global FORZA
        global FORZAM
        global EXPLICA
        global INFO
        
        root2 = Tk()
        root2.title("SIMULACION DE VARIACIONES EN TEMPERATURAS AL VARIAR LA CONCENTRACION DE GASES")
        root2.geometry('750x800')
        my_canvas2= Canvas(root2, width = 1000, height=500)
        my_canvas2.pack(fill ="both", expand= True)
        FIS= PhotoImage(file='FISLIDES.png', master=root2)
        
        FORZA =PhotoImage(file='Forcings.png', master=root2)
        FORZAM= my_canvas2.create_image(330,530, image= FORZA)#,anchor=NW)
        
        EXPLICA = Label(root2, text ="DESLICE LAS BARRAS A LAS CONCENTRACIONES DE GASES DESEADAS PARA EL CALCLO DE FORZAMIENTOS RADIATIVOS\n\
        \n PRESIONE CALCULAR",fg='blue',font = 'sans 9 bold')
        EXPLICA.place(x= 10,y=333)
        
        slider1 = Scale(root2, from_=330, to=600, length=400, resolution=20, orient=HORIZONTAL,tickinterval=20)
        rollo= my_canvas2.create_text(50,40, text="Cons. NO2\n (ppb)")
        slider1.place(x= 100, y = 25)#pack()
        nitroso_min=330

        slider2 = Scale(root2, from_=1860, to=2300, length=400, resolution=20, orient=HORIZONTAL)
        rollo2=my_canvas2.create_text(50, 120, text="Cons. NH4\n (ppb)")
        slider2.place(x= 100, y = 100)
        amonio_min=1860

        slider3=Scale(root2, from_=300, to= 900, length=400, resolution=50, orient=HORIZONTAL)
        rollo3=my_canvas2.create_text(50, 175, text= "Conc.CO2 \nfutura (ppm)")
        slider3.place(x= 100, y= 150)
        dioxido_min=300

        slider4=Scale(root2, from_=200, to= 800, length=400, resolution = 50, orient=HORIZONTAL,tickinterval=50)
        rollo4=my_canvas2.create_text(50, 225, text= "Conc.CO2\n actual (ppm)")
        slider4.place(x=100, y= 200)
        dioxido_actual=200

        button1 = Button(root2, text="Calcular", command=calculate, bd=4, relief="raised",state="active")
        button1.place(x= 180, y= 290)

        button2 = Button(root2, text="Borrar", command=borrar,bd=4, relief="raised",state="active")
        button2.place(x= 355, y= 290)

        VAMONOS = Button (root2, text="SALIR", command = juimonos,bd=4,bg="red")
        VAMONOS.place(x= 280, y=290)

        NO2_actual=my_canvas2.create_text(580, 50, text="La concentracion\n actual es = 330 ppb",fill = "blue",font = 'sans 10 bold')
        NH4_actual=my_canvas2.create_text(580, 120, text="La concentracion\n actual es = 1860 ppb",fill = "blue",font = 'sans 10 bold')

        INFO = Label(root2, text = "\n\
        Los forzamientos radiativos se refiere\n\
        al cambio en el flujo de energía\n\
        en la atmósfera causada por los gases\n\
        efecto de invernadero. \n\
        Se mide en watts por metro cuadrado.\n\
        Es un concepto científico usado para \n\
        cuantificar y comparar los factores externos\n\
        del cambio del balance de energía\n\
        en la tierra.\n\
        Su presencia acentúa el calentamiento\n\
        reflejado en un incremento en temperatura", anchor="w", justify="left", fg="blue")
        INFO.place(x= 485, y=420)

        HELPIOSA = Button(root2, text="Ayuda",command = HELP_SLIDE, bd=4, relief="raised")
        HELPIOSA.place(x= 450, y=290)
##        HELPIOSA_LBL = Label(root2, text="AYUDA",fg="blue")
##        HELPIOSA_LBL.place(x=600, y=230)         
         
def TEMPERATURA():
            
            os.startfile("CALES_NASA.exe")
            converter = pyttsx3.init()
            converter.setProperty('rate', 150)
            converter.say("EN ESTA OPCIÓN, SE PODRÁ OBTENER LA VARIACIÓN TEMPORAL DE LA PRECIPITACIÓN, TEMPERATURA MÁXIMA Y TEMPERATURA MÍNIMA,\n\
            DE LA CUENCA DE INTERÉS PARA UN DETERMINADO MES DEL AÑO. EL MODELO, ARROJA TAMBIÉN, LA TASA DE VARIACIÓN EN EL TIEMPO, COMO UN INDICADOR\n\
            DEL GRADO DE CALENTAMIENTO Y SU PERSPECTIVA EN EL TIEMPO.\n\
            SOLO INTRODUZCA LA LATITUD Y LA LONGITUD DE LA CUENCA EN EL ESPACIO PROVEÍDO. LA LONGITUD DEBE SER NEGATIVA.\n\
            POSTERIORMENTE, ELIJA LA VARIABLE DE DESPLIEGUE Y EL MES DE INTERÉS PARA QUE SE DESPLIEGUE LA GRÁFICA.\n\
            LOS DATOS PROVIENEN DE SERVIDORES DE LA NASA CON AUTORIZACIÓN PARA CONSULTA")
            converter.runAndWait()
            TEMP_VAR.destroy()
            TEMP_VAR_LBL.destroy()
    
def CC_CONECTION():
    global TEMP_VAR
    global TEMP_VAR_LBL
    global SLIDES
    global SLIDES_LBL
    global LETS_GO
    TEMP_VAR = Button(root, image = COMPUTER, command = TEMPERATURA)
    TEMP_VAR.place(x=570, y=420)
    TEMP_VAR_LBL = Label(root, text="CALENTAMIENTO",font= Font_tuple2,fg="blue")
    TEMP_VAR_LBL.place(x=550, y=400)

    SLIDES = Button(root, image = COMPUTER, command = SLI, state="active")
    SLIDES.place(x= 400, y=420)
    SLIDES_LBL = Label(root, text="FORZAMIENTOS", font= Font_tuple2,fg="blue")
    SLIDES_LBL.place(x=380, y =400)

    LETS_GO = Button(root, text ="SALIR", command=SALIR_CC)
    LETS_GO.place(x= 510, y=440)
    
    
def SALGAMOS():
    root.destroy()
    
def abandona():
    SALIR.destroy()
    MANUAL.destroy()
    MANUAL_LBL.destroy()
    MODELO.destroy()
    MODELO_LBL.destroy()
    
def USER_MANUAL():
    subprocess.Popen("Manual del Usuario.pdf", shell=True)
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("EL MANUAL DEL USUARIO ES UNA GUÍA PRÁCTICA PARA LA ADECUADA OPERACIÓN DEL MODELO DE BALANCE.\n\
    ES RECOMENDABLE IMPRIMIR EL DOCUMENTO PARA REFERENCIA DURANTE EL USO DEL PROGRAMA.\n\
    TAMBIÉN, SE PUEDE MINIMIZAR LA PANTALLA PARA RÁPIDO ACCESO A LA AYUDA.")
    converter.runAndWait()
    
def MODEL():
    global SALIR
    os.startfile("risk.exe")
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.say("AQUÍ, PODRÁ EJECUTAR EL BALANCE DE AGUA EN EL SUELO PARA CUALQUIER MUNICIPIO EN LAS CUENCAS.\n\
    PRESIONE LA PESTAÑA,DATOS DE ENTRADA, PARA INTRODUCIR LOS DATOS COMO SE SOLICITA. SE INCIA CON LA INTRODUCCIÓN DE UN NÚMERO ALEATORIO DE CUATRO DÍGITOS.\n\
    AL SELECCIONAR LA ENTIDAD FEDERATIVA, EL PROGRAMA LE SOLICITARÁ ELEGIR EL MUNICIPIO Y LA ESTACIÓN CLIMÁTICA.\n\
    AUXÍLIESE DE LAS AYUDAS MARCADAS CON UN SIGNO DE INTERROGACIÓN EN CADA RUBRO. EL MODELO DE BALANCE CONSIDERA A LA LLUVIA COMO UNA VARIABLE ESTOCÁSICA.\n\
    SE PRESENTA LA CURVA DE PROBABILIDAD PARA LAS VARIABLES PRECIPITACIÓN Y RENDIMIENTO.\n\
    SI EL MODELO DETECTA QUE EL RENDIMIENTO CALCULADO ES MENOR AL 50% DEL RENDIMIENTO ESPERADO, SE ACTIVA UNA PESTAÑA QUE LO LLEVARÁ A UNA BASE DE DATOS\n\
    DONDE PODRÁ CONSULTAR LA TECNOLOGÍA DISPONIBLE PARA SOBRELLEVAR EL RIESGO HÍDRICO.")
    converter.runAndWait()
    
    
def SWB():
    global MANUAL
    global MANUAL_LBL
    global MODELO
    global MODELO_LBL
    global SALIR
    print("hola")
    MANUAL= Button(root, text= "MANUAL USUARIO", command = USER_MANUAL,image=LIBRO)
    MANUAL.place(x= 850, y=420)
    MANUAL_LBL = Label(root, text= "MANUAL USUARIO", font= Font_tuple2,fg="blue")
    MANUAL_LBL.place(x= 830, y=400)

    MODELO= Button(root, command = MODEL,image=COMPUTER)
    MODELO.place(x= 1020, y=420)
    MODELO_LBL = Label(root, text= "MODELO SIMULACION", font= Font_tuple2,fg="blue")
    MODELO_LBL.place(x= 990, y=400)

    SALIR = Button(root, text="SALIR", command =abandona)
    SALIR.place(x= 950, y=430)
    
def BAND():
    webbrowser.open("http://hidrosuperf.imta.mx/bandas/", new=1)
    
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    
    converter.say("ALTERNATIVAMENTE,ESTE BOTON LO LLEVARÁ A LA PÁGINA DE LA BASE DE DATOS NACIONALES DE AGUAS.\n\
    AQUÍ, PODRÁ VISUALIZAR LA UBICACIÓN DE LAS ESTACIONES HIDROMÉTRICAS EN LAS CUENCAS.\n\
    EN LA PÁGINA, SELECCIONE DEL PANEL DE LA IZQUIERDA LA REGIÓN HIDROLÓGICA ADMINISTRATIVA PARA QUE SE DESPLIEGUE EN EL MAPA LAS ESTACIONES HIDROMÉTRICAS\n\
    POSTERIORMENTE, UBIQUE EL MOUSE EN LA ESTACIÓN DESEADA Y SE DESPLEGARÁ INFORMACIÓN ADICIONAL SOBRE EL PERIODO DE REGISTRO Y DATOS GENERALES DE LA ESTACIÓN.\n\
    PRESIONANDO EL ÍCONO A LA IZQUIERDA DEL NOMBRE DE LA REGIÓN ADMINISTRATIVA, PODRÁ BAJAR EL ARCHIVO CHEIP PARA POSTERIOR USO.\n\
    HACIA EL FINAL DE LA VENTANA, APARECE LA OPCIÓN DE DESCARGAR EL HISTÓRICO DE LA ESTACIÓN HIDROMÉTRICA EN ARCHIVO DIBEIS")
    converter.runAndWait()
    
def abandona_2():
    MANUAL_DSS.destroy()
    MANUAL_DSS_LBL.destroy()
    MODELO_DSS.destroy()
    MODELO_DSS_LBL.destroy()
    SALIR.destroy()
    
def DSS_MANUAL():
    subprocess.Popen("MANUAL_FACILITATOR.pdf", shell=True)
def MODEL_DSS():
    p=subprocess.Popen(r"facilitator-1.3.8.jar", shell=True)    
def FACILIT():
    global MANUAL_DSS
    global MANUAL_DSS_LBL
    global MODELO_DSS
    global MODELO_DSS_LBL
    global SALIR
    
    MANUAL_DSS= Button(root, command = DSS_MANUAL,image=LIBRO)
    MANUAL_DSS.place(x= 950, y=320)
    MANUAL_DSS_LBL = Label(root, text= "MANUAL USUARIO", font= Font_tuple2,fg="blue")
    MANUAL_DSS_LBL.place(x= 930, y=300)

    MODELO_DSS= Button(root, command = MODEL_DSS,image=COMPUTER)
    MODELO_DSS.place(x= 1120, y=320)
    MODELO_DSS_LBL = Label(root, text= "MODELO DE DECISION", font= Font_tuple2,fg="blue")
    MODELO_DSS_LBL.place(x= 1090, y=300)    
    
    SALIR = Button(root, text="SALIR", command =abandona_2)
    SALIR.place(x= 1050, y=330)

##    converter = pyttsx3.init()
##    converter.setProperty('rate', 150)
##    
##    converter.say("EN ESTE APARTADO PODRÁ HACER USO DE UN SISTEMA DE AYUDA A LA TOMA DE DECISIONES.\n\
##    EL PROGRAMA LLEVA POR NOMBRE, FACILITATOR, Y SE INCLUYE EL MANUAL PRÁCTICO DEL USUARIO.\n\
##    LA SECUENCIA EN LA IMPLEMENTACIÓN DEL PROGRAMA ES:\n\
##    PRIMERO, SE CREA UNA MATRIZ TENIENDO COMO COLUMNAS LOS CRITERIOS CON QUE SERÁN CALIFICADAS LAS ALTERNATIVAS PROPUESTAS QUE CONSTITUYEN LOS RENGLONES.\n\
##    POSTERIORMENTE SE CALIFICA EL IMPACTO QUE CADA ALTERNATIVA TIENE EN LOS PROBLEMAS PLANTEADOS UTILIZANDO LOS CRITERIOS.\n\
##    PARA ELIMINAR UNIDADES, SE DEBE DE CALIFICAR EN LA ESCALA DE CERO A UNO, SIENDO UNO, LA CALIFICACIÓN MAS ALTA.\n\
##    SE DEBE DE INSTRUIR AL PROGRAMA EL ÓRDEN JERÁRQUICO DE LOS CRITERIOS, ES DECIR, CUAL SERÁ EL CRITERIO DOMINANTE EN LA DECISIÓN\n\
##    EL ORDEN JERÁRQUICO PUEDE SER CAMBIADO PARA CONOCER COMO CAMBIAN LAS ALTERNATIVAS AL MODIFICAR EL ÓRDEN DE LOS CRITERIOS.\n\
##    AL CORRER EL PROGRAMA, SE MUESTRA UNA SALIDA GRÁFICA QUE SEÑALARÁ EL IMPACTO DE CADA ALTERNATIVA EN EL PROBLEMA PLANTEADO.")
##    converter.runAndWait()
def by_by_texti():
        texti.destroy()
        BY_texti.destroy()
        CREDITOS.destroy()
        CREDITOS_lbl.destroy()
def CREDIT():
        global texti
        global BY_texti
        texti=Text(root, height=23, width=75, wrap=WORD, bd=3,relief='solid',bg="white",fg="blue",font=('Helvetica','9','bold'))
        texti.place(x= 350, y=140)
        texti.insert(1.0,"  ACUAC. APLICACION COMPUTACIONAL PARA EL USO Y ANALISIS DEL AGUA EN CUENCAS\n\
        \n\
                                                     Dr, Ignacio Sánchez Cohen\n\
                                                     PROGRAMACIÓN, SIMULACION\n\
                                                     M.C. Sergio Ivan Jiménez\n\
                                                     PROGRAMACION GEE\n\
                                                     Dr. Marco Antonio Inzunza Ibarra\n\
                                                     VALIDACIÓN GEE\n\
                                                     Dr. Gabriel Díaz Padilla\n\
                                                     BASES DE DATOS GEOESPACIAL\n\
                                                     M.C. Rafael Alberto Guajardo Panes\n\
                                                     BASES DE DATOS REESCALADOS\n\
        \n\
                                                                  CONTACTO\n\
                                                     sanchez.ignacio@inifap.gob.mx\n\
                                                     https//www.inifap.gob.mx\n\
        \n\
                                                     CURSO DE ADISTRAMIENTO DISPONIBLE\n\
        ")
        texti.image_create(tk.END, image = INIFAP)
        
        BY_texti= Button(root, text="SALIR", command = by_by_texti)
        BY_texti.place(x= 760, y=460)
RH=Button(root, text="REGIONES HIDROLOGICAS", command=REG_HYDR, bd=5, image=REG_HYDR_IMG)
RH.place(x=40, y=60)
RH_lbl = Label(root, text = "CLICK PARA INICIAR\n (CLIMATOLOGÍA)",font= Font_tuple2,fg="blue")
RH_lbl.place(x= 30, y=20)

Borrar= Button(root, text="BORRAR", command=borras)
Borrar.place(x=40, y=4800)

Hydr=Button(root, text= "HIDROLOGIA", command = calculos, bd=5, image=HYDR_IMG, state="active")
Hydr.place(x=40, y=550)
Hydr_lbl= Label(root, text= "HIDROLOGIA", font= Font_tuple2,fg="blue")
Hydr_lbl.place(x=60, y=520)

##CLIMA= Button (root, text= "CLIMA", command = weather, bd=5, image=CLIMA_IMG, state="disabled")
##CLIMA.place(x=700, y=550)
##CLIMA_lbl= Label(root, text= "CLIMA", font= Font_tuple2,fg="blue")
##CLIMA_lbl.place(x=680, y=520)

BEGINING = Button(root, text="INICIO", command=start, bd=7, image=INICIO_IMG)
BEGINING.place(x=1050, y=120)
BEGINING_lbl= Label(root, text= "ESCUCHAR PARA EMPEZAR", font= Font_tuple2,fg="blue")
BEGINING_lbl.place(x=1000, y=95)

CREDITOS = Button(root,  bd = 7, image = Credito, command= CREDIT)
CREDITOS.place(x= 1040, y=220)
CREDITOS_lbl = Label (root, text="CREDITOS", font= Font_tuple2,fg="blue")
CREDITOS_lbl.place(x=1050, y=320)

ADVERTENCIA_lbl = Label(root, text= "ES IMPORTANTE VERIFICAR QUE LA VOZ\n DE MICROSOFT SEA ESPAÑOL",font= Font_tuple1,fg="blue")
ADVERTENCIA_lbl.place(x=980, y=180)

##KNOWLEDGE = Button(root, text="KNOWLEDGE BASE", command =KNOWLEDGE_BASE2, bd=5, image=COMPLE_IMG, state="disabled")
##KNOWLEDGE.place(x= 280, y=550)
##KNOWLEDGE_lbl= Label(root, text= "KNOWLEDGE BASE", font= Font_tuple2,fg="blue")
##KNOWLEDGE_lbl.place(x=270, y=520)

GEE = Button(root, text="GEE", command =GEE_CONECTION, bd=5, image=GEE_IMG, state="active")
GEE.place(x= 590, y=550)
GEE_lbl= Label(root, text= "CARACTERIZACION\nCUENCAS", font= Font_tuple2,fg="blue")
GEE_lbl.place(x=600, y=500)


EROSION = Button(root, text="EROSION", command =EROSION_CALC, bd=5, image=EROSION_IMG, state="active")
EROSION.place(x= 180, y=550)
EROSION_lbl= Label(root, text= "EROSION", font= Font_tuple2,fg="blue")
EROSION_lbl.place(x=210, y=520)

CC = Button(root, text="CAMBIO CLIMATICO", command =CC_CONECTION, bd=5, image=CAMBIO_IMG, state="active")
CC.place(x= 470, y=550)
CC_lbl= Label(root, text= "CAMBIO CLIMATICO", font= Font_tuple2,fg="blue")
CC_lbl.place(x=455, y=520)

AGR = Button(root, text="ARICULTURAS", command =AGR_CONECTION, bd=5, image=AGRIC_IMG, state="active")
AGR.place(x= 320, y=550)
CC_lbl= Label(root, text= "AGRICULTURA", font= Font_tuple2,fg="blue")
CC_lbl.place(x=340, y=520)

DR=Button(root, text="DISTRITOS DE RIEGO", command =DRS, bd=5, image=DISTRITOS_IMG, state="active")
DR.place(x= 750, y=550)
DR_lbl= Label(root, text= "DISTRITOS DE RIEGO", font= Font_tuple2,fg="blue")
DR_lbl.place(x=755, y=520)

BALANCE=Button(root, text="BALANCE_AGUA", command =SWB, bd=5, image=BALANCE_S, state="active")
BALANCE.place(x= 930, y=550)
BALANCE_lbl= Label(root, text= "BALANCE AGUA", font= Font_tuple2,fg="blue")
BALANCE_lbl.place(x=920, y=520)

DECISION=Button(root, command =FACILIT, bd=5, image=FACILITATOR, state="active")
DECISION.place(x= 1070, y=550)
DECISION_lbl= Label(root, text= "TOMA DE DECISIONES", font= Font_tuple2,fg="blue")
DECISION_lbl.place(x=1050, y=520)


##DR_AYUDA = Button(root, text="AYUDA", command=HELP_DR, state="disabled",font= Font_tuple1)
##DR_AYUDA.place(x= 800, y=615)




root.mainloop()

##sf = shp.Reader("CUENCAS_TAMAULIPAS.shp")
##plt.figure()
##for shape in sf.shapeRecords():
##    x = [i[0] for i in shape.shape.points[:]]
##    y = [i[1] for i in shape.shape.points[:]]
##    plt.plot(x,y)
##plt.show()
