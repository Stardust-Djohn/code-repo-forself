@echo off
setlocal enabledelayedexpansion
echo Now is changing perfix, please wait...
for /f "delims=" %%i in ('dir /b "*CNKI E-Study*"') do (
    echo %%i
    set var=%%i
    set var=!var:CNKI E-Study=!
    echo %%i !var!
    ren "%%i" "!var!"
)
pause