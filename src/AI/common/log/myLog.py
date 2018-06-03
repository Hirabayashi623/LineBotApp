import logging

def getLogger():
    # loggerオブジェクトの生成
    logger = logging.getLogger('LoggerTest')

    # ログの出力レベルの設定
    logger.setLevel(logging.DEBUG)

    # ログの出力先をファイルに設定
    fileHandler = logging.FileHandler('D:/eclipse/workspace/Python/src/AI/common/log/test.log')
    logger.addHandler(fileHandler)

    # ログの出力先をコンソールに設定
    streamHandler = logging.StreamHandler()
    logger.addHandler(streamHandler)

    # ログの出力形式の設定
    formatter = logging.Formatter('%(asctime)s:%(module)s:%(funcName)s:%(lineno)d【%(levelname)s】%(message)s')
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    return logger