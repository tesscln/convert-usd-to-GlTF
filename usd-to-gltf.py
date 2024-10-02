import bpy
import sys

def clear_scene():
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select all objects and delete them
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

def convert_usd_to_gltf(input_usd, output_gltf):
    clear_scene()  # Clear the scene before importing the new file
    
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Importing the .usd file
    bpy.ops.wm.usd_import(filepath=input_usd)

    # Exporting to .gltf (not .glb)
    bpy.ops.export_scene.gltf(filepath=output_gltf, export_format='GLTF_SEPARATE')  # For .gltf format

# Allow the script to be called with command-line arguments
if __name__ == "__main__":
    input_usd = sys.argv[-2]  # Second-to-last argument
    output_gltf = sys.argv[-1]  # Last argument

    convert_usd_to_gltf(input_usd, output_gltf)

