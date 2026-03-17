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

## 部署到阿里云 OSS（静态网站）

1. **登录** [阿里云控制台](https://ram.console.aliyun.com/) → 打开 **对象存储 OSS**。
2. **创建 Bucket**
   - **Bucket 名称**：自定（如 `h5-survey`，需全局唯一）。
   - **地域**：选离用户近的（如华东1）。
   - **存储类型**：标准存储。
   - **读写权限**：选 **公共读**（否则外网无法访问页面）。
   - 其他保持默认，创建。
3. **设置静态网站**
   - 进入该 Bucket → 左侧 **数据管理** → **静态页面**（或 **基础设置** 里的「静态页面」）。
   - 开启 **静态页面**。
   - **默认首页** 填：`1.主页/intro_public.html`（本问卷入口页）。
   - **默认 404 页** 可留空或填同一路径，保存。
4. **上传文件**
   - 在 **文件管理** 中，按 **Test1 的目录结构** 上传，保证路径一致：
     - 根目录：`All.mp3`、`index.html`、`vercel.json` 等。
     - 目录：`1.主页/`、`Q0/`、`Q1/`、`Q2/`、`Q3/`、`Q4/`、`结束/`、`scripts/` 等。
   - 可用 **ossutil** 在本地同步整个目录（安装与配置见 [ossutil 文档](https://help.aliyun.com/document_detail/120075.html)）：
     ```bash
     ossutil cp -r /Users/norie/Downloads/Test1/ oss://你的Bucket名/ --update
     ```
   - 或用控制台 **上传** → 选文件夹，保持子目录结构。
5. **访问**
   - Bucket 详情里查看 **Bucket 外网访问域名**，形如：`https://<bucket>.<region>.aliyuncs.com`。
   - 问卷入口：`https://<bucket>.<region>.aliyuncs.com/` 或  
     `https://<bucket>.<region>.aliyuncs.com/1.主页/intro_public.html`。
   - 手机浏览器打开上述链接即可访问。
6. **自定义域名（可选）**
   - 在 Bucket **传输管理** → **域名管理** 里绑定自己的域名，并做 CNAME 解析。
   - 中国大陆使用自有域名需完成 **ICP 备案**；使用 OSS 默认域名则无需备案。

---

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
