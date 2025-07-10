import tkinter as tk
import os
import json

# 表示・保存するテキストファイルのパス
NOTES_FILE = os.path.join(os.path.dirname(__file__), '..', 'notes.txt')
CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'window_config.json')

def read_notes():
    try:
        with open(NOTES_FILE, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def save_notes(event=None):
    text_content = text.get('1.0', 'end-1c')
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        f.write(text_content)

def set_topmost():
    root.attributes('-topmost', True)

def set_notopmost():
    root.attributes('-topmost', False)

def load_window_config():
    try:
        with open(CONFIG_FILE, encoding='utf-8') as f:
            config = json.load(f)
            return config.get('geometry', "+100+100")
    except Exception:
        return "+100+100"

def save_window_config():
    geometry = root.geometry()
    config = {'geometry': geometry}
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f)

def on_close():
    save_window_config()
    root.destroy()

root = tk.Tk()
root.title("Sticky Note")
root.attributes('-topmost', True)
root.geometry(load_window_config())

text = tk.Text(root, wrap='word', font=("Meiryo", 12), bg="#ffff88")
text.insert('1.0', read_notes())
text.pack(expand=True, fill='both')

# 右下にボタンフレームを重ねて表示
button_frame = tk.Frame(root, bg="#ffff88")
button_frame.place(relx=1.0, rely=1.0, anchor='se', x=-8, y=-8)  # 右下に少し余白

top_btn = tk.Button(button_frame, text="前面固定", command=set_topmost, font=("Meiryo", 8), width=6)
top_btn.pack(side='left', padx=1, pady=2)
back_btn = tk.Button(button_frame, text="解除", command=set_notopmost, font=("Meiryo", 8), width=6)
back_btn.pack(side='left', padx=1, pady=2)

text.bind('<KeyRelease>', save_notes)

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()