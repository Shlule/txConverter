import os
import sys
import pathlib

python_executable_path = sys.executable
my_app_path = pathlib.Path(sys.argv[0]).parent / "app.py"


batch_content = f"@echo off\nPowershell.exe -noexit -command \"{python_executable_path}\" \"{my_app_path}\" \"%1\" \"; exit\"\nREM \"PATH TO python.exe\" \"PATH TO maketx_tool.py\" \"%1\"\nPAUSE"
batch_name = "txConverter.bat"
# appdata = os.environ["APPDATA"]
batch_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "SendTo")
batch_path_full = f"{batch_path}/{batch_name}"

if __name__ == "__main__":

    print(batch_path_full)

    with open(batch_path_full, "w") as batch_file:
        batch_file.write(batch_content)