import tempfile
import subprocess


def check_syntax(code):
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".java", delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(["javac", f.name], capture_output=True)
        print(result.stderr.decode())
        f.close()
        return result.returncode == 0
