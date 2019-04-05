#
#

"""#253 Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
