import tempfile
import subprocess


def check_syntax(code, debug=False):
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".java", delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(["javac", f.name], capture_output=True)
        if debug:
            print(result.stderr.decode(), result.stdout.decode(), result.returncode)
        f.close()
        return result.returncode == 0
