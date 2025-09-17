import hashlib
import requests


pswd = input("Podaj hasło do sprawdzenia: ")
hash = hashlib.sha1(pswd.encode("utf-8")).hexdigest().upper()
prefix = hash[:5]
suffix = hash[5:]


url = f"https://api.pwnedpasswords.com/range/{prefix}"
response = requests.get(url)


if suffix in response.text:
    print("X To hasło wyciekło! Zmień je.")

else:
    print("V Wygląda na bezpieczne.")








