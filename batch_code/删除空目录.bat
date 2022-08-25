@echo off
rem TODO：修改内容

echo now is deleting empty dir
echo.
copy nul listnull.txt

for /f "delims=" %%i in ('dir /ad /b /s') do (
  dir /b "%%i" | findstr.>nul || echo %%i>>listnull.txt
)

set /a sum = 0
for /f %%i in (listnull.txt) do (
  rem 删除目录
  rd /q %%i
  set /a sum = sum+1
)

set sum = 
del /q listnull.txt >nul