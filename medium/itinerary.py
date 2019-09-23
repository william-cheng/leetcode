#
#

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

"""

import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        graph = collections.defaultdict(list)
        for s, t in tickets:
            graph[s].append(t)
        for k in graph:
            graph[k].sort(reverse=True)

        trip = []

        def dfs(graph, s):
            """graph: built graph; s: this starting location"""
            trip.append(s)
            if len(trip) == len(tickets) + 1:
                return 1
            if s in graph:
                n = len(graph[s])
                i = 0
                while i < n:
                    next_start = graph[s].pop()
                    if dfs(graph, next_start):
                        return 1
                    graph[s] = [next_start] + graph[s]
                    i += 1
            trip.pop()
            return 0

        dfs(graph, 'JFK')

        return trip


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(
            self.s.findItinerary(
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
            ),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        )

    def test_02(self):
        self.assertEqual(
            self.s.findItinerary(
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ]
            ),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )

    def test_03(self):
        self.assertEqual(
            self.s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]),
            ["JFK", "NRT", "JFK", "KUL"],
        )


unittest.main()
