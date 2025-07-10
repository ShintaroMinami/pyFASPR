import sys
import os
import subprocess
from tempfile import TemporaryDirectory
dir_path = os.path.dirname(os.path.abspath(__file__))
FASPR_BINARY = f"{dir_path}/bin/FASPR"

def run_FASPR(
        pdb: str,
        sequence: str=None,
        verbose: bool=False
    ) -> str:
    """
    Run FASPR to build sidechains for the input PDB file or PDB string.
    
    Parameters:
    pdb (str): PDB file path or PDB string.
    sequence (str, optional): Amino acid sequence. If provided, FASPR will use this sequence.
    verbose (bool, optional): If True, print the command being executed.
    """
    if isinstance(pdb, str) and os.path.isfile(pdb):
        pdb_text = open(pdb, 'r').read()
    else:
        pdb_text = pdb

    with TemporaryDirectory() as temp_dir:
        input_pdb = os.path.join(temp_dir, "input.pdb")
        output_pdb = os.path.join(temp_dir, "output.pdb")
        # Write the PDB content to a file
        with open(input_pdb, 'w') as f:
            f.write(pdb_text)
        command = f"{FASPR_BINARY} -i {input_pdb} -o {output_pdb}"
        if sequence:
            command += f" -s {sequence}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if verbose:
            print(f"Running command: {command}")
            if result.stdout:
                print(f"{result.stdout.decode()}")
            if result.stderr:
                print(f"{result.stderr.decode()}", file=sys.stderr)
        pdb_text_out = open(output_pdb, 'r').read()
    return pdb_text_out