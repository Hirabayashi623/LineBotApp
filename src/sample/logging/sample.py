import logging

# loggingのデフォルト設定はWARNING

print('【loggingを使用したログ出力】')
# logメソッドはログレベルと、メッセージを指定する
logging.log(0, 'notenst')
logging.log(10, 'debug')
logging.log(20, 'info')
logging.log(30, 'warning')
logging.log(40, 'error')
logging.log(50, 'critical')

# 各ログレベルのメソッドも準備されている
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')


# loggerオブジェクトの生成
logger = logging.getLogger('LoggerTest')

# ログの出力レベルの設定
logger.setLevel(logging.DEBUG)

# ログの出力先をファイルに設定
fileHandler = logging.FileHandler('test.log')
logger.addHandler(fileHandler)

# ログの出力先をコンソールに設定
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)

# ログ出力
print('【loggerを使用したログ出力】')
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

# ログの出力形式の設定
formatter = logging.Formatter('asctime: %(asctime)s, filename: %(filename)s, funcName: %(funcName)s, levelname: %(levelname)s, lineno: %(lineno)d, message: %(message)s, module: %(module)s, name: %(name)s, process: %(process)d, thread: %(thread)d')
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# ログ出力
print('【loggerを使用したログ出力※出力形式設定後】')
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
