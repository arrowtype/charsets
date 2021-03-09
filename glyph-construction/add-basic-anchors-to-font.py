"""
    Script for RoboFont.
    
    Adds anchors to glyphs in current font at a reasonable starter place, if they are not yet added.

    In some/most cases, it makes sense to adjust them after this, but it’s less clicking this way.

    This script is provided simply as an example, and may likely require adjustments from project to project.
"""
from vanilla.dialogs import *
from mojo.UI import AskYesNoCancel


replaceAnchors = AskYesNoCancel("Clear existing anchors in glyphs?")

files = getFile("Select files to set anchors in", allowsMultipleSelection=True, fileTypes=["ufo"])


lowerAlts = "a.italic g.italic"

upper = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
lower = [c for c in "abcdefghklmnopqrstuvwxyz"] + ["dotlessi", "dotlessj"] + lowerAlts.split(" ")
ascenders = [c for c in "bdfhklt"]


specialAnchors = {
    "A": {
        # place "top" anchor at middle top
        "ring": ("center", "boundsTop"), 
        # place "ogonek" at right-bottom corner of /A
        "ogonek": ("boundsRight", "baseline"),
    },
    "E": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "I": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "O": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "U": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "a": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "a.italic": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "e": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "e": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "dotlessi": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "o": {
        "ogonek": ("boundsRight", "baseline"),
    },
    "u": {
        "ogonek": ("boundsRight", "baseline"),
    },

}

# g.bounds = (x minimum, y minimum, x maximum, y maximum)

def getPos(glyph, positionName):

    if positionName == "center":
        return int(glyph.width / 2)

    if positionName == "boundsTop":
        return glyph.bounds[3]

    if positionName == "boundsBottom":
        return glyph.bounds[1]

    if positionName == "boundsLeft":
        return glyph.bounds[0]

    if positionName == "boundsRight":
        return glyph.bounds[2]

    if positionName == "baseline":
        return 0

    if positionName == "xHeight":
        return glyph.font.info.xHeight

    if positionName == "capHeight":
        return glyph.font.info.capHeight

    else:
        print()
        print(f"⚠️ Position name '{positionName}' incorrectly specified for glyph '{glyph.name}'.")
        print()


saveAndClose = AskYesNoCancel("Save & close fonts after adding anchors?")


def setBasicUpperAnchors(font, glyphName):
    """
        Set basic uppercase top/bottom anchors
    """
    if glyphName in font.keys():
        
        existingAnchors = [anchor.name for anchor in font[glyphName].anchors]

        for anchorName in ["top", "bottom"]:
            xPos = getPos(font[glyphName], "center")
            
            if anchorName == "top":
                yPos = font.info.capHeight
            if anchorName == "bottom":
                yPos = getPos(font[glyphName], "boundsBottom")

            if anchorName not in existingAnchors:
                font[glyphName].appendAnchor(anchorName,(xPos,yPos))


def setBasicLowerAnchors(font, glyphName):
    """
        Set basic lowercase top/bottom anchors
    """
    if glyphName in font.keys():
        
        existingAnchors = [anchor.name for anchor in font[glyphName].anchors]

        for anchorName in ["top", "bottom"]:
            xPos = getPos(font[glyphName], "center")

            if anchorName == "top" and glyphName not in ascenders:
                yPos = font.info.xHeight
            if anchorName == "top" and glyphName in ascenders:
                yPos = getPos(font[glyphName], "boundsTop")
            if anchorName == "bottom":
                yPos = getPos(font[glyphName], "boundsBottom")

            if anchorName not in existingAnchors:
                font[glyphName].appendAnchor(anchorName,(xPos,yPos))


def setSpecialCaseAnchors(font, glyphName):
    """
        Set special-case anchors
    """
    if glyphName in font.keys():

        existingAnchors = [anchor.name for anchor in font[glyphName].anchors]

        for anchorName in specialAnchors[glyphName].keys():

            xPos = getPos(font[glyphName], specialAnchors[glyphName][anchorName][0])
            yPos = getPos(font[glyphName], specialAnchors[glyphName][anchorName][1])

            if anchorName not in existingAnchors:
                font[glyphName].appendAnchor(anchorName,(xPos,yPos))


for file in files:
    if saveAndClose == 1:
        font = OpenFont(file, showInterface=False)
    elif saveAndClose == 0:
        font = OpenFont(file, showInterface=True)

    if replaceAnchors == 1:
        print("Clearing existing anchors in upper & lowercase glyphs.")
        for glyphName in upper + lower:
            if glyphName in font.keys():
                font[glyphName].clearAnchors()

    for glyphName in upper:
        setBasicUpperAnchors(font, glyphName)

    for glyphName in lower:
        setBasicLowerAnchors(font, glyphName)

    for glyphName in specialAnchors.keys():
        setSpecialCaseAnchors(font,glyphName)

    if saveAndClose == 1:
        font.save()
        font.close()
