import copy

class Node:
    def __init__(self, word: str):
        self.word = word
        self.characters = [character for character in word]
        self.sorted_characters = copy.copy(self.characters)
        self.sorted_characters.sort()
        self.length = len(word)
    
    def dump_node(self):
        print(f'word {self.word} characters {self.characters} sorted_characters {self.sorted_characters} length {self.length}')

class Solution1:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nodes = []
        for item in strs:
            nodes.append(Node(item))
        for item in nodes:
            item.dump_node()

        companions = {}
        for node in nodes:
            dict_key = ''.join(node.sorted_characters)
            if dict_key in companions:
                companions[dict_key].append(node.word)
            else:
                companions[dict_key] = [node.word]
        print(companions)
        overall_result = []
        print("Final Processing")
        for item in companions:
            print(companions[item])
            if len(companions[item]) != 0:
                overall_result.append(companions[item])

        nodes = []
        return overall_result

    
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
