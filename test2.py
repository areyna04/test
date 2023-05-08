import subprocess, re
import argparse

url = "http://34.70.174.129:5000/api/tasks"
max_requests = 1000
concurrent_requests = 50
concurrent_increment = 100
target_tpr = 600000
err = 0

parser = argparse.ArgumentParser(description='Descripción de tu script')
parser.add_argument('--token', type=str, help='El nombre a imprimir')

args = parser.parse_args()

token = args.token

print("Escenario 2")
while True:
    cmd = f"ab -p test.json -T application/json -n {concurrent_requests} -c {concurrent_requests} -H Content-Type:application/json -g output2.csv {url}" 
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    tpr = None
    rpm = None
    for line in result.stdout.splitlines():
        if line.startswith("Time per request"):
            tpr = float(re.findall(r'\d+\.\d+',line)[0])
        if line.startswith("Requests per second:"):
            rpm = float(re.findall(r'\d+\.\d+',line)[0])
        if line.startswith("Failed requests:"):
            err = float(re.findall(r'\d+',line)[0])
            if err != 0:
                break
    if tpr is None:
        break
    print(f"Time per request: {tpr}, Requests per second: {rpm}, Concurrent requests: {concurrent_requests}, Error: {err}")
    if tpr >= target_tpr :
        break
    concurrent_requests += concurrent_increment
print(f"Maximum RPM: {tpr}, Concurrent requests: {concurrent_requests}")