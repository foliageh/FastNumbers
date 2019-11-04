# -*- mode: python -*-

block_cipher = None

a = Analysis(['C:\\Users\\exe-builder\\FastNumbers\\main.py'],
             pathex=['C:\\Users\\exe-builder\\FastNumbers'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
		
a.datas += [('theme1.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme1.gif', "Data"),
            ('theme2.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme2.gif', "Data"),
            ('theme3.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme3.gif', "Data"),
            ('theme4.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme4.gif', "Data"),
            ('theme5.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme5.gif', "Data"),
            ('theme6.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\theme6.gif', "Data"),
            ('bg_img.gif','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\img\\bg_img.gif', "Data"),
            ('err.wav','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\sounds\\err.wav', "Data"),
            ('click.mp3','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\sounds\\click.mp3', "Data"),
            ('win.mp3','C:\\Users\\exe-builder\\FastNumbers\\resourсes\\sounds\\win.mp3', "Data")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='FastNumbers',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=['vcruntime140.dll'],
          runtime_tmpdir=None,
          console=False)