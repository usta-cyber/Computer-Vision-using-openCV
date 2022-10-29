# get Youtube Video information using pafy

import pafy
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
v = pafy.new(url)
print(v.title)
print(v.duration)
print(v.rating)
print(v.author)
print(v.length)
print(v.thumb)
print(v.videoid)
print(v.viewcount)