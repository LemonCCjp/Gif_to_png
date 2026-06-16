# made by 1101043

import glob
import os
import msvcrt
from PIL import Image
import sys

files = glob.glob("./入力\\*") #入力フォルダ内のすべてのファイルを取得
out_dir = "./出力" #出力フォルダのパス
os.makedirs(out_dir, exist_ok=True) # 出力フォルダが存在しない場合は作成

for file in files:
    gif_path = file
    file_name = gif_path.removeprefix("./入力\\").removesuffix(".gif")

    frame_sizes = []
    frame_count = 0

    gif = Image.open(gif_path)

    try:
        while True:
            frame_sizes.append(gif.size) # フレームのサイズを保存
            frame_count += 1 # フレーム数をカウント
            gif.seek(gif.tell() + 1) # 次のフレームに移動
    except EOFError:
        pass
    
    total_width = sum(w for w, h in frame_sizes) # フレームの枚数の合計分が幅になる
    height = frame_sizes[0][1] # 高さは変更無し

    combined = Image.new("RGBA", (total_width, height)) # 幅と高さを指定して新しい画像を作成

    gif = Image.open(gif_path)
    x_offset = 0
    try:
        while True:
            frame = gif.convert("RGBA")
            combined.paste(frame, (x_offset, 0)) # フレーム左から作成した画像に貼り付け
            x_offset += frame.width # 次のフレームの貼り付け位置を更新
            gif.seek(gif.tell() + 1) # 次のフレームに移動
    except EOFError:
        pass

    # 保存
    combined.save(f"./出力/{file_name}.png") # 出力フォルダにファイル名.pngで保存
    print(f"変換が完了しました: {file_name}.png")


print("いずれかのキーを入力して終了...") # 変換が完了した後、ユーザーがキーを入力するまでプログラムを終了しないようにする
while True:
    if msvcrt.kbhit():  # キー入力があったかどうか
        key = msvcrt.getch()  # 入力されたキーを取得
        sys.exit() # プログラムを終了
    