import sh_mod_loader.mod_loader


class MyMod(sh_mod_loader.mod_loader.Mod):
    def __init__(self):
        super().__init__()


def init():
    my_mod = MyMod()
    my_mod.name = "my_mod"
    my_mod.requires_mods = ["test_dependency"]
    return my_mod
