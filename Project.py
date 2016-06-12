import maya.cmds as cmds
import pymel.core as pmc

#mel.eval() za time sliderot(evaluacija na mel)

def setVis(str):
    
    cmds.setAttr( str, 0 )

def linear_cycle(planet):
    cmds.selectKey( planet, keyframe=True)
    cmds.keyTangent( inTangentType ='linear', outTangentType='linear' )          
    cmds.setInfinity ( poi='cycle' )

def slowAnimation( win ):

    objList = cmds.ls( 'my*' )
    
    if objList > 0:
        cmds.delete( objList )
    
    nice_try = cmds.polySphere( name='mySun', sx=True, sy=True )
    cmds.move( 0, 0, 0, nice_try )
    cmds.scale( 8, 8, 8, nice_try )
    orbitOfMercury=cmds.circle( nr=(0, 1, 0 ), c=(0, 0, 0),r=11.5 ,name='myOrbitMercury' )
    setVis( 'myOrbitMercury.visibility' )
    orbitOfVenus=cmds.circle( nr=(0, 1, 0 ), c=(0, 2, 0),r=15.5 ,name='myOrbitVenus' )
    setVis( 'myOrbitVenus.visibility' )
    orbitOfEarth=cmds.circle( nr=(0, 1, 0 ), c=(0, 4, 0),r=20.5 ,name='myOrbitEarth' )
    setVis( 'myOrbitEarth.visibility' )
    orbitOfMars=cmds.circle( nr=(0, 1, 0 ), c=(0, 6, 0),r=25.5 ,name='myOrbitMars' )
    setVis( 'myOrbitMars.visibility' )
    orbitOfJupiter=cmds.circle( nr=(0, 1, 0 ), c=(0, 8, 0),r=35.5 ,name='myOrbitJupiter' )
    setVis( 'myOrbitJupiter.visibility' )
    orbitOfSaturn=cmds.circle( nr=(0, 1, 0 ), c=(0, 10, 0),r=45.5 ,name='myOrbitSaturn' )
    setVis( 'myOrbitSaturn.visibility' )
    orbitOfUranus=cmds.circle( nr=(0, 1, 0 ), c=(0, 12, 0),r=53 ,name='myOrbitUranus' )
    setVis( 'myOrbitUranus.visibility' )
    orbitOfNeptune=cmds.circle( nr=(0, 1, 0 ), c=(0, 14, 0),r=60.5 ,name='myOrbitNeptune' )
    setVis( 'myOrbitNeptune.visibility' )
    orbitOfPluto=cmds.circle( nr=(0, 1, 0.2 ), c=(0, 16, 0),r=67 ,name='myOrbitPluto' )
    setVis( 'myOrbitPluto.visibility' )
    planetMercury=cmds.polySphere( name='myPlanetMercury', sx=True, sy=True )
    cmds.scale( 0.9, 0.9, 0.9, planetMercury )
    planetVenus=cmds.polySphere( name='myPlanetVenus', sx=True, sy=True )
    cmds.scale( 1.5, 1.5, 1.5, planetVenus )
    planetEarth=cmds.polySphere( name='myPlanetEarth', sx=True, sy=True )
    cmds.scale( 1.5, 1.5, 1.5, planetEarth )
    planetMars=cmds.polySphere( name='myPlanetMars', sx=True, sy=True )
    cmds.scale( 1.2, 1.2, 1.2, planetMars )
    planetJupiter=cmds.polySphere( name='myPlanetJupiter', sx=True, sy=True )
    cmds.scale( 4.5, 4.5, 4.5, planetJupiter )
    planetSaturn=cmds.polySphere( name='myPlanetSaturn', sx=True, sy=True )
    cmds.scale( 3.4, 3.4, 3.4, planetSaturn )
    planetUranus=cmds.polySphere( name='myPlanetUranus', sx=True, sy=True )
    cmds.scale( 2.5, 2.5, 2.5, planetUranus )
    planetNeptune=cmds.polySphere( name='myPlanetNeptune', sx=True, sy=True )
    cmds.scale( 2.5, 2.5, 2.5, planetNeptune )
    planetPluto=cmds.polySphere( name='myPlanetPluto', sx=True, sy=True )
    cmds.scale( 0.8, 0.8, 0.8, planetPluto )
    
    mtpMercury = cmds.pathAnimation( planetMercury, orbitOfMercury, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=880 )
    mtpVenus = cmds.pathAnimation( planetVenus, orbitOfVenus, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=225 )
    mtpEarth = cmds.pathAnimation( planetEarth, orbitOfEarth, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=365 )
    mtpMars = cmds.pathAnimation( planetMars, orbitOfMars, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=2300 )
    mtpJupiter = cmds.pathAnimation( planetJupiter, orbitOfJupiter, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=1150 )
    mtpSaturn = cmds.pathAnimation( planetSaturn, orbitOfSaturn, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=3000 )
    mtpUranus = cmds.pathAnimation( planetUranus, orbitOfUranus, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=8400.0 )
    mtpNeptune = cmds.pathAnimation( planetNeptune, orbitOfNeptune, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=16500 )
    mtpPluto = cmds.pathAnimation( planetPluto, orbitOfPluto, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=24800 )
    
    
    linear_cycle( mtpMercury )
    linear_cycle( mtpVenus )
    linear_cycle( mtpEarth )
    linear_cycle( mtpMars )
    linear_cycle( mtpJupiter )
    linear_cycle( mtpSaturn )
    linear_cycle( mtpUranus )
    linear_cycle( mtpNeptune )
    linear_cycle( mtpPluto )
    cmds.playbackOptions( max=24800 )
    pmc.deleteUI( win )
    
