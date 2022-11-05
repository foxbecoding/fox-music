"""
This set of classes helps manages
the retrieval of env values.

class total: 2
1.) GetEnv: 0 public method(s)
2.) UniqueId: 1 public method(s)
"""
from pathlib import Path

import os
import sys
import random
import string
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

class GetEnv:
    """Class to retrieve env values."""
    def __init__(self, env_name: str):
        self.env_name = env(env_name.upper())

    def __str__(self):
        return f"{self.env_name}"

class UniqueId:
    """Generate unique id."""
    def __init__(self):
        self.unique_id = ''

    def generate_id(self) -> None:
        """This method generates the unique id."""
        source = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(source) for i in range(8)))
        self.unique_id = result_str
    
    def __str__(self):
        self.generate_id()
        return f"{self.unique_id}"

class ExceptionError:
    def __init__(self, exception: str):
        self.exception = exception
        self.exception_data = ''

    def get_exception_data(self) -> None:
        """Get exception Data."""
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = str(exception_traceback.tb_frame.f_code.co_filename)
        line_number = str(exception_traceback.tb_lineno)
        self.exception_data = str(exception_type)+' '+self.exception+' '+filename+' '+line_number
    
    def __str__(self):
        self.get_exception_data()
        return f"{self.exception_data}"
