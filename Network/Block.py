# Index
# Timestamp
# Previous Hash
# Hash
# Data


class Block:
    def __init__(self, Data=None):
        self.Data = Data
        self.PreHash = None
        self.Hash = None
        self.Timestamp = None
        self.Nonce = None
