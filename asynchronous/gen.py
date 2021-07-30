async def make_number():
    for number in range(10):
        yield number


# if __name__ == "__main__":
#     gen = make_number()
#     for i in range(10):
#         print(next(gen))

