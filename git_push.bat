start /b "" "code" ./BOJ
pause
:loop
    git pull
    git add .
    git commit -m "auto push"
    git push
    TIMEOUT 600
goto loop
