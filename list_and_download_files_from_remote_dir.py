import paramiko
import fnmatch as mask
from stat import S_ISDIR, S_ISREG
import datetime as dt


def list_and_download_files_from_remote_dir(hostname, port, username, password, remote_path, file_mask, local_path):

    pairs = {"name": [], "size": [], "timestamp": []}

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password
    )

    connection = client.open_sftp()
    print("." * 100)

    for entry in connection.listdir_attr(remote_path):

        if S_ISDIR(entry.st_mode):
            print("%s is a directory and will be ignored" % entry.filename)

        elif S_ISREG(entry.st_mode):
            if mask.fnmatch(entry.filename, file_mask):
                pairs["name"].append(entry.filename)
                pairs["size"].append(entry.st_size)
                pairs["timestamp"].append(dt.datetime.fromtimestamp(entry.st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
                connection.get(remote_path + entry.filename, local_path + entry.filename)

    print(pairs)
    """for pair in pairs:
        print(p)"""

    connection.close()


HOSTNAME, PORT = "test.rebex.net", 22
USERNAME, PASSWORD = "demo", "password"
PRIVATE_KEY_FILE, PRIVATE_KEY_PASS = None, None
REMOTE_PATH = "/pub/example/"
FILE_MASK = "*.png"
LOCAL_PATH = "/dev/py/temp/"

if __name__ == "__main__":
    list_and_download_files_from_remote_dir(
        HOSTNAME,
        PORT,
        USERNAME,
        PASSWORD,
        REMOTE_PATH,
        FILE_MASK,
        LOCAL_PATH
    )

