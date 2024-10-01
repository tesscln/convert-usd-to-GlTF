# Use Ubuntu as a base image
FROM ubuntu:20.04

# Install necessary dependencies for Blender and xz-utils for extracting .tar.xz files
RUN apt-get update && apt-get install -y wget sudo libglu1-mesa libxi6 libxrender1 libpulse0 xz-utils

# Download Blender 3.6
RUN wget https://download.blender.org/release/Blender3.6/blender-3.6.0-linux-x64.tar.xz && \
    tar -xvf blender-3.6.0-linux-x64.tar.xz && \
    mv blender-3.6.0-linux-x64 /opt/blender

# Set Blender executable in PATH
ENV PATH="/opt/blender:$PATH"

# Install pip and Streamlit
RUN apt-get install -y python3-pip && pip3 install --no-cache-dir streamlit

# Copy your app files
COPY app.py /usr/src/app/app.py
COPY usd-to-glb.py /usr/src/app/usd-to-glb.py
COPY usd-to-gltf.py /usr/src/app/usd-to-gltf.py

# Set the working directory
WORKDIR /usr/src/app

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.port=8501"]
