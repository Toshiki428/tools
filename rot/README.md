# ROT Cipher Tool

## 概要

これは、シーザー暗号の一種であるROT暗号のエンコード・デコードを行うためのシンプルなコマンドラインツールです。

CTF（Capture The Flag）などでROT暗号を扱う際に便利です。

## 機能

- 指定したシフト数で文字列を変換します。
- シフト数を指定しない場合、ROT1からROT25までのすべての変換パターンを一覧表示します。
- 大文字と小文字の両方に対応しています。
- アルファベット以外の文字（数字、記号、スペースなど）は変換せず、そのまま維持します。

## 動作環境

- Python 3.6+

## インストール

### 1. プロジェクトの準備

まず、プロジェクトのコードを手元に用意します。

#### 方法A: Gitを利用する場合

`git`コマンドが使える環境が必要です。

```bash
# リポジトリをクローン
git clone https://github.com/Toshiki428/tools.git

# プロジェクトのディレクトリへ移動
cd tools/rot
```

#### 方法B: ZIPファイルでダウンロードする場合

リポジトリのWebページから「Code」→「Download ZIP」を選択してダウンロードします。  
ダウンロードしたZIPファイルを解凍し、ターミナルでその中の`rot`ディレクトリに移動してください。

### 2. 仮想環境のセットアップとライブラリのインストール

ここからの手順は、`rot`ディレクトリの中で行います。


#### a. 仮想環境の作成

`venv`という名前の仮想環境フォルダを作成します。

```bash
python -m venv venv
```

#### b. 仮想環境の有効化

作成した仮想環境を有効にします。

```bash
# Windowsの場合
.\venv\Scripts\activate

# macOS / Linux の場合
source venv/bin/activate
```

#### c. ライブラリのインストール

有効化した仮想環境の中で、`pip`を使って必要なライブラリをインストールします。

```bash
pip install -r requirements.txt
```

`deactivate` コマンドで仮想環境を終了できます。

## 使い方

`-t` または `--text` オプションで変換したい文字列を指定します。

### 特定のシフト数で変換する

`-d` または `--diff` オプションでシフト数を指定して、文字列を変換します。シフト数は `-25` から `25` の範囲で指定できます。

```bash
python main.py --text "Hello, World" --diff 13
```

**出力:**

```
Uryyb, Jbeyq
```

### すべてのシフトパターンを試す

`-d` オプションを指定しない場合、ROT1からROT25までのすべての結果が出力されます。  
これは、シフト数が不明な暗号文を解読する際に役立ちます。

```bash
python main.py --text "Uryyb, Jbeyq"
```

**出力:**

```
ROT1: Vszzc, Kcfzr
ROT2: Wtaad, Ldgas
ROT3: Xubbe, Mehbt
ROT4: Yvccf, Nficu
ROT5: Zwddg, Ogjdv
ROT6: Axeeh, Phkew
ROT7: Byffi, Qilfx
ROT8: Czggj, Rjmgy
ROT9: Dahhk, Sknhz
ROT10: Ebiil, Tloia
ROT11: Fcjjm, Umpjb
ROT12: Gdkkn, Vnqkc
ROT13: Hello, World
ROT14: Ifmmp, Xpsme
ROT15: Jgnnq, Yqtnf
ROT16: Khoor, Zruog
ROT17: Lipps, Asvph
ROT18: Mjqqt, Btwqi
ROT19: Nkrru, Cuxrj
ROT20: Olssv, Dvysk
ROT21: Pmttw, Ewztl
ROT22: Qnuux, Fxaum
ROT23: Rovvy, Gybvn
ROT24: Spwwz, Hzcwo
ROT25: Tqxxa, Iadxp
```

## ライセンス
このプロジェクトは[MITライセンス](../LICENSE)の下で公開されています。

