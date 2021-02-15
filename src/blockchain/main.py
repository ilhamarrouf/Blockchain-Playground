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
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, 'first block of the chain', time.time(), '0')
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def last_block(self):
        return self.chain[-1]

    def add_new_transaction(self, transaction):
        self.new_transactions.append(transaction)

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            # validate previous hash is valid or not
            block = chain[block_index]
            if block.previous_hash != previous_block.hash:
                return False

            # validate proof of work
            proof = block.hash
            if not self.is_valid_proof(block, proof):
                return False

            previous_block = block
            block_index += 1

        return True

    @staticmethod
    def is_valid_proof(block, block_hash):
        return block_hash.startswith('0' * Blockchain.difficulty)

    @staticmethod
    def find_proof_of_work(block):
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0', Blockchain.difficulty):
            block.nonce += 1
            computed_hash =  block.compute_hash()

        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block().hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def mine(self):
        if not self.new_transactions:
            return False

        for transaction in self.new_transactions:
            last_block = self.last_block()
            new_block = Block(last_block.index + 1, transaction, time.time(), last_block.hash)
            proof = self.find_proof_of_work(new_block)
            self.add_block(new_block, proof)

        self.new_transactions = []
        return True
