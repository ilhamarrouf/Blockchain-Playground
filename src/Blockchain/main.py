import json
import time
from hashlib import sha256

class Block:
    def __init__(self, index, transaction, timestamp, previous_hash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previous_hash =  previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block).hexdigest()

class Blockchain:
    difficulty = 2

    def __init__(self):
        self.new_transactions = []
        self.chain = []

    def create_genesis_block(self):
        genesis_block = Block(0, 'first block of the chain', time.time(), '0')
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def last_block(self):
        return self.chain[-1]

    def add_new_transaction(self, transaction):
        self.new_transactions.append(transaction)