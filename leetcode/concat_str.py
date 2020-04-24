from collections import Counter


def findSubstring(s: str, words):
    if not s or not words: return []
    one_word = len(words[0])
    word_num = len(words)
    n = len(s)
    if n < one_word * word_num: return []
    words = Counter(words)
    res = []
    for i in range(0, one_word):
        cur_cnt = 0
        left = i
        right = i
        cur_Counter = Counter()
        while right + one_word <= n:
            w = s[right:right + one_word]
            right += one_word
            # 匹配失败
            if w not in words:
                left = right
                cur_Counter.clear()
                cur_cnt = 0
            else:
                cur_Counter[w] += 1
                cur_cnt += 1
                # 有多余
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                # 成功
                if cur_cnt == word_num:
                    res.append(left)
    return res


if __name__ == '__main__':
    print(findSubstring("asdfgbarfoothefoobarman", ["foo", "bar"]))
