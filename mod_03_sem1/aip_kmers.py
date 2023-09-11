aip_kmers = open("newlines.txt",'w')
kmer1 = "ATGCNA"
kmer2 = "AAGCNC"
# Append newline when using write
aip_kmers.write(kmer1 + "\n")
aip_kmers.write(kmer2 + "\n")
# Appending newline not needed when using print
print(kmer1)
aip_kmers.close()
