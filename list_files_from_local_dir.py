import os
import fnmatch as mask


def list_files_from_local_dir(directory, file_mask):
    file_list = []
    for root, directories, files in os.walk(directory):
        for f in files:
            if mask.fnmatch(f, file_mask):
                file_path = os.path.join(root, f)

                if DEBUG:
                    print(file_path) #/dev/py/temp/WinFormClientSmall.png

                file_list.append(file_path)

    print("Number of files found: %d" % len(file_list))

    return file_list


DEBUG = False
FILE_MASK = "*.png"
LOCAL_PATH = "/dev/py/temp/"

if __name__ == "__main__":
    list_files_from_local_dir(LOCAL_PATH, FILE_MASK)

