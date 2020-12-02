#!/usr/bin/env python3
import subprocess


def run(command):
    subprocess.run(command.split())


run("poetry run flake8 .")  # find errors that will cause black to fail
run("poetry run isort .")
run("poetry run black .")
run("poetry run flake8 .")  # run it again in case black messed something up
run("poetry run mypy .")
run("poetry run pytest")
