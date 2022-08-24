import PyPDF2, os

# PDF (portable document format)

os.chdir(os.path.dirname(__file__))
file = open('encrypted.pdf', 'rb')
file2 = open('watermark.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)
reader2 = PyPDF2.PdfFileReader(file2)
print(reader.isEncrypted)
reader.decrypt('rosebud')
print(reader.numPages, '\n')

coverPage = reader.getPage(0)
waterPage = reader2.getPage(0)
coverPage.mergePage(waterPage)

page = reader.getPage(1)
page.rotateClockwise(180)
print(coverPage.extractText())

writer = PyPDF2.PdfFileWriter()
writer.addPage(coverPage)
writer.addPage(page)
for pages in range(2, reader.numPages):
    p = reader.getPage(pages)
    writer.addPage(p)

writer.encrypt('asdf')
output = open('encryptednew.pdf', 'wb')
writer.write(output)

file.close()
file2.close()
output.close()