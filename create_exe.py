import PyInstaller.__main__

PyInstaller.__main__.run([
    './src/send_alert.py',
    '--onefile',
    '--windowed'
])
