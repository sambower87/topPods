from .base_settings import *

from .production_settings import *

try:
   from .local_settings import *

except:
   pass