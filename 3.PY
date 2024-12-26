# 讀取輸入
n = int(input("請輸入陣列元素個數："))  # 第一行為陣列元素個數
array = list(map(int, input("請輸入陣列元素：").split()))  # 第二行為陣列元素

# 計算逆序對數量
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if array[i] > array[j]:
            count += 1

# 輸出結果
print(f"Output：{count}")
