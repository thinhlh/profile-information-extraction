import subprocess

def install_docker_image():
    install_docker_image_cmd = 'docker build --tag jamiele/libreoffice-pdf-cli .'
    
    install_docker_image = subprocess.Popen(install_docker_image_cmd.split(" "))
    install_docker_image.wait()
    print("Loaded docker image")