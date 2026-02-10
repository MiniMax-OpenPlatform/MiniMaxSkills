# MiniMaxSkills

MiniMaxSkills 是 MiniMax 官方提供的 AI Agent 技能库，基于 MiniMax 多模态模型，为 Agent 拓展语音合成、音乐生成等能力。

## 技能列表

### 语音 & 语音合成

| 技能 | 简介 | 核心功能 |
|------|------|----------|
| [mmVoice_Maker](./mmVoice_Maker/) | 基于 MiniMax Voice API 和 FFmpeg 的复杂语音制作技能。 | 支持多角色语音合成，可制作有声书、播客等。还提供了声音克隆（10秒–5分钟音频）、声音设计（文字描述生成）、音频后处理（合并、转换、归一化、裁剪）能力。 |
| [mmEasyVoice](./mmEasyVoice/) | 基于 MiniMax Speech 模型的语音合成技能。 | 快速文本转语音、简单易用、使 Agent 具备「说话」的能力 |

### 音乐

| 技能 | 简介 | 核心功能 |
|------|------|----------|
| [mmMusicMaker](./mmMusicMaker/) | 基于 MiniMax Music API 的音乐生成技能。 | 支持带歌词的完整歌曲生成、纯音乐/器乐生成、旋律哼唱/吟唱生成 |

## 快速开始

每个技能目录下都有 `SKILL.md`（详细使用说明）和 `reference/`（参考文档）。开始使用：

1. 进入你需要使用的技能目录
2. 阅读 `SKILL.md` 了解完整工作流程
3. 设置所需的 API Key（`MINIMAX_VOICE_API_KEY` 或 `MINIMAX_MUSIC_API_KEY`），即 MiniMax 按量计费 API Key
4. 按照步骤指引操作

## 环境要求

- Python 3.8+
- MiniMax 按量计费 API Key（[中国用户前往获取](https://platform.minimaxi.com/user-center/basic-information/interface-key), [海外用户前往获取](https://platform.minimax.io/user-center/basic-information/interface-key)）
- FFmpeg（mmVoice_Maker 的音频处理功能需要）
