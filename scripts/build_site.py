"""Build MkDocs and refresh docs/ served by the existing GitHub Pages setup."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict'], cwd=root, check=True)
output = root / 'site'
publish = root / 'docs'
manifest = root / '.site-files.json'
previous = json.loads(manifest.read_text()) if manifest.exists() else []
files = sorted(p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file())
protected = {'content', 'theme', 'scripts', '.github', '.git', '.openai', 'mkdocs.yml', 'requirements.txt', 'README.md'}
for name in set(previous) | set(files):
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts or relative.parts[0] in protected:
        raise RuntimeError(f'Unsafe published path: {name}')
publish.mkdir(exist_ok=True)
for name in set(previous) - set(files):
    (publish / name).unlink(missing_ok=True)
for name in files:
    dest = publish / name
    if dest.exists() and name not in previous:
        raise RuntimeError(f'Refusing to overwrite an existing file: {name}')
for name in files:
    dest = publish / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(output / name, dest)
(publish / '.nojekyll').touch()
manifest.write_text(json.dumps(files, indent=2) + '\n')
print(f'Prepared {len(files)} published files in docs/. Commit and push main to deploy.')
