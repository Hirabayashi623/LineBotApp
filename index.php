<?php

# vendorフォルダ配下のライブラリを自動で読込
require_once __DIR__ . '/vendor/autoload.php';

# CurlHTTPClientのインスタンス化
$httpClient = new \LINE\LINEBot\HTTPClient\CurlHTTPClient(getenv('CHANNEL_ACCESS_TOKEN'));
# LineBotのインスタンス化
$bot = new \LINE\LINEBot($httpClient, ['channelSecret' => getenv('CHANNEL_SECRET')]);

$signature = $_SERVER["HTTP_" . \LINE\LINEBot\Constant\HTTPHeader::LINE_SIGNATURE];
try {
  $events = $bot->parseEventRequest(file_get_contents('php://input'), $signature);
} catch(\LINE\LINEBot\Exception\InvalidSignatureException $e) {
  error_log("parseEventRequest failed. InvalidSignatureException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\UnknownEventTypeException $e) {
  error_log("parseEventRequest failed. UnknownEventTypeException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\UnknownMessageTypeException $e) {
  error_log("parseEventRequest failed. UnknownMessageTypeException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\InvalidEventRequestException $e) {
  error_log("parseEventRequest failed. InvalidEventRequestException => ".var_export($e, true));
}

foreach ($events as $event) {
  if (!($event instanceof \LINE\LINEBot\Event\MessageEvent)) {
    error_log('Non message event has come');
    continue;
  }
  if (!($event instanceof \LINE\LINEBot\Event\MessageEvent\TextMessage)) {
    error_log('Non text message has come');
    continue;
  }
  ############################################
  ### リプライトークンを取得
  ############################################
  $token = $event->getReplyToken();
  ############################################
  ### 受信したテキストを取得
  ############################################
  $recv_text = $event->getText();
  ############################################
  ### bot,replyText：テキストを送信する
  ### 第一引数：リプライトークン（取得から数十秒間しか使えない）
  ### 第二引数：送信するテキスト
  ############################################
  $bot->replyText($token, $recv_text);
}

 ?>