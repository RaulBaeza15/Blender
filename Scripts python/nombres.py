import bpy

# Ruta completa al archivo de texto
filename = "C:\\Users\\br0353\\Desktop\\Nombres\\nombres.txt"

# Abrir el archivo de texto y leer los nombres
with open(filename, "r") as file:
    names = file.read().splitlines()

# Configurar las propiedades del objeto llavero
scale = 0.1
location = (0, 0, 0)

# Crear un objeto llavero para cada nombre en la lista
for name in names:
    # Crear el objeto llavero
    bpy.ops.mesh.primitive_cube_add(location=location, scale=(scale, scale, scale))
    keychain = bpy.context.active_object
    keychain.name = f"{name}_keychain"
    
    # Agregar el nombre del objeto llavero como texto 3D
    bpy.ops.object.text_add(location=location, scale=(scale, scale, scale))
    text = bpy.context.active_object
    text.name = f"{name}_text"
    text.data.body = name
    
    # Mover el objeto de texto a la parte superior del objeto llavero
    text.location[2] += scale

    # Agrupar el objeto llavero y el objeto de texto juntos
    group_name = "keychains"
    if group_name not in bpy.data.groups:
        bpy.ops.group.create(name=group_name)
    bpy.data.groups[group_name].objects.link(keychain)
    bpy.data.groups[group_name].objects.link(text)

# Guardar el archivo
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

