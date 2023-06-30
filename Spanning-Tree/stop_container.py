import time
import docker

def stop_container(container_name, seconds):
    client = docker.from_env()
    
    time.sleep(seconds)

    try:
        container = client.containers.get(container_name)
        container.stop()
        print(f"Container '{container_name}' stopped successfully.")
        
    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
        
    except docker.errors.APIError as e:
        print(f"An error occurred while stopping container '{container_name}': {e}") 
    
    # try:
    #     container = client.containers.get(container_name)
    #     container.start()
    #     print(f"Container '{container_name}' started successfully.")
        
    # except docker.errors.NotFound:
    #     print(f"Container '{container_name}' not found.")
        
    # except docker.errors.APIError as e:
    #     print(f"An error occurred while starting container '{container_name}': {e}")

# Esempio di utilizzo
container_name = "node-8"
seconds = 10

stop_container(container_name, seconds)
