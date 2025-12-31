import subprocess
import sys
import os

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

data_path = os.path.join(os.getcwd(), 'data').replace('\\', '/').replace('C:', '/c')

run_command('docker build -f Dockerfile.preprocess -t iris-preprocess .')
run_command(f'docker run --rm -v "{data_path}:/data" iris-preprocess')

run_command('docker build -f Dockerfile.train -t iris-train .')
run_command(f'docker run --rm -v "{data_path}:/data" iris-train')

run_command('docker build -f Dockerfile.serve -t iris-serve .')
run_command(f'docker run -d -p 8000:8000 -v "{data_path}:/data" iris-serve')

print("Pipeline completed successfully.")
