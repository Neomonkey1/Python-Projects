# Author:   Raymond Harrison
#
# Purpose:  Python challenge
#
# Tested:   ver. 3.11.7 on Windows 11
#
#

import datetime as dt
import pytz


# Portland TZ
Portland = 'US/pacific'
pl_time = dt.datetime.now(pytz.timezone(Portland)).time()

# NY TZ
NY = 'US/eastern'
ny_time = dt.datetime.now(pytz.timezone(NY)).time()

# London TZ
London = 'Europe/London'
london_time = dt.datetime.now(pytz.timezone(London)).time()

# function to see if current time is within open or close times
def is_branch_open(time, branch_open, branch_close):    
    if branch_open <= time.hour <= branch_close:
        return True
    else:
        return False
branch_open = 9
branch_close = 17


if __name__ == '__main__':
    
    print(pl_time)
    print(ny_time)
    print(london_time)

    print(is_branch_open(pl_time,branch_open,branch_close))
    print(is_branch_open(ny_time,branch_open,branch_close))
    print(is_branch_open(london_time,branch_open,branch_close))




