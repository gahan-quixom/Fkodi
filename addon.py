import xbmcaddon
import xbmcgui
import sys
import urlparse
import xbmc

xbmc.log('**Addon Initialization***')
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
# __addon__ = xbmcaddon.Addon()
# __addonname__ = __addon__.getAddonInfo('name')
# __icon__ = __addon__.getAddonInfo('icon')

line1 = "Mk1"
line2 = "Building Armor"
line3 = "Powering on arc reactor"

xbmc.log('Dialog....')
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
xbmc.log('**EOF***')