import json
import hashlib
import time

class Blockchain:
    def __init__(self):
        # ブロックチェーン本体
        self.chain = []
        # ブロック内のトランザクション
        self.current_transactions = []
        # トランザクションのインデックス（何番目のブロック化を表す）
        self.tracsaction_index = 0

        # ジェネシスブロックを作成
        self.create_block('hoge', '00000')

    def create_block(self, nonce, privious_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'privious_hash' : privious_hash,
        }

        # ブロックを追加
        self.chain.append(block)
        return block

# ハッシュ値計算関数
def calculate_hash(block):
    tmp = json.dumps(block)
    return hashlib.sha256(tmp.encode()).hexdigest()

def proof_of_work(blockchain, previous_hash):
    nonce = 0
    while True:
        # ブロックを作成＆ブロックチェーンに追加
        block = blockchain.create_block(nonce, previous_hash)
        # ブロックのハッシュ値を計算
        guess_hash = calculate_hash(block)
        if guess_hash[:4] == '0000':
            break

        # 判定OKでなかった場合、追加した末尾のブロックを削除する
        blockchain.chain.pop()

        nonce += 1
    return block

# ブロックチェーンの作成
blockchain = Blockchain()
# このprevious_hashは適当な値です
block_hash = "e5c87e27a81ee16c491a2ca6fe1eb1310caed25d0fab1ccfa785ffbadafeb96b"
block = proof_of_work(blockchain, block_hash)

print(block)

# このブロックのハッシュ値
current_hash_value = calculate_hash(block)
print(current_hash_value)
