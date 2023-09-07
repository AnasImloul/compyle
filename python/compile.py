import tempfile
import subprocess


def check_syntax(code):
    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(["python", f.name], capture_output=True)
        # print(result.stderr.decode())
        f.close()
        return result.returncode == 0
