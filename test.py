import subprocess

url = "https://localhost:5000"

cmd = f"ab -n 100 -c 10 {url}"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

print(result.stdout)