import sys
from functions import decrypt_file, encrypt_file


def process_args(args: list[str]) -> dict[str, str]:
    options = {
        "filepath": args[0]
    }

    for i, arg in enumerate(args[1:]):
        if arg == "-p" or arg == "--password":
            if "password" not in options:
                if i + 2 >= len(args):
                    print("-p | --password usage: [-p | --password] <password>",
                          file=sys.stderr)
                else:
                    options["password"] = args[i+2]
            else:
                print("-p | --password: more then one time as argument!!!",
                      file=sys.stderr)
        elif arg == "-d" or arg == "--decode":
            if "mode" not in options:
                options["mode"] = "decode"
            else:
                print(f"-d | --decode | -e | --encode usage: more then one time as argument!!! {options['mode']} is used",
                      file=sys.stderr)
        elif arg == "-e" or arg == "--encode":
            if "mode" not in options:
                options["mode"] = "encode"
            else:
                print(f"-d | --decode | -e | --encode: more then one time as argument!!! {options['mode']} is used",
                      file=sys.stderr)
        elif arg == "-o" or arg == "--output":
            if "output" not in options:
                if i + 2 >= len(args):
                    print("-o | --output usage: [-o | --output] <password>",
                          file=sys.stderr)
                else:
                    options["output"] = args[i+2]
            else:
                print("-o | --output: more then one time as argument!!!",
                      file=sys.stderr)

    return options


def get_password():
    return input("With what password do you want to encrypt the file? ")


def get_mode():
    mode = input("""Which mode do you want to use?
                 Encrypt (e | encrypt | encode)
                 Decrypt (d | decrypt | decode)
                 """).lower()

    if mode == "e" or mode == "encrypt" or mode == "encode":
        return "encode"
    elif mode == "d" or mode == "decrypt" or mode == "decode":
        return "decode"
    else:
        print(f"cannot associate {mode} to a mode",
              file=sys.stderr)
        exit()


def main(argv: list[str]):
    if len(argv) < 2:
        print(f"usage: python {argv[0]} <filepath> [options]", file=sys.stderr)
        return

    options = process_args(argv[1:])

    filepath = options["filepath"]

    password = options.get("password")

    mode = options.get("mode")

    if password == None:
        password = get_password()

    if mode == None:
        mode = get_mode()

    if mode == "encode":
        print(f"encrypting {filepath} with password {password}")
        encrypt_file(filepath, password, options.get("output"))
    elif mode == "decode":
        print(f"decrypting {filepath} with password {password}")
        decrypt_file(filepath, password, options.get("output"))
    else:
        print(f"cannot find this option as mode: {mode}", file=sys.stderr)


if __name__ == "__main__":
    argv = sys.argv
    main(argv)
