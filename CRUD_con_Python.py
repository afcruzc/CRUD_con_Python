from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

root.title("Practica CRUD")

#------------------------------------Funciones Barra Menu------------------------------------
#-----Conexión a la BBDD-----
def conecxionBD():

    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute("CREATE TABLE DATOS_USUARIO (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario VARCHAR(50), apellido_usuario VARCHAR(50), password_usuario VARCHAR(32), direccion_usuario VARCHAR(50), comentarios VARCHAR(100))")

        messagebox.showinfo("Base de Datos", "Base de Datos creada con exito.")

    except:
        messagebox.showwarning("¡Atención!", "La Base de Datos ya existe.")

#-----Cerrar aplicación-----
def cerrarApp():

    valor=messagebox.askokcancel("Salir","¿Deseas salir?")
    if valor==True:
        confirmacion=messagebox.askquestion("Salir","¿Esta seguro?")
        if confirmacion=="yes":
            root.destroy()

#-----Borar Campos-----
def borrarCampos():

    ID.set("")
    nombre.set("")
    apellido.set("")
    password.set("")
    direccion.set("")
    textoComentario.delete(1.0,END)
#---------Crear Registro---------
def crear():
    miConexion= sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos = nombre.get(), apellido.get(), password.get(),direccion.get(), textoComentario.get("1.0",END)

    """miCursor.execute("INSERT INTO DATOS_USUARIO VALUES(NULL,'" + nombre.get() + "','" + apellido.get() + "','" + password.get() + "','" + direccion.get() + "','" + textoComentario.get("1.0",END) + "')")"""
    miCursor.execute("INSERT INTO DATOS_USUARIO VALUES(NULL,?,?,?,?,?)", (datos))
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "Resgistro ingresado con éxito.")
#---------Leer---------
def leer():
    miConexion= sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIO WHERE id=" + ID.get())

    infoUsuario = miCursor.fetchall()

    for usuario in infoUsuario:

        ID.set(usuario[0])
        nombre.set(usuario[1])
        apellido.set(usuario[2])
        password.set(usuario[3])
        direccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

#---------Actualizar---------
def actualizar():
    miConexion= sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos = nombre.get(), apellido.get(), password.get(),direccion.get(), textoComentario.get("1.0",END)

    """miCursor.execute("UPDATE DATOS_USUARIO SET nombre_usuario='" + nombre.get() + 
    "', apellido_usuario='" + apellido.get() + 
    "', password_usuario='" + password.get() +
    "', direccion_usuario='" + direccion.get() +
    "', comentarios='" + textoComentario.get("1.0", END) +
    "' WHERE id=" + ID.get())"""

    miCursor.execute("UPDATE DATOS_USUARIO SET nombre_usuario=?, apellido_usuario=?, password_usuario=?, direccion_usuario=?, comentarios=?" + 
    "WHERE id=" + ID.get(),(datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Resgistro actualizado con éxito.")

#---------Eliminar---------
def eliminar():
    miConexion= sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIO WHERE ID=" + ID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Resgistro eliminado con éxito.")
#-------------------------------------Comienzo de Barra de Menu-------------------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu= Menu(barraMenu, tearoff=0,)
bbddMenu.add_command(label="Conectar", command=conecxionBD)
bbddMenu.add_command(label="Salir", command=cerrarApp)

borrarMenu= Menu(barraMenu, tearoff=0,)
borrarMenu.add_command(label="Borrar Campos", command=borrarCampos)

crudMenu= Menu(barraMenu, tearoff=0,)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu= Menu(barraMenu, tearoff=0,)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

frameCampos=Frame(root)
frameCampos.pack()
#-------------------------------------Comienzo de labels-------------------------------------
labelID = Label(frameCampos, text="ID: ")
labelID.grid(row=0,column=0, padx=10, pady=10, sticky="n")

labelNombre = Label(frameCampos, text="Nombre: ")
labelNombre.grid(row=1,column=0, padx=10, pady=10)

labelApellido = Label(frameCampos, text="Apellido: ")
labelApellido.grid(row=2,column=0, padx=10, pady=10)

labelPassword = Label(frameCampos, text="Password: ")
labelPassword.grid(row=3,column=0, padx=10, pady=10)

labelDireccion = Label(frameCampos, text="Dirección: ")
labelDireccion.grid(row=4,column=0, padx=10, pady=10)

labelComentarios = Label(frameCampos, text="Comentarios: ")
labelComentarios.grid(row=5,column=0, padx=10, pady=10)
#-------------------------------------Comienzo de campos-------------------------------------

ID=StringVar()
nombre=StringVar()
apellido=StringVar()
password=StringVar()
direccion=StringVar()

cuadroID = Entry(frameCampos, textvariable=ID)
cuadroID.grid(row=0,column=1, padx=10,pady=10)
cuadroID.config(justify="left")

cuadroNombre = Entry(frameCampos, textvariable=nombre)
cuadroNombre.grid(row=1,column=1, padx=10,pady=10)
cuadroNombre.config(justify="left")

cuadroApellido = Entry(frameCampos, textvariable=apellido)
cuadroApellido.grid(row=2,column=1, padx=10,pady=10)
cuadroApellido.config(justify="left")

cuadroPassword = Entry(frameCampos, textvariable=password)
cuadroPassword.grid(row=3,column=1, padx=10,pady=10)
cuadroPassword.config(show="*",justify="left")

cuadroDireccion = Entry(frameCampos, textvariable=direccion)
cuadroDireccion.grid(row=4,column=1, padx=10,pady=10)
cuadroDireccion.config(justify="left")

textoComentario = Text(frameCampos, width=16, height=5)
textoComentario.grid(row=5,column=1, padx=10,pady=10)
scrollVert= Scrollbar(frameCampos, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------------------------Comienzo de Botones------------------------------------
frameBotones=Frame(root)
frameBotones.pack()

createButton= Button(frameBotones, text="Create", command=crear)
createButton.grid(row=0, column=1, sticky="e", padx=10,pady=10)

readButton= Button(frameBotones, text="Read", command=leer)
readButton.grid(row=0, column=2, sticky="e", padx=10,pady=10)

updateButton= Button(frameBotones, text="Update", command=actualizar)
updateButton.grid(row=0, column=3, sticky="e", padx=10,pady=10)

deleteButton= Button(frameBotones, text="Delete",command=eliminar)
deleteButton.grid(row=0, column=4, sticky="e", padx=10,pady=10)


root.mainloop()