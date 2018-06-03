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
        self.transaction_index = 0

        # ジェネシスブロックを作成
        self.create_block('hoge', '00000')

    def create_block(self, nonce, privious_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'previous_hash' : privious_hash,
        }

        # ブロックを追加
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender' : sender,
            'transaction_index' : self.transaction_index,
            'recipient' : recipient,
        })

        self.transaction_index += 1
        return self.transaction_index - 1, len(self.chain)

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

# マイニング処理
def mine(blockchain):
    # 直前のハッシュ値を計算
    previous_hash = calculate_hash(blockchain.chain[-1])
    # マイニング⇒ブロックを新規作成したと一緒
    proof_of_work(blockchain, previous_hash)
    # トランザクションの初期化
    blockchain.current_transactions = []
    blockchain.transaction_index = 0
    # カレントトランザクションにコインベースを追加
    blockchain.create_transaction(sender='0', recipient='my_address', amount=1)
    block = blockchain.chain[-1]

    # 新しいブロックの情報をresponseに代入しています
    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return response

# ブロックチェーンの作成
blockchain = Blockchain()

print(mine(blockchain))
