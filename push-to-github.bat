@echo off
REM 双击运行：把 verl-rl 课程推送到 GitHub（首次会弹出 GitHub 授权窗口，登录即可）
cd /d D:\learn\verl-rl
git config credential.helper manager
git push -u origin main
echo.
if %errorlevel%==0 (echo [成功] 已推送到 https://github.com/JohnSiegfried/verl-rl-course) else (echo [失败] 请检查网络/授权后重试)
pause
