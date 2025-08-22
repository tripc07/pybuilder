import random
import tkinter as tk
from tkinter import messagebox


def main():
    secret = random.randint(1, 100)

    root = tk.Tk()
    root.title('Guess the Number')

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    label = tk.Label(frame, text='Guess a number between 1 and 100:')
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    result_label = tk.Label(frame, text='')
    result_label.pack()

    def check_guess():
        try:
            guess = int(entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid integer')
            return
        if guess < secret:
            result_label.config(text='Too low, try again.')
        elif guess > secret:
            result_label.config(text='Too high, try again.')
        else:
            messagebox.showinfo('Congratulations!', 'You guessed it!')
            root.destroy()

    button = tk.Button(frame, text='Guess', command=check_guess)
    button.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
