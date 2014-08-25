import logging

log = logging.getLogger(__name__)

__author__ = 'andriod'

def avg(*nums):
    nums = [int(x) for x in nums]
    return sum(nums)/len(nums)

print(avg(1,23,9,"445",4.8))
