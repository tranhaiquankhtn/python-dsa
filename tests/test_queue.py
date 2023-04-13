from da.data_structure.queue import Queue


def test_queue():
    q = Queue[int]()

    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)

    assert q.deque() == 5
    assert q.length == 2

    q.enqueue(11)
    assert q.deque() == 7
    assert q.deque() == 9
    assert q.peek() == 11
    assert q.deque() == 11
    assert q.deque() is None
    assert q.length == 0

    q.enqueue(69)
    assert q.peek() == 69
    assert q.length == 1
