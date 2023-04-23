import subprocess, re

url = "http://localhost:5000/api/tasks"
max_requests = 1000
concurrent_requests = 10
concurrent_increment = 50
target_tpr = 1.5

print("Escenario 1")
while True:
    cmd = f"ab -n {max_requests} -c {concurrent_requests} -g output1.csv {url}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    tpr = None
    rpm = None
    for line in result.stdout.splitlines():
        if line.startswith("Time per request"):
            tpr = float(re.findall(r'\d+\.\d+',line)[0])
        if line.startswith("Requests per second:"):
            rpm = float(re.findall(r'\d+\.\d+',line)[0])
        if line.startswith("Failed requests:"):
            err = int(re.findall(r'\d+',line)[0])
            if err != 0:
                break
    if tpr is None:
        break
    print(f"Time per request: {tpr}, Requests per second: {rpm}, Concurrent requests: {concurrent_requests}, Error: {err}")
    if tpr >= target_tpr :
        break
    concurrent_requests += concurrent_increment
print(f"Maximum Time Per Request: {tpr}, Request per second: {rpm}, Error: {err}")

url = "http://localhost:5000/api/tasks"
max_requests = 1000
concurrent_requests = 1
concurrent_increment = 5
target_tpr = 600

print("Escenario 2")
while True:
    cmd = f"ab -p test.json -T application/json -n {max_requests} -c {concurrent_requests} -H Content-Type:application/json -g output2.csv -v 2{url}" 
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