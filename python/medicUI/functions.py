from maya import OpenMaya, OpenMayaUI
from Qt import QtWidgets
from Qt.QtCompat import wrapInstance

BlankSelectionList = OpenMaya.MSelectionList()
if not hasattr(__builtins__, "long"):
    long = int


def ClearSelection():
    OpenMaya.MGlobal.setActiveSelectionList(BlankSelectionList)


def getMayaMainWindow():
    return wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QtWidgets.QMainWindow)


def registSceneOpenCallback(function):
    return OpenMaya.MEventMessage.addEventCallback("SceneOpened", function)


def registNewSceneOpenCallback(function):
    return OpenMaya.MEventMessage.addEventCallback("NewSceneOpened", function)


def removeCallbacks(ids):
    for id in ids:
        OpenMaya.MMessage.removeCallback(id)
