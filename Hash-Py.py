import hashlib
from colorama import Fore, Style
import time

GLOBAL_CRYPT_STRING = b"Password" #Input your password you want hashed in plaintext here


print(Fore.RED, "\nThe default password that will hashed is " + Style.BRIGHT + "Password. " + Style.NORMAL + "To change this, edit the GLOBAL_CRYPT_STRING variable", Fore.GREEN)

wait = 5
wait2 = 1
loading = Fore.WHITE + "[" + Fore.LIGHTBLUE_EX + "*" + Fore.WHITE + "]"
success = Fore.WHITE + "[" + Fore.GREEN + "+"  + Fore.WHITE + "]"
hashingLogo = """
  _    __       ___           _______. __    __         .______   ____    ____ 
|  |  |  |     /   \         /       ||  |  |  |        |   _  \  \   \  /   / 
|  |__|  |    /  ^  \       |   (----`|  |__|  |  ______|  |_)  |  \   \/   /  
|   __   |   /  /_\  \       \   \    |   __   | |______|   ___/    \_    _/   
|  |  |  |  /  _____  \  .----)   |   |  |  |  |        |  |          |  |     
|__|  |__| /__/     \__\ |_______/    |__|  |__|        | _|          |__|     
"""
print(hashingLogo, Fore.WHITE)
print(Fore.LIGHTMAGENTA_EX + "I convert your plaintext string into MD5, SHA224, SHA384,and SHA256\n", Fore.WHITE)
time.sleep(wait)
print(Fore.RED, f"Hashing your string {GLOBAL_CRYPT_STRING}",Fore.WHITE)
time.sleep(wait2)

def md5():
    md5_crypt = hashlib.md5()
    GLOBAL_CRYPT_STRING
    print("Your password hash using MD5: ")
    finalMD5 = md5_crypt.hexdigest()
    print(Fore.YELLOW, finalMD5, "\n", Fore.GREEN, Fore.LIGHTBLUE_EX + "Hash block size = " + str(md5_crypt.block_size), Fore.BLUE + "Hash digest size = " + str(md5_crypt.digest_size),Fore.WHITE, "\n")
   
def sha224():
    sha224_crypt = hashlib.sha224()
    GLOBAL_CRYPT_STRING
    print("Your password hash using SHA224: ")
    sha224_final = sha224_crypt.hexdigest()
    print(Fore.YELLOW, sha224_final, "\n", Fore.GREEN, Fore.LIGHTBLUE_EX + "Hash block size = " + str(sha224_crypt.block_size), Fore.BLUE + "Hash digest size = " + str(sha224_crypt.digest_size),Fore.WHITE, "\n")

def sha384():
    sha384_crypt = hashlib.sha384()
    print("Your password hash using SHA384: ")
    sha384_final = sha384_crypt.hexdigest()
    print(Fore.YELLOW, sha384_final, "\n", Fore.GREEN, Fore.LIGHTBLUE_EX + "Hash block size = " + str(sha384_crypt.block_size), Fore.BLUE + "Hash digest size = " + str(sha384_crypt.digest_size),Fore.WHITE, "\n")


def sha256():
    sha256_crypt = hashlib.sha256()
    GLOBAL_CRYPT_STRING
    print("Your password hash using SHA256: ")
    sha256_final = sha256_crypt.hexdigest()
    print(Fore.YELLOW, sha256_final, "\n", Fore.GREEN, Fore.LIGHTBLUE_EX + "Hash block size = " + str(sha256_crypt.block_size), Fore.BLUE + "Hash digest size = " + str(sha256_crypt.digest_size),Fore.WHITE, "\n")

time.sleep(wait2)
print(loading + "Starting hashing process\n")
md5()
time.sleep(wait2)
sha224()
time.sleep(wait2)
sha384()
time.sleep(wait2)
sha256()
print(loading + " Cleaning up...")
time.sleep(wait2)
print(success + " Thanks for using this script!")
time.sleep(wait)

