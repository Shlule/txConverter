import os
import sys
import multiprocessing
import subprocess
from pathlib import Path
import conf

nb_cpu = multiprocessing.cpu_count()

authozied_format = [".tiff", ".exr", ".png"]

maketx_path = conf.maketx_path

def extract_authorized_file(folder_path: str):
    file_names = os.listdir(folder_path)
    files_to_convert: list[str] =[]
    for file_name in file_names:
        if not(Path(file_name).suffix.lower() in authozied_format):
            print(f"{file_name} have no corresponding extension. the extension must be {', '.join(authozied_format)}")
        else:
            files_to_convert.append(file_name)
    return files_to_convert


def create_file_path_list(folder_path:str):
    files_name = extract_authorized_file(folder_path)
    files_path:list[str] =[]
    for file_name in files_name:
        files_path.append(f"{folder_path}/{file_name}")
    return files_path

    
    

def convert_to_tx(file_path:str):

    test = file_path.split(".")
    file_output_path = f"{test[0]}.tx"

    process = subprocess.Popen([maketx_path, "-v", "-u", "--oiio","--filter", "lanczos3",file_path, "-o", file_output_path], shell=True, stdout=subprocess.PIPE)
    output, _ = process.communicate()

    
def main():
    folder_path = sys.argv[1]
    input_files = create_file_path_list(folder_path)
    max_processes = multiprocessing.cpu_count() -2

    with multiprocessing.Pool(max_processes)as pool:
        pool.map(convert_to_tx, input_files)
    print("Travaille terminé!")
    


if __name__ == "__main__":
    
    main()