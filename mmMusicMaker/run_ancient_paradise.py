import os
from pathlib import Path
import subprocess

ENV_PATH = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\.env")
SCRIPT = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\MiniMaxSkills\mmMusicMaker\scripts\generate_music.py")
OUTPUT = Path(r"C:\Users\hehaolan007\Desktop\Claw Project\MiniMaxSkills\mmMusicMaker\output_ancient_paradise.mp3")

for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
    if line.startswith("MINIMAX_MUSIC_API_KEY="):
        os.environ["MINIMAX_MUSIC_API_KEY"] = line.split("=", 1)[1].strip()

lyrics = "[intro] [outro]"
prompt = "pure music, ancient Chinese style, relaxing, ethereal paradise, peaceful, carefree, guzheng, dizi, erhu, nature sounds, no lyrics"

cmd = ["python", str(SCRIPT), "--lyrics", lyrics, "--prompt", prompt, "--output", str(OUTPUT), "--format", "mp3", "--bitrate", "256000", "--sample-rate", "44100"]

print("Generating ancient Chinese paradise pure music...")
print("Prompt:", prompt)
print("Lyrics:", lyrics)
print()

subprocess.run(cmd, check=True, timeout=600)
print()
print("Generated:", OUTPUT)
