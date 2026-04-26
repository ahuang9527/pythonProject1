import FileRenamer

# 1. 调用脚本中的FileRenamer类，创建对象（和原脚本使用方法一致）
# 这里可以用input()输入路径和前缀，也可以直接指定
target_folder = input("请输入要修改的文件夹路径：").strip()
name_prefix = input("请输入文件名前缀：").strip()

# 2. 实例化类，调用批量改名方法
renamer = FileRenamer.FileRenamer(target_folder, name_prefix)
renamer.batch_rename()