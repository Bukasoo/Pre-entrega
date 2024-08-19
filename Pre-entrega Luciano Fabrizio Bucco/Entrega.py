# Creo un diccionario el cual va a guardar los usuarios creados
#Tambien va a servir para mostrar por pantalla los usuarioas cuando se le indique
Usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario(Nombre, Contraseña):
    if Nombre in Usuarios:
        print("El usuario/a ya existe.")
    else:
        Usuarios[Nombre] = Contraseña
        print(f"Usuario/a {Nombre} registrado con éxito.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    if Usuarios:
        print("Usuarios registrados en la base de datos:")
        for Nombre, Contraseña in Usuarios.items():
            print(f"Nombre: {Nombre}, Contraseña: {Contraseña}")
    else:
        print("No hay usuarios registrados.")

# Función para el inicio sesión
def iniciar_sesion(Nombre, Contraseña):
    if Nombre in Usuarios and Usuarios[Nombre] == Contraseña:
        print(f"Bienvenido/a, {Nombre}!")
    else:
        print("Nombre de usuario/a o contraseña incorrectos.")

# Bucle principal del programa
while True:
    print("\n1.Registrar usuario")
    print("\n2.Mostrar usuarios")
    print("\n3.Iniciar sesión")
    print("\n4.Salir")
    opciones = input("Elige una opción: ")

    if opciones == "1":
        Nombre = input("Introduce el nombre de usuario/a: ")
        Contraseña = input("Introduce la contraseña: ")
        registrar_usuario(Nombre, Contraseña)
    elif opciones == "2":
        mostrar_usuarios()
    elif opciones == "3":
        Nombre = input("Introduce el nombre de usuario/a: ")
        Contraseña = input("Introduce la contraseña: ")
        iniciar_sesion(Nombre, Contraseña)
    elif opciones == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")