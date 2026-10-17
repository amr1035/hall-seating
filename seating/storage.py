"""قراءة/كتابة data.json بشكل آمن (قفل + كتابة ذرّية)."""
import json, os, threading
from django.conf import settings

_lock = threading.Lock()

def _path():
    return settings.DATA_FILE

def load():
    try:
        with open(_path(), encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save(data):
    p = str(_path())
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, p)

def add(table, name):
    with _lock:
        data = load()
        data.setdefault(str(table), []).append(name)
        save(data)
        return data

def remove(table, index):
    with _lock:
        data = load()
        lst = data.get(str(table), [])
        if 0 <= index < len(lst):
            lst.pop(index)
            if not lst:
                data.pop(str(table), None)
            save(data)
        return data
