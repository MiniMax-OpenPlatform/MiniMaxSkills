import argparse
import os
import sys
import requests

from utils_audio import hex_to_bytes, save_bytes, download_url

API_URL = "https://api.minimaxi.com/v1/music_generation"


def build_payload(args):
    payload = {
        "model": args.model,
        "lyrics": args.lyrics,
    }
    if args.prompt is not None:
        payload["prompt"] = args.prompt

    if args.output_format:
        payload["output_format"] = args.output_format

    if args.stream:
        payload["stream"] = True

    audio_setting = {}
    if args.sample_rate:
        audio_setting["sample_rate"] = args.sample_rate
    if args.bitrate:
        audio_setting["bitrate"] = args.bitrate
    if args.format:
        audio_setting["format"] = args.format
    if args.aigc_watermark is not None:
        audio_setting["aigc_watermark"] = args.aigc_watermark

    if audio_setting:
        payload["audio_setting"] = audio_setting

    return payload


def main():
    parser = argparse.ArgumentParser(description="Generate music with MiniMax Music API")
    parser.add_argument("--lyrics", required=True, help="Lyrics text (use \\n for line breaks)")
    parser.add_argument("--prompt", default=None, help="Style/scene prompt (optional for music-2.5)")
    parser.add_argument("--model", default="music-2.5", help="Model name (default: music-2.5)")
    parser.add_argument("--output", required=True, help="Output file path (e.g., ./music.mp3)")
    parser.add_argument("--output-format", choices=["hex", "url"], default="hex", help="Response format")
    parser.add_argument("--stream", action="store_true", help="Enable streaming (hex only)")
    parser.add_argument("--sample-rate", type=int, default=None)
    parser.add_argument("--bitrate", type=int, default=None)
    parser.add_argument("--format", dest="format", default=None, help="Audio format, e.g., mp3")
    parser.add_argument("--aigc-watermark", type=lambda v: v.lower() == "true", default=None)
    parser.add_argument("--download", action="store_true", help="Download if output_format=url")
    args = parser.parse_args()

    api_key = os.getenv("MINIMAX_MUSIC_API_KEY")
    if not api_key:
        print("MINIMAX_MUSIC_API_KEY is not set", file=sys.stderr)
        sys.exit(1)

    if args.stream and args.output_format != "hex":
        print("When --stream is true, output_format must be hex", file=sys.stderr)
        sys.exit(1)

    payload = build_payload(args)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    resp = requests.post(API_URL, json=payload, headers=headers, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    base_resp = data.get("base_resp", {})
    if base_resp.get("status_code") != 0:
        raise RuntimeError(f"API error: {base_resp}")

    audio_data = data.get("data", {}).get("audio")
    if not audio_data:
        raise RuntimeError("No audio data returned")

    if args.output_format == "hex":
        audio_bytes = hex_to_bytes(audio_data)
        saved = save_bytes(audio_bytes, args.output)
        print(saved)
        return

    # output_format == url
    if args.download:
        saved = download_url(audio_data, args.output)
        print(saved)
    else:
        # print URL for manual download
        print(audio_data)


if __name__ == "__main__":
    main()
