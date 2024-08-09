#字典的简单操作，将字典的键值对通过for赋值给另一个字典
grades = {"海洋" : 81,
          "瑞祥" : 78,
          "思是" : 99,
          "多尔" : 74,
          "牛瘟" : 62
}
grades_s = {}
for grades_key in grades:
    if grades[grades_key] > 90:
        grades_s [grades_key] = "甲"
    elif grades[grades_key] > 80:
        grades_s [grades_key] = "乙"
    elif grades[grades_key] > 70:
        grades_s [grades_key] = "丙"
    else:
        grades_s [grades_key] = "丁"
print(grades_s)