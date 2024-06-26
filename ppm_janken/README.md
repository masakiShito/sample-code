# PPM 法を使用したじゃんけんゲーム

このフォルダには、PPM (Prediction by Partial Matching) 法を使用してユーザーに負けにくいじゃんけんゲームを Python で実装した `ppm_janken.py` ファイルが含まれています。

## 概要

`ppm_janken.py` は、ユーザーの手のパターンを分析し、次の手を予測することで、コンピュータがユーザーに負けにくい手を選ぶじゃんけんゲームです。過去の手の履歴を利用して、PPM 法に基づいて次の手を予測し、その予測に基づいてコンピュータの手を決定します。

### 機能

- ユーザーの手の履歴を記録し、次の手を予測
- 予測されたユーザーの手に勝つ手をコンピュータが選択
- 過去 5 戦の結果を表示

### 使用方法

1. Python 3.x がインストールされていることを確認してください。
2. リポジトリをクローンするか、`ppm_janken.py` ファイルをダウンロードします。
3. ターミナルまたはコマンドプロンプトで `ppm_janken.py` があるディレクトリに移動します。
4. 以下のコマンドを実行してゲームを開始します。

```sh
python ppm_janken.py
```

5. 指示に従って手を入力します。R はグー、P はパー、S はチョキを表し、Q を入力するとゲームを終了します。

### ファイル構成

- ppm_janken.py: じゃんけんゲームのメインプログラム
- README.md: このファイル

### 例

ゲームを実行すると、以下のように手を入力して進めることができます。

```sh
手を入力してください (R: グー, P: パー, S: チョキ, Q: 終了): R
コンピュータの手: パー
コンピュータの勝ち
過去5戦の結果:
第1戦: コンピュータの勝ち

手を入力してください (R: グー, P: パー, S: チョキ, Q: 終了): S
コンピュータの手: グー
コンピュータの勝ち
過去5戦の結果:
第1戦: コンピュータの勝ち
第2戦: コンピュータの勝ち

```
