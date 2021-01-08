import youtube_dl

ydl_opt = {
    # 'listformats': True  # 다운로드 가능한 모든 포맷들 출력, YoutubeDL은 (best)라고 되어있는 파일 다운, 일단 포맷 이걸로 확인하고
    # 'format' : '18',  # 만약 그 중 18번 포맷 다운하고 싶다면

}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:  # 유튜브 YoutubeDL 이라는 객체를 생성해서 ydl에 저장
    ydl.download(['https://youtu.be/cGC5TESLo9I'])  # 다운받고싶은 영상 주소나 재생목록을 리스트 안에 넣으면 됨