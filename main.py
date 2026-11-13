import os
from pathlib import Path

output = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
output.joinpath('entry.txt').write_text(
    'I asked my AI coding agent to fix one bug. It wrote a regression test for the other six.',
    encoding='utf-8',
)
