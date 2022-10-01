from sys import stdout

class MemeError:
    ...

class Meme:
    def __init__(self, text=None):
        self.text = None
        self.res = None
    def with_text(self, text):
        """
        Init with text.
        """
        self.text = text
    def with_open(self, dir):
        """
        Init with file by open it automatically.
        """
        with open(dir, 'r') as f:
            self.text = f.read()
    def with_file(self, f):
        """
        Init with file handler.
        """
        self.text = f.read()
    
    def show(self):
        """
        Get the result as string or None.
        """
        return self.res

    def print(self, f=None):
        if self.res is None:
            return
        if f is None:
            f = stdout
        print(self.res, file=f)

class MemeGenerator(Meme):
    def trans(self, trans_tbl=None):
        """
        Replace all trans_tbl keys with their values. By default,
        
        ```
        trans_tbl = {
            "{": "{{",
            "}": "}}",
        }
        ```

        You should include the above rules if you want to customize.
        """
        if self.text is None:
            raise MemeError()
        if trans_tbl is None:
            trans_tbl = {
                "{": "{{",
                "}": "}}",
            }
        res = self.text
        for k, v in trans_tbl.items():
            res = res.replace(k, v)
        self.res = res

class MemeInterpreter(Meme):
    def format(self, **kwargs):
        """
        Format with arguments.
        """
        if self.text is None:
            raise MemeError()
        self.res = self.text.format(**kwargs)
