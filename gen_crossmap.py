import json

crossmap = {}
crossmap_hash_list = []

class CrossmapEntry:
    def __init__(self, translated_hash: int):
        self.hash = translated_hash

def load_crossmap_data():
    global crossmap

    data = open("native/crossmap.txt").readlines()
    for item in data:
        translation = item.split(",")
        crossmap[int(translation[0], 16)] = CrossmapEntry(int(translation[1], 16))

def allocate_crossmap_indices():
    global crossmap_hash_list
    for hash_key in crossmap.keys():
        crossmap_hash_list.append(crossmap[hash_key].hash)

def write_crossmap_header():
    crossmap_pairs = ",\n\t".join([f"{{0x{x:X}, 0x{x:X}}}" for x in crossmap_hash_list])
    open("crossmap.txt", "w+").write(f"""#pragma once

namespace zenith
{{
    const crossmap g_crossmap {{
        {crossmap_pairs}
    }};
}}
""")