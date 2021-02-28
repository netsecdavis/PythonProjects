from termcolor import colored
import hashlib

def tryOpen(wordlist):
  try:
    pass_file = open(wordlist, "r")
  except:
    print("[!!] File does not exist at specified path!")
    quit()

pass_hash = input("[*] Enter MD5 Hash: ")
wordlist = input("[*] Please specify the path to the password file: ")
tryOpen(wordlist)

for word in pass_file:
  print(colored("[-] Attempting: " + word.strip("\n"), 'red'))
  enc_wrd = word.encode('utf-8')
  md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

  if md5digest == pass_hash:
    print(colored("[+] Password Confirmed: " + word, 'green'))
    exit(0)

print("[!!] Password was not found in specified list.")
