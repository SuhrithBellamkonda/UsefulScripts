"""
This script is intended to clarify the difference between dBi, dBm, and dBV particularly in the context of antennas.

When the script is run, you will see a simple GUI made with Tkinter, where you can choose dBi, dBm, or dBV and input the appropriate value. 
Hit "Calculate", and the dB reading will then be displayed.

There will also be some useful info about these values at the bottom of the display.
""" 
import math
import tkinter as tk

def dbi(gain):
    return 10 * math.log10(gain)

def dbm(power):
    return 10 * math.log10(power / 0.001)

def dbv(voltage):
    return 20 * math.log10(voltage / 1)

def calculate():
    choice = formula_choice.get()
    if choice == 1: # dBi calculation
        gain = float(entry_value.get())
        result = dbi(gain)
        result = round(result, 4)
        label_result.config(text=f"Result: {result} dBi")
    elif choice == 2: # dBm calculation
        power = float(entry_value.get())
        result = dbm(power)
        result = round(result, 4)
        label_result.config(text=f"Result: {result} dBm")
    elif choice == 3: # dBV calculation
        voltage = float(entry_value.get())
        result = dbv(voltage)
        result = round(result, 4)
        label_result.config(text=f"Result: {result} dBV")

def update_label(*args):
    if formula_choice.get() == 1:
        label_value.config(text="Enter Gain:")
        label_formula.config(text="Formula: dBi = 10 * log(Gain)")
    elif formula_choice.get() == 2:
        label_value.config(text="Enter Power (mW):")
        label_formula.config(text="Formula: dBm = 10 * log(Power / 0.001W)")
    else:
        label_value.config(text="Enter Voltage (V):")
        label_formula.config(text="Formula: dBV = 20 * log(Voltage / 1V)")

# Create main window
window = tk.Tk()
window.title("Decibel Calculator")

formula_choice = tk.IntVar()
formula_choice.set(1)
formula_choice.trace_add('write', update_label)

font = ("Verdana", 12)
font2 = ("Verdana", 24)

label_choose = tk.Label(window, font=font, anchor = "w")
label_choose.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

radio_dbi = tk.Radiobutton(window, text="dBi", variable=formula_choice, value=1, font=font)
radio_dbi.grid(row=1, column=0, padx=10, pady=5, sticky="w")

radio_dbm = tk.Radiobutton(window, text="dBm", variable=formula_choice, value=2, font=font)
radio_dbm.grid(row=2, column=0, padx=10, pady=5, sticky="w")

radio_dbv = tk.Radiobutton(window, text="dBV", variable=formula_choice, value=3, font=font)
radio_dbv.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Input and calculation button
label_value = tk.Label(window, text="Enter Gain:", font=font)
label_value.grid(row=1, column=1, padx=10, pady=5)

entry_value = tk.Entry(window)
entry_value.grid(row=2, column=1, padx=10, pady=5)

button_calculate = tk.Button(window, text="Calculate", command=calculate, font=font)
button_calculate.grid(row=3, column=1, padx=10, pady=5)

# Result
label_result = tk.Label(window, text="", font=font2)
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Formula
label_formula = tk.Label(window, text="", font=font)
label_formula.grid(row=6, column=0, columnspan=2, padx=10, pady=1)

label_explanation = tk.Label(window, text="- dBi is a measure of gain relative to a hypothetical isotropic reference antenna (whose gain is 1). Higher dBi values correspond to higher directionality/narrower beamwidth.\n\n"
                                        "- dBm is a measure of power relative to 1mW, and it can be calculated given an output power.\n\n"
                                        "- dBV is a measure of power relative to 1V, and it can be calculated given an output voltage. The reason that the formula has a prefactor of 20 is that power is proportional to voltage squared.",
                             font=font, justify="left", wraplength=300)
label_explanation.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

update_label()
window.mainloop()