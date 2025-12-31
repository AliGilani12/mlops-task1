import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

# Preprocess
run_command('docker build -f Dockerfile.preprocess -t iris-preprocess .')
run_command('docker run --rm iris-preprocess')

# Train
run_command('docker build -f Dockerfile.train -t iris-train .')
run_command('docker run --rm iris-train')

# Deploy
run_command('docker build -f Dockerfile.serve -t iris-serve .')
run_command('docker run -d -p 8000:8000 iris-serve')

print("Pipeline completed successfully.")
