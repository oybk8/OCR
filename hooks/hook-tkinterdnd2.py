from PyInstaller.utils.hooks import collect_data_files, collect_submodules
datas = collect_data_files('tkinterdnd2', includes=['tkdnd/**'])
hiddenimports = collect_submodules('tkinterdnd2')