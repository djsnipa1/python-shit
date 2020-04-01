# coding=utf-8
import requests

# ## Get result of model_list

api_list = 'http://colormind.io/list/'
api = 'http://colormind.io/api/'

model_list = []


def colormind_requests(url):
    r = requests.get(url)
    result = r.json()
    model_list_result = result['result']

    for item in model_list_result:
        model_list.append(item)
    print(model_list)


colormind_requests(api_list)


def choose_model():
    for i, val in enumerate(model_list):
        print(str(i + 1) + " " + val)
    print("\nChoose")
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            x = int(input("\nPlease enter a number 1 through 6: \n"))
        except ValueError:
            print("\nI said A NUMBER damn it! \n")
            # better try again... Return to the start of the loop
            continue
        else:
            # age was successfully parsed!
            # we're ready to exit the loop.

            break
    if x > 6:
        print("\nThat number is higher than 6 fucker! \n")
        choose_model()
    else:
        choose = model_list[int(x) - 1]
        print("\nFinally! You choose: " + choose)

    # while True:
    #     try:
    #         return int(input("Please enter a number from 1 - 6: "))
    #     except ValueError:
    #         print("Invalid input. Please try again!")
    #
    # n = get_user_input()
    # print("Thanks! You entered: {0:d}".format(n))
    #
    # x = int(input())
    # try:
    #     print(type(x))
    #     choose = model_list[int(x) - 1]
    #     print(choose)
    #
    # except ValueError:
    #     print("Oops!", sys.exc_info()[0], "occured.")
    #     print("Please insert a number between 1-6")
    #     choose_model()
    #     # if type(x) == int:
        #     pass

    # else:
    #     print("Please enter a number from 1 to 6")
    #     choose_model()


choose_model()
