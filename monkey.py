import click
import os
from os import path
import subprocess

def cli():
    cur_dir = os.getcwd()

    files = [f for f in os.listdir(cur_dir) if path.isfile(f)]

    apk_files = []
    py_files = []

    for f in files:
        ext = os.path.splitext(f)[1]
        if ext == '.apk':
            apk_files.append(f)
        elif ext == '.py':
            py_files.append(f)

    if check_apk_file(apk_files)[0] == 1 and check_py_file(py_files)[0] == 1:
        print(check_apk_file(apk_files)[1])
        print(check_py_file(py_files)[1])
        run_monkey_runner(cur_dir + "\\" + str(py_files[0]))
    else:
        print("Make sure you have one apk and python file.")


def run_monkey_runner(script):
    print("Executing " + "monkeyrunner " + script + " ...")
    subprocess.call("monkeyrunner " + script, shell=True)


def check_apk_file(apk_files):
    return [len(apk_files), {

        0: "No apk file detected.",
        1: "Apk file is good.",
        2: "Only one apk file is allowed."

    }[len(apk_files)]]


def check_py_file(py_files):
    return [len(py_files), {

        0: "No python file detected.",
        1: "Python file is good.",
        2: "Only one python file is allowed."

    }[len(py_files)]]

