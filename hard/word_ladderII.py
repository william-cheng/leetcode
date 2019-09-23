import collections

class Solution(object):
    def _build_graph(self, nodes):
        # find all connected nodes given only one char changed in word
        connected = collections.defaultdict(list)
        L = len(nodes[0])
        for n in nodes:
            for i in range(L):
                connected[n[:i] + "*" + n[i + 1 :]].append(n)
        # build a graph represented in dict
        # { word: set([adjacent_word, ...]) }
        graph = collections.defaultdict(set)
        for ns in connected.values():
            for i in range(len(ns)):
                for n in ns[:i] + ns[i + 1 :]:
                    graph[ns[i]].add(n)
        return graph

    def findPath(self, graph, begin, end):
        paths = []
        q = [[[], begin]]
        shortest = float("inf")

        words = set(graph.keys())
        while q:
            next_ = []
            for p, n in q:

                if n == end:
                    another = p + [n]
                    paths.append(another)
                    shortest = min(shortest, len(another))
                    continue

                if n not in words:
                    continue

                for adj in graph[n]:
                    next_.append([p + [n], adj])

            words -= set([i[1] for i in q])
            q = next_

        return paths, shortest

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = self._build_graph([beginWord] + wordList)
        #return graph
        paths, shortest = self.findPath(graph, beginWord, endWord)
        return list(filter(lambda a: len(a) == shortest, paths))


if __name__ == "__main__":
    begin = "qa"
    end = "sq"
    words = [
        "si",
        "go",
        "se",
        "cm",
        "so",
        "ph",
        "mt",
        "db",
        "mb",
        "sb",
        "kr",
        "ln",
        "tm",
        "le",
        "av",
        "sm",
        "ar",
        "ci",
        "ca",
        "br",
        "ti",
        "ba",
        "to",
        "ra",
        "fa",
        "yo",
        "ow",
        "sn",
        "ya",
        "cr",
        "po",
        "fe",
        "ho",
        "ma",
        "re",
        "or",
        "rn",
        "au",
        "ur",
        "rh",
        "sr",
        "tc",
        "lt",
        "lo",
        "as",
        "fr",
        "nb",
        "yb",
        "if",
        "pb",
        "ge",
        "th",
        "pm",
        "rb",
        "sh",
        "co",
        "ga",
        "li",
        "ha",
        "hz",
        "no",
        "bi",
        "di",
        "hi",
        "qa",
        "pi",
        "os",
        "uh",
        "wm",
        "an",
        "me",
        "mo",
        "na",
        "la",
        "st",
        "er",
        "sc",
        "ne",
        "mn",
        "mi",
        "am",
        "ex",
        "pt",
        "io",
        "be",
        "fm",
        "ta",
        "tb",
        "ni",
        "mr",
        "pa",
        "he",
        "lr",
        "sq",
        "ye",
    ]
    import datetime
    st = datetime.datetime.now()
    graph = Solution().findLadders(begin, end, words)
    print(datetime.datetime.now() - st)
    print(graph)
