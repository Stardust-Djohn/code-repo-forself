rem-nojvm ½ûÓÃJAVAÐéÄâ»ú
rem-nosplash Æô¶¯ÉÁÆÁ(splash windows)½ûÓÃ

start C:\"Program Files"\MATLAB\R2020b\bin\matlab.exe -nosplash -r "run('URL_download.m')"

rem  60 seconds later kill Matlab

@ping -n 30 127.1 >nul 2>nul

taskkill/im matlab.exe