import sys

sys.path.append("libs/jme3-core-3.3.0-SNAPSHOT.jar")
sys.path.append("libs/jme3-desktop-3.3.0-SNAPSHOT.jar")
sys.path.append("libs/jme3-lwjgl3-3.3.0-SNAPSHOT.jar")

sys.path.append("libs/lwjgl.jar")
sys.path.append("libs/lwjgl-natives-linux.jar")
sys.path.append("libs/lwjgl-opengl.jar")
sys.path.append("libs/lwjgl-opengl-natives-linux.jar")
sys.path.append("libs/lwjgl-glfw.jar")
sys.path.append("libs/lwjgl-glfw-natives-linux.jar")

import java.io.IOException

from com.jme3.app import SimpleApplication
from com.jme3.scene.shape import Box
from com.jme3.scene import Geometry
from com.jme3.material import Material
from com.jme3.math import ColorRGBA

#  Sample 1 - how to get started with the most simple JME 3 application.
#  Display a blue 3D cube and view from all sides by
#  moving the mouse and pressing the WASD keys.
class HelloJME3 (SimpleApplication):
    def simpleInitApp(self):
        b = Box(1, 1, 1)                      # create cube shape
        geom = Geometry("Box", b)             # create cube geometry from the shape
        mat = Material(assetManager,
        "Common/MatDefs/Misc/Unshaded.j3md")  # create a simple material
        mat.setColor("Color", ColorRGBA.Blue) # set color of material to blue
        geom.setMaterial(mat)                 # set the cube's material
        rootNode.attachChild(geom)            # make the cube appear in the scene

print "Hello world!"
app = HelloJME3()
app.start() # start the game
