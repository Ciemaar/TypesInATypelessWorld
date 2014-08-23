import logging
import yaml


log = logging.getLogger(__name__)

__author__ = 'andriod'

def write_yaml(name, value):
    print(yaml.dumps({name:value}))

write_yaml("Bill Engvall",16)
write_yaml("Exit 269",["Gas", "Camping"])