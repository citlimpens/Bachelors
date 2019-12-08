#Quitar los nombres a la secuencia 
#Hacer el inverso complementario
FileName = "seqs_matk.txt"
def leerfasta(FileName):
	objeto = open(FileName, 'r')
	secuencias = []
	fragmentos = []
	for line in objeto:
		if line.startswith('>'):
			if fragmentos:
				secuencia = ' '.join(fragmentos)
				secuencias.append(secuencia)
				fragmentos = []
		else:
			seq = line.rstrip()
			fragmentos.append(seq)
	if fragmentos:
		secuencia = ' '.join(fragmentos)
		secuencias.append(secuencia)
	objeto.close()
	return secuencias

x = leerfasta(FileName) 
print(x)

def inverso(): 
	complementario = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	for linea in secuencias:
		print(key)
inverso()