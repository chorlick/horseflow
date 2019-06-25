import camelot

tables = camelot.read_pdf("./race_charts/BEL2019061901.pdf",flavor="stream")
print(tables[0].df[5:10])