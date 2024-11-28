import os
import re

def remove_html_tags(text):
    """移除文本中的HTML标签"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def merge_txt_files(folder_path, output_file):
    """合并文件夹中的所有txt文件，并移除HTML标签"""
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filename in os.listdir(folder_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        clean_content = remove_html_tags(content)
                        # 在不同的txt内容之间添加分隔符和空行
                        if outfile.tell() != 0:  # 检查文件是否为空
                            outfile.write('\n' + '*' * 20 + '\n\n')
                        outfile.write(clean_content + '\n')
        print(f"所有文件已合并到 {output_file}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    folder_path = input("请输入文件夹地址: ")
    output_file = os.path.join(folder_path, os.path.basename(folder_path) + '.txt')
    merge_txt_files(folder_path, output_file)