def get_even_squares(num_list:list)->list:
    """
    函式 get_even_squares(num_list):
    接受一個整數列表 num_list 作為參數
    使用【列表推導式(List Comprehension)】返回 num_list 中所有偶數的平方值列表
    """
    # return [num ** 2 for num in num_list if num % 2 == 0]
    return [num ** 2 for num in num_list if not num % 2 ]



# def get_odd_cubes(num_list:list)->list:
#     """
#     接受一個整數列表 num_list 作為參數
#     使用【迴圈】返回 num_list 中所有奇數的 3 次方值列表
#     """
#     return [num ** 3 for num in num_list if num % 2 != 0]
def get_odd_cubes(num_list: list)->list:
    """
    接受一個整數列表 num_list 作為參數
    使用【迴圈】返回 num_list 中所有奇數的 3 次方值列表
    """
    # 建立一個空列表來存儲結果
    result = []

    # 遍歷 num_list 中的每個元素
    for num in num_list:
        # 如果 num 是奇數
        if num % 2 != 0:
            # 計算 num 的 3 次方並添加到結果列表中
            result.append(num ** 3)

    # 返回包含所有奇數 3 次方值的列表
    return result

# 測試函式
def get_sliced_list(num_list:list)->list:
    """
    接受一個整數列表 num_list 作為參數
    使用【切片】返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表
    """
    return num_list [4:]

def format_numbers(numbers:list)->list:
    """
    接受一個數字列表 numbers 作為參數
    返回一個新列表,其中每個數字都被格式化為 8 個字元的寬度,並靠右對齊
    """
    # formatted_numbers = ["{:8}".format(num) for num in numbers]
    # return formatted_numbers
    return [f"{num:>8}"for num in numbers]

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_squares = get_even_squares(num_list)
odd_cubes = get_odd_cubes(num_list)
sliced_list = get_sliced_list(num_list)

formatted_even_squares = format_numbers(even_squares)
formatted_odd_cubes = format_numbers(odd_cubes)
formatted_sliced_list = format_numbers(sliced_list)

# 輸出結果
print("方法1 分二次")
print(",".join(formatted_even_squares))
print(",".join(formatted_odd_cubes))
print(",".join(formatted_sliced_list))

print("--"*30)
print("方法2 包起來")
new_list1=format_numbers(get_even_squares(num_list))
new_list2=format_numbers(get_odd_cubes(num_list))
new_list3=format_numbers(get_sliced_list(num_list))

print(",".join(new_list1))
print(",".join(new_list2))
print(",".join(new_list3))

print("--"*30)
print("結果一樣喔")


