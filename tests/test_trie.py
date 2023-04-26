from da.data_structure.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("feel")
    trie.insert("feat")

    expected = trie.find("fo")
    expected.sort()
    assert expected == [
        "foo",
        "fool",
        "foolish",
    ]

    trie.delete("fool")
    expected = trie.find("fo")
    expected.sort()
    assert expected == [
        "foo",
        "foolish",
    ]

    trie.delete("feel")
    expected = trie.find("fe")
    expected.sort()
    assert expected == [
        "feat",
    ]
