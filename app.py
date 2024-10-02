import streamlit as st
import os
import subprocess

# Create a temporary directory to save uploaded files
TEMP_DIR = './temp'
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

st.title("USD to GLB/GLTF Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a .usd file", type=["usd"])

if uploaded_file is not None:
    file_path = os.path.join(TEMP_DIR, uploaded_file.name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File successfully saved to {file_path}")
    
    # Choose the conversion format
    conversion_format = st.selectbox("Choose conversion format", ["GLB", "GLTF"])
    
    # Button to trigger the conversion
    if st.button("Convert"):
        st.write(f"Converting {uploaded_file.name} to {conversion_format}...")

        # Set the output file path based on the chosen format
        if conversion_format == "GLB":
            output_file = os.path.join(TEMP_DIR, f"{os.path.splitext(uploaded_file.name)[0]}.glb")
            command = ['blender', '--background', '--python', 'usd-to-glb.py', '--', file_path, output_file]
        else:
            output_file = os.path.join(TEMP_DIR, f"{os.path.splitext(uploaded_file.name)[0]}.gltf")
            command = ['blender', '--background', '--python', 'usd-to-gltf.py', '--', file_path, output_file]
        
        try:
            # Run the Blender command to perform the conversion
            subprocess.run(command, check=True)
            st.success(f"Conversion successful! File saved as {output_file}")
        except subprocess.CalledProcessError as e:
            st.error(f"Error during conversion: {e}")
