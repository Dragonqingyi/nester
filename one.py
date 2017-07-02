movies = ["The Holy Grail", "1975", "Terry Jones & Terry Gilliam", 91,
          ["Graham chapman", ["Michael Palin", "John Cleese", "Terry Gilliam",
                              "Eric Idle", "Terry Jones"]]]
"""这是one.py模块，供一个名为print_lol()的函数，这个函数的作用是打印列表，其中可能包含
               （也可能不包含）的嵌套列表"""


def print_lol(the_list):
    """
    这个函数取一个位置参数，名为the_list，这可以是任何python列表（也可以是包含嵌套的列表）。
    所指定的列表中的每个数据项会递归的输出到屏幕上，各数据各占一行
    :param the_list:
    :return:
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)
