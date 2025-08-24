import sh_mod_loader.mod_loader


import relative_import


class MyMod(sh_mod_loader.mod_loader.Mod):
    def __init__(self):
        super().__init__()

    def on_load(self, *args):
        print("on_load called successfully!")


mod = MyMod()
mod.name = "my_mod"
