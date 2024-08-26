import os


def clear_config_file():
    file_path = "config.toml"
    config_content = """url = ""\nfilename = ""\nheader = '''\n'''"""

    if os.path.exists(file_path):
        reply = input(
            "The file already exists. Would you like to overwrite it?\n(y/N): "
        )
        if reply.lower() == "y":
            try:
                with open("config.toml", "w") as config_file:
                    config_file.write(config_content + "\n")
            except Exception as e:
                print(e)
            else:
                print("Successfully rewritten config.toml")
        else:
            print("The file was not overwritten.")
    else:
        try:
            with open("config.toml", "a") as config_file:
                config_file.write(config_content + "\n")
        except Exception as e:
            print(e)
        else:
            print("Successfully written config.toml")
