
name = "txConverter"
version = "0.1.0"

authors = ["Rogouan"]
vcs = "git"

maketx_path = "<PUT_THE_MAKETX_PATH>"

def commands():
    """
    set the environnement variable for silex
    """
    env.PYTHONPATH.append("{root}")


@late()
def requires():
    return["python", "arnold"]



    