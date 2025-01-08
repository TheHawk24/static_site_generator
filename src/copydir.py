import os
import shutil

def recurse_dir(source):
    src = os.path.exists(source)
    if not src:
        raise Exception("The path specified does not exist")
    
    is_empty = os.listdir(path=source)
    if len(is_empty) == 0:
        return []

    contains = []

    for file in is_empty:
        res = os.path.join(source,file)
        if os.path.isfile(res):
            contains.append(res)
        else:
            contains.extend(recurse_dir(res))

    return contains


def create_directories(directory):
    split_directories = directory.split('/')
    if split_directories[0] == '':
        return ""
    created_so_far = ""
    for dir in split_directories:
        created_so_far += dir + "/"
        if not os.path.exists(created_so_far):
            os.mkdir(created_so_far)
        else:
            continue

    return created_so_far



def copy_to(source, destination):
    exists = os.path.exists(destination)
    if not exists:
        print("Destination does not exists...creating the destination")
        os.mkdir(destination)
        print("Created the destination")

    # Check if it contains anything
    is_empty = os.listdir(path=destination)
    if len(is_empty) != 0:
        print("Destination contains files. Removig files...")
        shutil.rmtree(destination)
        print("Removed files in the destination")

    # Copy files over to the empty directory
    ret = recurse_dir(source)

    for file in ret:
        join = "/".join(file.split("/")[2:-1])
        new_destination = os.path.join(destination,join)
        print(f"Create directory: {new_destination}")
        created_destination = create_directories(new_destination)
        print(f"Created directory: {created_destination}")
        copied_files = shutil.copy(file, created_destination)
        print(f"Copied {file} to {copied_files}")



