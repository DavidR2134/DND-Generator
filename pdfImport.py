from PyPDF2 import PdfReader

reader = PdfReader('Xanathar.pdf')

print(len(reader.pages))


for i in range(193-175):
    page = reader.pages[i+175]
    text = page.extract_text()
    with open('names.txt', 'a') as f:
        f.write(text)