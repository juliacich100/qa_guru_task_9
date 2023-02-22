import os
import tests.resources


def path_to_image(rel_path): return os.path.abspath(os.path.join(os.path.dirname(tests.resources.__file__), rel_path))