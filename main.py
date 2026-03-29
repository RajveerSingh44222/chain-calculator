import tkinter as tk
from gui import ChainCalculatorGUI


def main():
    root = tk.Tk()
    app = ChainCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()