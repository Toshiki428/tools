import string, argparse
from schema import Schema, And, Use, Or

def args_validate():
    """
    引数の検証
    """
    # 引数のスキーマ定義
    schema = Schema({
        "text": And(str, len),
        "diff": Or(None, And(Use(int), lambda n: -25<=n<=25, error="diff は -25 ~ 25 の範囲で入力してください。"))
    })

    # コマンドライン引数を取得
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", required=True, help="解読したいテキスト")
    parser.add_argument("-d", "--diff", help="ずらす文字数", type=int)
    args = parser.parse_args()

    # 引数を辞書に変換してスキーマ検証
    args_dict = vars(args)

    try:
        schema.validate(args_dict)
        return args_dict
    except Exception as e:
        print(f"検証エラー：{e}")
        return

def rot_n(text, n):
    """
    解読処理
    """
    new_text = ""
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    for char in text:
        if char in uppercase:
            index_number = uppercase.index(char)
            index_number = (index_number + n) % 26
            new_text += uppercase[index_number]
        elif char in lowercase:
            index_number = lowercase.index(char)
            index_number = (index_number + n) % 26
            new_text += lowercase[index_number]
        else:
            new_text += char

    return new_text

if __name__ == "__main__":
    args = args_validate()
    if not(args):
        exit()

    text = args["text"]
    diff = args["diff"]

    if diff is not None:
        result = rot_n(text, diff)
        print(result)
    else:
        for i in range(1, 26):
            result = rot_n(text, i)
            print(f"ROT{i}: {result}")
