from unicodedata import normalize

def removeAccentsOfString(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')