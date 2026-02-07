---
name: mm-music-maker
description: Create music with MiniMax music models (e.g., music-2.5). Use when generating songs or instrumental tracks from lyrics and style prompts, or when integrating MiniMax Music Generation API into scripts.
---

# MiniMax Music Maker

Use this skill to generate music with MiniMax’s Music Generation API. All usage and outputs are designed for **music-2.5** unless specified otherwise.

## Quick start

1) Set the API key:
```bash
export MINIMAX_MUSIC_API_KEY="your_api_key"
```

2) Generate music from lyrics (and optional prompt):
```bash
python scripts/generate_music.py \
  --lyrics "[Verse]\n...\n[Chorus]\n..." \
  --prompt "indie folk, melancholic, introspective" \
  --output ./output.mp3
```

## Script location

- `scripts/generate_music.py` — main generator (lyrics + prompt → audio)
- `scripts/utils_audio.py` — hex decoding + save helpers

## References

Read **references/minimax_music_api.md** for:
- Endpoint, auth header, payload schema
- Required/optional fields
- Output formats (hex/url) and constraints

## Notes

- `lyrics` is **required** by the API.
- `prompt` is optional for `music-2.5`.
- `output_format` defaults to `hex` (inline audio). Use `url` if you prefer a download URL.
- URLs expire (24h). Download immediately if using `url`.

## Prompt crafting (重要)

**核心原则**：用“描述”而不是“命令”，并保持结构化、清晰、可解析。

### 必备要素（推荐都写）
- **Genre/Subgenre**（含年代或地域）
- **Mood/Emotion**（2–3 个情绪词）
- **Tempo/BPM**（能写具体 BPM 就写）
- **Key Instruments**（3–5 个关键乐器/音色）
- **Vocals**（人声类型/处理方式/是否纯音乐）
- **Use case**（用途/场景）

### 可选增强
- **Structure**（段落结构）
- **References**（1–2 个风格参考）
- **Avoid/Negative**（排除项）

### Prompt 模板
**基础模板（新手）**
```
[Genre], [Mood], [Tempo/BPM], [Key Instruments], [Vocal Style]
```

**标准模板（推荐）**
```
Genre: [Specific genre + era]
Mood: [2-3 descriptors]
Tempo: [BPM or speed]
Instruments: [3-5 key instruments]
Vocals: [Type or instrumental only]
Use case: [scene/usage]
Avoid: [unwanted elements]
References: [1-2 artists/songs]
```

**高级模板（制作简报）**
```
Genre: … | Era: …
BPM: … | Key: …
Mood: … (可写情绪变化，如“从克制到爆发”)
Lead: …
Rhythm: …
Bass: …
Texture: …
Vocals: …
Structure: Intro / Verse / Chorus / Bridge / Outro
Avoid: …
Reference: …
```

### 结构标签（写在 lyrics 中）
```
[Intro]
[Verse]
[Pre-Chorus]
[Chorus]
[Bridge]
[Outro]
[Instrumental]
```

### 负面约束示例（Avoid）
- `No vocals` / `Instrumental only`
- `Avoid autotune`
- `No distorted guitars`
- `Avoid heavy reverb`
- `No trap hi-hats`

### 常见问题修复
- **风格不准**：加“年代 + 子风格 + 乐器锚点 + 参考艺人”
- **节奏不对**：写具体 BPM + 节奏描述（如 four-on-the-floor）
- **开头太模板**：在 lyrics 里写 [Intro] 并描述开场
- **人声不合**：把 Vocals 放到 prompt 前部，并加负面约束

## Prompt 质量检查清单
- 是否包含：风格 / 情绪 / BPM / 乐器 / 人声 / 用途
- 是否存在冲突（如“极慢 + 高能”）
- 是否有 Avoid 项过滤不要的元素
- 是否结构化（避免长段落散文）

## Recommended CLI patterns

Generate MP3 (hex response → file):
```bash
python scripts/generate_music.py \
  --lyrics "[Intro]\n..." \
  --prompt "cinematic, uplifting" \
  --output ./music.mp3 \
  --format mp3 \
  --bitrate 256000 \
  --sample-rate 44100
```

Generate and download from URL:
```bash
python scripts/generate_music.py \
  --lyrics "[Verse]\n..." \
  --prompt "lofi, rainy night" \
  --output ./music.mp3 \
  --output-format url \
  --download
```
