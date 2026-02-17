def validar_entero(numero):
    if not isinstance(numero, int):
        raise ValueError("El valor debe ser un número entero.")
    return numero


def convertir_a_base(numero, base):
    if numero == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    resultado = ""
    temp_num = numero

    while temp_num > 0:
        residuo = temp_num % base
        resultado = digitos[residuo] + resultado
        temp_num = temp_num // base

    return resultado


def a_binario(numero):
    return convertir_a_base(numero, 2)


def a_octal(numero):
    return convertir_a_base(numero, 8)


def a_hexadecimal(numero):
    return convertir_a_base(numero, 16)


def a_booleano(numero):
    return numero != 0


# --- Ejemplo de uso ---
numero = 25
numero = validar_entero(numero)

print(f"Decimal: {numero}")
print(f"Binario: {a_binario(numero)}")
print(f"Octal: {a_octal(numero)}")
print(f"Hexadecimal: {a_hexadecimal(numero)}")
print(f"Booleano: {a_booleano(numero)}")
