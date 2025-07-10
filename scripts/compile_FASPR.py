#! /usr/bin/env python
import subprocess
from pathlib import Path

dir_path = Path(__file__).resolve().parent.parent

command = f"g++ -w -O3 -o {dir_path}/pyfaspr/bin/FASPR {dir_path}/pyfaspr/FASPR/src/*.cpp"

subprocess.run(command, shell=True)
