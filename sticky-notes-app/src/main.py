import tkinter as tk
import os
import json
import threading

NOTES_FILE = os.path.join(os.path.dirname(__file__), '..', 'notes.json')
CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'window_config.json')

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {"text": "", "checkboxes": []}
    try:
        with open(NOTES_FILE, encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {"text": "", "checkboxes": []}
            if "checkboxes" not in data:
                data["checkboxes"] = []
            if "text" not in data:
                data["text"] = ""
            return data
    except Exception:
        return {"text": "", "checkboxes": []}

def save_notes(event=None):
    text_content = text.get('1.0', 'end-1c')
    checkboxes = []
    for cb in checkbox_widgets:
        idx = text.index(cb['window'])
        checkboxes.append({"index": idx, "checked": cb['var'].get()})
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump({"text": text_content, "checkboxes": checkboxes}, f, ensure_ascii=False, indent=2)

def set_topmost():
    root.attributes('-topmost', True)
    root.bind("<Unmap>", handle_unmap)

def set_notopmost():
    root.attributes('-topmost', False)
    root.bind("<Unmap>", handle_unmap)

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
    save_notes()
    root.destroy()

def insert_checkbox():
    var = tk.BooleanVar()
    cb = tk.Checkbutton(text, variable=var, command=save_notes)
    idx = text.index(tk.INSERT)
    text.window_create(idx, window=cb)
    checkbox_widgets.append({'window': idx, 'var': var, 'cb': cb})
    save_notes()

def restore_checkboxes():
    for cb in checkbox_widgets:
        try:
            cb['cb'].destroy()
        except Exception:
            pass
    checkbox_widgets.clear()
    data = load_notes()
    for cbinfo in data.get("checkboxes", []):
        var = tk.BooleanVar(value=cbinfo.get("checked", False))
        cb = tk.Checkbutton(text, variable=var, command=save_notes)
        try:
            text.window_create(cbinfo["index"], window=cb)
            checkbox_widgets.append({'window': cbinfo["index"], 'var': var, 'cb': cb})
        except Exception:
            continue

def handle_unmap(event=None):
    root.deiconify()
    # 1秒後にもう一度deiconifyを実行
    root.after(1000, root.deiconify)

def uncheck_all_checkboxes():
    for cb in checkbox_widgets:
        cb['var'].set(False)
    save_notes()

root = tk.Tk()
root.title("Sticky Note")
root.attributes('-topmost', True)
root.geometry(load_window_config())

# ウィンドウを最小化できないようにする
root.resizable(True, True)
root.protocol("WM_ICONIFY", lambda: None)
root.bind("<Unmap>", handle_unmap)

checkbox_widgets = []

# --- ボタンエリア ---
button_frame = tk.Frame(root, bg="#ffff88")
button_frame.pack(fill='x', side='top')

cb_btn = tk.Button(button_frame, text="☑ チェックボックス", font=("Meiryo", 9), command=insert_checkbox)
cb_btn.pack(side='left', padx=4, pady=4)

uncheck_btn = tk.Button(button_frame, text="チェックを外す", font=("Meiryo", 9), command=uncheck_all_checkboxes)
uncheck_btn.pack(side='left', padx=4, pady=4)

top_btn = tk.Button(button_frame, text="前面固定", command=set_topmost, font=("Meiryo", 8), width=8)
top_btn.pack(side='right', padx=2, pady=4)
back_btn = tk.Button(button_frame, text="解除", command=set_notopmost, font=("Meiryo", 8), width=8)
back_btn.pack(side='right', padx=2, pady=4)

def set_bottommost():
    root.attributes('-topmost', False)
    root.lower()

bottom_btn = tk.Button(button_frame, text="背面固定", command=set_bottommost, font=("Meiryo", 8), width=8)
bottom_btn.pack(side='right', padx=2, pady=4)

# --- テキストエリア ---
text = tk.Text(root, wrap='word', font=("Meiryo", 12), bg="#ffff88")
text.pack(expand=True, fill='both')

# テキストとチェックボックスの復元
data = load_notes()
text.insert('1.0', data.get("text", ""))
restore_checkboxes()

text.bind('<KeyRelease>', save_notes)
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()