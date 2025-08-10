import utils.functions_options as options
import utils.args_cli as args_cli

# Entrada do usuário e resultado
def main():
    try:
        args = args_cli.configure_arguments()

        if args.url:
            print(f"Analisando URL: {args.url}")
            result = options.verify_url(args.url)
            print(f"Resultado: {result}")
        elif args.filename:
            print(f"Analisando arquivo: {args.filename}")
            file = args.filename
            if args.speed:
                options.speed_verificator(file)
            else:
                options.normal_verificator(file)
    except Exception as e:
        print(f"ERRO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()