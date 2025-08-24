def init():
    import sh_mod_loader.mod_loader

    class MyMod(sh_mod_loader.mod_loader.Mod):
        def __init__(self):
            super().__init__()

    my_mod = MyMod()
    my_mod.name = "my_mod"
    my_mod.requires_packages = ["non_existent_package"]
    return my_mod
