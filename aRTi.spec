# -*- mode: python -*-


block_cipher = None


a = Analysis(['ARTI_GUI.py'],
             pathex=["C:\\aRTi\\ARTI"],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

for d in a.datas:
	if "pyconfig" in d[0]:
		a.datas.remode(d)
		break

a.datas += [("requirements.txt","C:\\aRTi\\ARTI\\requirements.txt","Data"),("utils\\images\\aRTi_200.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_200.png","Data"),("utils\\images\\aRTi_giant.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_giant.png","Data"),("utils\\images\\aRTi_ico.ico","C:\\aRTi\\ARTI\\utils\\images\\aRTi_ico.ico","Data"),("utils\\images\\aRTi_large.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_large.png","Data"),("utils\\images\\aRTi_medium.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_medium.png","Data"),("utils\\images\\aRTi_mini.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_mini.png","Data"),("utils\\images\\aRTi_white_giant.png","C:\\aRTi\\ARTI\\utils\\images\\aRTi_white_giant.png","Data"),("utils\\images\\aRTi_white_giant_ico.ico","C:\\aRTi\\ARTI\\utils\\images\\aRTi_white_giant_ico.ico","Data")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='aRTi.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='utils\\images\\aRTi_white_giant_ico.ico')
