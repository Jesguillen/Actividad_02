# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:29:44 2022

@author: JesusG
"""

import tkinter as tk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry ("1225x600")
ventana.config(bg="dark violet")

#Primera Fila

espacio = tk.Label(ventana, bg="dark violet", fg="black")
espacio.grid (row = 0, column = 0)

txt1 = tk.Label(ventana, text="Distancia Focal (mm)=", bg="dark violet", fg="black")
txt1.grid (row = 1, column = 0)

cuadro1 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro1.grid (row = 1, column = 1)

txt2 = tk.Label(ventana, text="Ancho del sensor (mm) =", bg="dark violet", fg="black")
txt2.grid (row = 1, column = 2)

cuadro2 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro2.grid (row = 1, column = 3)

txt3 = tk.Label(ventana, text="Solape Longitudinal (%)=", bg="dark violet", fg="black")
txt3.grid (row = 1, column = 4)

cuadro3 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro3.grid (row = 1, column = 5)

#SEGUNDA FILA

espacio1 = tk.Label(ventana, bg="dark violet", fg="dark violet")
espacio1.grid (row = 2, column = 0)

txt4 = tk.Label(ventana, text="Ancho de la imagen (Pixel)=", bg="dark violet", fg="black")
txt4.grid (row = 3, column = 0)

cuadro4 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro4.grid (row = 3, column = 1)

txt5 = tk.Label(ventana, text="Alto del sensor (mm)=", bg="dark violet", fg="black")
txt5.grid (row = 3, column = 2)

cuadro5 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro5.grid (row = 3, column = 3)

txt6 = tk.Label(ventana, text="Solape Transversal (%)=", bg="dark violet", fg="black")
txt6.grid (row = 3, column = 4)

cuadro6 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro6.grid (row = 3, column = 5)

#Tercera Fila

espacio2 = tk.Label(ventana, bg="dark violet", fg="black")
espacio2.grid (row = 4, column = 0)

txt7 = tk.Label(ventana, text="Alto de la imagen (Pixel) =", bg="dark violet", fg="black")
txt7.grid (row = 5, column = 0)

cuadro7 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro7.grid (row = 5, column = 1)

txt8 = tk.Label(ventana, text="Altura del vuelo (m)=", bg="dark violet", fg="black")
txt8.grid (row = 5, column = 2)

cuadro8 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro8.grid (row = 5, column = 3)

txt9 = tk.Label(ventana, text="Largo de la parcela (m)=", bg="dark violet", fg="black")
txt9.grid (row = 5, column = 4)

cuadro9 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro9.grid (row = 5, column = 5)

#Cuarta Fila

espacio3 = tk.Label(ventana, bg="dark violet", fg="black")
espacio3.grid (row = 6, column = 0)

txt10 = tk.Label(ventana, text="Ancho de la parcela (m)=", bg="dark violet", fg="black")
txt10.grid (row = 7, column = 1)

cuadro10 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro10.grid (row = 7, column = 2)

txt11 = tk.Label(ventana, text="Velocidad del vuelo (m/s)=", bg="dark violet", fg="black")
txt11.grid (row = 7, column = 3)

cuadro11 = tk.Entry(ventana, font = "arial 12", justify = "center")
cuadro11.grid (row = 7, column = 4)

espacio3 = tk.Label(ventana, bg="dark violet", fg="dark violet")
espacio3.grid (row = 8, column = 0)


espacio3 = tk.Label(ventana, bg="dark violet", fg="dark violet")
espacio3.grid (row = 10, column = 0)

#Resultados
textResult = tk.Text(ventana)
textResult.grid(row = 11, column = 0, columnspan = 6)

#Cálculo 

def resultados():
    textResult.delete(1.0, tk.END)
    dist_focal = float(cuadro1.get())
    ancho_sensor = float(cuadro2.get())
    solape_long = float(cuadro3.get())
    ancho_imgen = float(cuadro4.get())
    alt_sensor = float(cuadro5.get())
    RSI = ancho_sensor/ancho_imgen
    solape_trans = float(cuadro6.get())
    altura_img = int(cuadro7.get())
    alt_vuelo = float(cuadro8.get())
    largo_parcela = float(cuadro9.get())
    ancho_parcela = float(cuadro10.get())
    vel_vuelo = float(cuadro11.get())
    
    
    #GSD
    GSD = (((alt_vuelo * 100 )/ (dist_focal)) * RSI)
    textResult.insert(tk.END, f"GSD = {GSD}cm/pixel\n\n")
    
    #Escala de Vuelo
    escala_vuelo = 1/((dist_focal/1000)/alt_vuelo)
    textResult.insert(tk.END, f"Escala de vuelo = {escala_vuelo}\n\n")
    
    #Ancho de la imagen
    AIMGTomada = (ancho_sensor*escala_vuelo)/1000
    textResult.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {AIMGTomada}m\n\n")
    
    #Alto de la imagen
    AIMGTomada = (alt_sensor*escala_vuelo)/1000
    textResult.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {AIMGTomada}m\n\n")
    
    #Base Aérea
    base_aer = (((ancho_imgen * GSD )/100)* (1-(solape_long/100)))
    textResult.insert(tk.END, f"Base Aerea = {base_aer}\n\n")
    
    #Distancia entre pasadas
    DxPasada = (((altura_img * GSD )/100)) * (1-(solape_trans/100))
    textResult.insert(tk.END, f"Distancia entre Pasadas = {DxPasada}m\n\n")
    
    #Tiempo entre fotos y velocidad de vuelo
    t_fotos = base_aer/vel_vuelo
    vel_vuelo= base_aer/t_fotos
    textResult.insert(tk.END, f"Tiempo entre fotos = {t_fotos}s\n\n")
    textResult.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo}m/s\n\n")
    
    #Número de pasadas
    num_pasadas = ancho_parcela/DxPasada
    textResult.insert(tk.END, f"Numero de Pasadas = {num_pasadas}\n\n")
    
    #Número de fotos por pasada
    num_fotos = (largo_parcela/base_aer)+1
    textResult.insert(tk.END, f"Numero de Fotos por Pasada = {num_fotos}\n\n")
    
    #Número de fotos por vuelo
    num_f_v= num_fotos*num_pasadas
    textResult.insert(tk.END, f"Numero de Fotos por Vuelo = {num_f_v}\n\n")
    
    #Distancia de Vuelo
    dist_vuelo = (num_pasadas*largo_parcela)+ancho_parcela
    textResult.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo}m\n\n")
    
    #Duración de vuelo 
    t_vuelo= ((num_f_v * t_fotos)/60)
    textResult.insert(tk.END, f"Duracion del Vuelo = {t_vuelo}min")
    
    popup_showinfo()

#Ventana Emergente
def popup_showinfo():
    message ="¡realizado!"
    showinfo(message)
    
#Botón de Cálculo (con cambio de color incluido)
boton_calculo = tk.Button(text = "Calcular", font= 'Cambria 11', command = resultados)
boton_calculo.grid(row = 9, column = 2, columnspan = 2)


#Título 
ventana.title("Calculadora de parámetros de vuelo de drone")

ventana.mainloop()