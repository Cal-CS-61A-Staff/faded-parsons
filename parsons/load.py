import glob
import os
from collections import defaultdict, OrderedDict

import yaml

from constants import UTILITY_FILES, PARSONS_GLOB, PARSONS_FOLDER_PATH 


def load_config(problem_name):
  """
  Loads a YAML file, assuming that the YAML file is located at {PARSONS_FOLDER_PATH}/{problem_name}.yaml
  Normalizes problem_name to lowercase as all filenames should be lowercased.
   
  Args:
      problem_name: The name of the problem.

  Returns: The contents of the YAML file as a defaultdict, returning None
      for unspecified attributes.
  """
  path = os.path.join(os.path.abspath(PARSONS_FOLDER_PATH), problem_name.lower() + ".yaml")
  try:
    with open(os.path.abspath(path), 'r') as file:
      config = yaml.load(file, Loader=yaml.Loader)
    if type(config) == dict:
      config = defaultdict(lambda: None, config)
    return config
  except IOError as e:
    pass
  raise Exception("Cannot find path {0}".format(path))

def problem_name_from_file(filename):
  with open(filename, "r", encoding="utf8") as f:
    cur_lines = f.readlines()
    for line in cur_lines:
        cur_words = line.lstrip().split()
        if cur_words and cur_words[0] == 'def':
            func_sig = cur_words[1]
            name = func_sig[:func_sig.index('(')]
            return name

def problem_name_to_file(problem_name, extension):
  return f'{PARSONS_FOLDER_PATH}/{problem_name.lower()}.{extension}'
   
def path_to_name(names_to_paths, path):
    for key, val in names_to_paths.items():
        if val == path:
            return key
