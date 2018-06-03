import http.server

# サーバを起動するスクリプトファイル

# 第1引数→IPアドレスを指定
# 第2引数→ポートを指定
server_address = ("", 8082)

#1 ハンドラを設定
handler_class = http.server.CGIHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler_class)

# サーバの起動
server.serve_forever()