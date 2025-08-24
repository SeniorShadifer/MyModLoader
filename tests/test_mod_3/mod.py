def init():
    import sh_mod_loader.mod_loader

    class MyMod(sh_mod_loader.mod_loader.Mod):
        def __init__(self):
            super().__init__()

    return MyMod()
