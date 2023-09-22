import tkinter as tk
from tkinter import ttk, filedialog
from flask import Flask, request, jsonify
import pyautogui
import time
import threading
import json
import os
import random

app = Flask(__name__)

mock_data = {
    "parameter": None,
    "value": None,
    "response_type": None,
    "response_content": None,
    "request_method": None
}

command_stop_flag = threading.Event()

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mock_endpoint():
    if request.method != mock_data["request_method"]:
        return "Método de solicitud no permitido para este mock", 405
    
    if request.method == "GET":
        param_value = request.args.get(mock_data["parameter"])
    else:
        if not request.json:
            return "Se espera datos en formato JSON", 415
        param_value = request.json.get(mock_data["parameter"])

    if param_value == mock_data["value"]:
        if mock_data["response_type"] == "JSON":
            return jsonify(eval(mock_data["response_content"]))
        else:
            return mock_data["response_content"]

    if param_value == mock_data["value"]:
        if mock_data["response_type"] == "JSON":
            try:
                response_data = json.loads(mock_data["response_content"])
                return jsonify(response_data)
            except json.JSONDecodeError:
                return "Error: El contenido de la respuesta no es un JSON válido.", 400
        else:
            return mock_data["response_content"]
    return "No coincide", 400

def start_mock_api(param_name, param_value, response_type, response_content, request_method, port):
    mock_data["parameter"] = param_name
    mock_data["value"] = param_value
    mock_data["response_type"] = response_type
    mock_data["response_content"] = response_content
    mock_data["request_method"] = request_method

    t = threading.Thread(target=lambda: app.run(port=port))
    t.start()

def setup_api_tab(tab):
    ttk.Label(tab, text="Método de Solicitud:").grid(column=0, row=0)
    methods = ["GET", "POST", "PUT", "DELETE"]
    request_method = ttk.Combobox(tab, values=methods)
    request_method.grid(column=1, row=0)

    ttk.Label(tab, text="Nombre del Parámetro:").grid(column=0, row=1)
    param_name = ttk.Entry(tab)
    param_name.grid(column=1, row=1)

    ttk.Label(tab, text="Valor:").grid(column=0, row=2)
    param_value = ttk.Entry(tab)
    param_value.grid(column=1, row=2)

    ttk.Label(tab, text="Tipo de Respuesta:").grid(column=0, row=3)
    response_types = ["XML", "JSON", "Texto"]
    response_type = ttk.Combobox(tab, values=response_types)
    response_type.grid(column=1, row=3)

    ttk.Label(tab, text="Contenido de Respuesta:").grid(column=0, row=4)
    response_content = tk.Text(tab, width=25, height=5)
    response_content.grid(column=1, row=4)

    start_button = ttk.Button(tab, text="Iniciar API", command=lambda: start_mock_api(param_name.get(), param_value.get(), response_type.get(), response_content.get("1.0", tk.END), request_method.get(), 5000))
    start_button.grid(column=0, row=5, columnspan=2)

def load_commands_from_file(text_widget):
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, file.read())

def execute_commands(commands, status_label):
    command_stop_flag.clear()
    lines = commands.strip().split('\n')
    i = 0
    loops = {}  # Para manejar loops
    while i < len(lines) and not command_stop_flag.is_set():
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        if line.startswith("loop over words:"):
            words = eval(line.split(":")[1].strip())
            loop_start = i + 1
            loop_end = lines.index("end loop", loop_start)
            for word in words:
                for j in range(loop_start, loop_end):
                    if command_stop_flag.is_set():
                        break
                    loop_line = lines[j].replace("current_word", word)
                    execute_single_command(loop_line)
            i = loop_end + 1
        elif line == "loop:":
            if i not in loops:
                loops[i] = 0
            i += 1
        elif line == "goto loop":
            if loops.get(i - 1, 0) < 10:  # Limitamos la repetición del loop a 10 veces para evitar un bucle infinito
                i = i - 2  # Regresamos a la línea anterior al "loop:"
                loops[i - 1] += 1
                continue
            else:
                loops[i - 1] = 0
                i += 1
        else:
            execute_single_command(line)
            i += 1

    if command_stop_flag.is_set():
        status_label.config(text="Ejecución cancelada")
    else:
        status_label.config(text="Ejecución completada")

def execute_single_command(command):
    if command.startswith("#"):
        return
    
    parts = command.split()
    if not parts:
        return
    
    cmd = parts[0]
    args = [evaluate_arg(arg) for arg in parts[1:]]

    if cmd == 'open':
        pyautogui.hotkey('win', 'r')
        pyautogui.write(args[0])
        pyautogui.press('enter')
    elif cmd == 'close':
        os.system(f"taskkill /im {args[0]}.exe /f")
        #pyautogui.hotkey('alt', 'f4')
    elif cmd == 'type':
        pyautogui.write(' '.join(args))
    elif cmd == 'press':
        if '+' in args[0]:
            keys = args[0].split('+')
            pyautogui.hotkey(*keys)
        else:
            pyautogui.press(args[0])
    elif cmd == 'wait':
        time.sleep(float(args[0]))
    elif cmd == 'move' and args[0] == 'mouse':
        x_offset = int(args[1])
        y_offset = int(args[2])
        current_x, current_y = pyautogui.position()
        pyautogui.moveTo(current_x + x_offset, current_y + y_offset)


def evaluate_arg(arg):
    if "random(" in arg:
        start, end = map(int, arg.replace("random(", "").replace(")", "").split(","))
        return str(random.randint(start, end))
    return arg

def cancel_execution(status_label):
    command_stop_flag.set()
    status_label.config(text="Ejecución cancelada")

def setup_keyboard_mouse_tab(tab):
    instructions = ttk.Label(tab, text="Enter keyboard and mouse commands:")
    instructions.grid(column=0, row=0, columnspan=3)

    action_content = tk.Text(tab, width=50, height=20)
    action_content.grid(column=0, row=1, columnspan=3)

    load_button = ttk.Button(tab, text="Load from file", command=lambda: load_commands_from_file(action_content))
    load_button.grid(column=0, row=2)

    status_label = ttk.Label(tab, text="Esperando comandos...")
    status_label.grid(column=0, row=3, columnspan=3)

    start_button = ttk.Button(tab, text="Execute Commands", command=lambda: [status_label.config(text="Ejecutando..."), threading.Thread(target=lambda: execute_commands(action_content.get("1.0", tk.END), status_label)).start()])
    start_button.grid(column=0, row=4, columnspan=2)

    cancel_button = ttk.Button(tab, text="Cancelar", command=lambda: cancel_execution(status_label))
    cancel_button.grid(column=2, row=4)

def main():
    root = tk.Tk()
    root.title("Mockup Tool")

    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='API Mockup')
    setup_api_tab(tab1)

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='Keyboard & Mouse Emulation')
    setup_keyboard_mouse_tab(tab2)

    tabControl.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
