
def word_break(s, words):
    if not s:
        return True
    queue = {0: False}
    while queue:
        i = queue.keys()[0]
        del queue[i]
        x = s[i:]
        for w in words:
            if x == w:
                return True
            if x.startswith(w):
                sub_i = i + len(w)
                if sub_i not in queue:
                    queue[sub_i] = False
    return False

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(word_break(s, words))
