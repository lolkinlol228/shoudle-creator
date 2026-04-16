
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Дополнительные данные для включения
added_files = []

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'flask',
        'sqlite3',
        'json',
        'datetime',
        'docx',
        'docx.shared',
        'docx.enum.text',
        'docx.oxml',
        'docx.oxml.ns',
        'contextlib',
        'threading',
        'werkzeug',
        'jinja2',
        'click',
        'itsdangerous',
        'markupsafe',
        'lxml',
        'pillow'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ScheduleManager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # True для отображения консоли, False для скрытия
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Можно указать путь к .ico файлу
)
