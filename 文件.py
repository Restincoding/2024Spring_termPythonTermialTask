'''
可以操作文件的读、写、追加函数
'''

#读取文件内容并打印
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("读取成功！文件内容如下：")
            print(content)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

#向文件写入内容
def write_file(file_path, content_to_write):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content_to_write)
            print(f"内容已成功写入到文件 {file_path}")
    except Exception as e:
        print(f"写入文件时发生错误：{e}")

#向文件追加内容
def append_file(file_path, content_to_append):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content_to_append)
            print(f"内容已成功追加到文件 {file_path}")
    except Exception as e:
        print(f"追加内容到文件时发生错误：{e}")

if __name__ == "__main__":
    #创建一个新文件
    file_path = "example.txt"
    
    #写入内容
    content = "早上好！"
    write_file(file_path, content)

    #读取内容
    read_file(file_path)

    #追加内容
    content_append = "如果稍后见不到你，那么中午好、晚上好"
    append_file(file_path, content_append)
    
    #再次读取内容
    read_file(file_path)