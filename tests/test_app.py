import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe_list, add_numbers

def test_dedupe_list():
    """测试去重功能"""
    assert dedupe_list([1, 2, 2, 3]) == [1, 2, 3]
    assert dedupe_list(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert dedupe_list([]) == []
    assert dedupe_list([1, 1, 1]) == [1]

def test_add_numbers():
    """测试加法功能"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(10, -5) == 5