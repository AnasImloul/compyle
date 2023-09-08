import os
import subprocess
import tempfile


def check_syntax(code):
    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".rs", delete=False) as f:
        f.write(code)
        f.flush()
        name = os.path.basename(f.name)[:-3]
        args = ["rustc", f.name, "--crate-type=lib", "-o", os.path.join(os.path.dirname(f.name), f"{name}.rlib")]
        result = subprocess.run(args, capture_output=True)
        # print(result.stderr.decode(), result.stdout.decode(), result.returncode)
        f.close()
        return result.returncode == 0
