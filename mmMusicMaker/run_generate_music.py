import os
from pathlib import Path
import subprocess

ENV_PATH = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\.env")
SCRIPT = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\mmMusicMaker\mm-music-maker\scripts\generate_music.py")
OUTPUT = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\mmMusicMaker\festive_chinese.mp3")

# load env
for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
    if line.startswith("MINIMAX_MUSIC_API_KEY="):
        os.environ["MINIMAX_MUSIC_API_KEY"] = line.split("=", 1)[1].strip()

lyrics = """[Intro]
锣鼓喧天瑞气来
灯火万家照春台
[Verse]
红绸舞动迎新岁
花开富贵满堂彩
[Chorus]
金风送喜万家欢
福满人间共团圆
鼓声起舞灯影旋
中国风里庆丰年
[Verse]
笙箫齐鸣添雅韵
瑞狮腾跃福星临
[Chorus]
金风送喜万家欢
福满人间共团圆
鼓声起舞灯影旋
中国风里庆丰年"""

prompt = "Chinese traditional, festive, joyful, bright, ceremonial, drums, gongs, suona, erhu, guzheng"

cmd = [
    "python",
    str(SCRIPT),
    "--lyrics", lyrics,
    "--prompt", prompt,
    "--output", str(OUTPUT),
    "--format", "mp3",
    "--bitrate", "256000",
    "--sample-rate", "44100",
]

subprocess.run(cmd, check=True)
print(str(OUTPUT))
