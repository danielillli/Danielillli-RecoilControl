import pyautogui
import tkinter as tk
import keyboard
from pynput import mouse
import threading
import time  # Import the time module

# Global variables
power = 1
is_running = False
gui_visible = True

def recoil():
    while is_running:
        pyautogui.moveRel(0, power)  # Move the mouse down by 'power' pixels
        time.sleep(0.01)  # Control the speed of the recoil effect

def start_recoil():
    global is_running
    if not is_running:
        is_running = True
        recoil_thread = threading.Thread(target=recoil)
        recoil_thread.start()

def stop_recoil():
    global is_running
    is_running = False

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            start_recoil()
        else:
            stop_recoil()

def update_power(val):
    global power
    power = int(val)

def decrease_power():
    global power
    if power > 1:
        power -= 1
    power_scale.set(power)

def increase_power():
    global power
    if power < 9:
        power += 1
    power_scale.set(power)

def toggle_gui():
    global gui_visible
    if gui_visible:
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window
    gui_visible = not gui_visible

def close_script():
    stop_recoil()  # Ensure recoil stops when the script closes
    root.quit()

# Setting up the GUI
root = tk.Tk()
root.title("Recoil Control")
root.overrideredirect(True)  # Remove default window controls (minimize, maximize, close)
root.attributes("-topmost", True)  # Always on top

# Create a frame to allow dragging the window
def start_drag(event):
    root.x = event.x
    root.y = event.y

def do_drag(event):
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")

frame = tk.Frame(root, bg="gray")
frame.pack(fill=tk.BOTH, expand=1)

frame.bind("<ButtonPress-1>", start_drag)
frame.bind("<B1-Motion>", do_drag)

# Add the power scale to the frame
power_scale = tk.Scale(frame, from_=1, to=9, orient=tk.HORIZONTAL, label="Power", command=update_power)
power_scale.pack()

# Register global hotkeys using keyboard
keyboard.add_hotkey('F1', decrease_power)
keyboard.add_hotkey('F2', increase_power)
keyboard.add_hotkey('F3', toggle_gui)
keyboard.add_hotkey('F4', close_script)

# Start a listener for mouse events using pynput
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Start the Tkinter main loop
root.mainloop()
