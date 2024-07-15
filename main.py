import pyshorteners

long_url = input("Informe o link a ser encurtado: ")

type_tiny = pyshorteners.Shortener()

short_link = type_tiny.tinyurl.short(long_url)

print("Seu link encurtado é:" + short_link)