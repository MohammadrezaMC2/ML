import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

########################### Parameters ##########################
rAvgDiam = 12  # diameter of averaging square in px
thrsHi = 12  # threshold above grey value of averaging area
thrsLo = 8  # threshold below grey value of averaging area
imgPath = r'C:\Users\a00566345\Desktop\Zu 5.2\Thresholding'
imgName = r'\Faint-Dent.bmp'

colorBrightDefect = (255, 0, 0, 50)
colorDarktDefect = (0, 0, 255, 50)
defectLabelOpacity = 0.3  # relative opacity of defect marking overly (MUST BE betwees 0 and 1)


# defectLabelOpacity=0 if defectLabelOpacity < 0 else defectLabelOpacity = 1 if defectLabelOpacity > 1


########################### FUNCTIONS ###########################

# create img mask from boolean array
def createDefectMask(boolArray, defectLabelOpacity):
    maskOpacity = defectLabelOpacity * 255.0
    output = np.multiply(boolArray, maskOpacity)
    output = Image.fromarray(output)
    output = output.convert('L')
    output = ImageOps.invert(output)
    return output


# overlay defect markers with original image
def makeResultIMG(colBrightDef, colDarkDefect, origImg, darkDMask, brightDMask):
    darkDefectColor = Image.new(mode='RGBA', size=origImg.size, color=colDarkDefect)
    brightDefectColor = Image.new(mode='RGBA', size=origImg.size, color=colBrightDef)

    imgOut = Image.composite(origImg, darkDefectColor, darkDMask)
    imgOut = Image.composite(imgOut, brightDefectColor, brightDMask)

    imgOut.show()
    # imgOut.save(imgPath + r'\Output.bmp')


########################### MAIN ###########################

def main(rAvgDiam, thrsHi, thrsLo, imgPath, imgName, colorBrightDefect, colorDarktDefect):
    img = Image.open(imgPath + imgName).convert('L')
    imgBlur = img.filter(ImageFilter.BoxBlur(rAvgDiam / 2))

    imgArr = np.asarray(img, dtype=int)
    imgBlurArr = np.asarray(imgBlur, dtype=int)

    diffArr = imgBlurArr - imgArr

    darkDefects = diffArr > thrsLo
    darkDefectMask = createDefectMask(darkDefects, defectLabelOpacity)
    # darkDefectsRel = diffArr-thrsLo
    # darkDefectsRel[darkDefectsRel<0]=0

    brightDefects = diffArr < (-1) * thrsHi
    brightDefectMask = createDefectMask(brightDefects, defectLabelOpacity)

    # build image
    makeResultIMG(colorBrightDefect, colorDarktDefect, img, darkDefectMask, brightDefectMask)


main(rAvgDiam, thrsHi, thrsLo, imgPath, imgName, colorBrightDefect, colorDarktDefect)