# # notebooks/split_data.py
# import os
# import random
# import shutil

# def split_folder(src_dir, dst_train, dst_val, val_ratio=0.2):
#     os.makedirs(dst_train, exist_ok=True)
#     os.makedirs(dst_val, exist_ok=True)
#     files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
#     random.shuffle(files)
#     split = int(len(files) * val_ratio)
#     for i, fname in enumerate(files):
#         src = os.path.join(src_dir, fname)
#         dst = dst_val if i < split else dst_train
#         shutil.copy(src, os.path.join(dst, fname))
#     print(f"Split {len(files)} files → {len(files)-split} train, {split} val in {os.path.basename(src_dir)}")

# if __name__ == "__main__":
#     import sys
#     src, train_dst, val_dst = sys.argv[1], sys.argv[2], sys.argv[3]
#     split_folder(src, train_dst, val_dst)

# splitdata.py
import os
import random
import shutil
import sys

def split_folder(src_dir, val_dst, val_ratio=0.2):
    os.makedirs(val_dst, exist_ok=True)
    
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(files)
    
    split = int(len(files) * val_ratio)
    val_files = files[:split]

    for fname in val_files:
        src = os.path.join(src_dir, fname)
        dst = os.path.join(val_dst, fname)
        shutil.move(src, dst)  # Move only to val

    print(f"Moved {split} images to {val_dst}, kept {len(files) - split} in {src_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python splitdata.py <source_folder> <val_output_folder>")
        sys.exit(1)

    src_dir = sys.argv[1]
    val_dir = sys.argv[2]
    
    split_folder(src_dir, val_dir)

