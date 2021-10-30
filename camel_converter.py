from typing import Optional
def camel_converter(camel_str: str, kebab: Optional[bool] = False) -> str:
    raw_str = ""
    output_str = ""
    splitted: list[str] = []
    for i in range(len(camel_str)):
        if camel_str[i].isupper():
            if raw_str:
                splitted.append(raw_str)
            raw_str = ""
            raw_str += camel_str[i]
        else:
            raw_str += camel_str[i]
    
    if kebab:
        output_str = "-".join(splitted)
    else:
        output_str = "_".join(splitted)

    return output_str.lower()
