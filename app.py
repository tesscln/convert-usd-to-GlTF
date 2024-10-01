import streamlit as st
import os
import subprocess

# Create a temporary directory if it doesn't exist
temp_dir = "./temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# File uploader widget
uploaded_file = st.file_uploader("Upload your USD file", type=["usd"])

if uploaded_file is not None:
    # Display file information
    st.write(f"File uploaded:\n\n{{\n\"filename\":\"{uploaded_file.name}\"\n\"filetype\":\"{uploaded_file.type}\"\n\"filesize\":{uploaded_file.size}\n}}")

    # Save the uploaded file to the temporary directory
    input_path = os.path.join(temp_dir, uploaded_file.name)
    
    # Write the uploaded file to disk
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File successfully saved to {input_path}")

    # Ask user to choose the output format
    option = st.selectbox("Choose conversion format", ("GLB", "GLTF"))

    # Set the output path
    output_file_name = os.path.splitext(uploaded_file.name)[0]  # Remove the extension
    if option == "GLB":
        output_path = os.path.join(temp_dir, f"{output_file_name}.glb")
        conversion_script = "usd-to-glb.py"
    else:
        output_path = os.path.join(temp_dir, f"{output_file_name}.gltf")
        conversion_script = "usd-to-gltf.py"
    
    st.write(f"Converting {uploaded_file.name} to {option}...")

    # Run the conversion script
    try:
        subprocess.run(["blender", "--background", "--python", conversion_script, "--", input_path, output_path], check=True)
        st.success(f"Conversion successful! File saved as {output_path}")
    except subprocess.CalledProcessError as e:
        st.error(f"Error during conversion: {e}")
