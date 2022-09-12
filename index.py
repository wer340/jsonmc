import json
import os
from os import path
from textwrap import indent
# with open("./directors/ang-lee.json") as actor:
    # data = json.loads(actor.read() )
db_names=["actors","directors"] 
for  db_name in db_names:  
    src=path.realpath("./"+db_name+"/")  
    dir_list=os.listdir(src)

    with open("./"+db_name+".json","w+",encoding="utf8") as directors:
        directors.write("[\n\n")
        for item in dir_list:
            with open("./"+db_name+"/"+item,encoding="utf8") as actor:
                data=json.loads(actor.read() )
                li=json.dumps(data,indent=4)
                directors.write(f"{li},\n")
        
        directors.write("{}\n\n]")

