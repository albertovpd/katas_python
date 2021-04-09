# https://www.codewars.com/kata/52685f7382004e774f0001f7/solutions/python

# def make_readable(seconds):    
#     hours,rem=divmod(seconds,3600)
#     minutes,seconds=divmod(rem,60)
#     hours, minutes, seconds = str(hours), str(minutes), str(seconds)
#     if len(hours)==1:
#         hours="0"+hours
#     if len(minutes)==1:
#         minutes="0"+minutes
#     if len(seconds)==1:
#         seconds="0"+seconds
            
#     return hours+":"+minutes+":"+seconds

def make_readable(seconds):
    hours,rem=divmod(seconds,3600)
    minutes,seconds=divmod(rem,60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)