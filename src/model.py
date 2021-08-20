import os

def list_files(path):
    directries = os.scandir(path=path)
    files = []
    dirs = []
    for f in directries:
        if f.is_file():
            files.append(f.name)
        elif f.is_dir():
            dirs.append(f.name)
        else:
            print("???", f)
    return {"files":files,"dirs":dirs}

# def get_tags_by_filepath(path):
