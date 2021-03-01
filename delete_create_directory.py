import shutil
import time as t
import os


def delete_temp_dir():
    try:
        shutil.rmtree(directory)
        t.sleep(5)
    except OSError as e:
        print("Deletion of the directory %s failed: %s" % (directory, e.strerror))
    else:
        print("Successfully deleted the directory %s" % directory)

def create_temp_dir():
    """ access_rights = 755:
    read and execute access for everyone, write access for the owner """

    try:
        os.chdir("/")
        os.makedirs(directory, access_rights)
    except OSError as e:
        print("Creation of the directory %s failed: %s" % (directory, e.strerror))
    else:
        print("Successfully created the directory %s" % directory)


directory = "/dev/temp/"
access_rights = 0o755

if __name__ == "__main__":
    delete_temp_dir()
    create_temp_dir()

