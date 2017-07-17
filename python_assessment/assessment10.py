#explored stackoveflow tounderstand the concepts
#the code doesn't work as of now
#V.imp learn to install external libraries, however the code should work
from datetime import *
from dateutil import *
from dateutil.tz import *
utc_zone = tz.tzutc()
local_zone = tz.tzlocal()
local_time = datetime.strptime("2008-09-17 14:02:00", '%Y-%m-%d %H:%M:%S')
local_time = local_time.replace(tzinfo=local_zone)
utc_time = local_time.astimezone(utc_zone)
utc_string = utc_time.strftime('%Y-%m-%d %H:%M:%S')
