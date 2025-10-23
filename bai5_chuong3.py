def check_values(i, j, k):
    """
    Thực thi đoạn mã điều kiện và in ra kết quả cuối cùng của i, j, k.
    """
    i_initial, j_initial, k_initial = i, j, k


    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else: # i >= j
        if j > k:
            j = i
        else:
            i = k

    print(f"({i_initial}, {j_initial}, {k_initial}) -> i = {i}, j = {j}, k = {k}")


print("Kết quả xuất ra màn hình cho các trường hợp:")
print("------------------------------------------")


print("(a) i = 3, j = 5, and k = 7:")
check_values(3, 5, 7)


print("\n(b) i = 3, j = 7, and k = 5:")
check_values(3, 7, 5)


print("\n(c) i = 5, j = 3, and k = 7:")
check_values(5, 3, 7)


print("\n(d) i = 5, j = 7, and k = 3:")
check_values(5, 7, 3)


print("\n(e) i = 7, j = 3, and k = 5:")
check_values(7, 3, 5)


print("\n(f) i = 7, j = 5, and k = 3:")
check_values(7, 5, 3)
