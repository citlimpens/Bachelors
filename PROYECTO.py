Variables = ["S", "I"]
VariablesOriginales = ["S", "I"]
Parametros = ["gamma", "beta"]
ParametrosOriginales = ["gamma", "beta"]

def insercionvariables():
	MasVariables = input("Las variables obligatorias son S e I, ¿Desea agregar otra variable? (S/N) ")
	if MasVariables == "S":
		Variable1 = input("¿Desea agregar la variable R? (S/N) ")
		if Variable1 == "S":
			Variables.append("R")
			print("Tus variables son: ", Variables)
			Variable2 = input("Desea agregar la variable E? (S/N) ")
			if Variable2 == "S":
				Variables.append("E")
				print("Tus variables son: ", Variables)
		else:
			print("Tus variables son: ", Variables)
	else:
		print("Tus variables son: ", Variables)
				

insercionvariables()



def insercionparametros():
	MasParametros = input("Los parámetros obligatorios son gamma y beta, ¿Deseas que tu modelo sea con demografía? (S/N) ")
	if MasParametros == "S":
		Parametros.append("alpha")
		Parametros.append("miu")
		print("Tus parámetros son: ", Parametros)
		Parametro1 = input("¿Desea agregar muerte por la enfermedad? (S/N) ")
		if Parametro1 == "S":
			Parametros.append("u")
			print("tus parámetros son: ", Parametros)

	else:
		print("Tus parámetros son: ", Parametros)

	ParametroSus = input("¿Desea que los individuos vuelvan a estado de susceptibilidad? (S/N)")
	if ParametroSus == "S":
		Parametros.append("delta")
		print("Tus parámetros son: ", Parametros)

insercionparametros()

def ecuaciones():
	beta = "beta"
	gamma = "gamma"
	alpha = "alpha"
	miu = "miu"
	u = "u"
	S = "S"
	I = "I"
	R = "R"
	E = "E"

	if Variables == VariablesOriginales:
		if Parametros == ParametrosOriginales:
			print("Es un modelo SI, sin demografía)
			SIsS = beta 
			SIsI = ""		
		elif "u" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SIS con demografía y muerte por la enfermedad")
				SISdmS = ""
				SISdmI = ""
			else:
				print("Es un modelo SI con demografía y muerte por la enfermedad")
				SIdmS = ""
				SIdmI = ""
		elif "alpha" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SIS con demografía")
				SISdS = ""
				SISdI = ""
			else:
				print("Es un modelo SI con demografía")
				SIdS = ""
				SIdI = ""
		elif "delta" in Parametros:
			print("Es un modelo SIS sin demografía")
			SISsS = ""
			SISsI = ""
	elif "E" in Variables: 
		if Parametros == ParametrosOriginales:
			print("Es un modelo SEIR, sin demografía")
			SEIRsS = ""
			SEIRsI = ""
			SEIRsE = ""
			SEIRsR = ""
		elif "u" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SEIRS con demografía y muerte por la enfermedad")
				SEIRSdmS = ""
				SEIRSdmI = ""
				SEIRSdmE = ""
				SEIRSdmR = ""
			else:
				print("Es un modelo SEIR con demografía y muete por la enfermedad")
				SEIRdmS = ""
				SEIRdmI = ""
				SEIRdmE = ""
				SEIRdmR = ""
		elif "alpha" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SEIRS con demografía")
				SEIRdS = ""
				SEIRdI = ""
				SEIRdE = ""
				SEIRd R = ""
			else:
				print("Es un modelo SEIR con demografía")
		elif "delta" in Parametros:
			print("Es un modelo SEIRS sin demografía")
	elif "R" in Variables: 
		if Parametros == ParametrosOriginales:
			print("Es un modelo SIR, sin demografía")
		elif "u" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SIRS con demografía y muerte por la enfermedad")
			else:
				print("Es un modelo SIR con demografía y muerte por la enfermedad")
		elif "alpha" in Parametros:
			if "delta" in Parametros:
				print("Es un modelo SIRS con demografía")
			else:
				print("Es un modelo SIR con demografía")
		elif "delta" in Parametros:
			print("Es un modelo SIRS sin demografía")

ecuaciones()






