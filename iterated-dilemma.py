#!/usr/bin/python3
'''
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
'''
import sys
import prisoners_dilemma
from loadfromdir import get_list_of_filenames
import os

modules = sys.argv
del modules[0]

if len(modules) == 0:
    modules = prisoners_dilemma.default_module_names
    print('No command-line arguments found, using default_module_names')

updated_modules = []

for module_index in range(len(modules)):
    if modules[module_index] == '-d':
        assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
        module_directory = modules[module_index + 1]
        assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
        if not (module_directory[-1] == '/'):
            module_directory += '/'
        add_to_modules = get_list_of_filenames(module_directory)
        for module in add_to_modules:
            updated_modules.append(module)
    elif modules[module_index - 1] == '-d':
        continue
    else:
        add_to_modules = modules[module_index]
        updated_modules.append(add_to_modules)

for module_path in updated_modules:
    assert os.path.isfile(module_path), "There is no file named {}".format(module_path)

prisoners_dilemma.main(updated_modules)
