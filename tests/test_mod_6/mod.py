import sh_mod_loader.mod_loader


class MyMod(sh_mod_loader.mod_loader.Mod):
    def __init__(self):
        super().__init__()


def init():
    my_mod = MyMod()
    my_mod.name = "my_mod"
    my_mod.requires_packages = [
        input("Please input name of any package, installed on your enivrovment: ")
    ]
    return my_mod
