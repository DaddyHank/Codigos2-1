import tkinter as tk
from tkinter import *
from pymongo import MongoClient
from tkinter import messagebox
import bson as bs

#conexion a la database
client = MongoClient("mongodb://Darien:yo%20cuando123@localhost:27017/?authMechanism=SCRAM-SHA-1")
db = client["Empleados_Hospital"]
collection = db["Empleados"]

#funcion para insertar documento

def limpiar_campos():
    id_entry.delete(0,tk.END)
    nombre_entry.delete(0,tk.END)
    edad_entry.delete(0,tk.END)

def insertar_documento():
    nombre = nombre_entry.get()
    edad = int(edad_entry.get())
    documento = {"nombre":nombre,"edad":edad}
    result = collection.insert_one(documento)
    messagebox.showinfo("Genial",f"Documento insertado con _id:{result.inserted_id}")
    limpiar_campos()

def buscar_documentos():
    resultados.delete(0,tk.END)#limpiar la lista de resultados
    for doc in collection.find():
        resultados.insert(tk.END,f"Id:{doc['_id']},Nombre:{doc['nombre']},Edad:{doc['edad']}")

def select_documentos(event):
    id_entry.delete(0,tk.END)
    nombre_entry.delete(0,tk.END)
    edad_entry.delete(0,tk.END)
    object = resultados.selection_get()
    for doc in collection.find():
        id = doc['_id']
        if(str(id) in object):
            id_entry.insert(0,doc["_id"])
            nombre_entry.insert(0,doc["nombre"])
            edad_entry.insert(0,doc["edad"])

def delete_document():
    id_en = id_entry.get()
    collection.delete_one({"_id": bs.ObjectId(id_en)})
    messagebox.showinfo("Genial",f"Eliminaste correctamente el elemento de id:{id_en}")
    buscar_documentos()
    limpiar_campos()

def update_document():
    id = id_entry.get()
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    collection.update_one({"_id":bs.ObjectId(id)},{"$set":{"nombre":nombre,"edad":edad}})

#crear una ventana de tkinter
ventana = tk.Tk()
ventana.title("Aplicacion Mongo base de datos")

#crear elementos de la gui
id_label = tk.Label(ventana,text="id:")
id_entry = tk.Entry(ventana)

nombre_label = tk.Label(ventana,text="Nombre")
nombre_entry = tk.Entry(ventana)

edad_label = tk.Label(ventana,text="Edad:")
edad_entry = tk.Entry(ventana)

#botones
insertar_button = tk.Button(ventana,text="Insertar",command=insertar_documento)
buscar_button = tk.Button(ventana,text="Buscar",command=buscar_documentos)
eliminar_button = tk.Button(ventana,text="Eliminar",command=delete_document)
actualizar_button = tk.Button(ventana,text="Editar",command=update_document)

resultados = tk.Listbox(ventana,width=590)
resultados.bind("<Button-1>",select_documentos)

#colocar elementos de la gui
id_label.pack()
id_entry.pack()

nombre_label.pack()
nombre_entry.pack()

edad_label.pack()
edad_entry.pack()

insertar_button.pack()
buscar_button.pack()
eliminar_button.pack()
actualizar_button.pack()

resultados.pack()

#tamaño de la ventana
ventana.geometry("800x600")

#disparo de eventos
buscar_documentos()

#iniciar interfaz
ventana.mainloop()