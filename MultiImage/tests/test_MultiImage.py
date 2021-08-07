#pylint: disable=C0103, C0301
"""
Testing Suite for MultiImage class.
"""
__author__ = "Noupin"

#Third Party Imports
import numpy as np
from PIL import Image

#First Party Imports
from .. import MultiImage
from ..utils.image import loadImage, CVToPIL


multiImage = MultiImage(r"test.png")


def test_StringConstructor():
    image = MultiImage(r"test.png")

    assert isinstance(image, MultiImage)


def test_CVConstructor():
    npImage = loadImage(r"test.png")
    image = MultiImage(npImage)

    assert isinstance(image, MultiImage)


def test_PILConstructor():
    npImage = loadImage(r"test.png")
    PILImage = CVToPIL(npImage)
    image = MultiImage(PILImage)

    assert isinstance(image, MultiImage)


def test_PILImageType():
    assert isinstance(multiImage.PILImage, Image.Image)


def test_CVImageType():
    assert isinstance(multiImage.CVImage, np.ndarray)
    assert multiImage.CVImage.dtype == np.uint8
    
    assert isinstance(multiImage.CVBGRImage, np.ndarray)
    assert multiImage.CVBGRImage.dtype == np.uint8


def test_encodeImage():
    assert isinstance(multiImage.encode(), str)
