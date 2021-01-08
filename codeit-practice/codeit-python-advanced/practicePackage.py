import youtube_dl

with youtube_dl.YoutubeDL() as ydl:  # 유튜브 YoutubeDL 이라는 객체를 생성해서 ydl에 저장
    ydl.download(['https://youtu.be/cGC5TESLo9I'])  # 다운받고싶은 영상 주소나 재생목록을 리스트 안에 넣으면 됨