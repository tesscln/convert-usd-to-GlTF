import streamlit as st
import os
import subprocess

# Function to run a Python script for conversion
def run_conversion_script(script_name, input_path, output_path):
    try:
        # Run the appropriate conversion script with input and output paths
        result = subprocess.run(['python', script_name, input_path, output_path], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error running the conversion script: {str(e)}"

# Streamlit UI
st.title("USD to GLB/GLTF Converter")

# File uploader for .usd files
uploaded_file = st.file_uploader("Upload a USD file", type=["usd"])

if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    st.write("File uploaded:", file_details)

    # Save the uploaded file temporarily
    input_path = f"./temp/{uploaded_file.name}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Let the user choose between GLB or GLTF
    conversion_choice = st.radio("Convert to:", ('GLB', 'GLTF'))

    # Generate output file name based on user's choice
    output_extension = 'glb' if conversion_choice == 'GLB' else 'gltf'
    output_path = f"./temp/{uploaded_file.name.split('.')[0]}.{output_extension}"

    # Conversion button
    if st.button("Convert"):
        if uploaded_file.name.endswith(".usd"):
            if conversion_choice == "GLB":
                output = run_conversion_script('usd-to-glb.py', input_path, output_path)
            else:
                output = run_conversion_script('usd-to-gltf.py', input_path, output_path)
            
            st.success(f"Conversion to {conversion_choice} completed!")
            st.write(output)
            st.download_button("Download the converted file", data=open(output_path, "rb"), file_name=output_path.split('/')[-1])
        else:
            st.error("Error: Please upload a valid .usd file.")
else:
    st.warning("Please upload a USD file to start the conversion.")
