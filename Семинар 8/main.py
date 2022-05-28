from UI import * 
from model import *
from log import *

if choos_operation() == '1': 
    init(get_string())
    log_it()
else:
    import_file()
    log_it()