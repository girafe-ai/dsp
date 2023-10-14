import scipy
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def deconvolve(x, y):
    y = y[:len(x)]
    X = np.fft.rfft(x)
    Y = np.fft.rfft(y)
    H = Y/X
    h = np.fft.irfft(H)
    return h


orig, sr = sf.read('/Users/i.beskrovnyy/examples/fav_file/gt.wav')
reverb, _ = sf.read('/Users/i.beskrovnyy/examples/fav_file/reverbed/29a46458-7b7e-11ed-a04c-acde48001122.wav')

h = deconvolve(orig, reverb)

# print(h)

plt.plot(h)
plt.show()

restore_rev = scipy.signal.fftconvolve(orig, h, 'full')[:len(orig)]
sf.write('restore.wav', restore_rev, sr)
