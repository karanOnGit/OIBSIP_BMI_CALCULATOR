from tkinter import *


def return_value(bmi):
    if 10 <= bmi < 16:
        result_label.config(text=f"BMI Index {bmi:.2f} \nSevere Thinness")
    elif 16 <= bmi < 17:
        result_label.config(text=f"BMI Index {bmi:.2f} \nModerate Thinness")
    elif 17 <= bmi < 18.5:
        result_label.config(text=f"BMI Index {bmi:.2f} \nMild Thinness")
    elif 18.5 <= bmi < 25:
        result_label.config(text=f"BMI Index {bmi:.2f} \nNormal")
    elif 25 <= bmi < 30:
        result_label.config(text=f"BMI Index {bmi:.2f} \nOverweight")
    elif 30 <= bmi < 35:
        result_label.config(text=f"BMI Index {bmi:.2f} \nObese Class I")
    elif 35 <= bmi < 40:
        result_label.config(text=f"BMI Index {bmi:.2f} \nObese Class II")
    elif 40 <= bmi < 70:
        result_label.config(text=f"BMI Index {bmi:.2f} \nObese Class III")
    else:
        result_label.config(text="Weight Inappropiate")


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if feet_box.get():
            height = height * 0.3048
        else:
            height = height / 100

        bmi = weight / (height**2)
        return_value(bmi)
    except ZeroDivisionError:
        result_label.config(text="Zero is non-divisible integer")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


def update_height_label(*args):
    if feet_box.get():
        height_label.config(text="Height (feet):")
    else:
        height_label.config(text="Height (cm):")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x330")
    root.title("BMI Calculator")

    main_frame = Frame(root, padx=20, pady=20, bg="#123")
    main_frame.pack(fill=BOTH, expand=True)

    heading_label = Label(
        main_frame,
        text="BMI Calculator",
        font=("Arial", 20, "bold"),
        anchor="w",
        bg="#123",
        fg="#fff",
    )
    heading_label.pack(fill=X, pady=(0, 20))

    weight_frame = Frame(main_frame, height=30, bg="#123")
    weight_frame.pack(fill=X, pady=(0, 10))
    weight_frame.pack_propagate(False)

    weight_label = Label(
        weight_frame,
        text="Weight (kg):",
        font=("Arial", 12, "bold"),
        anchor="w",
        bg="#123",
        fg="#fff",
    )
    weight_label.pack(side=LEFT)

    weight_entry = Entry(
        weight_frame,
        border=3,
        width=12,
        font=("Arial", 10, "bold"),
        bg="#123",
        fg="#fff",
    )
    weight_entry.pack(side=RIGHT, expand=False, fill=BOTH)

    height_frame = Frame(main_frame, bg="#123", height=30)
    height_frame.pack(fill=X, pady=(0, 10))
    height_frame.propagate(False)

    height_label = Label(
        height_frame,
        text="Height (cm):",
        font=("Arial", 12, "bold"),
        anchor="w",
        bg="#123",
        fg="#fff",
    )
    height_label.pack(side=LEFT)

    height_entry = Entry(
        height_frame,
        border=3,
        width=12,
        font=("Arial", 10, "bold"),
        bg="#123",
        fg="#fff",
    )
    height_entry.pack(side=RIGHT, expand=False, fill=BOTH)

    unit_frame = Frame(main_frame, bg="#123")
    unit_frame.pack(fill=X, pady=(0, 10))

    feet_box = BooleanVar()
    feet_check = Checkbutton(
        unit_frame,
        text="Use feet",
        variable=feet_box,
        bg="#123",
        fg="#fff",
        selectcolor="#123",
        activebackground="#123",
        activeforeground="#fff",
    )
    feet_check.pack(side=LEFT)

    feet_box.trace("w", update_height_label)

    submit_button = Button(
        main_frame,
        text="Calculate BMI",
        font=("Arial", 12, "bold"),
        command=calculate_bmi,
        bg="#123",
        fg="#fff",
        cursor="hand2",
    )
    submit_button.pack(pady=(0, 20))

    result_label = Label(
        main_frame, text="", font=("Arial", 14, "bold"), bg="#123", fg="#fff"
    )
    result_label.pack()

    root.resizable(False, False)
    root.mainloop()
