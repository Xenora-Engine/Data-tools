import json

natives = {}

class Arg:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type  

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

class NativeFunc:
    def __init__(self, namespace: str, name: str, hash: int, args: list[dict], return_type: str):
        self.namespace = namespace
        self.name = name
        self.hash = hash
        self.args: list[Arg] = []
        self.return_type = return_type
        for arg in args:
            self.args.append(Arg(arg["name"], arg["type"]))

    def get_native_def_str(self) -> str:
        param_decl = ", ".join(str(arg) for arg in self.args)
        param_pass = ", ".join(arg.name for arg in self.args)
        hex_hash = f"0x{self.hash:X}"
        return f"FORCEINLINE {self.return_type} {self.name}({param_decl}) {{ return invoke<{self.return_type}>({hex_hash}, {param_pass}); }}"

def load_natives_data():
    global natives
    data = json.load(open("native/native.json"))
    for ns, natives_list in data.items():
        natives[ns] = []
        for hash_str, native_data in natives_list.items():
            natives[ns].append(NativeFunc(ns, native_data["name"], int(hash_str, 16), native_data["params"], native_data["return_type"]))

def write_natives_header():
    natives_buf = ""
    for ns, nvs in natives.items():
        natives_buf += f"namespace {ns}\n{{\n"
        for nat_data in nvs:
            natives_buf += f"\t{nat_data.get_native_def_str()}\n"
        natives_buf += "}\n\n"
    
    open("natives.txt", "w+").write(f"""#pragma once
#include "invoker/invoker.hpp"

{natives_buf}
""")