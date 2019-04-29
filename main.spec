# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\for_project_kvant\\main.py'],
             pathex=['C:\\Users\\for_project_kvant'],
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

		
		
a.datas += [('thema1.gif','C:\\Users\\for_project_kvant\\thema1.gif', "Data"), ('thema2.gif','C:\\Users\\for_project_kvant\\thema2.gif', "Data"), ('thema3.gif','C:\\Users\\for_project_kvant\\thema3.gif', "Data"), ('thema4.gif','C:\\Users\\for_project_kvant\\thema4.gif', "Data"), ('thema5.gif','C:\\Users\\for_project_kvant\\thema5.gif', "Data"), ('thema6.gif','C:\\Users\\for_project_kvant\\thema6.gif', "Data"), ('err.wav','C:\\Users\\for_project_kvant\\err.wav', "Data"), ('click.mp3','C:\\Users\\for_project_kvant\\click.mp3', "Data"), ('win.mp3','C:\\Users\\for_project_kvant\\win.mp3', "Data"), ('infa.txt','C:\\Users\\for_project_kvant\\infa.txt', "Data"), ('iconka.gif','C:\\Users\\for_project_kvant\\iconka.gif', "Data")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='FastNumbers(beta)',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)