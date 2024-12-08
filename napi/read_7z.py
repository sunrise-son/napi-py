import subprocess
import tempfile
from io import BytesIO
from typing import Optional

NAPI_ARCHIVE_PASSWORD = "iBlm8NTigvru0Jr0"


def un7zip_api_response(content_7z: bytes) -> Optional[bytes]:
    buffer = BytesIO(content_7z)
    with tempfile.NamedTemporaryFile() as stream:
        stream.write(buffer.read())
        stream.flush()
        cmd = ["7zr", "e", "-p" + NAPI_ARCHIVE_PASSWORD, "-so", stream.name]

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        except FileNotFoundError as fnf:
            raise fnf
        except OSError:
            return None

        return proc.stdout.read()
