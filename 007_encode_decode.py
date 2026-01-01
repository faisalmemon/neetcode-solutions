class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f'{len(word):03d}'
            result += word
        return result

    def decode(self, s: str) -> List[str]:
        result_list = []

        index = 0
        total_length = len(s)
        while index < total_length:
            prefix_digits = s[index:index+3]
            prefix_length = int(prefix_digits)
            index += 3
            word = s[index:index+prefix_length]
            result_list.append(word)
            index += prefix_length
        return result_list
