# 前回までの実装内容をここで読み込んでいます
import json
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0

        # ジェネシスブロックを作成してください
        self.create_block('hoge', '00000')

        # トランザクションとトランザクションのindexを初期化してください
        self.current_transactions = []
        self.transaction_index = 0


    # ジェネシスブロックを作成する関数を完成させてください
    def create_block(self, nonce, previous_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'previous_hash' : previous_hash,
        }
        # ブロックの追加をします
        self.chain.append(block)
        return block


# 以下の関数を完成させてください
def calculate_hash(block):
    tmp = json.dumps(block)
    return hashlib.sha256(tmp.encode()).hexdigest()

blockchain = Blockchain()
# blockにはジェネシスブロックを渡しています
block = blockchain.chain[0]
hash_value = calculate_hash(block)
print(hash_value)

