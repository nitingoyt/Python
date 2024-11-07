import PyPDF2

merge = PyPDF2.PdfMerger()

# Append PDF files
merge.append('MCA2020-onwards-sallybus toc - Copy.pdf')
merge.append('MCA2020-onwards-sallybus toc.pdf')

# Write to a new PDF file
with open('merged.pdf', 'wb') as file:
    merge.write(file)

print("PDFs merged successfully.")


def merge_pdfs(pdf_list, output_pdf_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    with open(output_pdf_path, 'wb') as output_file:
        merger.write(output_file)

pdf_list = ['MCA2020-onwards-sallybus toc - Copy.pdf', 'MCA2020-onwards-sallybus toc.pdf']
merge_pdfs(pdf_list, 'merged1.pdf')
print("PDFs merged into merged1.pdf.")