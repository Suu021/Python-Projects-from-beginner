def decodeMorse(morse_code):
    MORSE_CODE = {".-": "A",
                  "-...": "B",
                  "-.-.": "C",
                  "-..": "D",
                  ".": "E",
                  "..-.": "F",
                  "--.": "G",
                  "....": "H",
                  "..": "I",
                  ".---": "J",
                  "-.-": "K",
                  ".-..": "L",
                  "--": "M",
                  "-.": "N",
                  "---": "O",
                  ".--.": "P",
                  "--.-": "Q",
                  ".-.": "R",
                  "...": "S",
                  "–": "T",
                  "..-": "U",
                  "...-": "V",
                  ".--": "W",
                  "-..-": "X",
                  "-.--": "Y",
                  "--..": "Z",
                  "...---...": "SOS",
                  "-----": "0",
                  "·----": "1",
                  "··---": "2",
                  "···--": "3",
                  "····-": "4",
                  "·····": "5",
                  "-····": "6",
                  "--···": "7",
                  "---··": "8",
                  "----·": "9",
                  "--··--": ",",
                  "··--··": "?",
                  "·----·": "'",
                  "-··-·": "/",
                  "-·--·": "(",
                  "-·--·-": ")",
                  "·-···": "&",
                  "---···": ":",
                  "-·-·-·": ";",
                  "-···-": "=",
                  "-····-": "-",
                  "··--·-": "_",
                  '·-··-·': '"',
                  "···-··-": "$",
                  "·--·-·": "@",
                  "-.-.--": "!",
                  ".-.-.-": ".",
                  "": " "
                  }

    code_morse = morse_code.strip()
    code_morse = code_morse.replace("  ", " ")
    letter = code_morse.split(" ")
    for k, v in enumerate(letter):
        translation = v.replace(v, MORSE_CODE[v])
        letter[k] = translation
    phrase = ''.join(letter)
    return phrase


from re import match

print("=-=" * 10)
print(f"{'MORSE DECODER':^30}")
print("=-=" * 10)

while True:
    morseC = input('enter the morse code you want to decode: ')
    while not match(r'^[\s.-]+$', morseC):
        print(f"Invalid input! It must have only dots, dashs and spaces. Please, try again.")
        morseC = input('enter the morse code you want to decode: ')
    d_morse = decodeMorse(morseC)
    if d_morse == " ":
        d_morse = "None"
    print(f'The decoding of "{morseC}" is: {d_morse}')
    print("---" * 10)
    option = input("Would you like to continue? [Y/N] ")
    if option.upper() == "N":
        print("check back often!")
        break
