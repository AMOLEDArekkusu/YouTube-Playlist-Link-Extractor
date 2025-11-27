import yt_dlp
import sys
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
import csv

class YouTubeExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist Link Extractor")
        self.root.geometry("600x600")

        # --- UI Elements ---

        # Label
        tk.Label(root, text="Enter YouTube Playlist URL:", font=("Arial", 12, "bold")).pack(pady=(15, 5))

        # Input Field
        self.url_entry = tk.Entry(root, width=60, font=("Arial", 10))
        self.url_entry.pack(pady=5)

        # Options Container
        options_frame = tk.Frame(root)
        options_frame.pack(pady=5)

        # Format Options
        format_frame = tk.LabelFrame(options_frame, text="Link Format", padx=10, pady=5)
        format_frame.pack(side=tk.LEFT, padx=10)
        
        self.format_var = tk.StringVar(value="watch")
        tk.Radiobutton(format_frame, text="Standard (watch?v=)", variable=self.format_var, 
                      value="watch", font=("Arial", 9)).pack(anchor="w")
        tk.Radiobutton(format_frame, text="Embed (/embed/)", variable=self.format_var, 
                      value="embed", font=("Arial", 9)).pack(anchor="w")

        # File Output Options
        file_frame = tk.LabelFrame(options_frame, text="File Output", padx=10, pady=5)
        file_frame.pack(side=tk.LEFT, padx=10)

        self.file_type_var = tk.StringVar(value="txt")
        tk.Radiobutton(file_frame, text="Text file (.txt)", variable=self.file_type_var, 
                      value="txt", font=("Arial", 9)).pack(anchor="w")
        tk.Radiobutton(file_frame, text="Excel CSV (.csv)", variable=self.file_type_var, 
                      value="csv", font=("Arial", 9)).pack(anchor="w")

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        # Start Button
        self.start_btn = tk.Button(btn_frame, text="Extract Links", command=self.start_extraction, 
                                   bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        # Clear Button
        tk.Button(btn_frame, text="Clear Log", command=self.clear_log, padx=10, pady=5).pack(side=tk.LEFT, padx=10)

        # Output Text Area
        tk.Label(root, text="Extraction Log:", font=("Arial", 10)).pack(pady=(10, 0), anchor="w", padx=20)
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Consolas", 9))
        self.log_area.pack(pady=5, padx=20)

        # Status Label
        self.status_label = tk.Label(root, text="Ready", fg="blue", font=("Arial", 10))
        self.status_label.pack(side=tk.BOTTOM, pady=10)

    def log(self, message):
        """Updates the text area with a message."""
        # Use root.after to ensure thread safety when updating UI from a background thread
        self.root.after(0, lambda: self._insert_log(message))

    def _insert_log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def clear_log(self):
        self.log_area.delete('1.0', tk.END)

    def start_extraction(self):
        url = self.url_entry.get().strip()
        link_format = self.format_var.get()
        file_type = self.file_type_var.get()

        if not url:
            messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")
            return
        
        # Disable button during processing
        self.start_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Processing...", fg="orange")
        self.log(f"--- Starting Processing for: {url} ---")
        self.log(f"--- Link Mode: {link_format} | File Type: {file_type.upper()} ---")
        
        # Run extraction in a separate thread to prevent GUI freezing
        thread = threading.Thread(target=self.run_extraction_logic, args=(url, link_format, file_type))
        thread.daemon = True # Ensures thread closes if window closes
        thread.start()

    def run_extraction_logic(self, playlist_url, link_format, file_type):
        # Options to ensure we only get metadata (fast) and don't download videos
        ydl_opts = {
            'extract_flat': True,  # Extract metadata only
            'quiet': True,         # Suppress internal messages
            'ignoreerrors': True,  # Skip errors
        }

        extracted_data = [] # List of dictionaries
        self.log("Connecting to YouTube... Please wait.")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(playlist_url, download=False)

                if 'entries' in result:
                    # It is a playlist
                    self.log(f"Playlist Found: {result.get('title', 'Unknown')}")
                    count = len(result['entries'])
                    self.log(f"Total videos found: {count}")
                    self.log("Extracting URLs...")
                    
                    for entry in result['entries']:
                        if entry:
                            title = entry.get('title', 'No Title')
                            video_id = entry.get('id')
                            if video_id:
                                if link_format == "embed":
                                    full_url = f"https://www.youtube.com/embed/{video_id}"
                                else:
                                    full_url = f"https://www.youtube.com/watch?v={video_id}"
                                
                                extracted_data.append({"url": full_url, "title": title})
                else:
                    # It is a single video
                    video_id = result.get('id')
                    title = result.get('title')
                    
                    if link_format == "embed":
                        full_url = f"https://www.youtube.com/embed/{video_id}"
                    else:
                        full_url = f"https://www.youtube.com/watch?v={video_id}"
                        
                    extracted_data.append({"url": full_url, "title": title})
                    self.log("Single video found.")

        except Exception as e:
            self.log(f"Error: {e}")
            self.root.after(0, lambda: self.status_label.config(text="Error occurred", fg="red"))
        
        # Output results
        if extracted_data:
            self.log(f"\n--- Extracted {len(extracted_data)} Links ---")
            
            try:
                if file_type == "csv":
                    filename = "playlist_links.csv"
                    # Using utf-8-sig ensures Excel recognizes the CSV correctly
                    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
                        writer = csv.writer(f)
                        writer.writerow(["Video URL", "Title"]) # CSV Header
                        for item in extracted_data:
                            writer.writerow([item['url'], item['title']])
                else:
                    filename = "playlist_links.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        for item in extracted_data:
                            f.write(f"{item['url']} | {item['title']}\n")

                self.log(f"Successfully saved links to '{filename}'")
                self.root.after(0, lambda: self.status_label.config(text="Completed Successfully", fg="green"))
                self.root.after(0, lambda: messagebox.showinfo("Success", f"Extracted {len(extracted_data)} links to {filename}"))
            except Exception as e:
                self.log(f"Failed to save file: {e}")
        else:
            self.log("No videos found or playlist is private.")
            self.root.after(0, lambda: self.status_label.config(text="Failed / Empty", fg="red"))

        # Re-enable button
        self.root.after(0, lambda: self.start_btn.config(state=tk.NORMAL))

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = YouTubeExtractorApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to start GUI: {e}")
        input("Press Enter to exit...")
