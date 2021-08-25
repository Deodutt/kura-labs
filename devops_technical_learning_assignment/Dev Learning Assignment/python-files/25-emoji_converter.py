msg = input(">")
words = msg.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😢",
    "8)": "😎",
    ">.>": "😒",
    ":D": "😂",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
