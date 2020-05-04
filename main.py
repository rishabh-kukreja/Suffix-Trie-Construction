class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertAt(i, string)
	
	def insertAt(self,i, string):
		Node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in Node:
				Node[letter] = {}
			Node = Node[letter]
		Node[self.endSymbol] = True
			

    def contains(self, string):
		node = self.root
		for i in string:
			if i not in node:
				return False
			node = node[i]
		return self.endSymbol in node