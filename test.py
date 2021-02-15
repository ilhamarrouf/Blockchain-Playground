import unittest
from src.blockchain.main import Blockchain

class BlockchainTestCase(unittest.TestCase):
    def test_blockchain(self):
        blockchain = Blockchain()
        blockchain.add_new_transaction('Testing Dummy Data')
        self.assertEqual(blockchain.mine(), True)
        self.assertEqual(blockchain.chain_valid(blockchain.chain), True)
        self.assertEqual(len(blockchain.chain), 1)

if __name__ == '__main__':
    unittest.main()