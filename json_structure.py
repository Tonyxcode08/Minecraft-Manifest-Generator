import uuid

#UUID Generation
uuid_1 = uuid.uuid4()
uuid_2 = uuid.uuid4()

#Default Values
name = "my mod"
description = "my modpack"
min_engine_version = [1, 20, 0]
datatype = "data"

#Version list
version = [1, 0, 0]



def generate_manifest():
    return {
            "format_version" : 2,
            "header" : {
                "name" : name,
                "description" : description,
                "uuid" : str(uuid_1),
                "version" : version,
                "min_engine_version" : min_engine_version,
            },
            "modules" : [
                {
                    "description" : description,
                    "type" : datatype,
                    "uuid" : str(uuid_2),
                    "version" : version
                },
            ]
        }