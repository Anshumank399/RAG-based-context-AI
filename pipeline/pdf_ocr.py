import subprocess

cmd = "surya_ocr data/sample2.pdf --langs en --results_dir data/results/"

try:
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    print("Command executed successfully:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("An error occurred while executing the command:")
    print(e.stderr)
