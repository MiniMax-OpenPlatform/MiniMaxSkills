# MiniMaxSkills

MiniMaxSkills is a collection of AI agent skills powered by MiniMax multimodal models. These skills extend agent capabilities with voice synthesis, music generation, and more.

<p align="left">
  <a href="README-CN.md"><img src="https://img.shields.io/badge/中文-README--CN-blue" alt="中文"></a>
</p>

## Skills List

### Voice & Speech

| Skill | Description | Key Features |
|-------|-------------|--------------|
| [mmVoice_Maker](./mmVoice_Maker/) | Complex text-to-speech production skill powered by MiniMax Voice API and FFmpeg. | Support multi-voice synthesis, can create audiobooks, podcasts, etc. Also provides voice cloning (10s–5min audio), voice design (text prompt), audio post-processing (merge, convert, normalize, trim) capabilities. |
| [mmEasyVoice](./mmEasyVoice/) | Text-to-speech skill based on MiniMax Speech model. | Quick text-to-speech conversion, simple and easy to use, enables Agent to "speak" |

### Music

| Skill | Description | Key Features |
|-------|-------------|--------------|
| [mmMusicMaker](./mmMusicMaker/) | Music generation skill powered by MiniMax Music API. | Support standard songs with lyrics, pure instrumental music, melodic chanting/humming, structured prompt crafting, multiple output formats (hex/url) |

## Getting Started

Each skill has its own `SKILL.md` with detailed usage instructions and `reference/` docs. To get started:

1. Navigate to the skill directory you want to use
2. Read the `SKILL.md` for the complete workflow
3. Set the required API key (`MINIMAX_VOICE_API_KEY` or `MINIMAX_MUSIC_API_KEY`), i.e. MiniMax Pay-as-you-go API Key
4. Follow the step-by-step guide

## Requirements

- Python 3.8+
- MiniMax Pay-as-you-go API Key ([Get one here (overseas users)](https://platform.minimax.io/user-center/basic-information/interface-key), [Get one here (Chinese users)](https://platform.minimaxi.com/user-center/basic-information/interface-key))
- FFmpeg (required for audio processing in mmVoice_Maker)
