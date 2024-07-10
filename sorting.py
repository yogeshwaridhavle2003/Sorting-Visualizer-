from tkinter import *
from tkinter import ttk
import random
import time

def bubble_sort(data, drawData, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, focus_bar=j, temp_color="blue", speed=speed)
                time.sleep(speed)

def quick_sort(data, head, tail, drawData, speed):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, speed)
        quick_sort(data, head, partitionIndex-1, drawData, speed)
        quick_sort(data, partitionIndex+1, tail, drawData, speed)

def partition(data, head, tail, drawData, speed):
    pivot = data[tail]
    border = head - 1
    for j in range(head, tail):
        if data[j] < pivot:
            border += 1
            data[border], data[j] = data[j], data[border]
        drawData(data, focus_bar=j, temp_color="green", speed=speed)
        time.sleep(speed)
    border += 1
    data[border], data[tail] = data[tail], data[border]
    drawData(data, focus_bar=border, temp_color="blue", speed=speed)
    time.sleep(speed)
    return border

def drawData(data, focus_bar=None, temp_color=None, speed=0.1):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    bar_width = canvas_width / len(data)
    max_value = max(data)
    
    for i, value in enumerate(data):
        bar_height = (value / max_value) * canvas_height
        x0 = i * bar_width
        y0 = canvas_height - bar_height
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        fill_color = temp_color if i == focus_bar else "red"
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color)
        canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), font=("Arial", 10))
        root.update()
        if temp_color:
            time.sleep(speed)

def start_algorithm():
    global data
    speed = speed_scale.get()
    if selected_alg.get() == "Bubble Sort":
        bubble_sort(data, drawData, speed)
    elif selected_alg.get() == "Quick Sort":
        quick_sort(data, 0, len(data) - 1, drawData, speed)

def generate_data():
    global data
    data_size = size_scale.get()
    min_value = min_scale.get()
    max_value = max_scale.get()
    data = [random.randint(min_value, max_value) for _ in range(data_size)]
    drawData(data)

root = Tk()
root.title("Sorting Algorithm Visualizer")

frame = Frame(root)
frame.pack(side=TOP)

canvas = Canvas(root, width=800, height=400)
canvas.pack()

label = Label(frame, text="Select Algorithm:")
label.pack(side=LEFT, padx=10)
selected_alg = ttk.Combobox(frame, values=["Bubble Sort", "Quick Sort"])
selected_alg.pack(side=LEFT, padx=10)
selected_alg.set("Bubble Sort")

generate_button = Button(frame, text="Generate Data", command=generate_data)
generate_button.pack(side=LEFT, padx=10)
start_button = Button(frame, text="Start Sorting", command=start_algorithm)
start_button.pack(side=LEFT, padx=10)

size_scale = Scale(frame, from_=5, to=100, orient=HORIZONTAL, label="Data Size")
size_scale.set(30)
size_scale.pack(side=LEFT, padx=10)
min_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, label="Min Value")
min_scale.set(0)
min_scale.pack(side=LEFT, padx=10)
max_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, label="Max Value")
max_scale.set(100)
max_scale.pack(side=LEFT, padx=10)

speed_label = Label(frame, text="Speed:")
speed_label.pack(side=LEFT, padx=10)
speed_scale = Scale(frame, from_=0.1, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Speed")
speed_scale.set(0.5)
speed_scale.pack(side=LEFT, padx=10)

root.mainloop()
