morseCode = {"A":".-","B":"-...","C":"-.-."}
morseCode["D"] = "-.."
morseCode["E"] = "."
morseCode["F"] = "..-."
morseCode["G"] = "--."
morseCode["H"] = "...."
morseCode["I"] = ".."
morseCode["J"] = ".---"
morseCode["K"] = "-.-"
morseCode["L"] = ".-.."
morseCode["M"] = "--"
morseCode["N"] = "-."
morseCode["O"] = "---"
morseCode["P"] = ".--."
morseCode["Q"] = "--.-"
morseCode["R"] = ".-."
morseCode["S"] = "..."
morseCode["T"] = "-"
morseCode["U"] = "..-"
morseCode["V"] = "...-"
morseCode["W"] = ".--"
morseCode["X"] = "-..-"
morseCode["Y"] = "-.--"
morseCode["Z"] = "--.."

message = input("key your morse code :").upper()
encodedMessage = ""
FILE=open("morse.txt", 'r+')
FILE.read(encodedMessage)
FILE.close()
for character in message:
    
    if character in morseCode:
       encodedMessage += morseCode[character] + " "
       
    else:
       encodedMessage += " "
