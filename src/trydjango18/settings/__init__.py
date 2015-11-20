from .base import *

try:
	from .local import *  #override the settings of .base.py file
except:
	pass


try:
	from .production import *
except:
	pass