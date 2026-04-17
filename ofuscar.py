import marshal, base64

def proteger(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        codigo = f.read()
    
    # Compilar y codificar
    paso1 = compile(codigo, '', 'exec')
    paso2 = marshal.dumps(paso1)
    paso3 = base64.b288_encode(paso2) if hasattr(base64, 'b288_encode') else base64.b64encode(paso2)
    
    with open(nombre_archivo, 'w') as f:
        f.write(f"import marshal, base64;exec(marshal.loads(base64.b64decode({paso3})))")
    print(f"✅ {nombre_archivo} protegido.")

archivos = ['auth.py', 'main.py', 'report.py', 'reporter.py']
for a in archivos:
    try: proteger(a)
    except: print(f"❌ Error en {a}")
