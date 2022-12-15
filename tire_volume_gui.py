
import tkinter as tk
import number_entry as nent

from cmath import pi


def main():

    root = tk.Tk()

    frm_main = tk.Frame(root)
    frm_main.master.title("Tire Volume")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)


    populate_main_window(frm_main)


    root.mainloop()
    

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the text fields and the results.
    lbl_width = tk.Label(frm_main, text="Width (mm):")
    lbl_ratio = tk.Label(frm_main, text="Aspect Ratio:")
    lbl_diam = tk.Label(frm_main, text="Diameter(in):")
    lbl_vol = tk.Label(frm_main, text="Volume (liters):")
    
    # Create three text fields.
    ent_width = nent.IntEntry(frm_main, 80, 300, width=5)
    ent_ratio = nent.FloatEntry(frm_main, 30, 90, width=5)
    ent_diam = nent.FloatEntry(frm_main, 10, 30, width=5)

    # Create label that displays results.
    lbl_result = tk.Label(frm_main, width=8, anchor="w")

    # Create the clear button.
    btn_clear = tk.Button(frm_main, text="Clear")


 # Layout all the labels, text fields, and buttons in a grid.
    lbl_width.grid( row=0, column=0, padx=3, pady=2, sticky="e")
    ent_width.grid( row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_ratio.grid( row=1, column=0, padx=3, pady=2, sticky="e")
    ent_ratio.grid( row=1, column=1, padx=3, pady=2, sticky="w")
    lbl_diam.grid(  row=2, column=0, padx=3, pady=2, sticky="e")
    ent_diam.grid(  row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_vol.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
    lbl_result.grid(row=3, column=1, padx=3, pady=2, sticky="w")
    btn_clear.grid( row=3, column=2, padx=3, pady=2)

    def calculate(event):
        try:
            # Get inputs from the user.
            width = ent_width.get()
            asp_ratio = ent_ratio.get()
            diameter = ent_diam.get()

            # Compute the volume of the tire.
            volume = pi * width**2 * asp_ratio * (width * asp_ratio + 2540 * diameter ) / 10000000000

            # Display the results.
            lbl_result.config(text=f"{volume:.1f}")

        except ValueError:
            # When the user deletes all the digits in the volume
            # entry box, clear the labels.
            lbl_result.config(text=f"")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_width.delete(0, tk.END)
        ent_ratio.delete(0, tk.END)
        ent_diam.delete(0, tk.END)
        lbl_result.config(text="")
        ent_width.focus()


    ent_width.bind("<KeyRelease>", calculate)
    ent_ratio.bind("<KeyRelease>", calculate)
    ent_diam.bind("<KeyRelease>", calculate)

    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_width.focus()


if __name__ == "__main__":
    main()