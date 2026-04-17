import time
minutes = int(input("分数を入力してください："))
seconds = int(input("秒数を入力してください："))
total_seconds = minutes * 60 + seconds
for i in range(total_seconds, 0, -1):
    m = i // 60
    s = i % 60
    print(f"{m}:{s:02d}")
    time.sleep(1)
print("時間になりました！")