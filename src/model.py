import os

def list(path):
    directries = os.scandir(path=path)
    files = []
    dirs = []
    for f in directries:
        if f.is_file():
            files.append({"name":f.name, "tags":[]})
        elif f.is_dir():
            dirs.append({"name":f.name, "tags":[]})
        else:
            print("???", f)
    return {"files":files,"dirs":dirs}

# def get_tags_by_filepath(path):
