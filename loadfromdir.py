'''
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
'''
import glob


def get_list_of_filenames(dirname):
    return glob.glob(dirname + '*.py')
