import os
from . import chalicelib

TESTUSER = chalicelib.get_parameters(os.environ['testuser'])
TESTPASSWORD = chalicelib.get_parameters(os.environ['testpassword'])