import numpy as np
import cv2
from tqdm import tqdm

def video_creator(arrays, file='output.avi'):
    height = 200
    width = 200
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    fps = 1000
    video_filename = file
    out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))
    for n, array in tqdm(enumerate(arrays)):
        if n % 3 == 0:
            frame = frame_creator(array)
            frame = cv2.normalize(frame, None, 255, 0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            out.write(cv2.merge([frame, frame, frame]))
    out.release()

def column_creator(h, H):
    column = []
    for i in range(H):
        if i < h:
            column.append(1)
        else:
            column.append(0)
    return np.array(column[::-1], dtype=np.uint8)

def frame_creator(array):
    w = len(array)
    h = max(array)
    if h > w:
        print('Error -- H > W')
    else:
        frame = np.zeros((h, w), dtype=np.uint8)
        for j in range(w):
            frame[:, j] = column_creator(array[j], h)
        return frame*255

array = [i for i in range(1, 200 + 1)]
np.random.shuffle(array)

def bubble_sort_generator(array):
    arraycopy = array.copy()
    while True:
        arrays = []
        n = len(arraycopy)
        for i in range(n):
            for j in range(n - i - 1):
                if arraycopy[j] > arraycopy[j+1]:
                    arraycopy[j], arraycopy[j+1] = arraycopy[j+1], arraycopy[j]
                arrays.append(list(arraycopy))
        yield arrays

def selection_sort_generator(array):
    arraycopy = array.copy()
    while True:
        arrays = []
        n = len(arraycopy)
        for i in range(n): 
            min_idx = i 
            for j in range(i + 1, n): 
                if arraycopy[min_idx] > arraycopy[j]: 
                    min_idx = j        
            arraycopy[i], arraycopy[min_idx] = arraycopy[min_idx], arraycopy[i]
            arrays.append(list(arraycopy))
        yield arrays

#for arrays in bubble_sort_generator(array):
#    break
#
#video_creator(arrays,file='bubble_sort.avi')

#for arrays in selection_sort_generator(array):
#    break
#
#video_creator(arrays,file='selection_sort.avi')