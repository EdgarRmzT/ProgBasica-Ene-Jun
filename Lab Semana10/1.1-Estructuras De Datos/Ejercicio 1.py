#Analisis de texto con diccionarios y conjuntos

def analizar_texto(texto):
    pal=texto.lower().split()
    tot_pal=len(pal)
    pal_unicas=set(pal)
    cant_pal_unicas=len(pal_unicas)
    frec_pal={}
    for pal in pal:
        if pal in frec_pal:
            frec_pal[pal]+=1
        else:
            frec_pal[pal]=1
    
    palmas_frec=""
    frec_maxima=0
    for pal, frec in frec_pal.items():
        if frec>frec_maxima:
            palmas_frec=pal
            frec_maxima=frec

    print("Número total de palabras:", tot_pal)
    print("Cantidad de palabras únicas:", cant_pal_unicas)
    print("Frecuencia de cada palabra:", frec_pal)
    print("Palabra más frecuente:", palmas_frec, "con", frec_maxima, "apariciones")

texto = input("Ingresa un texto: ")
analizar_texto(texto)