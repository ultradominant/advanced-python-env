def all_eq(strings):
    max_len = 0

    for s in strings:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in strings:
        if len(s) < max_len:
            s = s + "_" * (max_len - len(s))
        result.append(s)

    return result
