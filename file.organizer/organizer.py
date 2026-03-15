from pathlib import Path
from datetime import datetime
import shutil

txt = Path("pasta_txt")
txt.mkdir(exist_ok=True)

xlsx = Path("pasta_xlsx")
xlsx.mkdir(exist_ok=True)

docx = Path("pasta_docx")
docx.mkdir(exist_ok=True)

png = Path("pasta_png")
png.mkdir(exist_ok=True)

pdf = Path("pasta_pdf")
pdf.mkdir(exist_ok=True)

jpg = Path("pasta_jpg")
jpg.mkdir(exist_ok=True)

pasta_origem = Path("descompact")

contador = 0
extensoes = set()

log = open("registro.log", "a", encoding="utf-8")

for arquivo in pasta_origem.iterdir():

    if arquivo.is_file():

        contador += 1
        extensoes.add(arquivo.suffix)

        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if arquivo.suffix == ".txt":
            destino = txt / arquivo.name
            shutil.move(arquivo, txt)

        elif arquivo.suffix == ".docx":
            destino = docx / arquivo.name
            shutil.move(arquivo, docx)

        elif arquivo.suffix == ".pdf":
            destino = pdf / arquivo.name
            shutil.move(arquivo, pdf)

        elif arquivo.suffix == ".png":
            destino = png / arquivo.name
            shutil.move(arquivo, png)

        elif arquivo.suffix == ".jpg":
            destino = jpg / arquivo.name
            shutil.move(arquivo, jpg)

        elif arquivo.suffix == ".xlsx":
            destino = xlsx / arquivo.name
            shutil.move(arquivo, xlsx)

        else:
            continue

        log.write(f"{data} | {arquivo.name} -> {destino}\n")

log.close()

print(f"Foram organizados {contador} arquivos")
print("Extensões encontradas:", extensoes)





