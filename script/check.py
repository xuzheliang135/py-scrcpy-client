import subprocess

source_dirs = "scrcpy tests script scrcpy_ui"
subprocess.check_call(f"isort --check --diff {source_dirs}", shell=True)
subprocess.check_call(f"black --check --diff {source_dirs}", shell=True)
subprocess.check_call(
    f"flake8 --ignore W503,E203,E501,E731,F403,F401 {source_dirs} --exclude scrcpy_ui/ui_main.py",
    shell=True,
)
