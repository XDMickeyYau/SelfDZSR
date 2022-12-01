# %%
import cv2
import os
import itertools

# %%
def read_img(hr_dir,sr_dir,file,seq):
    name, ext = os.path.splitext(file)
    hr = cv2.imread(os.path.join(hr_dir, name+ext))
    sr = cv2.imread(os.path.join(sr_dir, name+seq+ext))
    assert hr is not None and sr is not None
    return hr, sr

# %%
def write_img(sr_out,sr_out_dir,file,seq):
    name, ext = os.path.splitext(file)
    assert cv2.imwrite(os.path.join(sr_out_dir, name+seq+ext),sr_out)

# %%
def match_size(hr,sr):
    hr_shape = hr.shape[:2]
    sr_shape = sr.shape[:2]
    if hr_shape != sr_shape:
        sr_out = cv2.resize(sr,hr_shape[::-1])
    else:
        sr_out = sr
    return sr_out
    

# %% [markdown]
# Interface

# %%
def match_size_single(hr_dir,sr_dir,file,seq=""):
    hr, sr = read_img(hr_dir,sr_dir,file,seq)
    sr_out = match_size(hr, sr)
    return sr_out

# %%
def match_size_multiple(hr_dir,sr_dir,sr_out_dir,seqs=[""]):
    os.makedirs(sr_out_dir,exist_ok=True)
    files = os.listdir(hr_dir)
    print("files",files)
    for file, seq in itertools.product(files,seqs):
        sr_out = match_size_single(hr_dir,sr_dir,file,seq)
        write_img(sr_out,sr_out_dir,file,seq)    

# %% [markdown]
# main

# %%
def __main__():
    hr_dir = "HR_raw"
    sr_dir = "HR_mismatch"
    sr_out_dir = "HR_match"
    seqs = [""]
    match_size_multiple(hr_dir,sr_dir,sr_out_dir,seqs)

# %%
#__main__()


