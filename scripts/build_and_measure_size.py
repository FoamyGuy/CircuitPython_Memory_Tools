import os
import shutil
import subprocess

REPO_URL = "https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_Layout.git"
#REPO_URL = "https://github.com/adafruit/Adafruit_CircuitPython_BLE_iBBQ.git"
BRANCH_NAME = "main"


def get_project_dir_name(repo_url):
    return repo_url.split("/")[-1].replace(".git", "")

def utf8len(s):
    return len(s.encode('utf-8'))

def find_v8_mpy_zip():
    for file in os.listdir("./"):
        if "8.x-mpy" in file:
            print("Found 8.x mpy zip:")
            print(file)
            return file


PROJECT_DIR = f"./tmp/{get_project_dir_name(REPO_URL)}"

if os.path.exists(PROJECT_DIR):
    print("Deleting Project Dir...")
    shutil.rmtree(PROJECT_DIR)

print("Cloning...")
os.system(f"git clone -b {BRANCH_NAME} {REPO_URL} {PROJECT_DIR}")
print("Building Bundles...")
os.chdir(PROJECT_DIR)
os.system(f"circuitpython-build-bundles --filename_prefix  {get_project_dir_name(REPO_URL)} --library_location .")

found_v8_mpy_zip = find_v8_mpy_zip()

# if found_v8_mpy_zip:
#     shutil.unpack_archive(found_v8_mpy_zip)

os.chdir(found_v8_mpy_zip)
os.chdir(os.listdir("./")[0])
os.chdir("lib")
if os.path.isfile(os.listdir("./")[0]):
    mpy_file = os.listdir("./")[0]
    file_stats = os.stat(mpy_file)
    print(f'mpy file size: {file_stats.st_size} bytes')

    # command = ['strings', mpy_file]
    # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.)
    # strings_command_output = p.stdout.read()
    # retcode = p.wait()

    os.system(f"strings {mpy_file} > strings_output.txt")
    string_file_stats = os.stat("strings_output.txt")
    print(f'strings output size: {string_file_stats.st_size} bytes')
    print(f"strings percentage of mpy: {(string_file_stats.st_size / file_stats.st_size)*100.0:.2f}%")