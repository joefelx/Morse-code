import pyfiglet
morse_constant = ["•", "-"]

alphabets = {
    "A": f"{morse_constant[0]}{morse_constant[1]}",
    "B": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    "C": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[1]}{morse_constant[0]}",
    "D": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}",
    "E": f"{morse_constant[0]}",
    "F": f"{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}{morse_constant[0]}",
    "G": f"{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}",
    "H": f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    "I": f"{morse_constant[0]}{morse_constant[0]}",
    "J": f"{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}",
    "K": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[1]}",
    "L": f"{morse_constant[0]}{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}",
    "M": f"{morse_constant[1]}{morse_constant[1]}",
    "N": f"{morse_constant[1]}{morse_constant[0]}",
    "O": f"{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}",
    "P": f"{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}",
    "Q": f"{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}{morse_constant[1]}",
    "R": f"{morse_constant[0]}{morse_constant[1]}{morse_constant[0]}",
    "S": f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    "T": f"{morse_constant[1]}",
    "U": f"{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}",
    "V": f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}",
    "W": f"{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}",
    "X": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}",
    "Y": f"{morse_constant[1]}{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}",
    "Z": f"{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}",
}

numbers={
    1: f"{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}",
    2: f"{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}",
    3: f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}{morse_constant[1]}",
    4: f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[1]}",
    5: f"{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    6: f"{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    7: f"{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}{morse_constant[0]}",
    8: f"{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}{morse_constant[0]}",
    9: f"{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[0]}",
    0: f"{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}{morse_constant[1]}",
}

morse_text = pyfiglet.figlet_format("MORSE CODE")
print(morse_text)
input_text = input("Enter a text to Convert in Morse Code: ").upper()

morse_code = ""

for text in input_text:
    if text == " ":
        morse_code += " "
    else:
        morse_code += f"{alphabets[text]} "

print(f"You text {input_text} is converted into {morse_code}")
