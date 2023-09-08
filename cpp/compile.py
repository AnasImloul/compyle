import subprocess
import tempfile
import os


def check_syntax(code, debug=False):
    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".cpp", delete=False) as f:
        f.write(code)
        f.flush()
        name = os.path.basename(f.name)[:-3]
        output_file = os.path.join(os.path.dirname(f.name), f"{name}.exe")
        result = subprocess.run(["g++", "-std=c++11", f.name, "-o", output_file], capture_output=True)
        if debug:
            print(result.stderr.decode(), result.stdout.decode(), result.returncode)
        f.close()
        return result.returncode == 0
