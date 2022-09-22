class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for word in s.split(" "):
            words.append(word[-1::-1])
        return " ".join(words)