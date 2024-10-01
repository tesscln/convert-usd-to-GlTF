# Use an official Blender image as a base
FROM blender:3.3.0

# Install pip and other necessary Python packages
RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install --no-cache-dir streamlit

# Copy the local app and conversion scripts to the container
COPY app.py /usr/src/app/app.py
COPY usd-to-glb.py /usr/src/app/usd-to-glb.py
COPY usd-to-gltf.py /usr/src/app/usd-to-gltf.py

# Create a directory for storing temporary files
RUN mkdir -p /usr/src/app/temp

# Set the working directory
WORKDIR /usr/src/app

# Expose Streamlit's default port (8501)
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.port=8501"]
