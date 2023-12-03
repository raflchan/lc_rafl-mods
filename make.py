from zipfile import ZipFile
import os

with ZipFile('modpack.zip', 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk('modpack'):
        for filename in filenames:
            if filename == 'make.py':
                continue
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            print(filePath)
            zipObj.write(filePath, os.path.relpath(filePath, 'modpack'))
