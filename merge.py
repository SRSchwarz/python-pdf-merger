import os
import glob
from pathlib import Path
from PyPDF2 import PdfFileMerger

def main():
    "merge pdfs in alphabetic/numerical order"
    fi = Path("result.pdf")
    if fi.is_file():
        os.remove(fi)

    pdfs = glob.glob("*.pdf")
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    with open('./result.pdf', 'wb') as fout:
        merger.write(fout)

if __name__ == '__main__':
    main()
