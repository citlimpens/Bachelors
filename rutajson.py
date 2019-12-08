import json
ruta = 'usagov_bitly_data2012-03-16-1331923249.txt'
registros = [json.loads(linea) for linea in open(ruta)]
print(len(registros))
registros[0]
