import ListShuffle
import OrgaincAlphaFeather
import nuke

# nuke.pluginAddPath('./icons',addToSysPath=False)
# nuke.pluginAddPath('./gizmos',addToSysPath=False)



my_menu = nuke.menu('Nodes').addMenu('My_Nuke_Tools')
my_menu.addCommand("LS", 'ListShuffle.main()', "",icon='ListShuffle.png')
my_menu.addCommand("Orgainc Alpha Feather", 'OrgaincAlphaFeather.main()', "",icon='OrgaincAlphaFeather.png')
