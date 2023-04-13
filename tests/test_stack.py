from da.data_structure.stack import Stack


def test_stack():
    st = Stack[int]()
    st.push(5)
    st.push(7)
    st.push(9)

    assert st.pop() == 9
    assert st.length == 2

    st.push(11)
    assert st.pop() == 11
    assert st.pop() == 7
    assert st.peek() == 5
    assert st.pop() == 5
    assert st.pop() is None

    st.push(69)
    assert st.peek() == 69
    assert st.length == 1
