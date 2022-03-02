'''
Author: wangzhongjie
Date: 2022-03-01 15:20:44
LastEditors: wangzhongjie
LastEditTime: 2022-03-01 15:33:49
Description: 
Email: UvDream@163.com
'''
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    print("closing file")
