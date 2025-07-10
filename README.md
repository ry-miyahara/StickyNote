# スティッキーノートアプリ

このプロジェクトは、Pythonの標準ライブラリ（tkinter）だけで作成されたシンプルなスティッキーノート（付箋）アプリケーションです。  
ユーザーはノートの作成・編集・表示を直感的なインターフェースで行うことができます。

## ディレクトリ構成

```
sticky-notes-app/
├── src/
│   └── main.py      # アプリ本体
├── notes.txt        # 付箋として表示・編集するテキスト
└── README.md        # このファイル
```

## 動作環境

- Python 3.x（tkinterが利用できる環境）

## インストール方法

1. リポジトリをクローンします:
   ```
   git clone <repository-url>
   ```
2. プロジェクトディレクトリに移動します:
   ```
   cd sticky-notes-app
   ```

## 使い方

1. `notes.txt` に表示したい内容を記載してください。
2. アプリケーションを起動します:
   ```
   python src/main.py
   ```
   - ウィンドウが最前面に表示され、内容を編集すると自動保存されます。
   - 右下の「前面固定」「解除」ボタンでウィンドウの表示順を切り替えられます。

## exe化（Windows向け）

Pythonがインストールされていない環境でも使いたい場合は、[PyInstaller](https://pyinstaller.org/) でexe化できます。

1. PyInstallerをインストール
   ```
   pip install pyinstaller
   ```
2. exeファイルを作成
   ```
   cd src
   pyinstaller --onefile --noconsole main.py
   ```
3. `dist/main.exe` が生成されます。`notes.txt` を同じ階層または適切な場所に配置してください。

---

ご不明点があれば [issues](https://github.com/) までご連絡ください。