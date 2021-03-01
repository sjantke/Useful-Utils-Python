import os
import time as t
import datetime as dt
import fnmatch as mask
import zipfile

import list_files_from_local_dir as fl


def compress_files(file_list, file_mask, target_dir, archive_name):
    os.chdir(target_dir)  # change directory to target output dir
    with zipfile.ZipFile(file=archive_name, mode="w", compression=zipfile.ZIP_DEFLATED) as zip:
        for file_path in file_list:
            f = os.path.basename(file_path)
            #print(f) #WinFormClientSmall.png
            if mask.fnmatch(f, file_mask):
                zip.write(file_path, f) # use f to prevent absolute path in archive
        print("All files matching file mask %s have been compressed successfully" % file_mask)
    zip.close()

def print_compressed_files(archive_name):
    with zipfile.ZipFile(file=archive_name, mode="r") as zip:
        for detail in zip.infolist():
            print("File Name: " + detail.filename)
            print("\tCompressed: " + str(detail.compress_size) + " bytes")
            print("\tDecompressed: " + str(detail.file_size) + " bytes")
    zip.close()

def decompress_files(archive_name, target_dir):
    with zipfile.ZipFile(file=archive_name, mode="r") as zip:
        #print("Archive Content:")
        #zip.printdir()
        os.chdir(INPUT_DIR)
        print("Decompressing now...")
        zip.extractall()
        #zip.extract("WinFormClientSmall.png")
        print("Decompressing done")
    zip.close()

# ----------------------------------------------------------------------------------------------------
DEBUG = False

LOCAL_PATH = "/dev/py/temp/"
FILE_MASK = "*.png"
files = fl.list_files_from_local_dir(LOCAL_PATH, FILE_MASK)

OUTPUT_DIR = "/dev/py/data/output/"
ARCHIVE_NAME = "archive_" + dt.datetime.fromtimestamp(t.time()).strftime('%Y%m%d%H%M%S') + ".zip"
INPUT_DIR = "/dev/py/data/input/"

if __name__ == "__main__":
    f = files
    compress_files(f, FILE_MASK, OUTPUT_DIR, ARCHIVE_NAME)
    print_compressed_files(ARCHIVE_NAME)
    decompress_files(ARCHIVE_NAME, INPUT_DIR)

