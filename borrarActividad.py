from cargarActividad import cargarActividad

def borrarActividad(archivoActividad, nombreUsuario):
    actividad_dict = cargarActividad(archivoActividad)
    if (nombreUsuario in actividad_dict):
        del actividad[nombreUsuario]
        with open(archivoActividad, 'w') as f:
            for usuario_guardado, estado in actividad_dict.items():
                f.write(f"{usuario_guardado};{estado}\n")
        mensaje = "Usuario eliminado de la actividad correctamente."
    else:
        mensaje = "El usuario no se encuentra apuntado a esta actividad."
    return mensaje

