usuario_correcto = "Admin"
contraseña_correcta = "Admin2026"

intentos_usuario = 3
intentos_contraseña = 3

# -------- VALIDACIÓN DEL USUARIO --------
while intentos_usuario > 0:
    usuario = input("Ingrese el nombre de usuario: ")

    tiene_letra = False
    tiene_numero = False

    for c in usuario:
        if c.isalpha():
            tiene_letra = True
        if c.isdigit():
            tiene_numero = True

    if not (tiene_letra and tiene_numero):
        intentos_usuario -= 1
        print("El usuario debe contener al menos una letra y un número.")
        print(f"Intentos restantes de usuario: {intentos_usuario}")
    elif usuario != usuario_correcto:
        intentos_usuario -= 1
        print("Usuario incorrecto.")
        print(f"Intentos restantes de usuario: {intentos_usuario}")
    else:
        print("Usuario correcto.")
        break

if intentos_usuario == 0:
    print("Acceso denegado. Se agotaron los intentos de usuario.")
else:
    # -------- VALIDACIÓN DE CONTRASEÑA --------
    while intentos_contraseña > 0:
        contraseña_ingresada = input("Ingrese la contraseña: ")

        if contraseña_ingresada == contraseña_correcta:
            print("¡Acceso concedido!")
            break
        else:
            intentos_contraseña -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos_contraseña}")

            if intentos_contraseña == 0:
                print("Acceso denegado. Se agotaron los intentos de contraseña.")