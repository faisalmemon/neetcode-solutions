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

class Solution:

    nodes = []

    def anagram_node_of(self, node) -> Node|None:
        for candidate in self.nodes:
            if node == candidate:
                continue
            if node.length != candidate.length:
                continue
            if node.sorted_characters == candidate.sorted_characters:
                print(f"matched: {node.word} {candidate.word}")
                return candidate
        return None

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for item in strs:
            self.nodes.append(Node(item))
        for item in self.nodes:
            item.dump_node()

        companions = {}
        for node in self.nodes:
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

        return overall_result
