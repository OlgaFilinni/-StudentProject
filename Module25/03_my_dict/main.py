class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)
