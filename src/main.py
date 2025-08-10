#!/usr/bin/env python3
import sys
print("Iniciando...")

try:
    import args_cli
    print("Args importado")
    
    import functions_options
    print("Functions importado")
    
    args = args_cli.configure_arguments()
    print(f"Argumentos: {args}")
    
    if args.url:
        print(f"Processando URL: {args.url}")
        result = functions_options.verify_url(args.url)
        print(f"Resultado: {result}")
        
except Exception as e:
    print(f"ERRO: {e}")
    import traceback
    traceback.print_exc()
