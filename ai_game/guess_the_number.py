import random

def guess_number():
    print("1から100までの数字を考えてください。私がそれを当てます。")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"私の推測は {guess} です。")
        
        feedback = input("それは (h)高すぎる、(l)低すぎる、または (c)正しい ですか？ ").lower()
        
        if feedback == 'c':
            print(f"やった！ 数字 {guess} を {attempts} 回の試行で当てました！")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("無効な入力です。もう一度入力してください。")

if __name__ == '__main__':
    guess_number()
