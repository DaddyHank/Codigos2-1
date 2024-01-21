import smtplib
import tkinter as tk
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import scrolledtext
from tkinter import messagebox


mensaje_mime = MIMEMultipart()

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        archivo_adjunto = open(ruta_archivo, 'rb').read()
      
        nombre_archivo = ruta_archivo.split("/")[-1]

        tipo_contenido = MIMEBase('application', 'octet-stream')
        tipo_contenido.set_payload(archivo_adjunto)
        encoders.encode_base64(tipo_contenido)
        tipo_contenido.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}')

        mensaje_mime.attach(tipo_contenido)
        
        # Mostrar el nombre del archivo junto al botón de subir archivo
        nombre_archivo_label.config(text=f"Archivo adjunto: {nombre_archivo}")

def enviar_correo():
    try:
        username = correo_entry.get()
        password = password_entry.get()
        destinatario = destinatario_entry.get()
        asunto = asunto_entry.get()
        smtp_server = 'smtp.gmail.com'
        port = 587

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()

 
        server.login(username, password)

        mensaje_mime['From'] = username
        mensaje_mime['To'] = destinatario
        mensaje_mime['Subject'] = asunto

        # Adjuntando el cuerpo del mensaje como texto HTML
        mensaje_mime.attach(MIMEText(cuerpo_texto.get("1.0", tk.END), 'html'))


        server.sendmail(username, destinatario, mensaje_mime.as_string())
        server.quit()

        messagebox.showinfo(title="¡Enviado!",message="Se ha enviado el mensaje correctamente")
        correo_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)
        destinatario_entry.delete(0,tk.END)
        asunto_entry.delete(0,tk.END)
        cuerpo_texto.delete(0,tk.END)
    except:
        if(len(correo_entry.get()) == 0 or len(password_entry.get())==0 or len(destinatario_entry.get()) == 0 or len(asunto_entry.get()) == 0):
            messagebox.showinfo(title="¡Error!",message="Debes rellenar el correo, la contraseña, el destinatario y el asunto")
        if("@gmail.com" in correo_entry.get() and "@gmail.com" in destinatario_entry.get()):
            pass
        else:
            messagebox.showinfo(title="¡Error!",message="¡Correos invalidos!")

ventana = tk.Tk()
ventana.title("Envío de Correo")
ventana.geometry("600x425")  


correo_label = tk.Label(ventana, text="Correo:")
correo_label.pack()
correo_entry = tk.Entry(ventana, width=40) 
correo_entry.pack()

password_label = tk.Label(ventana, text="Contraseña:")
password_label.pack()
password_entry = tk.Entry(ventana, show="*", width=40)
password_entry.pack()

destinatario_label = tk.Label(ventana, text="Destinatario:")
destinatario_label.pack()
destinatario_entry = tk.Entry(ventana, width=40)
destinatario_entry.pack()

asunto_label = tk.Label(ventana, text="Asunto:")
asunto_label.pack()
asunto_entry = tk.Entry(ventana, width=40)
asunto_entry.pack()

cuerpo_label = tk.Label(ventana, text="Cuerpo:")
cuerpo_label.pack()

# Campo de texto grande para el cuerpo
cuerpo_texto = scrolledtext.ScrolledText(ventana, width=40, height=10)
cuerpo_texto.pack()

# Etiqueta para mostrar el nombre del archivo adjunto
nombre_archivo_label = tk.Label(ventana, text="")
nombre_archivo_label.pack()

# Botón para abrir un archivo
abrir_archivo_button = tk.Button(ventana, text="Adjuntar Archivo", command=abrir_archivo)
abrir_archivo_button.pack()

# Botón para enviar el correo
enviar_button = tk.Button(ventana, text="Enviar Correo", command=enviar_correo)
enviar_button.pack()

#variables globales


ventana.mainloop()
