# USD to GLB/GLTF Converter
## Convert your .usd file to .gltf or .glb

This Streamlit app allows users to upload `.usd` files and convert them to `.glb` or `.gltf` formats using Blender.

## Prerequisites

1. **Download and Install Blender**  
   Please download and install Blender (version 3.6 or above) from the official [Blender website](https://www.blender.org/download/).

   After installation, ensure that Blender is accessible via the command line. To check if Blender is available, open a terminal and run:

   ```bash
   blender --version

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/tesscln/convert-usd-to-GlTF.git
cd convert-usd-to-GlTF
```

### Step 2: Set Up a Virtual Environment

Depending on what you use locally (conda, venv, virtualenv).


### Step 3: Install Required Python Packages

```bash
pip install -r requirements.txt
```

---

### Step 4: Running the app

```bash
streamlit run app.py
```

Once the app is running, open your browser and go to the displayed URL (usually ```http://localhost:8501```).

### Step 5: Using the app

1. Upload a **.usd** file.
2. **Choose the format:** Select whether you want to convert the file to **.glb** or **.gltf**.
    
    For GlTF conversion: this app converts the **.usd** to a separate GlTF, meaning it creates a **.gltf** file and a **.bin** file. Instead, if you would like an embedded GlTF file, you can refer to the ***Appendix*** section below.

3. **Click "Convert":** The app will process the file and save the converted version in the **./temp/** directory.

---

### Appendix

Modifying the Conversion Script for **GLTF** from **separate** to **embedded**.

1. Open the ```usd-to-gltf.py``` file. 
2. Modify the following line:
    ```bpy.ops.export_scene.gltf(filepath=output_gltf, export_format='GLTF_SEPARATE')```

    to:

    ```bpy.ops.export_scene.gltf(filepath=output_gltf, export_format='GLTF_EMBEDDED')``` 

3. Then in your terminal, run:

```bash
    git add usd-to-gltf.py
    git commit -m "Modified usd-to-gltf.py to convert the file to an embedded one"
```

---

### Troubleshooting

If you encounter any issues, here are some common troubleshooting tips:

- **Blender Not Found**: If the app can't find Blender, ensure that it's installed and accessible via the command line. You may need to add Blender to your **system's PATH**.

- **Missing Dependencies**: If you run into missing dependency errors, make sure to install all required Python packages.

---

### Contributing

Feel free to submit issues or pull requests to improve this application!