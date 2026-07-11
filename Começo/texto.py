texto = "Esse texto tem uma quebra de linha \nE aqui vai ter uma \ttabulação"
print(texto)

texto = "Aqui VOU Testar CAPTAlize"
print(texto.capitalize())

print(texto.upper())
print(texto.lower())
print(texto.startswith("Aqui"))
print(texto.endswith("Aqui"))
print(texto.count("A"))
print("Testar" in texto)
print(texto.replace("Testar", "utilizar"))