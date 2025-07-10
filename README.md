# pyFASPR
A python wrapper of FASPR, a fast and accurate protein sidechain builder

## Install
#### via PyPI
``` bash
pip install pyfaspr
```

#### via GitHub
``` bash
pip install git+https://github.com/ShintaroMinami/pyFASPR.git
```

## Usage as python module
``` python
from pyfaspr import run_FASPR

# PDB file input
pdb_text_out = run_FASPR(pdb="pdb/file/path.pdb")

# PDB string input
pdb_text_in = "
ATOM      1  N   GLY A   1     -12.034   2.689  10.030  1.00  0.00
ATOM      2  CA  GLY A   1     -11.462   3.121   8.735  1.00  0.00
ATOM      3  C   GLY A   1     -10.273   2.258   8.357  1.00  0.00
....
"
pdb_text_out = run_FASPR(pdb=pdb_text_in)

# Override sequence
seq_update = "GTILIFLDKNKEQAEKLAKEVGVTEIYESDN..."
pdb_text_out = run_FASPR(pdb=pdb_in, sequence=seq_update)

```

## Usage of pyfaspr script
``` bash
# To build sidechains
pyfaspr input.pdb

# Build sidechains with overriding new sequence
pyfaspr input.pdb -s GTILIFLDKNKEQAEKLAKEVGVTEIYESDN...

# To build sidechains and save a new PDB file
pyfaspr input.pdb -o output.pdb
```

### Option details
``` bash
usage: pyfaspr [-h] [--sequence SEQUENCE] [--output_pdb OUTPUT_PDB] [--verbose] pdb

Run FASPR to build sidechains for a PDB file.

positional arguments:
  pdb                   Input PDB file path

options:
  -h, --help            show this help message and exit
  --sequence SEQUENCE, -s SEQUENCE
                        Amino acid sequence to be overridden (optional) (default: None)
  --output_pdb OUTPUT_PDB, -o OUTPUT_PDB
                        Output PDB file path (optional) (default: None)
  --verbose, -v         Enable verbose output (default: False)
```


## Original GitHub reopository
This code includes [tommyhuangthu](https://github.com/tommyhuangthu)'s excellent open source software, FASPR. The original repository is available on MIT license here, https://github.com/tommyhuangthu/FASPR.git.

The author of this repo appreciate to the FASPR team for making such great methods and software available!

## Citations
``` bibtex
@article{huang2020faspr,
  title={FASPR: an open-source tool for fast and accurate protein side-chain packing},
  author={Huang, Xiaoqiang and Pearce, Robin and Zhang, Yang},
  journal={Bioinformatics},
  volume={36},
  number={12},
  pages={3758--3765},
  year={2020},
  publisher={Oxford University Press}
}
```