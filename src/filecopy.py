import os
import shutil
from pathlib import Path

def copy_files(origin, destination):
    root = Path(__file__).parent.parent
    origin_path = os.path.join(root, origin)
    destination_path = os.path.join(root, destination)

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
        
    os.mkdir(destination_path)

    paths = os.listdir(origin_path)
    for path in paths:
        full_path = os.path.join(origin_path, path)
        if os.path.isfile(full_path):
            shutil.copy(os.path.join(origin_path, path), destination_path)
        else:
            copy_files(os.path.join(origin_path, path), os.path.join(destination_path, path))
