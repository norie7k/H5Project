# Hello World 内测问卷

静态问卷站点，可部署到 Vercel 公网访问。

## 部署到 Vercel

1. **把项目放进 Git 仓库**（GitHub / GitLab / Bitbucket）
   ```bash
   cd /path/to/Test1
   git init
   git add .
   git commit -m "init"
   git remote add origin <你的仓库地址>
   git push -u origin main
   ```

2. **在 Vercel 里导入项目**
   - 打开 [vercel.com](https://vercel.com) 并登录
   - 点击 **Add New** → **Project**
   - 选择刚推送的仓库，**Framework Preset** 选 **Other**（纯静态）
   - **Root Directory** 保持默认（项目根目录）
   - 点击 **Deploy**

3. **访问**
   - 部署完成后会得到 `https://xxx.vercel.app`
   - 根路径 `/` 会跳转到问卷主页（`1.主页/intro_public.html`）

## 本地预览

用任意静态服务器打开根目录即可，例如：

```bash
npx serve .
# 或
python3 -m http.server 8080
```

然后访问 `http://localhost:8080` 或 `http://localhost:8080/1.主页/intro_public.html`。

## 说明

- **index.html**：根路径入口，访问 `/` 时跳转到问卷主页
- **vercel.json**：根路径重写到主页；并设置安全相关响应头
- **.vercelignore**：排除 `.venv`、脚本等，减少上传体积
- **大体积音频**：原始 8 个 .wav 在 `.gitignore` 中，不推送。请用脚本生成「最多 120 秒」的 MP3 后再提交并推送，线上即可正常播放：
  ```bash
  brew install ffmpeg   # 若未安装
  bash scripts/trim_audio_to_120s.sh
  git add "1.主页"/*.mp3 Q3/*.mp3 Q4/*.mp3 结束/*.mp3 scripts/
  git add -u
  git commit -m "chore: 大音频裁切 120s 并转 MP3"
  git push
  ```
