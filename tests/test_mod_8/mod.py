def init():
    import sh_mod_loader.mod_loader

    class MyMod(sh_mod_loader.mod_loader.Mod):
        def __init__(self):
            super().__init__()

        def on_load(self, *args):
            print("on_load called successfully!")

    my_mod = MyMod()
    my_mod.name = "my_mod"
    return my_mod
