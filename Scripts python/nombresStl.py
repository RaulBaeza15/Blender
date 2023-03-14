import bpy
import os

# Ruta al archivo de texto
filepath = "C:\\Users\\br0353\\Desktop\\Nombres\\nombres.txt"

# Abre el archivo de texto y lee cada línea
with open(filepath, "r") as file:
    for line in file:
        # Crea un nuevo objeto y asigna el nombre de la línea
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(0, 0, 0))
        bpy.context.active_object.name = line.strip()

        # Exporta el objeto como STL
        export_path = "C:\\Users\\br0353\\Desktop\\Nombres\\" + line.strip() + ".stl"
        bpy.ops.export_mesh.stl(filepath=export_path, check_existing=False, use_selection=True)
        
        # Elimina el objeto creado
        bpy.data.objects[line.strip()].select_set(True)
        bpy.ops.object.delete()

