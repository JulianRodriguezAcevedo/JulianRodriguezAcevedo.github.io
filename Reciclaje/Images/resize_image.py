import os

# --- CONFIGURACIÓN ---
# ¡IMPORTANTE! Cambia esta ruta a la de tu carpeta de imágenes.
# Ejemplos:
# Windows: "C:\\Users\\TuUsuario\\Desktop\\fotos_desordenadas"
# macOS/Linux: "/Users/TuUsuario/Desktop/fotos_desordenadas"
RUTA_CARPETA = "fotos_desordenadas"

# (Opcional) Puedes cambiar el prefijo del nuevo nombre.
# Si lo dejas vacío (''), los nombres serán "1.jpg", "2.png", etc.
PREFIJO = 'imagen_'

# (Opcional) El número con el que comenzará la enumeración.
NUMERO_INICIAL = 1

# --- ADVERTENCIA DE SEGURIDAD ---
print("************************************************************")
print("¡ADVERTENCIA! Este script cambiará permanentemente el nombre")
print("de los archivos de imagen en la siguiente carpeta:")
print(f" -> {os.path.abspath(RUTA_CARPETA)}")
print("************************************************************")
print("Se recomienda hacer una COPIA DE SEGURIDAD antes de continuar.")

# Pedir confirmación al usuario
confirmacion = input("¿Estás seguro de que quieres continuar? (escribe 'si' para confirmar): ")

if confirmacion.lower() != 'si':
    print("Operación cancelada por el usuario.")
    exit()

# --- LÓGICA DEL SCRIPT ---
try:
    # Obtener una lista de todos los archivos en el directorio
    archivos = os.listdir(RUTA_CARPETA)
    
    # Ordenar los archivos alfabéticamente para un renombrado consistente
    archivos.sort()
    
    # Filtrar solo los archivos que son imágenes
    extensiones_imagen = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
    imagenes = [f for f in archivos if f.lower().endswith(extensiones_imagen)]

    if not imagenes:
        print("No se encontraron archivos de imagen en la carpeta especificada.")
        exit()

    print(f"\nSe encontraron {len(imagenes)} imágenes. Empezando a renombrar...")

    # Inicializar el contador
    contador = NUMERO_INICIAL

    # Recorrer cada archivo de imagen
    for nombre_antiguo in imagenes:
        # 1. Separar el nombre de su extensión
        _, extension = os.path.splitext(nombre_antiguo)
        
        # 2. Crear el nuevo nombre del archivo
        # Usamos zfill(3) para rellenar con ceros a la izquierda (ej: 001, 002, ..., 010, ..., 100)
        # Si tienes más de 999 imágenes, cambia el 3 por 4 o más.
        nombre_nuevo = f"{PREFIJO}{str(contador).zfill(3)}{extension.lower()}"
        
        # 3. Obtener las rutas completas
        ruta_antigua = os.path.join(RUTA_CARPETA, nombre_antiguo)
        ruta_nueva = os.path.join(RUTA_CARPETA, nombre_nuevo)
        
        # 4. Renombrar el archivo
        os.rename(ruta_antigua, ruta_nueva)
        
        print(f"  '{nombre_antiguo}'  ->  '{nombre_nuevo}'")
        
        # 5. Incrementar el contador para el siguiente archivo
        contador += 1

    print("\n¡Proceso completado exitosamente!")

except FileNotFoundError:
    print(f"\nERROR: La carpeta '{RUTA_CARPETA}' no fue encontrada.")
    print("Por favor, verifica que la ruta en la variable RUTA_CARPETA sea correcta.")
except Exception as e:
    print(f"\nHa ocurrido un error inesperado: {e}")