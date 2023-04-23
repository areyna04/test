import subprocess

url = "https://107.23.134.168:5000/api/tasks"

cmd = f"ab -n 100 -c 10 {url}"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

print(result.stdout)