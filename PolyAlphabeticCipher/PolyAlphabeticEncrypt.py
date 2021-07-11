
# The rotate function is defined
def rotate(letter, key):
    
    # Checks if letter is in lowercsae
  if letter.islower():
      
    #   Shifting of each character is carried out
    shift = ord(key) - ord('a')
    new = ord(letter) + shift
    
    # Checks if the letter has gone past z
    if new > ord('z'):
      new = new - 26
    # Checks if the letter hasn't gone past a
    elif new < ord('a'):
      new = new + 26
    new = chr(new)
    # If everything is fine, the program continues without subtracting or adding 26 to compensate
  else:
    new = letter
    
    if letter.isupper():
          new = ord(letter) + key
          if new > ord('Z'):
                new = new - 26
          new = chr(new)
    else:
          new = letter
  return new

encrypted = ""
counter = 0

# Runs until i is not in the range of len(plaintext)
def polyPrint(message, key):
  encrypted = ""
  counter = 0
  for i in range(len(message)):
    letter = message[i]
    if letter.islower():
      subkey = key[counter % len(key)]
      encrypted = encrypted + rotate(letter, subkey)
      counter += 1
    else:
      encrypted = encrypted + letter
  return encrypted

  # Final value is returned
  # print("Encrypted with '" + key + "':")
  # print(encrypted)    