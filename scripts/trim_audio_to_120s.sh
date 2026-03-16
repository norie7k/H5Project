#!/usr/bin/env bash
# 将 8 个大体积 .wav 裁切为最多 120 秒并转为 MP3（128k），便于推送到 GitHub。
# 使用前请安装 ffmpeg：brew install ffmpeg
# 在项目根目录执行：bash scripts/trim_audio_to_120s.sh

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v ffmpeg &>/dev/null; then
  echo "请先安装 ffmpeg："
  echo "  brew install ffmpeg"
  exit 1
fi

trim_to_mp3() {
  local src="$1"
  if [[ ! -f "$src" ]]; then
    echo "跳过（文件不存在）: $src"
    return 0
  fi
  local dir="${src%/*}"
  local base="${src##*/}"
  local name="${base%.wav}"
  local dest="${dir}/${name}.mp3"
  echo "处理: $src -> $dest (最多 120 秒, 128k MP3)"
  ffmpeg -i "$src" -t 120 -b:a 128k -y "$dest" -hide_banner -loglevel warning
  echo "  -> 完成"
}

trim_to_mp3 "1.主页/开始.wav"
trim_to_mp3 "1.主页/Anescanada Church (228b0e69c58b4598944a1314c89018a1).wav"
trim_to_mp3 "Q3/drama.wav"
trim_to_mp3 "Q3/system.wav"
trim_to_mp3 "Q4/early.wav"
trim_to_mp3 "Q4/The Texas Transportation Security Administration (b2f5ddad8b0846b4beaa70f6b2d2ae7a).wav"
trim_to_mp3 "结束/Whispering.wav"
trim_to_mp3 "结束/over.wav"

echo ""
echo "全部完成。请执行："
echo "  git add 1.主页/*.mp3 Q3/*.mp3 Q4/*.mp3 结束/*.mp3"
echo "  git add -u"
echo "  git commit -m 'chore: 大音频裁切 120s 并转 MP3'"
echo "  git push"
