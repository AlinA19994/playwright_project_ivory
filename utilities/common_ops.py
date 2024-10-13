import time
import xml.etree.ElementTree as ET


def get_time_stamp():
    return time.time()


def get_data(node_name):
    root = ET.parse('../configuration/data.xml').getroot()
    return root.find('.//' + node_name).text
