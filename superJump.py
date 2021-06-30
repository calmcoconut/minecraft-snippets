from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")
position = mc.player.getTilePos()
x,y,z = position.x,position.y,position.z

y+=80
mc.player.setTilePos(x,y,z)
