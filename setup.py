import subprocess
import setuptools
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext


with open("README.md", "r") as fh:
    long_description = fh.read()

class compile_FASPR(build_ext):
    def build_extension(self, ext):
        subprocess.run(
            f'g++ -w -O3 -o {self.build_lib}/pyfaspr/bin/FASPR {self.build_lib}/pyfaspr/FASPR/src/*.cpp',
            shell=True
            )

setuptools.setup(
    name="pyfaspr",
    use_scm_version={'local_scheme': 'no-local-version'},
    author="Shintaro Minami",
    description="A python wrapper of FASPR, a fast and accurate protein sidechain builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShintaroMinami/pyfaspr",
    cmdclass={
        'build_ext': compile_FASPR,
    },
    ext_modules=[Extension('', [])],
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    install_requires=['pdbutil'],
    scripts=[
        'scripts/pyfaspr'
    ],

)