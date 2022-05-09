start /b "" "code" C:\Users\barah\Desktop\알고리즘\boj\BOJ
:loop
    git pull
    git add .
    git commit -m "auto push"
    git push
    TIMEOUT 600
goto loop
