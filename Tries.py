
class Node:
    def __init__(self):
        self.childeren = dict()
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root

        for c in word:
            if c not in current_node.childeren:
                current_node.childeren[c] = Node()
            current_node = current_node.childeren[c]

        current_node.is_end_of_word = True


    def search(self, word):
        current_node = self.root

        for c in word:
            if c not in current_node.childeren:
                return False

            current_node = current_node.childeren[c]

            return current_node.is_end_of_word

    def delete(self, word):
        self._delete(self.root, word, 0)
        pass

    def has_prefix(self, prefix):
        current_node = self.root

        for c in prefix:
            if c not in current_node.childeren:
                return False

            current_node = current_node.childeren[c]

            return True

    def starts_with(self, prefix):
        words = []
        current_node = self.root

        for c in prefix:
            if c not in current_node.childeren:
                return words

            current_node = current_node.childeren[c]

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for c, child_node in current_node.childeren.items():
                _dfs(child_node, path + [c])

        _dfs(current_node, list(prefix))

        return words


    def list_words(self,):
        words = []

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for c, child_node in current_node.childeren.items():
                _dfs(child_node, path + [c])

        _dfs(self.root, [])

        return words


    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False

            current_node.is_end_of_word = False
            return len(current_node.childeren) == 0

        c = word[index]
        node = current_node.childeren.get(c)

        if node is None:
            return False
        delete_current_node = self._delete(node, word, index + 1)

        if delete_current_node:
            del current_node.childeren[c]
            return  len(current_node.childeren) == 0 and not current_node.is_end_of_word
        return False




if __name__ == '__main__':
    trie = Trie()

    trie.insert('hello')
    trie.insert('henry')
    trie.insert('mike')
    trie.insert('minimal')
    trie.insert('minimum')

    print(trie.list_words())

    print(trie.has_prefix('m'))
    print(trie.starts_with('m'))










