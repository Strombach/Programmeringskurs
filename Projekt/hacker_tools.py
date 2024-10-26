from toolbox import crypto_tool

class Args:
    def __init__(self):
        self.file = "README.md"
        self.decryptkey = None
        self.newkey = True
        self.encrypt = True
        self.key = None

test = Args()

crypto_tool.crypto_tool(test)
