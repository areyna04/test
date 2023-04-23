import subprocess

url = "http://localhost:5000/api/tasks"

# Definir el número máximo de solicitudes que se intentarán
max_requests = 10000

# Definir el número inicial de solicitudes concurrentes
concurrent_requests = 10

# Definir el incremento de solicitudes concurrentes en cada iteración
concurrent_increment = 10

# Definir la tasa de solicitudes por minuto a superar
target_rpm = 1000

# Iniciar la iteración de prueba y error
while True:
    # Ejecutar el comando ab y capturar su salida
    cmd = f"ab -n {max_requests} -c {concurrent_requests} {url}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Analizar la salida del comando ab para obtener la tasa de solicitudes por minuto
    rpm = None
    for line in result.stdout.splitlines():
        print(line.startswith("Requests per minute:"))
        if line.startswith("Requests per minute:"):
            rpm = float(line.split(":")[1].strip())
            break

    # Si no se pudo obtener la tasa de solicitudes por minuto, salir del bucle
    if rpm is None:
        break

    # Imprimir la tasa de solicitudes por minuto actual y las solicitudes concurrentes utilizadas
    print(f"RPM: {rpm}, Concurrent requests: {concurrent_requests}")

    # Si se alcanza la tasa de solicitudes por minuto objetivo, salir del bucle
    if rpm >= target_rpm:
        break

    # Aumentar el número de solicitudes concurrentes para la próxima iteración
    concurrent_requests += concurrent_increment

# Imprimir la tasa de solicitudes por minuto máxima alcanzada
print(f"Maximum RPM: {rpm}, Concurrent requests: {concurrent_requests}")