import hashlib
import requests


def check_pswd(pswd):

    hash = hashlib.sha1(pswd.encode("utf-8")).hexdigest().upper()
    prefix, suffix = hash[:5], hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Błąd API.")
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0


if __name__ == "__main__":
    pswd = input("Podaj hasło do sprawdzenia: ")
    result = check_pswd(pswd)
    if result:
        print(f"[X] Twoje hasło pojawiło się w wyciekach {result} razy! Zmień je.")
    else:
        print("[V] Wygląda na to, że Twoje hasło nie pojawiło się w znanych wyciekach.")

