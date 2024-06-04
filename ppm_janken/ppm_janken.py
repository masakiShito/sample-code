import random
from collections import defaultdict, deque

class PPMJanken:
    def __init__(self):
        self.history = ""
        self.context_length = 3
        self.counts = defaultdict(lambda: defaultdict(int))
        self.recent_results = deque(maxlen=5)  # 過去5戦の結果を保存するデータ構造
    
    def update_history(self, user_move):
        self.history += user_move
        if len(self.history) > self.context_length:
            self.history = self.history[-self.context_length:]
        
    def predict_user_move(self):
        context = self.history[-(self.context_length-1):]
        if context in self.counts:
            predictions = self.counts[context]
            if predictions:
                predicted_move = max(predictions, key=predictions.get)
                return predicted_move
        return random.choice(['R', 'P', 'S'])

    def update_counts(self, user_move):
        context = self.history[-(self.context_length-1):]
        self.counts[context][user_move] += 1

    def get_computer_move(self, user_move):
        prediction = self.predict_user_move()
        self.update_counts(user_move)
        self.update_history(user_move)
        
        # Predict user's next move and choose the move to beat it
        if prediction == 'R':
            return 'P'  # Paper beats Rock
        elif prediction == 'P':
            return 'S'  # Scissors beat Paper
        else:
            return 'R'  # Rock beats Scissors

    def play(self):
        moves = {'R': 'グー', 'P': 'パー', 'S': 'チョキ'}
        while True:
            user_move = input("手を入力してください (R: グー, P: パー, S: チョキ, Q: 終了): ").upper()
            if user_move == 'Q':
                break
            if user_move not in moves:
                print("無効な手です。R、P、またはSを入力してください。")
                continue

            computer_move = self.get_computer_move(user_move)
            print(f"コンピュータの手: {moves[computer_move]}")

            if computer_move == user_move:
                result = "引き分け"
            elif (computer_move == 'R' and user_move == 'S') or (computer_move == 'P' and user_move == 'R') or (computer_move == 'S' and user_move == 'P'):
                result = "コンピュータの勝ち"
            else:
                result = "あなたの勝ち"
            
            self.recent_results.append(result)
            print(result)
            self.display_recent_results()

    def display_recent_results(self):
        print("過去5戦の結果:")
        for i, result in enumerate(self.recent_results, 1):
            print(f"第{i}戦: {result}")

if __name__ == "__main__":
    game = PPMJanken()
    game.play()
