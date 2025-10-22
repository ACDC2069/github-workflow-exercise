def dedupe_list(input_list):
    """
    去除列表中的重复元素，保持原有顺序
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    # 测试去重功能
    test_list = [1, 2, 2, 3, 4, 4, 5]
    result = dedupe_list(test_list)
    print(f"Original: {test_list}")
    print(f"Deduped: {result}")