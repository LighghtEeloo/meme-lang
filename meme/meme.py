class Meme:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.template = "".join(f.readlines())

    def print(self, **kwargs):
        return self.template.format(**kwargs)
