## Introduction

This repository contains a tool for image metadata extraction build with Python. The module used in this project is `Pillow`.

## Features
- All the images inside the "***images***" folder will be extracted. No need to input filenames!!
- The extracted metadata will be stored in a ***csv*** file.
- All the unique metadata will be stored; not a single one will left behind.

## Drawbacks
- The output ***csv*** file will get overwritten every-time the script is executed. So, better keep a backup of the output file after every execution.

## Installation
- Install python from the [official website](https://www.python.org/downloads/). (*recommended version 3.11.5*)
- Open **terminal** and execute the following line:
```sh
$ pip install Pillow
```
- Download the zip file of this repository and extract it.
- Navigate to the extracted repository folder through **terminal** and execute the following line:
```sh
$ python main.py
```

> **Note :** *Remember to place the images in the "**images**" folder before the last step.*