import random

def number_guessing_game():
    print("数字当てゲームへようこそ！")
    print("1から100までの数字を当ててください。")

    # ランダムな数字を生成
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # ユーザーに数字を入力させる
            guess = int(input("あなたの予想: "))
            attempts += 1

            # 数字が範囲外の場合の処理
            if guess < 1 or guess > 100:
                print("1から100までの数字を入力してください。")
                continue

            # 予想が正解かどうかをチェック
            if guess < target_number:
                print("もっと大きな数字です。")
            elif guess > target_number:
                print("もっと小さな数字です。")
            else:
                print(f"おめでとうございます！正解は {target_number} でした。")
                print(f"あなたは {attempts} 回で正解しました。")
                break

        except ValueError:
            print("無効な入力です。数字を入力してください。")

if __name__ == "__main__":
    number_guessing_game()
