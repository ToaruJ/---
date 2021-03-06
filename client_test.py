from threading import Thread
from multiprocessing import Process, Queue, Pipe
from time import sleep
import tkinter as tk
from tkinter.messagebox import showinfo
from GameCore import GameCore
from PIL import ImageTk, Image, ImageDraw
from ClientDisplay import ClientDisplay
from copy import deepcopy
import DataTransPacks as pac
import socket
import time

def _thread_main(pipe):
    for i in range(10):
        if not pipe.empty():
            data = pipe.get()
            print(data)
        sleep(1)

init_dict = {'info': [1, 0, 5, 0, 1189, 0, 375],
             'tanks': [[1, 100, 50, 0, 18, 5.32, 4.52],
                       [2, 100, 50, 0, 0, 59.32, 50.82],
                       [3, 100, 50, 0, 0, 41.32, 42.52],
                       [4, 10, 90, 0, 0, 55.32, 47.52],
                       [5, 100, 50, 0, 0, 50.32, 40.52]],
             'bulls': [],
             'obs': [[4, 34], [5, 35], [5, 36], [6, 37], [7, 38], [8, 39], [8, 40], [9, 41], [10, 42], [10, 43], [11, 44], [12, 45], [12, 46], [13, 31], [13, 47], [14, 30], [14, 48], [15, 30], [15, 49], [15, 50], [16, 29], [16, 33], [16, 34], [16, 35], [16, 36], [16, 37], [16, 38], [16, 39], [16, 40], [16, 51], [17, 18], [17, 19], [17, 20], [17, 21], [17, 22], [17, 23], [17, 24], [17, 25], [17, 26], [17, 27], [17, 28], [17, 29], [17, 30], [17, 31], [17, 32], [17, 52], [17, 53], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [18, 28], [18, 54], [19, 28], [19, 55], [19, 56], [20, 27], [20, 57], [21, 27], [21, 58], [22, 26], [22, 59], [22, 60], [23, 26], [24, 25], [25, 25], [26, 24], [27, 24], [28, 23], [29, 22], [30, 22], [30, 27], [30, 28], [30, 29], [30, 30], [30, 31], [30, 32], [30, 33], [30, 34], [30, 35], [30, 36], [30, 37], [30, 38], [30, 39], [30, 40], [30, 41], [30, 42], [30, 43], [30, 44], [30, 45], [30, 46], [30, 47], [30, 48], [30, 49], [30, 50], [30, 51], [30, 52], [30, 53], [30, 54], [30, 55], [31, 21], [31, 27], [31, 28], [31, 29], [31, 30], [31, 31], [31, 32], [31, 33], [31, 34], [31, 35], [31, 36], [31, 37], [31, 38], [31, 39], [31, 40], [31, 41], [31, 42], [31, 43], [31, 44], [31, 45], [31, 46], [31, 47], [31, 48], [31, 49], [31, 50], [31, 51], [31, 52], [31, 53], [31, 54], [31, 55], [32, 21], [32, 27], [32, 28], [32, 29], [32, 30], [32, 31], [32, 32], [32, 33], [32, 34], [32, 35], [32, 36], [32, 37], [32, 38], [32, 39], [32, 40], [32, 41], [32, 42], [32, 43], [32, 44], [32, 45], [32, 46], [32, 47], [32, 48], [32, 49], [32, 50], [32, 51], [32, 52], [32, 53], [32, 54], [32, 55], [32, 58], [33, 20], [33, 27], [33, 28], [33, 29], [33, 30], [33, 31], [33, 32], [33, 33], [33, 34], [33, 35], [33, 36], [33, 37], [33, 38], [33, 39], [33, 40], [33, 41], [33, 42], [33, 43], [33, 44], [33, 45], [33, 46], [33, 47], [33, 48], [33, 49], [33, 50], [33, 51], [33, 52], [33, 53], [33, 54], [33, 55], [33, 59], [34, 20], [34, 27], [34, 28], [34, 29], [34, 30], [34, 31], [34, 32], [34, 33], [34, 34], [34, 35], [34, 36], [34, 37], [34, 38], [34, 39], [34, 40], [34, 41], [34, 42], [34, 43], [34, 44], [34, 45], [34, 46], [34, 47], [34, 48], [34, 49], [34, 50], [34, 51], [34, 52], [34, 53], [34, 54], [34, 55], [34, 60], [35, 19], [35, 27], [35, 28], [35, 29], [35, 30], [35, 31], [35, 32], [35, 33], [35, 34], [35, 35], [35, 36], [35, 37], [35, 38], [35, 39], [35, 40], [35, 41], [35, 42], [35, 43], [35, 44], [35, 45], [35, 46], [35, 47], [35, 48], [35, 49], [35, 50], [35, 51], [35, 52], [35, 53], [35, 54], [35, 55], [35, 61], [36, 19], [36, 27], [36, 28], [36, 29], [36, 30], [36, 31], [36, 32], [36, 33], [36, 34], [36, 35], [36, 36], [36, 46], [36, 47], [36, 48], [36, 49], [36, 50], [36, 51], [36, 52], [36, 53], [36, 54], [36, 55], [36, 62], [37, 18], [37, 27], [37, 28], [37, 29], [37, 30], [37, 31], [37, 32], [37, 33], [37, 34], [37, 37], [37, 38], [37, 39], [37, 40], [37, 41], [37, 42], [37, 43], [37, 44], [37, 45], [37, 48], [37, 49], [37, 50], [37, 51], [37, 52], [37, 53], [37, 54], [37, 55], [37, 63], [38, 18], [38, 27], [38, 28], [38, 29], [38, 30], [38, 31], [38, 32], [38, 35], [38, 36], [38, 37], [38, 38], [38, 39], [38, 40], [38, 41], [38, 42], [38, 43], [38, 44], [38, 45], [38, 46], [38, 47], [38, 50], [38, 51], [38, 52], [38, 53], [38, 54], [38, 55], [38, 64], [39, 17], [39, 27], [39, 28], [39, 29], [39, 30], [39, 33], [39, 34], [39, 35], [39, 36], [39, 37], [39, 38], [39, 39], [39, 40], [39, 41], [39, 42], [39, 43], [39, 44], [39, 45], [39, 46], [39, 47], [39, 48], [39, 49], [39, 52], [39, 53], [39, 54], [39, 55], [39, 64], [40, 17], [40, 27], [40, 28], [40, 29], [40, 31], [40, 32], [40, 33], [40, 34], [40, 35], [40, 36], [40, 37], [40, 38], [40, 39], [40, 40], [40, 41], [40, 42], [40, 43], [40, 44], [40, 45], [40, 46], [40, 47], [40, 48], [40, 49], [40, 50], [40, 51], [40, 53], [40, 54], [40, 55], [40, 65], [41, 16], [41, 27], [41, 28], [41, 30], [41, 31], [41, 32], [41, 33], [41, 34], [41, 35], [41, 36], [41, 37], [41, 38], [41, 39], [41, 40], [41, 41], [41, 42], [41, 43], [41, 44], [41, 45], [41, 46], [41, 47], [41, 48], [41, 49], [41, 50], [41, 51], [41, 52], [41, 54], [41, 55], [41, 66], [42, 16], [42, 27], [42, 29], [42, 30], [42, 31], [42, 32], [42, 33], [42, 34], [42, 35], [42, 36], [42, 37], [42, 38], [42, 39], [42, 40], [42, 41], [42, 42], [42, 43], [42, 44], [42, 45], [42, 46], [42, 47], [42, 48], [42, 49], [42, 50], [42, 51], [42, 52], [42, 53], [42, 55], [42, 67], [43, 28], [43, 29], [43, 30], [43, 31], [43, 32], [43, 33], [43, 34], [43, 35], [43, 36], [43, 37], [43, 38], [43, 39], [43, 40], [43, 41], [43, 42], [43, 43], [43, 44], [43, 45], [43, 46], [43, 47], [43, 48], [43, 49], [43, 50], [43, 51], [43, 52], [43, 53], [43, 54], [43, 68], [44, 28], [44, 29], [44, 30], [44, 31], [44, 32], [44, 33], [44, 34], [44, 35], [44, 36], [44, 37], [44, 38], [44, 39], [44, 40], [44, 41], [44, 42], [44, 43], [44, 44], [44, 45], [44, 46], [44, 47], [44, 48], [44, 49], [44, 50], [44, 51], [44, 52], [44, 53], [44, 54], [44, 69], [45, 27], [45, 28], [45, 29], [45, 30], [45, 31], [45, 32], [45, 33], [45, 34], [45, 35], [45, 36], [45, 37], [45, 38], [45, 39], [45, 40], [45, 41], [45, 42], [45, 43], [45, 44], [45, 45], [45, 46], [45, 47], [45, 48], [45, 49], [45, 50], [45, 51], [45, 52], [45, 53], [45, 54], [45, 55], [45, 70], [46, 27], [46, 28], [46, 29], [46, 30], [46, 31], [46, 32], [46, 33], [46, 34], [46, 35], [46, 36], [46, 37], [46, 38], [46, 39], [46, 40], [46, 41], [46, 42], [46, 43], [46, 44], [46, 45], [46, 46], [46, 47], [46, 48], [46, 49], [46, 50], [46, 51], [46, 52], [46, 53], [46, 54], [46, 55], [46, 71], [47, 27], [47, 28], [47, 29], [47, 30], [47, 31], [47, 32], [47, 33], [47, 34], [47, 35], [47, 36], [47, 37], [47, 38], [47, 39], [47, 40], [47, 41], [47, 42], [47, 43], [47, 44], [47, 45], [47, 46], [47, 47], [47, 48], [47, 49], [47, 50], [47, 51], [47, 52], [47, 53], [47, 54], [47, 55], [47, 72], [48, 27], [48, 28], [48, 29], [48, 30], [48, 31], [48, 32], [48, 33], [48, 34], [48, 35], [48, 36], [48, 37], [48, 38], [48, 39], [48, 40], [48, 41], [48, 42], [48, 43], [48, 44], [48, 45], [48, 46], [48, 47], [48, 48], [48, 49], [48, 50], [48, 51], [48, 52], [48, 53], [48, 54], [48, 55], [48, 73], [49, 7], [49, 27], [49, 28], [49, 29], [49, 30], [49, 31], [49, 32], [49, 33], [49, 34], [49, 35], [49, 36], [49, 37], [49, 38], [49, 39], [49, 40], [49, 41], [49, 42], [49, 43], [49, 44], [49, 45], [49, 46], [49, 47], [49, 48], [49, 49], [49, 50], [49, 51], [49, 52], [49, 53], [49, 54], [49, 55], [49, 74], [50, 8], [50, 27], [50, 28], [50, 29], [50, 30], [50, 31], [50, 32], [50, 33], [50, 34], [50, 35], [50, 36], [50, 37], [50, 38], [50, 39], [50, 40], [50, 41], [50, 42], [50, 43], [50, 44], [50, 45], [50, 46], [50, 47], [50, 48], [50, 49], [50, 50], [50, 51], [50, 52], [50, 53], [50, 54], [50, 55], [50, 75], [51, 9], [51, 27], [51, 28], [51, 29], [51, 30], [51, 31], [51, 32], [51, 33], [51, 34], [51, 35], [51, 36], [51, 37], [51, 38], [51, 39], [51, 40], [51, 41], [51, 42], [51, 43], [51, 44], [51, 45], [51, 46], [51, 47], [51, 48], [51, 49], [51, 50], [51, 51], [51, 52], [51, 53], [51, 54], [51, 55], [51, 75], [52, 10], [52, 27], [52, 28], [52, 29], [52, 30], [52, 31], [52, 32], [52, 33], [52, 34], [52, 35], [52, 36], [52, 37], [52, 38], [52, 39], [52, 40], [52, 41], [52, 42], [52, 43], [52, 44], [52, 45], [52, 46], [52, 47], [52, 48], [52, 49], [52, 50], [52, 51], [52, 52], [52, 53], [52, 54], [52, 55], [52, 76], [53, 11], [53, 27], [53, 28], [53, 29], [53, 30], [53, 31], [53, 32], [53, 33], [53, 34], [53, 35], [53, 36], [53, 37], [53, 38], [53, 39], [53, 40], [53, 41], [53, 42], [53, 43], [53, 44], [53, 45], [53, 46], [53, 47], [53, 48], [53, 49], [53, 50], [53, 51], [53, 52], [53, 53], [53, 54], [53, 55], [53, 77], [54, 12], [54, 27], [54, 28], [54, 29], [54, 30], [54, 31], [54, 32], [54, 33], [54, 34], [54, 35], [54, 36], [54, 37], [54, 38], [54, 39], [54, 40], [54, 41], [54, 42], [54, 43], [54, 44], [54, 45], [54, 46], [54, 47], [54, 48], [54, 49], [54, 50], [54, 51], [54, 52], [54, 53], [54, 54], [54, 55], [54, 78], [55, 13], [55, 27], [55, 28], [55, 29], [55, 30], [55, 31], [55, 32], [55, 33], [55, 34], [55, 35], [55, 36], [55, 37], [55, 38], [55, 39], [55, 40], [55, 41], [55, 42], [55, 43], [55, 44], [55, 45], [55, 46], [55, 47], [55, 48], [55, 49], [55, 50], [55, 51], [55, 52], [55, 53], [55, 54], [55, 55], [55, 79], [56, 14], [56, 27], [56, 28], [56, 29], [56, 30], [56, 31], [56, 32], [56, 33], [56, 34], [56, 35], [56, 36], [56, 37], [56, 38], [56, 39], [56, 40], [56, 41], [56, 42], [56, 43], [56, 44], [56, 45], [56, 46], [56, 47], [56, 48], [56, 49], [56, 50], [56, 51], [56, 52], [56, 53], [56, 54], [56, 55], [56, 80], [57, 15], [57, 27], [57, 28], [57, 29], [57, 30], [57, 31], [57, 32], [57, 33], [57, 34], [57, 35], [57, 36], [57, 37], [57, 38], [57, 39], [57, 40], [57, 41], [57, 42], [57, 43], [57, 44], [57, 45], [57, 46], [57, 47], [57, 48], [57, 49], [57, 50], [57, 51], [57, 52], [57, 53], [57, 54], [57, 55], [58, 16], [58, 27], [58, 28], [58, 29], [58, 30], [58, 31], [58, 32], [58, 33], [58, 34], [58, 35], [58, 36], [58, 37], [58, 38], [58, 39], [58, 40], [58, 41], [58, 42], [58, 43], [58, 44], [58, 45], [58, 46], [58, 47], [58, 48], [58, 49], [58, 50], [58, 51], [58, 52], [58, 53], [58, 54], [58, 55], [59, 16], [59, 27], [59, 28], [59, 29], [59, 30], [59, 31], [59, 32], [59, 33], [59, 34], [59, 35], [59, 36], [59, 37], [59, 38], [59, 39], [59, 40], [59, 41], [59, 42], [59, 43], [59, 44], [59, 45], [59, 46], [59, 47], [59, 48], [59, 49], [59, 50], [59, 51], [59, 52], [59, 53], [59, 54], [59, 55], [60, 17], [60, 46], [61, 18], [61, 45], [62, 19], [62, 44], [63, 20], [63, 43], [64, 21], [64, 42], [65, 22], [65, 40], [65, 41], [66, 23], [66, 39], [66, 46], [66, 47], [66, 48], [66, 49], [66, 50], [66, 51], [66, 53], [66, 54], [66, 55], [66, 56], [66, 57], [66, 58], [66, 59], [67, 24], [67, 38], [67, 46], [67, 47], [67, 48], [67, 49], [67, 52], [67, 53], [67, 54], [67, 55], [67, 56], [67, 57], [67, 58], [67, 59], [68, 25], [68, 37], [68, 46], [68, 47], [68, 50], [68, 51], [68, 52], [68, 53], [68, 54], [68, 55], [68, 56], [68, 57], [68, 58], [68, 59], [69, 36], [69, 48], [69, 49], [69, 50], [69, 51], [69, 52], [69, 53], [69, 54], [69, 55], [69, 56], [69, 57], [69, 58], [69, 59], [69, 72], [70, 35], [70, 46], [70, 47], [70, 48], [70, 49], [70, 50], [70, 51], [70, 52], [70, 53], [70, 54], [70, 55], [70, 56], [70, 57], [70, 58], [70, 59], [70, 70], [70, 71], [71, 34], [71, 46], [71, 47], [71, 48], [71, 49], [71, 50], [71, 51], [71, 52], [71, 53], [71, 54], [71, 55], [71, 56], [71, 57], [71, 58], [71, 59], [71, 69], [72, 33], [72, 46], [72, 47], [72, 48], [72, 49], [72, 50], [72, 51], [72, 52], [72, 53], [72, 54], [72, 55], [72, 56], [72, 57], [72, 58], [72, 59], [72, 67], [72, 68], [73, 32], [73, 46], [73, 47], [73, 48], [73, 49], [73, 50], [73, 51], [73, 52], [73, 53], [73, 54], [73, 55], [73, 56], [73, 57], [73, 58], [73, 59], [73, 66], [74, 31], [74, 46], [74, 47], [74, 48], [74, 49], [74, 50], [74, 51], [74, 52], [74, 53], [74, 54], [74, 55], [74, 56], [74, 57], [74, 58], [74, 59], [74, 64], [74, 65], [75, 46], [75, 47], [75, 48], [75, 49], [75, 50], [75, 51], [75, 52], [75, 53], [75, 54], [75, 55], [75, 56], [75, 57], [75, 58], [75, 59], [75, 62], [75, 63], [76, 46], [76, 47], [76, 48], [76, 49], [76, 50], [76, 51], [76, 52], [76, 53], [76, 54], [76, 55], [76, 56], [76, 57], [76, 58], [76, 59], [76, 61], [77, 46], [77, 47], [77, 48], [77, 49], [77, 50], [77, 51], [77, 52], [77, 53], [77, 54], [77, 55], [77, 56], [77, 57], [77, 58], [77, 59], [77, 60], [78, 46], [78, 47], [78, 48], [78, 49], [78, 50], [78, 51], [78, 52], [78, 53], [78, 54], [78, 55], [78, 56], [78, 57], [78, 58], [78, 59], [79, 28], [79, 46], [79, 47], [79, 48], [79, 49], [79, 50], [79, 51], [79, 52], [79, 53], [79, 54], [79, 55], [79, 56], [79, 57], [79, 58], [79, 59]],
             'props': [], 'safe': [1, 1, 99, 99, 1, 1, 99, 99],
             'grass': [[5, 60], [5, 61], [5, 62], [5, 63], [5, 64], [5, 65], [5, 66], [5, 67], [5, 68], [5, 69], [5, 70], [6, 60], [6, 61], [6, 62], [6, 63], [6, 64], [6, 65], [6, 66], [6, 67], [6, 68], [6, 69], [6, 70], [7, 60], [7, 61], [7, 62], [7, 63], [7, 64], [7, 65], [7, 66], [7, 67], [7, 68], [7, 69], [7, 70], [8, 60], [8, 61], [8, 62], [8, 63], [8, 64], [8, 65], [8, 66], [8, 67], [8, 68], [8, 69], [8, 70], [9, 60], [9, 61], [9, 62], [9, 63], [9, 64], [9, 65], [9, 66], [9, 67], [9, 68], [9, 69], [9, 70], [10, 60], [10, 61], [10, 62], [10, 63], [10, 64], [10, 65], [10, 66], [10, 67], [10, 68], [10, 69], [10, 70], [11, 60], [11, 61], [11, 62], [11, 63], [11, 64], [11, 65], [11, 66], [11, 67], [11, 68], [11, 69], [11, 70], [12, 60], [12, 61], [12, 62], [12, 63], [12, 64], [12, 65], [12, 66], [12, 67], [12, 68], [12, 69], [12, 70], [13, 60], [13, 61], [13, 62], [13, 63], [13, 64], [13, 65], [13, 66], [13, 67], [13, 68], [13, 69], [13, 70], [14, 60], [14, 61], [14, 62], [14, 63], [14, 64], [14, 65], [14, 66], [14, 67], [14, 68], [14, 69], [14, 70], [15, 60], [15, 61], [15, 62], [15, 63], [15, 64], [15, 65], [15, 66], [15, 67], [15, 68], [15, 69], [15, 70], [16, 60], [16, 61], [16, 62], [16, 63], [16, 64], [16, 65], [16, 66], [16, 67], [16, 68], [16, 69], [16, 70], [24, 48], [30, 26], [30, 68], [36, 37], [36, 38], [36, 39], [36, 40], [36, 41], [36, 42], [36, 43], [36, 44], [36, 45], [37, 35], [37, 36], [37, 46], [37, 47], [38, 33], [38, 34], [38, 48], [38, 49], [39, 31], [39, 32], [39, 50], [39, 51], [40, 30], [40, 52], [41, 29], [41, 53], [42, 28], [42, 54], [43, 27], [43, 55], [44, 27], [44, 55], [45, 18], [45, 26], [45, 56], [46, 26], [46, 56], [47, 25], [47, 57], [48, 25], [48, 57], [49, 24], [49, 58], [49, 71], [50, 24], [50, 58], [51, 24], [51, 58], [52, 24], [52, 58], [53, 24], [53, 58], [54, 24], [54, 58], [55, 24], [55, 58], [56, 24], [56, 58], [57, 24], [57, 58], [58, 25], [58, 57], [59, 25], [59, 57], [60, 26], [60, 56], [61, 26], [61, 56], [62, 27], [62, 55], [63, 27], [63, 55], [64, 28], [64, 54], [65, 29], [65, 53], [66, 30], [66, 52], [67, 31], [67, 32], [67, 50], [67, 51], [68, 33], [68, 34], [68, 48], [68, 49], [69, 35], [69, 46], [69, 47], [69, 71], [70, 37], [70, 38], [70, 39], [70, 40], [70, 41], [70, 42], [70, 43], [70, 44], [70, 45], [72, 16], [72, 17], [72, 18], [72, 19], [72, 20], [72, 21], [72, 22], [72, 23], [72, 24], [72, 25], [73, 16], [73, 17], [73, 18], [73, 19], [73, 20], [73, 21], [73, 22], [73, 23], [73, 24], [73, 25], [74, 16], [74, 17], [74, 18], [74, 19], [74, 20], [74, 21], [74, 22], [74, 23], [74, 24], [74, 25], [75, 16], [75, 17], [75, 18], [75, 19], [75, 20], [75, 21], [75, 22], [75, 23], [75, 24], [75, 25], [76, 16], [76, 17], [76, 18], [76, 19], [76, 20], [76, 21], [76, 22], [76, 23], [76, 24], [76, 25], [76, 33], [77, 16], [77, 17], [77, 18], [77, 19], [77, 20], [77, 21], [77, 22], [77, 23], [77, 24], [77, 25], [78, 16], [78, 17], [78, 18], [78, 19], [78, 20], [78, 21], [78, 22], [78, 23], [78, 24], [78, 25], [79, 16], [79, 17], [79, 18], [79, 19], [79, 20], [79, 21], [79, 22], [79, 23], [79, 24], [79, 25], [80, 16], [80, 17], [80, 18], [80, 19], [80, 20], [80, 21], [80, 22], [80, 23], [80, 24], [80, 25], [81, 16], [81, 17], [81, 18], [81, 19], [81, 20], [81, 21], [81, 22], [81, 23], [81, 24], [81, 25], [82, 16], [82, 17], [82, 18], [82, 19], [82, 20], [82, 21], [82, 22], [82, 23], [82, 24], [82, 25], [83, 16], [83, 17], [83, 18], [83, 19], [83, 20], [83, 21], [83, 22], [83, 23], [83, 24], [83, 25], [84, 16], [84, 17], [84, 18], [84, 19], [84, 20], [84, 21], [84, 22], [84, 23], [84, 24], [84, 25], [85, 16], [85, 17], [85, 18], [85, 19], [85, 20], [85, 21], [85, 22], [85, 23], [85, 24], [85, 25], [89, 41]]}


