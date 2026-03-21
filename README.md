# 🎬 YouTube Playlist Link Extractor

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![Dependency](https://img.shields.io/badge/Dependency-yt--dlp-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> A simple yet powerful **Python GUI application** to extract all video URLs from YouTube playlists. Supports standard/embed link formats and exports to TXT/CSV files—built for ease of use and flexibility.


## 🚀 Key Features

- 🖥️ **Intuitive GUI**: User-friendly graphical interface powered by Tkinter.
- 📋 **Playlist Extraction**: Extract all videos from **public or unlisted** YouTube playlists.
- 🎥 **Single Video Support**: Also works with individual YouTube video links.
- 🔗 **Dual Link Formats**:
  - **Standard**: `https://www.youtube.com/watch?v=ID` (for watching/sharing).
  - **Embed**: `https://www.youtube.com/embed/ID` (for web developers/iframes).
- 💾 **Flexible Export**:
  - Save as **Text file (.txt)**: Simple "URL | Title" list.
  - Save as **Excel CSV (.csv)**: Structured table with UTF-8 BOM support (compatible with Excel/Google Sheets).
- ⚡ **Threaded Processing**: Keeps the interface responsive while fetching YouTube data.


## 📋 Prerequisites

- Python 3.6+
- Active internet connection (to fetch playlist/video data from YouTube)


## 🛠️ Installation

1. **Clone or Download** this repository (or save the `youtube_playlist_extractor.py` file locally).
2. **Install Dependencies**:
   The script relies on `yt-dlp` to interact with YouTube. Install it via pip:
   ```bash
   pip install yt-dlp


(Note: `tkinter`, `csv`, and `threading` are included with Python by default—no extra installation required.)

## 🚀 How to Run

1. **Open your terminal/command prompt.**
2. **Navigate to the folder containing `youtube_playlist_extractor.py`.**
3. **Launch the app**
   ```bash
      python youtube_playlist_extractor.py

## 🎮 Usage

1. **Enter URL**: Paste a YouTube Playlist URL (or single video URL) into the input field.
2. **Select Link Format**:
      **. Standard**: Best for watching or sharing links.
      **. Embed**: Ideal for web developers embedding videos in iframes.
3. **Select File Output**:
      **. Text file (.txt)**: Simple list of "URL | Title".
      **. Excel CSV (.csv)**: Structured table compatible with Microsoft Excel or Google Sheets.
4. **Extract**: Click the **Extract Links** button.
5. **Results**:
      Progress updates in the log window.
      Once finished, `playlist_links.txt` or `playlist_links.csv` is saved in the same folder as the script.
   
## 🔧 Troubleshooting

**-  ❌ "No videos found"**: Ensure the playlist is set to **Public** or **Unlisted** (private playlists cannot be accessed).
**-  ⏸️ Script freezes**: Threading prevents UI lockups, but slow internet may delay log updates—be patient!
**-  📝 CSV character issues**: The script uses `utf-8-sig` encoding for Excel compatibility. If problems persist, import the CSV via Excel’s "Data > From Text/CSV" option.


## 📸 Screenshot

<img width="752" height="790" alt="image" src="https://github.com/user-attachments/assets/d5425575-b7d1-46f7-8842-4ca70f26f955" />
