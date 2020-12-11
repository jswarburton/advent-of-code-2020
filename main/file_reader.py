def read(file_name: str, path: str = "main/resources") -> list:
    output = []
    with open(f"{path}/{file_name}") as f:
        lines = f.readlines()
        for line in lines:
            output.append(line.strip())

    return output
