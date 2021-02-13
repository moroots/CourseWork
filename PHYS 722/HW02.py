# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:07:19 2021

@author: Magnolia
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
from copy import copy

class images:

    def __init__(self, filepath):
        self.image = io.imread(filepath)
        self.red = self.image[:, :, 0]
        self.green = self.image[:, :, 1]
        self.blue = self.image[:, :, 2]
        self.info = {'shape': self.image.shape,
                     'dtype': self.image.dtype,
                     'levels': [self.image.min(), self.image.max()],
                     'combos':  (self.image.max() + 1)**len(self.image[0,0,:])
                     }
        return

    def ndvi_rough(self):
        # if type(wav1) and type(wav2) is not list: print("inputs must be type: list")

        # ndvi = (self.green - self.blue) / (self.green + self.blue)
        # print(self.image[self.image[] == (97, 0, 0)])
        wav1 = copy(self.image); wav2 = copy(self.image);

        for i in range(0, len(self.image[:,0,0])):
            for j in range(0, len(self.image[0, :, 0])):
                if wav1[i, j, :] is not [97, 0, 0]:
                    wav1[i, j, :] = 0
                # wav2[self.image != (131, 0, 181)] = 0
        ndvi = (wav1 - wav2) / (wav1 + wav2)

        ndvi[np.isnan(ndvi)] = 0; ndvi[np.isinf(ndvi)] = 0

        fig, ax = plt.subplots(figsize = (10, 6))
        im = ax.imshow(ndvi, norm=colors.LogNorm(vmin=0.01, vmax=10), cmap='gist_earth')
        # im = ax.imshow(ndvi, vmin=0, vmax=10, cmap='gist_earth')
        fig.colorbar(im, ax=ax)

        # plt.imshow(test, cmap='hot')

        # fig, ax = plt.subplots(2,2,figsize=(10, 6))

        # ax[0, 0].imshow(self.image)

        # im = ax[1, 0].imshow(self.red, cmap='Reds')
        # divider = make_axes_locatable(ax[1,0])
        # cax = divider.append_axes("right", size="5%", pad=0.05)
        # fig.colorbar(im, cax=cax)

        # im = ax[0, 1].imshow(self.green, cmap='Greens')
        # divider = make_axes_locatable(ax[0,1])
        # cax = divider.append_axes("right", size="5%", pad=0.05)
        # fig.colorbar(im, cax=cax)

        # im = ax[1, 1].imshow(self.blue, cmap='Blues')
        # divider = make_axes_locatable(ax[1,1])
        # cax = divider.append_axes("right", size="5%", pad=0.05)
        # fig.colorbar(im, cax=cax)


        return wav1


    def channels(self, save=False, save_name='image', dpi=600):

        fig, ax = plt.subplots(2,2,figsize=(10, 6))

        ax[0, 0].imshow(self.image)

        im = ax[1, 0].imshow(self.red, cmap='Reds')
        divider = make_axes_locatable(ax[1,0])
        cax = divider.append_axes("right", size="5%", pad=0.05)
        fig.colorbar(im, cax=cax)

        im = ax[0, 1].imshow(self.green, cmap='Greens')
        divider = make_axes_locatable(ax[0,1])
        cax = divider.append_axes("right", size="5%", pad=0.05)
        fig.colorbar(im, cax=cax)

        im = ax[1, 1].imshow(self.blue, cmap='Blues')
        divider = make_axes_locatable(ax[1,1])
        cax = divider.append_axes("right", size="5%", pad=0.05)
        fig.colorbar(im, cax=cax)

        if save:
            plt.savefig(f'{save_name}.png', dpi=dpi)
            plt.savefig(f'{save_name}.jpg', dpi=dpi)
            print("Figures have been saved")

        return

# test = images("me_on_a_mountain.jpg")
# ndvi = test.ndvi_rough()
# channels = test.channels()


#%% TEstbed

test = images("me_on_a_mountain.jpg")

# if type(wav1) and type(wav2) is not list: print("inputs must be type: list")

# ndvi = (self.green - self.blue) / (self.green + self.blue)
# print(self.image[self.image[] == (97, 0, 0)])
wav1 = copy(io.img_as_float(test.red)); wav2 = copy(io.img_as_float(test.red));

'''
RGB (97, 0, 0)
Wavelength 780 nm
RGB value: #610000

RGB (255, 0, 0)
WAvelength: 650 nm
RGB value: #ff0000

Reference
https://www.w3schools.com/colors/colors_rgb.asp
https://www.johndcook.com/wavelength_to_RGB.html
'''

wav1[wav1 != 97] = np.Nan
wav2[wav2 != 255] = np.Nan
print(wav2.mean(), wav1.mean())
# for i in range(0, len(test.image[:,0,0])):
#     for j in range(0, len(test.image[0, :, 0])):
#         if wav1[i, j, :] is not [97, 0, 0]:
#             wav1[i, j, :] = 0
#         # wav2[self.image != (131, 0, 181)] = 0
ndvi = (wav1 - wav2) / (wav1 + wav2)

ndvi[np.isnan(ndvi)] = 0; ndvi[np.isinf(ndvi)] = 0

fig, ax = plt.subplots(figsize = (10, 6))
im = ax.imshow(wav1, norm=colors.LogNorm(vmin=0.01, vmax=10), cmap='gist_earth')
# im = ax.imshow(ndvi, vmin=0, vmax=10, cmap='gist_earth')
fig.colorbar(im, ax=ax)

fig, ax = plt.subplots(figsize = (10, 6))
im = ax.imshow(wav2, norm=colors.LogNorm(vmin=0.01, vmax=10), cmap='gist_earth')
# im = ax.imshow(ndvi, vmin=0, vmax=10, cmap='gist_earth')
fig.colorbar(im, ax=ax)

fig, ax = plt.subplots(figsize = (10, 6))
im = ax.imshow(ndvi, norm=colors.LogNorm(vmin=0.01, vmax=10), cmap='gist_earth')
# im = ax.imshow(ndvi, vmin=0, vmax=10, cmap='gist_earth')
fig.colorbar(im, ax=ax)

print(f"Theoretial NDVI: {(50 - 10) / (50 + 10)}")
print(f"Mean: {ndvi.mean()} \nMax: {ndvi.max()} \nMin: {ndvi.min()}")
print(f"NDVI: {(wav1.mean() - wav2.mean()) / (wav1.mean() + wav2.mean())}")


# plt.imshow(test, cmap='hot')

# fig, ax = plt.subplots(2,2,figsize=(10, 6))

# ax[0, 0].imshow(self.image)

# im = ax[1, 0].imshow(self.red, cmap='Reds')
# divider = make_axes_locatable(ax[1,0])
# cax = divider.append_axes("right", size="5%", pad=0.05)
# fig.colorbar(im, cax=cax)

# im = ax[0, 1].imshow(self.green, cmap='Greens')
# divider = make_axes_locatable(ax[0,1])
# cax = divider.append_axes("right", size="5%", pad=0.05)
# fig.colorbar(im, cax=cax)

# im = ax[1, 1].imshow(self.blue, cmap='Blues')
# divider = make_axes_locatable(ax[1,1])
# cax = divider.append_axes("right", size="5%", pad=0.05)
# fig.colorbar(im, cax=cax)







