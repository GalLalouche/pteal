from os import PathLike
import tempfile
import subprocess


def compile_and_run(path: str) -> str:
  with tempfile.NamedTemporaryFile() as temp_file:
    subprocess.check_output(["clang", path, "-o", temp_file.name])

    result = subprocess.run([temp_file.name], check=True, capture_output=True)

    return result.stdout.decode("utf-8")
