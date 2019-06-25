import slate
pdf_file = open('./race_charts/BEL2019061901.pdf','rb')
with open('example.pdf') as f:
    doc = slate.PDF(f)
print(doc)