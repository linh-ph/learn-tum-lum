<?php
// Install the library via Composer: composer require google/cloud-text-to-speech
require_once __DIR__ . '/vendor/autoload.php';

use Google\Cloud\TextToSpeech\V1\AudioConfig;
use Google\Cloud\TextToSpeech\V1\AudioEncoding;
use Google\Cloud\TextToSpeech\V1\SsmlVoiceGender;
use Google\Cloud\TextToSpeech\V1\TextToSpeechClient;
use Google\Cloud\TextToSpeech\V1\VoiceSelectionParams;

// Your Google Cloud Platform project ID
$projectId = 'YOUR_PROJECT_ID';

// Instantiates a client
$client = new TextToSpeechClient([
    'projectId' => $projectId,
]);

// Set the text input to be synthesized
$text = 'Hello, world!';

// Build the voice request
$voice = (new VoiceSelectionParams())
    ->setLanguageCode('en-US')
    ->setSsmlGender(SsmlVoiceGender::FEMALE);

// Build the audio configuration request
$audioConfig = (new AudioConfig())
    ->setAudioEncoding(AudioEncoding::MP3);

// Perform the text-to-speech request
$response = $client->synthesizeSpeech($text, $voice, $audioConfig);
$audioContent = $response->getAudioContent();

// The audio content in MP3 format
header('Content-Type: audio/mpeg');
header('Content-Disposition: attachment; filename="output.mp3"');
header('Content-Length: ' . strlen($audioContent));
print($audioContent);

$client->close();
// You will also need to have the Google Cloud SDK installed 
// and authenticated in order to use this code.