def fastAnimation( win ):

    objList = cmds.ls( 'my*' )
    
    if objList > 0:
        cmds.delete( objList )
    
    nice_try = cmds.polySphere( name='mySun', sx=True, sy=True )
    cmds.move( 0, 0, 0, nice_try )
    cmds.scale( 8, 8, 8, nice_try )
    orbitOfMercury=cmds.circle( nr=(0, 1, 0 ), c=(0, 0, 0),r=11.5 ,name='myOrbitMercury' )
    setVis( 'myOrbitMercury.visibility' )
    orbitOfVenus=cmds.circle( nr=(0, 1, 0 ), c=(0, 2, 0),r=15.5 ,name='myOrbitVenus' )
    setVis( 'myOrbitVenus.visibility' )
    orbitOfEarth=cmds.circle( nr=(0, 1, 0 ), c=(0, 4, 0),r=20.5 ,name='myOrbitEarth' )
    setVis( 'myOrbitEarth.visibility' )
    orbitOfMars=cmds.circle( nr=(0, 1, 0 ), c=(0, 6, 0),r=25.5 ,name='myOrbitMars' )
    setVis( 'myOrbitMars.visibility' )
    orbitOfJupiter=cmds.circle( nr=(0, 1, 0 ), c=(0, 8, 0),r=35.5 ,name='myOrbitJupiter' )
    setVis( 'myOrbitJupiter.visibility' )
    orbitOfSaturn=cmds.circle( nr=(0, 1, 0 ), c=(0, 10, 0),r=45.5 ,name='myOrbitSaturn' )
    setVis( 'myOrbitSaturn.visibility' )
    orbitOfUranus=cmds.circle( nr=(0, 1, 0 ), c=(0, 12, 0),r=53 ,name='myOrbitUranus' )
    setVis( 'myOrbitUranus.visibility' )
    orbitOfNeptune=cmds.circle( nr=(0, 1, 0 ), c=(0, 14, 0),r=60.5 ,name='myOrbitNeptune' )
    setVis( 'myOrbitNeptune.visibility' )
    orbitOfPluto=cmds.circle( nr=(0, 1, 0.2 ), c=(0, 16, 0),r=67 ,name='myOrbitPluto' )
    setVis( 'myOrbitPluto.visibility' )
    planetMercury=cmds.polySphere( name='myPlanetMercury', sx=True, sy=True )
    cmds.scale( 0.9, 0.9, 0.9, planetMercury )
    planetVenus=cmds.polySphere( name='myPlanetVenus', sx=True, sy=True )
    cmds.scale( 1.5, 1.5, 1.5, planetVenus )
    planetEarth=cmds.polySphere( name='myPlanetEarth', sx=True, sy=True )
    cmds.scale( 1.5, 1.5, 1.5, planetEarth )
    planetMars=cmds.polySphere( name='myPlanetMars', sx=True, sy=True )
    cmds.scale( 1.2, 1.2, 1.2, planetMars )
    planetJupiter=cmds.polySphere( name='myPlanetJupiter', sx=True, sy=True )
    cmds.scale( 4.5, 4.5, 4.5, planetJupiter )
    planetSaturn=cmds.polySphere( name='myPlanetSaturn', sx=True, sy=True )
    cmds.scale( 3.4, 3.4, 3.4, planetSaturn )
    planetUranus=cmds.polySphere( name='myPlanetUranus', sx=True, sy=True )
    cmds.scale( 2.5, 2.5, 2.5, planetUranus )
    planetNeptune=cmds.polySphere( name='myPlanetNeptune', sx=True, sy=True )
    cmds.scale( 2.5, 2.5, 2.5, planetNeptune )
    planetPluto=cmds.polySphere( name='myPlanetPluto', sx=True, sy=True )
    cmds.scale( 0.8, 0.8, 0.8, planetPluto )
    
    mtpMercury = cmds.pathAnimation( planetMercury, orbitOfMercury, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=88 )
    mtpVenus = cmds.pathAnimation( planetVenus, orbitOfVenus, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=25 )
    mtpEarth = cmds.pathAnimation( planetEarth, orbitOfEarth, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=65 )
    mtpMars = cmds.pathAnimation( planetMars, orbitOfMars, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=200 )
    mtpJupiter = cmds.pathAnimation( planetJupiter, orbitOfJupiter, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=150 )
    mtpSaturn = cmds.pathAnimation( planetSaturn, orbitOfSaturn, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=300 )
    mtpUranus = cmds.pathAnimation( planetUranus, orbitOfUranus, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=800 )
    mtpNeptune = cmds.pathAnimation( planetNeptune, orbitOfNeptune, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=6500 )
    mtpPluto = cmds.pathAnimation( planetPluto, orbitOfPluto, f=True, fa='x', fm=True, ua='y', stu=1.0, etu=4800 )
    
    
    linear_cycle( mtpMercury )
    linear_cycle( mtpVenus )
    linear_cycle( mtpEarth )
    linear_cycle( mtpMars )
    linear_cycle( mtpJupiter )
    linear_cycle( mtpSaturn )
    linear_cycle( mtpUranus )
    linear_cycle( mtpNeptune )
    linear_cycle( mtpPluto )
    cmds.playbackOptions( max=4800 )
    pmc.deleteUI(win)
    

win = pmc.window( title="Animation" )
gridLayout = pmc.gridLayout( nr=2, nc=1, cwh=(180, 80) )
strText = 'if you want animation to be fast click on the "Fast animation" button, else if you want animation to be slower click in "Slow animation" button'    
ExpText = pmc.text( label = strText, align='left', ww=True, parent=gridLayout )
flowLayout = pmc.flowLayout( columnSpacing=20, parent=gridLayout )
btnSlow = pmc.button( label='Slow animation', parent=flowLayout, command=lambda *args: slowAnimation(win) )
btnFast = pmc.button( label='Fast animation', parent=flowLayout, command=lambda *args: fastAnimation(win) )
pmc.windowPref( win, wh=( 180, 100) , le=300, te=300 )

win.show()


    
    
