urls = ["http://meiwen.me/src/index.html",
        "http://1000chi.com/game/index.html",
        "http://see.xidian.edu.cn/cpp/html/1429.html",
        "https://docs.python.org/2/howto/regex.html",]

from Regex import getter

for url in urls:
    print(getter(url))
