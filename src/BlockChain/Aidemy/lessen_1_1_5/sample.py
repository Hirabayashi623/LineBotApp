class Blockchain:
    def __init__(self):
        # ここに初期値を定義してください
        self.chain = []                     # ブロックチェーンを保存する
        self.current_transactions = []      # ブロックごとのトランザクションを保存
        self.transaction_index = 0          # 現在のブロックにおける何番目のトランザクションかを保存する

    # マイニングにより新しいブロックを作成する
    def create_block(self, nonce, previous_hash):
        pass

    # トランザクション(取引情報)をブロックに追加する
    def create_transaction(self, sender, recipient, amount):
        pass

    # 現在のチェーンを確認する
    def create_node(self, node):
        pass

    # チェーンが正しいかどうか検証する
    def valid_chain(self, chain):
        pass

    # コンセンサスアルゴリズムによりブロックを承認する
    def resolve_conflicts(self, block_list):
        pass


blockchain = Blockchain()
blockchain.chain