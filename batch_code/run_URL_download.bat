rem-nojvm ����JAVA�����
rem-nosplash ��������(splash windows)����

start C:\"Program Files"\MATLAB\R2020b\bin\matlab.exe -nosplash -r "run('URL_download.m')"

rem  60 seconds later kill Matlab

@ping -n 30 127.1 >nul 2>nul

taskkill/im matlab.exe