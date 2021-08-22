import os
import json
import model

def exec(argv):
    try:
        command = argv[0]
        if command == "list":
            return list_files(argv[1])
        elif command == "list-tagged":
            return list_tagged_files(argv[1])
        elif  command == "add-tag":
            return add_tag(argv[1], argv[2])
        elif  command == "remove-tag":
            return remove_tag(argv[1], argv[2])
        else:
            print("invalid command:", command)
            return 1
    except Exception as e:
        print(e)
        return 1

def list_files(path):
    ret = model.list_files(path)
    print(json.dumps(ret, ensure_ascii=False))
    return 0

def list_tagged_files(tag):
    print("list_tagged_files", tag)
    return 0

def add_tag(path, tag):
    print("add_tag", path)
    return 0

def remove_tag(path, tag):
    print("remove_tag", path)
    return 0
