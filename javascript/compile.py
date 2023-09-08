import subprocess
import tempfile


def check_syntax(code, debug=False):
    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".js", delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(["node", f.name], capture_output=True)
        if debug:
            print(result.stderr.decode(), result.stdout.decode(), result.returncode)
        f.close()
        return result.returncode == 0
