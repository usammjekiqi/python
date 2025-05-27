class mYclass:
    def __init__(self):
        self._protected_cafiabel = "this is  protected"

    def _protected_method(self):
        print("tis is protected method")


myclass = mYclass()
print(myclass._protected_cafiabel)
print(myclass._protected_method)