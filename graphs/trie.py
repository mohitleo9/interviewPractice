def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault('_end', '_end')
    return root


asdf = make_trie('foo', 'bar', 'baz', 'barz')
import pprint; pprint.pprint(asdf)
