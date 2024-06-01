import json
# import os
import re


def menu():
    print("""
        ***************選單***************
        1. 查詢指定學號成績
        2. 新增指定學號的課程名稱與分數
        3. 顯示指定學號的各科平均分數
        4. 離開
        **********************************
        """)
    choice = input("請選擇操作項目：")
    return choice

def get_student_info(student_id: str)->list|dict:
    """
    根據學號返回該學生的個人資料字典，如果找不到該學生，
    則手動拋出 ValueError 與錯誤訊息供上層呼叫程式處理。
    """
    student_info = next((student for student in data if student["student_id"] == student_id), None)
    if student_info is None:
        raise ValueError(f"=>發生錯誤: 學號 {student_id} 找不到.")

    return student_info

def add_course(student_id: str, course_name: str, course_score: str) -> None:
    """
    為指定學生添加一門課程及其分數，並寫回 students.json，
    如果找不到該學生，則手動拋出 ValueError與錯誤訊息，
    並使用斷言確保課程名稱與課程分數不可為空字串，供上層呼叫程式處理。
    """
    for student in data:
        if student['student_id'] == student_id:
            assert course_name.strip(), "課程名稱不可空白."
            assert course_score.strip(), "課程分數不可空白."
            new_course = {'name': course_name, 'score': float(course_score)}

            student['courses'].append(new_course)

            # 將更新後的數據寫回 students.json 檔案
            with open('students.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
                return (f"新增{new_course['name']}:{new_course['score']}資料成功 ")
    raise ValueError(f"學號 {student_id} 找不到.")


def calculate_average_score(student_data)->float:
    """
    傳入學生的個人資料字典後，計算並返回該學生所有課程的平均分數，
    如果該學生沒有課程，則返回 0.0。
    """
    courses = student_data.get("courses", [])
    if not courses:
        return 0.0
    try:
        total_score = sum(course["score"] for course in courses)
        return total_score / len(courses)
    except ValueError as ve:
       raise ValueError (f"{ve}")
    except Exception as e:
       raise Exception(f"其他錯誤: {e}")

def choice_1_run():
    student_id = input("請輸入學號: ")
    try:
        student_info = get_student_info(path_json, student_id)
        print(f"學生資料: {json.dumps(student_info, ensure_ascii=False, indent=2)}")
    except FileNotFoundError as fnfe:
       raise FileNotFoundError (f"查無此人...")
    except ValueError as ve:
       raise ValueError (f"學號為數值{ve}")
    except Exception as e:
       raise Exception(f"其他錯誤: {e}")

def choice_2_run():
    student_id = input("請輸入學號: ")
    course_name = input("請輸入課程名稱: ")
    course_score = float(input("請輸入課程分數: "))
    add_course(path_json, student_id, course_name, course_score)


        # print(ve)



def pad_to_width(word:str, width:int, )->str:
    """
    補字元使的 width 符合設定
    因半形字與全形字的不同寬

    """
    s = str(word)
    half_width_count = len(re.findall(r'[\x00-\x7F]', s))  # 找出半形字的數量
    full_width_count = len(s) - half_width_count  # 找出全形字的數量

    s_width = width -len(s)   # 計算無半型字串要補的的空白
    padding = width -full_width_count-(half_width_count//2) # 計算有半形的需要填充的空格數量

    if half_width_count  > 0:                    #如果有半形字
        if half_width_count %2==0:                   #如果半形字為偶數
            return s + chr(12288) * padding              # 填充全形空白
        else:                                        #如果半形字為奇數
            padding=padding-1
            return s+ chr(12288) * padding +' '         # 填充全形空白+一個空格 chr(32)
    return s+ chr(12288) *(s_width)               #如果沒有半形字

def choice_3_run11():
    student_id = input("請輸入學號: ")
    try:
        student_info = get_student_info(student_id)  #讀取學生資料
        average_score = calculate_average_score(student_info)  #算平均

        col_width = [14, 2]  # 定义列宽
        CLASS_H = ["課程", "分數"]
        # print_data=f"|"+"|".join(f'{col:{chr(12288)}^{width}}' for col, width in zip(header,col_width))+"|"
        headers = ["| " + " | ".join(f'{col:{chr(12288)}^{width}}' for col, width in zip(CLASS_H,col_width)) + " |"]
        print("\n".join(headers))
        # print("-" * sum(col_width) + "---")  # 根据列宽打印分割线
        for course in student_info['courses']:
            row = ["| " + " | ".join([pad_to_width(course['name'], col_width[0]), pad_to_width(str(course['score']), col_width[1])]) + " |"]
            print("\n".join(row))
        num_courses = len(student_info['courses'])
        print(f"學號 {student_id} ,共修習了 {num_courses} 門課程,平均分數: {average_score:.2f}")
        # print(f"學號 {student_id} 平均分數: {average_score:.2f}")
    except FileNotFoundError as fnfe:
       raise FileNotFoundError (f"請輸入正確值{fnfe}")
    #    print(fnfe)
    except ValueError as ve:
       raise ValueError (f"請輸入正確值{ve}")
    except Exception as e:
       raise Exception(f"其他錯誤: {e}")

def choice_3_run():
    student_id = input("請輸入學號: ")
    try:
        student_info = get_student_info(student_id)  # 讀取學生資料
        average_score = calculate_average_score(student_info)  # 算平均

        col_width = [14, 2]  # 定義列寬
        CLASS_H = ["課程", "分數"]
        headers = ["| " + " | ".join(f'{col:{chr(12288)}^{width}}' for col, width in zip(CLASS_H, col_width)) + " |"]
        print("\n".join(headers))
        for course in student_info['courses']:
            row = ["| " + " | ".join([pad_to_width(course['name'], col_width[0]), pad_to_width(str(course['score']), col_width[1])]) + " |"]
            print("\n".join(row))
        num_courses = len(student_info['courses'])
        print(f"學號 {student_id} ,共修習了 {num_courses} 門課程,平均分數: {average_score:.2f}")
    except FileNotFoundError as fnfe:
       raise FileNotFoundError (f"請輸入正確值{fnfe}")
    #    print(fnfe)
    except ValueError as ve:
       raise ValueError (f"請輸入正確值{ve}")
    except Exception as e:
       raise Exception(f"其他錯誤: {e}")

# 定義 JSON 文件路徑
path_json = 'students.json'
with open(path_json, encoding='utf-8') as file:
    data = json.load(file)

while True:
    choice = menu()

    if choice == "1":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            print(f"=>學生資料: {json.dumps(student_info, indent=2, ensure_ascii=False)}")
        except ValueError as e:
            print(f"=>發生錯誤: {e}")
        except Exception as e:
            print(f"=>其它例外: {e}")

    elif choice == "2":
        student_id = input("請輸入學號: ")
        course_name = input("請輸入要新增課程的名稱: ")
        course_score = input("請輸入要新增課程的分數: ")
        try:
            add_course(student_id, course_name, course_score)
            print("=>課程已成功新增。")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")
    elif choice == "3":
        try:
            choice_3_run()
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")

    elif choice in ("4", ""):
        print("=>程式結束。")
        break
    else:
        print("無效的選擇，請重新輸入。")




