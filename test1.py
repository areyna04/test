import subprocess, re

url = "http://localhost:5000/api/tasks"
max_requests = 50000
concurrent_requests = 10
concurrent_increment = 50
target_tpr = 1.5
err = 0

print("Escenario 1")
while True:
    cmd = f"ab -n {concurrent_requests} -c {concurrent_requests} -g output1.csv {url}"
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
