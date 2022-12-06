import moviepy.editor as mp
import argparse
import os

# 使用 argparse 模組來處理命令列參數
parser = argparse.ArgumentParser()
parser.add_argument("video_file")
parser.add_argument("text_file")
parser.add_argument("output_dir")
args = parser.parse_args()


# 檢查輸出目錄是否存在，如果不存在則建立
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
# 讀取影片檔案
video = mp.VideoFileClip(args.video_file)

# 讀取文字檔
with open(args.text_file) as f:
    lines = f.readlines()


# 將文字檔的每一行轉換成時間分段的資訊
segments = []
for line in lines:
    # 忽略空白行
    if line.strip() == "":
        continue
    
    # 使用 ! 分割時間和標題
    time_str, title = line.strip().split("@", 1)
    # 去除時間字串中的 ! 符號
    time_str = time_str.strip("!")
    # 將時間字串轉換成時間點
    time = int(time_str.split(":")[0]) * 60 + int(time_str.split(":")[1])
    # 將時間點和標題儲存到列表中
    segments.append((time, title))
    #print(time)
    #print(title)
    # 依序處理每一個時間分段
last_time=0
for i in range(len(segments) - 1):
    start = segments[i][0]
    end = segments[i+1][0]
    title = segments[i][1]
    print(start,end,title)
    # 從影片中截取指定的時間區間
    clip = video.subclip(int(start), int(end))
    # 將截取的影片儲存到指定的檔案名稱中
    clip.write_videofile(args.output_dir + "/" +str(i)+"_"+title + ".mp4")
    #last_time=end
