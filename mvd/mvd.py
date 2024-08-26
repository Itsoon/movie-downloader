import toml
import argparse

from .config_file import clear_config_file

# from mvd import run_cmd


def main():

    parser = argparse.ArgumentParser(description="MVD by Itsoon")
    parser.add_argument("url", nargs="?", help="url")
    parser.add_argument(
        "--clear-config", "-cc", action="store_true", help="Clear config file"
    )
    parser.add_argument("--output", "-O", type=str, help="Output file")
    parser.add_argument("--header", "-H", type=str, help="Header")

    args = parser.parse_args()

    if args.clear_config:
        clear_config_file()
        exit()

    with open("config.toml", "r") as file:
        config = toml.load(file)

    url = config["url"]

    filename = config["filename"]
    filename = filename.replace(" ", "_")

    header = config["header"]
    if not url or not filename or not header:
        if not args.output or not args.header or not args.url:
            print("shit")
            exit()
        else:
            url = args.url
            filename = args.output
            header = args.header

    url = url.replace(" ", "").strip()
    filename = filename.replace(" ", "").strip()
    header = header.split("\n")

    table = []

    table.append(f"wget -O {filename} \\")

    for i in header:
        if len(i) > 1:
            if i.startswith("Range: bytes="):
                table.append("--header='Range: bytes=0-' \\")
                continue
            elif i.startswith("If-Range:") or i.startswith("GET"):
                continue
            else:
                table.append(f"--header='{i}' \\")

    def CheckRange():
        for t in table:
            if t.startswith("--header='Range: bytes=") or t.startswith(
                '--header="Range: bytes='
            ):
                return True
        return False

    if not CheckRange():
        table.append("--header='Range: bytes=0-' \\")

    table.append(f'"{url}"')

    for i in table:
        print(i)
