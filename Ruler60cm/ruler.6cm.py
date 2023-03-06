import Part
import Draft
from FreeCAD import Base

rump = Part.makeBox(60, 20, 1)

def makeMarks(rump, stepNum, length, stepLength):
    for x in range(1, stepNum):
        box = Part.makeBox(0.2, length, 1)
        myvec = FreeCAD.Vector(x * stepLength - 0.1, 20 - length, 0)
        box.Placement.Base = myvec
        rump = rump.cut(box)
    return rump

# Extrude Text
def createExtrudedText(String, FontFile, Size, Tracking):
    ss = Draft.make_shapestring(String, FontFile, Size, Tracking)
    # Gui.runCommand('Part_Extrude',0)
    f = App.getDocument('Unnamed').addObject('Part::Extrusion','Extrude')
    # f = App.getDocument('Unnamed').getObject('Extrude')
    f.Base = ss
    f.DirMode = "Normal"
    f.DirLink = None
    f.LengthFwd = 1.0
    f.LengthRev = 0.000000000000000
    f.Solid = False
    f.Reversed = False
    f.Symmetric = False
    f.TaperAngle = 0.000000000000000
    f.TaperAngleRev = 0.000000000000000
    return [f, ss]

# 10 mm marks
rump = makeMarks(rump, 6, 10, 10)
# 5 mm marks
rump = makeMarks(rump, 12, 5, 5)
# 1 mm marks
rump = makeMarks(rump, 60, 2, 1)

for x in range (1, 7):

    [f, ss] = createExtrudedText(str(x), "C:/Windows/Fonts/Calibri.ttf", 5, 0.0)
    myvec = FreeCAD.Vector(-5 + x * 10, 9, 0)
    ss.Placement.Base = myvec
    # rump.cut(f)
# rump = rump.cut(f)
# pl = FreeCAD.Vector(3, 3, 3)
# text = Draft.make_text("1", placement=pl)

#rump.cut(text)

Part.show(rump)
# doc.recompute()
Gui.activeDocument().activeView().viewAxometric()
FreeCAD.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
