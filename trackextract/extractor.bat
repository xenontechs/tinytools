@echo off

rem defaults
set AUDIO_EXTENSION=ogg

rem Check if a file path was provided
if "%~1"=="" (
  echo Usage: extractor.bat FILE_PATH
  echo - or drag video file on to this file
  echo expected result: 
  echo - a new folder named after the video file with one audio file per track in the video file
  echo defaults: 
  echo - audio file output extension: %AUDIO_EXTENSION%
  echo limits: 
  echo - number of expected audio tracks: 5
  echo - tested under specific conditions, this script tries one thing only. adapt script if needed
  exit /b 1
)

set "FILE_PATH=%~f1"

rem Create the new folder
set "FOLDER_PATH=%~dpn1"
mkdir "%FOLDER_PATH%"

echo extracting tracks 
echo from: %FILE_PATH%
echo to: %FOLDER_PATH%

ffmpeg -i %FILE_PATH% ^
    -map 0:1 -c copy %FOLDER_PATH%\track1.%AUDIO_EXTENSION% ^
    -map 0:2 -c copy %FOLDER_PATH%\track2.%AUDIO_EXTENSION% ^
    -map 0:3 -c copy %FOLDER_PATH%\track3.%AUDIO_EXTENSION% ^
    -map 0:4 -c copy %FOLDER_PATH%\track4.%AUDIO_EXTENSION% ^
    -map 0:5 -c copy %FOLDER_PATH%\track5.%AUDIO_EXTENSION% 