import hashlib
from Block import Block as block


class Ledger:
    def __init__(self):
        self.block_object = None
        self.ledger_array = []
        self.obj = block("Initial Block")
        self.obj.PreHash = "0"
        self.sha256 = hashlib.sha256()
        self.ed_str = self.obj.PreHash + self.obj.Data
        self.sha256.update(self.ed_str.encode("ascii"))
        self.obj.Hash = self.sha256.hexdigest()
        self.ledger_array.append(self.obj)

    def AddBlock(self, block_object):
        block_obj = block_object
        block_obj.PreHash = self.ledger_array[-1].Hash
        ed_str = block_obj.PreHash + block_obj.Data
        sha256 = hashlib.sha256()
        sha256.update(ed_str.encode("ascii"))
        block_obj.Hash = sha256.hexdigest()
        self.ledger_array.append(block_obj)


