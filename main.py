import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from analizador import instruccion, realizar_operaciones, generar_grafica, limpiar_lista, crear_archivo_errores, limpiar_lista_errores, lexemas_grafico


class ventana_principal:
    def __init__(self, root):
        #Variable Analizado
        self.archivo_seleccionado=False
        self.archivo_analizado=False

        #Ventana Pricipal
        self.root = root
        self.root.title("PROYECTO 1 - CARLOS MANUEL LIMA Y LIMA")
        self.root.geometry("1000x600")
        self.root.configure(bg='#0799b6')
        self.root.resizable(0,0)

        #Frame Botones Opciones
        opciones_frame=tk.Frame(root,bg='#114c5f')

        boton_archivo=tk.Menubutton(opciones_frame, text="Archivo", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')        
        boton_archivo.place(x=50, y=10, width=150)

        opciones=Menu(boton_archivo,tearoff=0)
        boton_archivo["menu"]=opciones
        opciones.add_command(label="Abrir", font=("Verdana", 13), activeforeground='black', command=self.buscar_archivo)
        opciones.add_command(label="Guardar", font=("Verdana", 13),  activeforeground='black', command=self.guardar_archivo)
        opciones.add_command(label="Guardar Como", font=("Verdana", 13),  activeforeground='black', command=self.guardar_como)
        opciones.add_command(label="Salir", font=("Verdana", 13), activeforeground='black', command=self.salir)

        boton_analizar=tk.Button(opciones_frame,text="Analizar", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.analizar)
        boton_analizar.place(x=250, y=10, width=150)

        boton_errores=tk.Button(opciones_frame,text="Errores", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.errores)
        boton_errores.place(x=450,y=10, width=150)

        boton_reporte=tk.Button(opciones_frame,text="Reporte", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.reporte)
        boton_reporte.place(x=650, y=10, width=150)

        opciones_frame.pack(pady=0)
        opciones_frame.pack_propagate()
        opciones_frame.configure(width=1000, height=50)
        
        #Frame Cuadro De Texto
        cuadrotexto_frame=tk.Frame(root,bg='#0799b6')
        self.cuadroTexto = scrolledtext.ScrolledText(cuadrotexto_frame, font=("Verdana", 10), bg="white", width=110, height=33)
        self.cuadroTexto.place(x=0, y=0)
        cuadrotexto_frame.pack(pady=5)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.configure(width=900, height=550)


    def buscar_archivo(self):
        texto_archivo = ""
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
        try:
            self.ruta_seleccionada= nueva_ruta = filedialog.askopenfilename(filetypes=[("Archivos JSON", f"*.json")])
            with open(nueva_ruta, encoding="utf-8") as archivo_json:
                texto_archivo = archivo_json.read()
            self.texto = texto_archivo
            self.cuadroTexto.delete(1.0, "end")
            self.cuadroTexto.insert(1.0, self.texto)
            messagebox.showinfo("Abrir", "Archivo Cargado Correctamente.")
            self.archivo_seleccionado=True
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
            return
    
    def guardar_archivo(self):
        try:
            if self.archivo_seleccionado==True:
                self.texto = self.cuadroTexto.get(1.0, "end")
                archivo = open(self.ruta_seleccionada, 'w', encoding="utf-8")
                archivo.write(self.texto)
                messagebox.showinfo("Guardar", "Archivo Guardado Correctamente.")
            else:
                messagebox.showwarning("Error", "No se ha seleccionado ningún archivo.")
            return
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
            return

    def guardar_como(self):
        try:
            if self.archivo_seleccionado==True:
                self.texto = self.cuadroTexto.get(1.0, "end")
                self.archivo = asksaveasfilename(filetypes=[("Archivos JSON", f"*.json")], defaultextension=[("Archivos JSON", f"*.json")], initialfile=" ")
                archivo = open(self.archivo, 'w', encoding="utf-8")
                archivo.write(self.texto)
                messagebox.showinfo("Guardar Como", "Archivo Guardado Correctamente.")
            else:
                messagebox.showwarning("Error", "No se ha seleccionado ningún archivo.")
            return
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
            return

    def salir(self):
        try:
            messagebox.showinfo("Salir", "Gracias por utilizar el programa.")
            self.root.destroy()
        except:
            messagebox.showerror("Error", "Se ha producido un error.")


    def analizar(self):
        limpiar_lista_errores()
        limpiar_lista()
        try:
            if self.archivo_seleccionado==True:
                instruccion(self.texto)
                lexemas_grafico()
                realizar_operaciones()
                messagebox.showinfo("Analizar", "Análisis Realizado Correctamente.")
                self.archivo_analizado=True
            else:
                messagebox.showwarning("Error", "No se ha seleccionado ningún archivo.")
        except:
            messagebox.showerror("Error", "Se ha producido un error.")
            return

    def reporte(self):
        try:
            if self.archivo_analizado==True:
                generar_grafica(str("REPORTE_202201524"))
                messagebox.showinfo("Reporte", "Reporte Creado Correctamente.")
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except:
            messagebox.showerror("Error", "Se ha producido un error.")
            return

    def errores(self):
        try:
            if self.archivo_analizado==True:
                crear_archivo_errores()
                messagebox.showinfo("Errores", "Reporte de Errores Creado Correctamente.")
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except:
            messagebox.showerror("Error","Se ha producido un error.")
            return

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()