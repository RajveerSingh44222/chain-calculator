import tkinter as tk
from logic import calc

root = tk.Tk()
root.title("Chain Calculator")
root.geometry("500x550")
root.configure(bg="#0F172A")

current_input = ""
result = None
current_operation = None
is_dark = True


def toggle_theme():
    global is_dark

    if is_dark:
        root.configure(bg="white")
        entry.configure(bg="white", fg="black", insertbackground="black")
        toggle_btn.configure(bg="lightgray", fg="black")
        btn7.configure(bg="lightgray", fg="black")
        btn8.configure(bg="lightgray", fg="black")
        btn9.configure(bg="lightgray", fg="black")
        btn_div.configure(bg="lightgray", fg="black")
        btn4.configure(bg="lightgray", fg="black")
        btn5.configure(bg="lightgray", fg="black")
        btn6.configure(bg="lightgray", fg="black")
        btn_mul.configure(bg="lightgray", fg="black")
        btn1.configure(bg="lightgray", fg="black")
        btn2.configure(bg="lightgray", fg="black")
        btn3.configure(bg="lightgray", fg="black")
        btn_sub.configure(bg="lightgray", fg="black")
        btn0.configure(bg="lightgray", fg="black")
        btn_dot.configure(bg="lightgray", fg="black")
        btn_equal.configure(bg="lightgray", fg="black")
        btn_add.configure(bg="lightgray", fg="black")
        btn_clear.configure(bg="lightgray", fg="black")
        toggle_btn.configure(text="Switch to Dark")
        is_dark = False
    else:
        root.configure(bg="#0F172A")
        entry.configure(bg="white", fg="black", insertbackground="black")
        toggle_btn.configure(bg="#1E293B", fg="white")
        btn7.configure(bg="#1E293B", fg="white")
        btn8.configure(bg="#1E293B", fg="white")
        btn9.configure(bg="#1E293B", fg="white")
        btn_div.configure(bg="#1E293B", fg="white")
        btn4.configure(bg="#1E293B", fg="white")
        btn5.configure(bg="#1E293B", fg="white")
        btn6.configure(bg="#1E293B", fg="white")
        btn_mul.configure(bg="#1E293B", fg="white")
        btn1.configure(bg="#1E293B", fg="white")
        btn2.configure(bg="#1E293B", fg="white")
        btn3.configure(bg="#1E293B", fg="white")
        btn_sub.configure(bg="#1E293B", fg="white")
        btn0.configure(bg="#1E293B", fg="white")
        btn_dot.configure(bg="#1E293B", fg="white")
        btn_equal.configure(bg="#1E293B", fg="white")
        btn_add.configure(bg="#1E293B", fg="white")
        btn_clear.configure(bg="#1E293B", fg="white")
        toggle_btn.configure(text="Switch to Light")
        is_dark = True


def update_display(value):
    entry.delete(0, tk.END)
    entry.insert(0, value)


def click_number(num):
    global current_input
    current_input += num
    update_display(current_input)


def click_decimal():
    global current_input
    if "." not in current_input:
        if current_input == "":
            current_input = "0."
        else:
            current_input += "."
        update_display(current_input)


def click_operator(op):
    global current_input, result, current_operation

    if current_input == "":
        if result is not None:
            current_operation = op
        return

    number = float(current_input)

    if result is None:
        result = number
    elif current_operation is None:
        result = number
    else:
        new_result = calc(result, number, current_operation)
        if new_result is None:
            update_display("Error")
            clear_all_state()
            return
        result = new_result
        update_display(result)

    current_operation = op
    current_input = ""


def click_equal():
    global current_input, result, current_operation

    if current_input == "" or result is None or current_operation is None:
        return

    number = float(current_input)
    final_result = calc(result, number, current_operation)

    if final_result is None:
        update_display("Error")
        clear_all_state()
        return

    result = final_result
    current_input = str(final_result)
    current_operation = None
    update_display(final_result)


def clear_all_state():
    global current_input, result, current_operation
    current_input = ""
    result = None
    current_operation = None


def clear_all():
    clear_all_state()
    update_display("")


toggle_btn = tk.Button(
    root,
    text="Switch to Light",
    width=22,
    height=2,
    command=toggle_theme,
    bg="#1E293B",
    fg="white"
)
toggle_btn.grid(row=0, column=0, columnspan=4, pady=10)

entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 20),
    justify="right",
    bg="white",
    fg="black",
    insertbackground="black"
)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

btn7 = tk.Button(root, text="7", width=5, height=2, command=lambda: click_number("7"), bg="#1E293B", fg="white")
btn7.grid(row=2, column=0)

btn8 = tk.Button(root, text="8", width=5, height=2, command=lambda: click_number("8"), bg="#1E293B", fg="white")
btn8.grid(row=2, column=1)

btn9 = tk.Button(root, text="9", width=5, height=2, command=lambda: click_number("9"), bg="#1E293B", fg="white")
btn9.grid(row=2, column=2)

btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda: click_operator("/"), bg="#1E293B", fg="white")
btn_div.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", width=5, height=2, command=lambda: click_number("4"), bg="#1E293B", fg="white")
btn4.grid(row=3, column=0)

btn5 = tk.Button(root, text="5", width=5, height=2, command=lambda: click_number("5"), bg="#1E293B", fg="white")
btn5.grid(row=3, column=1)

btn6 = tk.Button(root, text="6", width=5, height=2, command=lambda: click_number("6"), bg="#1E293B", fg="white")
btn6.grid(row=3, column=2)

btn_mul = tk.Button(root, text="*", width=5, height=2, command=lambda: click_operator("*"), bg="#1E293B", fg="white")
btn_mul.grid(row=3, column=3)

btn1 = tk.Button(root, text="1", width=5, height=2, command=lambda: click_number("1"), bg="#1E293B", fg="white")
btn1.grid(row=4, column=0)

btn2 = tk.Button(root, text="2", width=5, height=2, command=lambda: click_number("2"), bg="#1E293B", fg="white")
btn2.grid(row=4, column=1)

btn3 = tk.Button(root, text="3", width=5, height=2, command=lambda: click_number("3"), bg="#1E293B", fg="white")
btn3.grid(row=4, column=2)

btn_sub = tk.Button(root, text="-", width=5, height=2, command=lambda: click_operator("-"), bg="#1E293B", fg="white")
btn_sub.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", width=5, height=2, command=lambda: click_number("0"), bg="#1E293B", fg="white")
btn0.grid(row=5, column=0)

btn_dot = tk.Button(root, text=".", width=5, height=2, command=click_decimal, bg="#1E293B", fg="white")
btn_dot.grid(row=5, column=1)

btn_equal = tk.Button(root, text="=", width=5, height=2, command=click_equal, bg="#1E293B", fg="white")
btn_equal.grid(row=5, column=2)

btn_add = tk.Button(root, text="+", width=5, height=2, command=lambda: click_operator("+"), bg="#1E293B", fg="white")
btn_add.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", width=22, height=2, command=clear_all, bg="#1E293B", fg="white")
btn_clear.grid(row=6, column=0, columnspan=4, pady=10)

root.mainloop()