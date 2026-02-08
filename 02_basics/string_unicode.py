# Unicode support — Python 3 strings are Unicode by default
emoji = "Python 🐍 is 🔥"
hindi = "नमस्ते दुनिया"
punjabi = "ਸਤ ਸ੍ਰੀ ਅਕਾਲ"
print("Emoji:", emoji)
print("Hindi:", hindi)
print("Punjabi:", punjabi)
print()

# Length of string (counts characters, not bytes)
print("Length of emoji string:", len(emoji))        # 16 (🐍 and 🔥 are one character each)
print("Length of hindi:", len(hindi))               # 12
print()

# ord() → gives Unicode code point of a character
print("Unicode of 'A':", ord('A'))                  # 65
print("Unicode of '🐍':", ord('🐍'))                # 128013
print("Unicode of 'ਸ':", ord('ਸ'))                  # 2581
print()

# chr() → opposite — character from code point
print("Character from 65:", chr(65))                # A
print("Character from 128013:", chr(128013))        # 🐍
print()
