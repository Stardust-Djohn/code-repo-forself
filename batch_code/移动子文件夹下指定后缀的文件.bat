for /f "tokens=* delims=" %%i in ('dir /b /a-d /s "*.$ls"') do (move "%%i" "%%~dpi./../")

pause