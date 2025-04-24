import tkinter as tk
from tkinter import ttk
import time

MAX_TRACK = 199

def fcfs(requests, head):
    sequence = []
    total_movement = 0
    for req in requests:
        total_movement += abs(head - req)
        sequence.append(req)
        head = req
    return sequence, total_movement

def sstf(requests, head):
    sequence = []
    total_movement = 0
    pending = requests.copy()
    while pending:
        closest = min(pending, key=lambda x: abs(head - x))
        total_movement += abs(head - closest)
        sequence.append(closest)
        head = closest
        pending.remove(closest)
    return sequence, total_movement

def scan(requests, head):
    sequence = []
    total_movement = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    for req in right:
        total_movement += abs(head - req)
        sequence.append(req)
        head = req
    if left:
        total_movement += abs(head - 0)
        head = 0
        for req in reversed(left):
            total_movement += abs(head - req)
            sequence.append(req)
            head = req
    return sequence, total_movement

def cscan(requests, head):
    sequence = []
    total_movement = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    for req in right:
        total_movement += abs(head - req)
        sequence.append(req)
        head = req
    if left:
        total_movement += abs(head - MAX_TRACK)
        total_movement += MAX_TRACK
        head = 0
        for req in left:
            total_movement += abs(head - req)
            sequence.append(req)
            head = req
    return sequence, total_movement

# GUI Setup
root = tk.Tk()
root.title("Disk Scheduling Simulator")
root.geometry("1000x650")

tk.Label(root, text="Disk Requests (comma separated):").pack()
entry_requests = tk.Entry(root, width=60)
entry_requests.pack()

tk.Label(root, text="Initial Head Position:").pack()
entry_head = tk.Entry(root, width=20)
entry_head.pack()

tk.Label(root, text="Select Algorithm:").pack()
algo_var = tk.StringVar(value="FCFS")
algo_menu = ttk.Combobox(root, textvariable=algo_var)
algo_menu['values'] = ("FCFS", "SSTF", "SCAN", "C-SCAN")
algo_menu.pack()

canvas = tk.Canvas(root, width=950, height=250, bg="white")
canvas.pack(pady=20)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack()

def animate_movement(x1, x2, y):
    # Simple animation from x1 to x2 with a moving arrow
    direction = 1 if x2 > x1 else -1
    arrow = canvas.create_polygon(x1, y-5, x1-10, y, x1, y+5, fill="blue", outline="black")
    for x in range(int(x1), int(x2), direction*3):
        canvas.move(arrow, direction*3, 0)
        canvas.update()
        time.sleep(0.01)
    canvas.delete(arrow)

def draw_disk(requests, initial_head, sequence):
    canvas.delete("all")
    scale = 900 / MAX_TRACK
    y = 125

    # Draw base track line
    canvas.create_line(25, y, 925, y, fill="gray", width=2)

    # Draw all track markers
    for r in sorted(set(requests + [initial_head])):
        x = 25 + r * scale
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")
        canvas.create_text(x, y + 15, text=str(r), font=("Arial", 8))

    head = initial_head
    for req in sequence:
        x1 = 25 + head * scale
        x2 = 25 + req * scale
        animate_movement(x1, x2, y)
        canvas.create_oval(x2-8, y-8, x2+8, y+8, fill="green")
        canvas.create_text(x2, y, text=str(req), fill="white", font=("Arial", 9, "bold"))
        head = req

def run_simulation():
    try:
        requests = list(map(int, entry_requests.get().split(',')))
        head = int(entry_head.get())
        algo = algo_var.get()
        if not all(0 <= r <= MAX_TRACK for r in requests + [head]):
            raise ValueError("All values must be between 0 and 199.")
        if algo == "FCFS":
            seq, total = fcfs(requests, head)
        elif algo == "SSTF":
            seq, total = sstf(requests, head)
        elif algo == "SCAN":
            seq, total = scan(requests, head)
        elif algo == "C-SCAN":
            seq, total = cscan(requests, head)
        draw_disk(requests, head, seq)
        output_label.config(text=f"Order: {seq}\nTotal Head Movement: {total}")
    except Exception as e:
        output_label.config(text=f"Error: {str(e)}")

tk.Button(root, text="Run Simulation", command=run_simulation, font=("Arial", 12, "bold")).pack(pady=10)

root.mainloop()
