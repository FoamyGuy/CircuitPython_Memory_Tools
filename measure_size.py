import os


def find_v8_mpy_zip():
    for file in os.listdir("./"):
        if "8.x-mpy" in file:
            print("Found 8.x mpy zip:")
            print(file)
            return file


def measure_sizes():
    found_v8_mpy_zip = find_v8_mpy_zip()
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
        print(f"strings percentage of mpy: {(string_file_stats.st_size / file_stats.st_size) * 100.0:.2f}%")

if __name__ == '__main__':
    measure_sizes()