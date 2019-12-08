import os

from Bio import SeqIO
from Bio import Entrez
Entrez.email = "cit3014@hotmail.com"
filename = "secuencias.fasta"
if not os.path.isfile(filename):
	net_handle = Entrez.efetch(db="nuccore",id = lista, rettype="fasta", retmode="text")
    out_handle = open(filename, "w")
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print("Saved")

from Bio.Align.Applications import ClustalwCommandline
clustalw_exe = r"/Users/Cit/anaconda/clustalw2"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="secuencias.fasta")
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()

from Bio import AlignIO
align = AlignIO.read("secuencias.aln", "clustal")
print(align)