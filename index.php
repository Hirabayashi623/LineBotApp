<?php

# vendor�t�H���_�z���̃��C�u�����������œǍ�
require_once __DIR__ . '/vendor/autoload.php';

# CurlHTTPClient�̃C���X�^���X��
$httpClient = new \LINE\LINEBot\HTTPClient\CurlHTTPClient(getenv('CHANNEL_ACCESS_TOKEN'));
# LineBot�̃C���X�^���X��
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
  ### ���v���C�g�[�N�����擾
  ############################################
  $token = $event->getReplyToken();
  ############################################
  ### ��M�����e�L�X�g���擾
  ############################################
  $recv_text = $event->getText();
  ############################################
  ### bot,replyText�F�e�L�X�g�𑗐M����
  ### �������F���v���C�g�[�N���i�擾���琔�\�b�Ԃ����g���Ȃ��j
  ### �������F���M����e�L�X�g
  ############################################
  $bot->replyText($token, $recv_text);
}

 ?>