class GamePage(tk.Frame):
    """
    开始游戏后的界面
    """
    def __init__(self, master, connector, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.connect = connector
        self.mapdisplay = None

        self.canvas_main = tk.Canvas(self, width=600, height=600)
        self.canvas_main.pack(padx=5, pady=5)
        self.frame1 = tk.Frame(self)
        self.frame1.pack(side=tk.BOTTOM, padx=10, pady=5)
        tk.Label(self.frame1, text='生命值').pack(side=tk.LEFT, padx=10, pady=5)
        self.label_hp = tk.Label(self.frame1, text='')
        self.label_hp.pack(side=tk.LEFT, padx=(10, 30), pady=5)
        tk.Label(self.frame1, text='子弹数').pack(side=tk.LEFT, padx=(30, 10), pady=5)
        self.label_bullet = tk.Label(self.frame1, text='')
        self.label_bullet.pack(side=tk.LEFT, padx=(10, 30), pady=5)
        tk.Label(self.frame1, text='杀敌').pack(side=tk.LEFT, padx=(30, 10), pady=5)
        self.label_kill = tk.Label(self.frame1, text='')
        self.label_kill.pack(side=tk.LEFT, padx=(10, 30), pady=5)
        tk.Label(self.frame1, text='剩余玩家').pack(side=tk.LEFT, padx=(30, 10), pady=5)
        self.rank = tk.IntVar()
        self.label_rank = tk.Label(self.frame1, textvariable=self.rank)
        self.label_rank.pack(side=tk.LEFT, padx=10, pady=5)

        self.all_map = None
        self.small_map = None
        self.delay = 0
        self.player_id = 0
        self.key_down = {'Up': 0, 'Down': 0, 'Left': 0, 'Right': 0, 'fire': 0}  # 按下的按键
        self.game_end = False

        self.gamecore = GameCore(2)

    def key_handler(self, event):
        """
        对按键事件的响应，持续按则持续响应
        :param event: 按键类型事件
        """
        if event.keysym == 'Up' or event.keysym.lower() == 'w':
            self.key_down['Up'] = 1
        elif event.keysym == 'Down' or event.keysym.lower() == 's':
            self.key_down['Down'] = 1
        elif event.keysym == 'Left' or event.keysym.lower() == 'a':
            self.key_down['Left'] = 1
        elif event.keysym == 'Right' or event.keysym.lower() == 'd':
            self.key_down['Right'] = 1
        elif event.keysym == 'Return' or event.keysym == 'space':
            self.key_down['fire'] = 1

    def game_start(self, mapdata, playerid):
        """
        游戏的初始化
        """
        self.game_end = False
        self.player_id = playerid
        self.delay = 0

        self.gamecore.game_init(mapdata, [playerid, 1])

        self._readplayer_info(mapdata['tanks'])
        self.mapdisplay = ClientDisplay(mapdata, self.player_id)

        self.master.bind('<KeyPress>', self.key_handler)
        self.after(0, self._game)
        self.after(0, self._key_trans)

    def _game(self):
        """
        游戏30帧主循环
        """
        if not self.game_end:
            #data = self.connect.get_udp_data()
            self.after(int(self.delay) + 1, self._game)
            self.gamecore.gaming()
            data = self.gamecore.output_data()
            if data:
                self.mapdisplay.changedict(data)
                nowtime = time.time()
                allmap = self.mapdisplay.Draw()
                smallmap = self.mapdisplay.SmallMap()
                self.canvas_main.delete(tk.ALL)
                del self.all_map
                del self.small_map
                self.all_map = ImageTk.PhotoImage(allmap)
                self.small_map = ImageTk.PhotoImage(smallmap)
                self.canvas_main.create_image(0, 0, anchor=tk.NW,
                                              image=self.all_map)
                self.canvas_main.create_image(0, 0, anchor=tk.NW,
                                              image=self.small_map)
                self.delay = (time.time() - nowtime) * 1000
                if self.delay > 30:
                    print(self.delay)
                else:
                    self.delay = 30
                if 'tanks' in data:
                    self._readplayer_info(data['tanks'])
                if int(self.label_hp['text']) <= 0:
                    self.after(0, self.ending)
                elif 'info' in data and data['info'][1] >= 0 and int(self.label_hp['text']) > 0:
                    self.after(0, self.ending)
                if len(data['props']) > 0:
                    print("props", data['props'])
                # print('yes')

    def _key_trans(self):
        """
        对用户按键处理
        """
        if not self.game_end:
            keydict = deepcopy(self.key_down)
            keydict['id'] = self.player_id
            delay = 50
            for value in self.key_down.values():
                if value == 1:
                    delay = 50
                    #self.connect.send_data_udp(keydict)
                    self.gamecore.input_data(keydict)
                    break
            self.key_down = {'Up': 0, 'Down': 0, 'Left': 0, 'Right': 0, 'fire': 0}
            self.after(delay, self._key_trans)

    def _readplayer_info(self, tanks):
        '''
        传入从服务器来的坦克信息列表，更改自己的信息
        '''
        self.rank.set(len(tanks))
        for tank in tanks:
            if tank[0] == self.player_id:
                self.label_hp.config(text=tank[1])
                self.label_bullet.config(text=tank[2])
                self.label_kill.config(text=tank[3])
                break

    def ending(self):
        """
        游戏结束相关处理
        """
        self.game_end = True
        # self.connect.game_end()
        # self.master.toMenuPage()


if __name__ == '__main__':

    tki = tk.Tk()
    tki.geometry('%dx%d+%d+%d' % (800, 700, tki.winfo_screenwidth() / 2 - 400,
                                  tki.winfo_screenheight() / 2 - 350))
    gamepage = GamePage(tki, None)
    gamepage.place(in_=tki, x=0, y=0, relwidth=1, relheight=1)
    gamepage.game_start(init_dict, 4)
    tki.mainloop()

    '''
    tki = tk.Tk()
    tki.geometry('%dx%d+%d+%d' % (800, 700, tki.winfo_screenwidth() / 2 - 400,
                                  tki.winfo_screenheight() / 2 - 350))
    canvas = tk.Canvas(tki, width=500, height=500)
    canvas.pack()
    img = Image.new("RGB", (500,500), (192,192,192))
    draw = ImageDraw.ImageDraw(img)
    draw.ellipse((100, 100, 200,200), 'red')
    bmptk = ImageTk.BitmapImage(img)
    canvas.create_bitmap(0,0,anchor=tk.NW, bitmap=bmptk)
    draw.ellipse((200, 200, 300, 300), 'blue')
    tki.mainloop()
    '''
    # gamepage.ending()

