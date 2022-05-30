def ensure_nonexistence(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
