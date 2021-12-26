import atexit

def all_done(value):
    print(f"all done {value}")

atexit.register(all_done, "Reganto")

#@atexit.register
#def all_done():
#    print("done")

