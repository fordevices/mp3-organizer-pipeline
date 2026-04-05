OpenGL Readme file Rev 1 for Winamp OpenGL plugins 
---------------------------------------------------

Prince's 3D OpenGL plugins for Winamp.
by CJ Cliffe



Quick Info:
-----------

If you feel the plugins are running extremely slow, and have very poor image
quality, than you may not have downloaded the correct ICD for your card, or you
may have placed it in the improper directory.  Make sure your OpenGL32.DLL is 
in the same directory as WINAMP.EXE, NOT IN THE PLUGINS DIRECTORY...

3Dfx owners will have to rename 3Dfxopengl.dll to OpenGL32.DLL before it will work!

Don't forget to press [SpaceBar] to change textures!



Table of Contents
-----------------

1. Finding the right ICD (or MCD) for your video card.
	1.1 Figuring out which video card you have
	1.2 Finding out where to get the ICD (or MCD) for your card
	1.3 Installing the ICD so that Winamp can use it
	
2. Errors
	1.1 Errors in Wa3dgl.dll and what they mean










[Section 1:   Finding the right ICD (or MCD) for your video card.]


	1.1 Figuring out which video card you have:
	-------------------------------------------
	In most cases you should already know what 3D accelerator is in
	your computer, because MOST computers do NOT ship with a 3D accelerator
	card (exception of DELL and a few others which ship with FireGL)
	the most common reason for having a 3D accelerator is because
	you specifically bought one as an add-on.

	If you don't know, the easiest way to find out is to check your device
	manager.   To open your device manager, right-click the mouse on the 
	"My Computer" icon on your desktop and select "Properties".   From there 
	select the "devices" tab.  Expand the "Display adapters" option on the list.

	If you have a 3Dfx card, it may be listed under the "Multimedia" section
	or "Video and Game adapters"
	
	You should now have a list of all the display adapters in your system,
	jot down the name/manufacturer of your card, and proceed to step 1.2



	
	
	1.2 Finding out where to get the ICD (or MCD) for your card
	-----------------------------------------------------------
	Now that you know the manufacturer and name of your card, you can
	try to go to the website for that manufacturer.

	some common manufacturers are:

	Creative Labs: www.creativelabs.com
	Diamond Multimedia: www.diamondmm.com
	Canopus Corporation: www.canopus.com
	STB (Simply The Best): www.stb.com
	
	and, for all 3Dfx Voodoo Graphics cards:

	www.3dfx.com


	IF you have an OpenGL driver for Quake2 for your card, you MAY be able
	to use it to run the plugins,  I have had success using the Quake2 MCD
	for Rendition and 3Dfx with the plugins, if the plugins behave irratically
	while using the MCD, discontinue use of it..


	
	If you're unable to find the driver for your card, try doing a search
	on www.altavista.com or your 
	favourite search engine for:
 					 "<card name> opengl icd"	




	


	1.3 Installing the ICD so that Winamp can use it
	------------------------------------------------
	Although you installed the plugins into your Winamp\Plugins directory, you 
	are required to place your OpenGL ICD in the same directory as Winamp,
	meaning your OpenGL32.dll has to be in the same directory as Winamp.exe

	If you fail to install the correct driver, you may recieve an error, 
	or, the plugins will run very slowly.

	Some card manufacturers such as 3Dfx have decided to name their DLL's
	incorrectly, 3Dfx users will have to RENAME 3DfxopenGL.dll to OpenGL32.dll
	before they can use it.











[Section 2: Errors]


	1.1 Errors in Wa3dgl.dll and what they mean
	-------------------------------------------

	
Error:	Unable to resolve <functionname> please consult ReadmeGL.txt

What this means:
	
	The OpenGL32.dll you are using doesn't contain the proper functions, you should
	make sure that if you're using a Quake2 MCD that it is indeed the latest version
	and is the proper device for your card.

	If you're sure you have the latest driver for your card, contact your 
	manufacturer and inform them of the missing functions.






Error: Unable to Load <dllname> please consult ReadmeGL.txt

What this means:

	If it's unable to load OPENGL32.DLL, please consult Section 1 of this file,
	ensure that you've got the correct driver for your card, and that it is indeed
	the newest driver.   And make sure if you have a 3Dfx that you remembered to
	rename 3Dfxopengl.dll to Opengl32.dll before copying it into the Winamp directory.


	If it's unable to load GLU32.DLL this means you are using an older version of
	Windows95 that didn't contain OpenGL support.  Obtain a Windows95b CD and upgrade
	your system, or download a copy of GLU32.DLL off a friend and place it in your
	C:\Windows\System directory.  It should also be	available at 
	http://wa3dgl.home.ml.org on the downloads page.























Fin.
	


	