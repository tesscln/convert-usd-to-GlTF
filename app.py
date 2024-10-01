import streamlit as st
import os
import subprocess

# Function to run a Python script
def run_conversion_script(script_name, file_path):
    try:
        # Run the appropriate conversion script
        result = subprocess.run(['python', script_name, file_path], capture_output=True, text=True)
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
    with open(f"./temp/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Let the user choose between GLB or GLTF
    conversion_choice = st.radio("Convert to:", ('GLB', 'GLTF'))

    # Conversion button
    if st.button("Convert"):
        file_path = f"./temp/{uploaded_file.name}"
        
        if uploaded_file.name.endswith(".usd"):
            if conversion_choice == "GLB":
                output = run_conversion_script('usd-to-glb.py', file_path)
            else:
                output = run_conversion_script('usd-to-gltf.py', file_path)
            
            st.success("Conversion completed!")
            st.text(output)
        else:
            st.error("Error: Please upload a valid .usd file.")
else:
    st.warning("Please upload a USD file to start the conversion.")
