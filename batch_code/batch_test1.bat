@echo off
echo start creating...
echo.
echo.
for /l %%n in (0,1,10) do (
echo this is file %%n >> file%%n.txt
)
echo complished!