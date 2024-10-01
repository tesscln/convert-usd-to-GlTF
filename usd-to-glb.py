import bpy
import sys

def clear_scene():
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select all objects and delete them
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

def convert_usd_to_glb(input_usd, output_glb):
    clear_scene()
    
    # Importing the .usd file
    bpy.ops.wm.usd_import(filepath=input_usd)

    # Exporting to .glb
    bpy.ops.export_scene.gltf(filepath=output_glb, export_format='GLB')

# Allow the script to be called with command-line arguments
if __name__ == "__main__":
    input_usd = sys.argv[-2]  # Second-to-last argument
    output_glb = sys.argv[-1]  # Last argument

    convert_usd_to_glb(input_usd, output_glb)

