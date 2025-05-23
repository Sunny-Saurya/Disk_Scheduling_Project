# Disk Scheduling Simulator 🚀

This is a **Python-based Disk Scheduling Simulator** built using `Tkinter` GUI. It visualizes and compares four disk scheduling algorithms — **FCFS**, **SSTF**, **SCAN**, and **C-SCAN** — by animating the movement of the disk head across different track requests.

---

## 🧠 What is Disk Scheduling?

In operating systems, **disk scheduling** is used to determine the order in which disk I/O requests are processed. Since moving the disk head takes time, different algorithms aim to minimize the **total head movement** and improve efficiency.

---

## 🧮 Supported Algorithms

### 1. FCFS (First-Come, First-Served)
- Processes requests in the order they arrive.
- Simple but not necessarily optimal in terms of head movement.

### 2. SSTF (Shortest Seek Time First)
- Selects the request that is **closest to the current head position**.
- Reduces total head movement but may cause starvation of far-off requests.

### 3. SCAN (Elevator Algorithm)
- Head moves in one direction, servicing all requests in its path, then reverses.
- Good balance between fairness and performance.

### 4. C-SCAN (Circular SCAN)
- Similar to SCAN, but after reaching the end, the head jumps to the beginning without servicing in reverse.
- Provides more uniform wait time.

---

## 🖥️ GUI Features

- Input field for **disk requests** (comma-separated values).
- Input field for **initial head position**.
- Dropdown to select the **scheduling algorithm**.
- **Canvas animation** showing head movement between tracks.
- Displays the **sequence of servicing** and **total head movement**.

---

![Demo Simulator SnapShot](<Screenshot 2025-04-24 190725.png>)

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Open your terminal and navigate to the project folder.
4. Run the simulator:
   ```bash
   python disk_scheduler.py