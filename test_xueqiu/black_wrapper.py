import logging

import allure
logging.basicConfig(level=logging.INFO)

def black_wrapper(fun):
    def run(*args, **kwargs):
        #取self
        start = args[0]
        try:

            logging.info("start find: \nargs: " + str(args) + "kwargs" +str(kwargs))
            #返回find
            return fun(*args, **kwargs)

        except Exception as e:
            start.screenshot("map.jpg")
            with open("./map.jpg", 'rb') as b:
                picture_data = b.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.JPG)

            #遍历黑名单
            for black in start.black_list:
                bl = start.finds(*black)
                if len(bl) > 0:
                    bl[0].click()

                    return fun(*args, **kwargs)

            raise e
    return run

# def black_wrapper(fun):
#     def run(*args, **kwargs):
#         basepage = args[0]
#         try:
#             return fun(*args, **kwargs)
#         # 捕获元素没找到异常
#         except Exception as e:
#             # 遍历黑名单中的元素，进行处理
#             for black in basepage.black_list:
#                 eles = basepage.finds(*black)
#                 # 黑名单被找到
#                 if len(eles) > 0:
#                     # 对黑名单元素进行点击，可以自由扩展
#                     eles[0].click()
#                     return fun(*args, **kwargs)
#             raise e
#
#     return run