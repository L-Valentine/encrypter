from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


class Encrypt:

    def __init__(self, path, password, output_file):
        self.path = path
        self.password = password
        self.output_file = output_file

    def enc_write(self):
        file_writer = PdfFileWriter()
        try:
            file_reader = PdfFileReader(self.path)
        except FileNotFoundError:
            print(f'Encorrect file path: {self.path}')
            sys.exit()

        for page in range(file_reader.numPages):
            file_writer.addPage(file_reader.getPage(page))

        file_writer.encrypt(self.password)

        with open(self.output_file, 'wb') as file:
            file_writer.write(file)

        print(f'[+] Created - {self.output_file}')


example = Encrypt('hello_world.pdf', '12345', 'hw.pdf')
example.enc_write()
