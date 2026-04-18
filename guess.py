import random

answer = random.randint(1, 10)
guess = 0
count = 0
while guess != answer and count < 5:
    guess = int(input("数字を当ててください："))
    count += 1
    if guess < answer:
        print("小さいです。")
    elif guess > answer:
        print("大きいです。")
    else:
        print(f"{count}回目で正解です！")
if count == 5 and guess != answer:
    print(f"残念！正解は{answer}でした。")  
