import bpy

def convert_usd_to_gltf(input_usd, output_gltf):
    
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Importing the .usd file
    bpy.ops.wm.usd_import(filepath=input_usd)

    # Exporting to .gltf
    bpy.ops.export_scene.gltf(filepath=output_gltf, export_format='GLB')

# Example usage
input_usd = '/Users/tessclln/Desktop/project/RC/Assets/_Class1RC.usd'
output_gltf = '/Users/tessclln/Desktop/project/RC/Assets/_Class1RC-try.glb'
convert_usd_to_gltf(input_usd, output_gltf)