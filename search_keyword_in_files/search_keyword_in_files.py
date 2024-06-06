import os

def search_keyword_in_files(directory, keyword, output_file):
    """
    指定されたディレクトリ内のテキストファイルから特定のキーワードを含む行を検索し、結果を新しいファイルに出力します。

    :param directory: 検索するディレクトリのパス
    :param keyword: 検索するキーワード
    :param output_file: 出力ファイルのパス
    """
    result_lines = []

    # 指定されたディレクトリ内のすべてのファイルを検索
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                
                # テキストファイルを開いてキーワードを検索
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line in lines:
                        if keyword in line:
                            result_lines.append(line.strip())

    # 結果を新しいファイルに出力
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in result_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    # 使用例
    search_directory = "example_directory"  # 検索するディレクトリのパスを指定
    search_keyword = "example_keyword"  # 検索するキーワードを指定
    output_file_path = "output.txt"  # 出力ファイルのパスを指定

    search_keyword_in_files(search_directory, search_keyword, output_file_path)
    print(f"キーワード '{search_keyword}' を含む行が '{output_file_path}' に書き出されました。")
