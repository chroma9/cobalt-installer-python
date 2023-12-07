import os as OS
import urllib.request as request
import zipfile as zip

download = str("https://github.com/Raytwo/Cobalt/releases/download/v1.0.0/release.zip")
platforms = ["Yuzu","Ryujinx","SDCard","Test Platform"]

install_locations = {
    "Yuzu": OS.path.join(OS.getenv("APPDATA"), "yuzu", "sdmc"),
    "Ryujinx": OS.path.join(OS.getenv("APPDATA"), "Ryujinx", "sdcard"),
    "SDCard": str("sdcard:\\"),
    "Test Platform": str("test_dir"),
}

def wait_for_keypress():
    input("Press any key to continue...")

def print_error(error):
    print(error)
    wait_for_keypress()

def print_newline():
    print("")

def download_callback(block_num, block_size, total_size):
    percent = (block_num * block_size / total_size) * 100.0
    print(f"Downloading: {percent:.1f}%", end='\r', flush=True)

if __name__ == "__main__":
    print("Welcome to the Simple Cobalt Installer!")
    print_newline()
    for i in range(len(platforms)):
        print(str(i + 1) + ") " + platforms[i])
    print_newline()
    platform = input("Please select a platform: ")
    print_newline()
    
    platform = platforms[int(platform) - 1]

    location = install_locations[platform]

    print("Downloading Cobalt... please be patient.")
    print_newline()

    request.urlretrieve(download, "cobalt.zip", download_callback)

    print("Dowload complete! Installing to \"{}\"".format(location))
    print_newline()

    with zip.ZipFile("./cobalt.zip", "r") as zipfile:
        zipfile.extractall(location)
    
    OS.remove("./cobalt.zip")

    print("Thank you for using the Simple Cobalt Installer!")
    print_newline()
    wait_for_keypress()
