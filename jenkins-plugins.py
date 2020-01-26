# Jenkins Plugins Info Regex
import re

# Name
jenk_plugs_name = re.compile(r"(plugin-name)=(\".*.\"\s)\s*")

jenk_plugs_class = re.compile(r"class=(\".*.\"\s)")
jenk_plugs_depenent = (r"class=(\"dependent-list\").*data-(plugin-id)=(\".*.\")+")

jenk_plugs_dependancies = (r"class=(\"dependency-list\").*data-(plugin-id)=(\".*.\")+")