# YouTube-Playlist-Link-Extractor
YouTube Playlist Link Extractor

A simple Python GUI application that allows you to extract all video URLs from a YouTube playlist. You can choose to format the links as standard URLs (watch?v=) or embed URLs (/embed/) and save the output to either a Text file (.txt) or a CSV file (.csv).

Features

GUI Interface: Easy-to-use graphical interface built with Tkinter.

Playlist Extraction: extract all videos from a public or unlisted YouTube playlist.

Single Video Support: Works with single video links as well.

Link Formatting: Choose between Standard (https://www.youtube.com/watch?v=ID) or Embed (https://www.youtube.com/embed/ID) formats.

Export Options: Save your list as a simple Text file or an Excel-compatible CSV file (UTF-8 with BOM support).

Threaded Processing: The interface remains responsive while fetching data.

Prerequisites

Python 3.6+: Make sure Python is installed on your system.

Internet Connection: Required to fetch playlist data from YouTube.

Installation

Clone or Download this repository (or save the Youtubelist_extractor.py file).

Install the required dependency:
The script relies on yt-dlp to interact with YouTube. Install it via pip:

pip install yt-dlp


(Note: tkinter, csv, and threading are included with Python by default and do not need to be installed.)

How to Run

Open your terminal or command prompt.

Navigate to the folder containing the script.

Run the script using Python:

python youtube_playlist_extractor.py


Usage

Enter URL: Paste a YouTube Playlist URL (or a single video URL) into the input field.

Select Link Format:

Standard: Good for watching or sharing.

Embed: Useful for web developers or embedding videos in iframes.

Select File Output:

Text file (.txt): A simple list of "URL | Title".

Excel CSV (.csv): A structured table compatible with Microsoft Excel or Google Sheets.

Extract: Click the Extract Links button.

Results: * The progress will be shown in the log window.

Once finished, a file named playlist_links.txt or playlist_links.csv will be created in the same folder as the script.

Troubleshooting

"No videos found": Ensure the playlist is Public or Unlisted. Private playlists cannot be accessed.

Script freezes: The script uses threading to prevent freezing, but a slow internet connection might delay the log updates.

CSV characters look weird: The script uses utf-8-sig encoding, which should fix display issues in Excel. If issues persist, try importing the data into Excel using the "Data > From Text/CSV" option.

<img width="752" height="790" alt="image" src="https://github.com/user-attachments/assets/d5425575-b7d1-46f7-8842-4ca70f26f955" />
