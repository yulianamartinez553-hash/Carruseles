#!/usr/bin/env bash
# STLabs v4: framing fijo + A/V sync. Color/ASS/SFX iguales a v3 pro.
set -euo pipefail
MASTER=/workspace/videos/sebas-master.mp4
VOICE=/tmp/video-edit/v3/voice.wav
ASS=/tmp/video-edit/v4/overlays.ass
FONTDIR=/tmp/video-edit/v2/fonts
AUD=/tmp/video-edit/v4/audio_final.wav
OUT=/opt/cursor/artifacts/STLabs-sebas-cafeteria-edit.mp4
DUR_V=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "$MASTER")
ASS_ESC=${ASS//:/\\:}
FONT_ESC=${FONTDIR//:/\\:}
VF="[0:v]scale=1620:2880:force_original_aspect_ratio=increase,crop=1620:2880,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,colorlevels=rimin=0.035:gimin=0.032:bimin=0.030:rimax=0.965:gimax=0.968:bimax=0.970,eq=contrast=1.07:brightness=0.015:saturation=1.14:gamma=1.03,colorbalance=rs=0.015:gs=0.008:bs=-0.012:rm=0.02:gm=0.01:bm=-0.01:rh=0.01:gh=0.005:bh=-0.008,unsharp=3:3:0.35:3:3:0.0,scale=1080:1920:flags=lanczos,ass=${ASS_ESC}:fontsdir=${FONT_ESC},setpts=PTS-STARTPTS[v];[1:a]asetpts=PTS-STARTPTS[a]"
ffmpeg -y -i "$MASTER" -i "$AUD" -filter_complex "$VF" -map "[v]" -map "[a]" \
  -c:v libx264 -preset veryfast -crf 17 -pix_fmt yuv420p \
  -c:a aac -b:a 256k -ac 2 -ar 48000 -t "$DUR_V" -movflags +faststart "$OUT"
