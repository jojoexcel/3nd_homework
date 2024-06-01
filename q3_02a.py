import json
import os


def get_student_info(student_id: str) -> dict:
    """
    根據學號返回該學生的個人資料字典，如果找不到該學生，則 raise ValueError。
    """
    for student in data:
        if student['student_id'] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到.")


def add_course(student_id: str, course_name: str, course_score: str) -> None:
    """
    為指定學生添加一門課程及其分數，如果找不到該學生，則 raise ValueError，並使用斷言確保課程名稱與課程分數不為空字串
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

            return
    raise ValueError(f"學號 {student_id} 找不到.")


def calculate_average_score(student_data: dict) -> float:
    """
    計算並返回一位學生所有課程的平均分數，如果該學生沒有課程，則返回 0.0。
    """
    scores = [course['score'] for course in student_data.get('courses', [])]
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0.0


# 主程式
file_name = "students.json"

# 確保 JSON 檔案存在
if not os.path.isfile(file_name):
    print("找不到 JSON 檔案。")
    exit()

# 讀取 JSON 檔案並自動關閉檔案
with open(file_name, encoding='utf-8') as file:
    data = json.load(file)

while True:
    print(f"{'*'*15}選單{'*'*15}")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print('*' * 34)
    choice = input("請選擇操作項目：")

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
            print(f"=>發生錯誤: {e}")
        except Exception as e:
            print(f"=>其它例外: {e}")
    elif choice == "3":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            average_score = calculate_average_score(student_info)
            print(f"=>各科平均分數: {average_score}")
        except ValueError as e:
            print(f"=>發生錯誤: {e}")
        except Exception as e:
            print(f"=>其它例外: {e}")
    elif choice in ("4", ""):
        print("=>程式結束。")
        break
    else:
        print("=>請輸入有效的選項。")