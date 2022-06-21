import numpy as np

def lotto(selected_nums):
    global result
    lotto_num = np.random.choice(np.arange(1, 46), size=6, replace=False)

    check = 0
    second = False
    for selected_num in selected_nums:
        if selected_num in lotto_num: check += 1
        if selected_num == lotto_num[5]: second = True

    if check == 6: result = "1등"
    elif check == 5:
        if second: result = "2등"
        else: result = "3등"
    elif check == 4: result == "4등"
    elif check == 4: result == "5등"
    else: result = "미당첨"
    print(f"당첨번호는 {lotto_num}입니다.\n당신은 {result}입니다.")

result = "미당첨"
num = 0
while result == "미당첨":
    lotto([4, 17, 27, 33, 45])
    num += 1
print(num)