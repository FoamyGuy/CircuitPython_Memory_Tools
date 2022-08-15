import os
import zipfile

import requests


def download_latest_bundle():
    json_resp = requests.get(
        "https://api.github.com/repos/adafruit/Adafruit_CircuitPython_Bundle/releases/latest").json()

    for asset in json_resp["assets"]:
        if "adafruit-circuitpython-bundle-8" in asset["name"]:
            print(asset["browser_download_url"])
            bundle_zip = requests.get(asset["browser_download_url"], allow_redirects=True)
            download_filename = asset["browser_download_url"].split("/")[-1]
            bundle_out = open(download_filename, 'wb')
            bundle_out.write(bundle_zip.content)
            bundle_out.close()
            with zipfile.ZipFile(download_filename, "r") as zip_ref:
                zip_ref.extractall(".")
            # shutil.move(f'{download_filename.replace(".zip", "")}/lib/', ".")
            # shutil.move(f'{download_filename.replace(".zip", "")}/examples/', ".")
    return download_filename

def find_v8_mpy_zip():
    for file in os.listdir("./"):
        if "8.x-mpy" in file:
            #print("Found 8.x mpy zip:")
            #print(file)
            return file


def measure_sizes(module_name):
    # New Version:

    found_v8_mpy_zip = find_v8_mpy_zip()
    os.chdir(found_v8_mpy_zip)
    os.chdir(os.listdir("./")[0])
    os.chdir("lib")
    if os.path.isfile(os.listdir("./")[0]):
        mpy_file = os.listdir("./")[0]
        file_stats = os.stat(mpy_file)
        print("Modified Version:")
        print(f'mpy file size: {file_stats.st_size} bytes')

        # command = ['strings', mpy_file]
        # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.)
        # strings_command_output = p.stdout.read()
        # retcode = p.wait()

        os.system(f"strings {mpy_file} > strings_output.txt")
        string_file_stats = os.stat("strings_output.txt")
        print(f'strings output size: {string_file_stats.st_size} bytes')
        print(f"strings percentage of mpy: {(string_file_stats.st_size / file_stats.st_size) * 100.0:.2f}%")

    # Published Version:
    print("===========")
    print("Published Version:")
    downloaded_filename = download_latest_bundle()
    os.chdir(downloaded_filename.replace(".zip", ""))
    os.chdir("lib")
    single_mpy_file = f"./{module_name}.mpy"
    if os.path.exists(single_mpy_file):
        # if it's a single mpy file

        file_stats = os.stat(single_mpy_file)
        print(f'mpy file size: {file_stats.st_size} bytes')
        os.system(f"strings {single_mpy_file} > published_strings_output.txt")
        string_file_stats = os.stat("published_strings_output.txt")
        print(f'strings output size: {string_file_stats.st_size} bytes')
        print(f"strings percentage of mpy: {(string_file_stats.st_size / file_stats.st_size) * 100.0:.2f}%")


if __name__ == '__main__':
    measure_sizes("adafruit_si1145")