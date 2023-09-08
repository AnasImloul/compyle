import os
import subprocess
import tempfile


def check_syntax(code):
    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".rs", delete=False) as f:
        f.write(code)
        f.flush()
        args = ["gofmt", f.name]
        result = subprocess.run(args, capture_output=True)
        # print(result.stderr.decode(), result.stdout.decode(), result.returncode)
        f.close()
        return result.returncode == 0
