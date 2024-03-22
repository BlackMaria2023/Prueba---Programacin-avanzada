from campaña import Campaña, LargoExcedidoException
from anuncio import Video, SubTipoInvalidoException

try:
    # Crear una instancia de Campaña con un anuncio de tipo Video
    campaña = Campaña("Campaña de prueba", [Video()])

    # Solicitar nuevo nombre de campaña y nuevo subtipo para el anuncio
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio: ")

    # Intentar asignar el nuevo nombre y subtipo con manejo de excepciones
    try:
        campaña.nombre = nuevo_nombre
    except LargoExcedidoException as e:
        # Escribir el mensaje de la excepción en el archivo error.log
        with open("error.log", "a") as file:
            file.write(str(e) + "\n")

    try:
        campaña.anuncios[0].sub_tipo = nuevo_subtipo
    except SubTipoInvalidoException as e:
        # Escribir el mensaje de la excepción en el archivo error.log
        with open("error.log", "a") as file:
            file.write(str(e) + "\n")

except Exception as e:
    # Manejo de excepciones no especificadas, escribir el mensaje en el archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")