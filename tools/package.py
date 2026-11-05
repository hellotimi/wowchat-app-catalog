"""Rebuild static packages using only Python's standard library."""
import hashlib
import json
import shutil
import tarfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
apps = json.loads((root / 'apps.json').read_text(encoding='utf-8'))
for app in apps:
    app_id = app['id']
    if not app_id or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in app_id):
        raise ValueError('Invalid application ID')
    folder = root / 'sources' / app_id
    config = json.loads((folder / 'package.json').read_text(encoding='utf-8'))
    assert config['id'] == app_id
    archive = root / 'packages' / f'{app_id}.tar.gz'
    with tarfile.open(archive, 'w:gz') as tar:
        for path in sorted(folder.rglob('*')):
            if path.is_file():
                tar.add(path, arcname=path.relative_to(folder).as_posix())
    shutil.copyfile(folder / 'icon.svg', root / 'icons' / f'{app_id}.svg')
    app.update(version=config['version'], icon=f'icons/{app_id}.svg', package=f'packages/{app_id}.tar.gz',
               sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), size=archive.stat().st_size)
    print(app_id, app['version'], app['sha256'])
(root / 'apps.json').write_text(json.dumps(apps, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
