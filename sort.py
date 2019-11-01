def sort_list(lis, start, end):
    # 判断结束位置
    if start < end:
        i, j = start, end
        # 设置初始值
        base = lis[i]
        while i < j:
            # 此循环可将 序列分为两部分
            while i < j and lis[j] >= base:
                j = j - 1
            lis[i] = lis[j]

            while i < j and lis[i] <= base:
                i = i + 1
            lis[j] = lis[i]
        lis[i] = base

        # 将序列 一分为二 此为小值列表
        sort_list(lis, start, i - 1)
        # 此为大值列表
        sort_list(lis, j + 1, end)

    return lis


if __name__ == '__main__':
    lis = [1, 2, 3, 5, 7, 11, 4, 6]
    sort_list(lis, 0, len(lis) - 1)
    print(lis)
