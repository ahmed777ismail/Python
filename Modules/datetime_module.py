from datetime import datetime as dt
from datetime import date as d
from datetime import time as t
from datetime import timedelta as tdelta


today_date = d.today()
birth_date = d(1996, 8, 21)
days = (today_date - birth_date).days


