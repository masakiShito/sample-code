import random
import sys
from collections import defaultdict

class PPMTextPredictor:
    def __init__(self):
        self.context_length = 3
        self.history = []
        self.counts = defaultdict(lambda: defaultdict(int))
    
    def update_history(self, words):
        self.history.extend(words)
        if len(self.history) > self.context_length:
            self.history = self.history[-self.context_length:]
    
    def update_counts(self, context, next_word):
        self.counts[tuple(context)][next_word] += 1
    
    def predict_next_word(self):
        context = tuple(self.history[-(self.context_length-1):])
        if context in self.counts:
            predictions = self.counts[context]
            if predictions:
                predicted_word = max(predictions, key=predictions.get)
                return predicted_word
        return random.choice(list(self.counts.keys())) if self.counts else ""
    
    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.context_length):
            context = words[i:i + self.context_length - 1]
            next_word = words[i + self.context_length - 1]
            self.update_counts(context, next_word)
    
    def predict_text(self, input_text, num_words=10):
        self.history = input_text.split()
        predicted_text = input_text
        for _ in range(num_words):
            next_word = self.predict_next_word()
            predicted_text += " " + next_word
            self.update_history([next_word])
        return predicted_text

if __name__ == "__main__":
    # コマンドラインからトレーニングテキストを入力させる
    training_text = input("トレーニングテキストを入力してください: ")
    
    predictor = PPMTextPredictor()
    predictor.train(training_text)
    
    # コマンドラインから予測したいテキストを入力させる
    input_text = input("予測したいテキストを入力してください: ")
    predicted_text = predictor.predict_text(input_text, num_words=10)
    print("予測されたテキスト:", predicted_text)
