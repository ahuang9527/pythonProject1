import os


class FileRenamer:
    """批量重命名文件工具类（面向对象）"""

    def __init__(self, folder_path, prefix):
        """
        初始化
        :param folder_path: 要修改的文件夹路径
        :param prefix: 新文件名前缀
        """
        self.folder_path = folder_path  # 目标文件夹路径
        self.prefix = prefix  # 文件名前缀
        self.script_name = os.path.basename(__file__)  # 获取当前脚本文件名（避免重命名自己）

    def is_valid_file(self, file_name):
        """判断是否是有效文件（过滤文件夹、过滤脚本本身）"""
        # 拼接完整路径
        full_path = os.path.join(self.folder_path, file_name)
        # 1. 必须是文件  2. 不能是当前脚本
        return os.path.isfile(full_path) and file_name != self.script_name

    def batch_rename(self):
        """批量修改文件名（核心函数）"""
        # 检查文件夹是否存在
        if not os.path.isdir(self.folder_path):
            print(f"错误：路径 {self.folder_path} 不是有效文件夹！")
            return

        # 获取文件夹下所有内容
        file_list = os.listdir(self.folder_path)
        count = 0  # 记录修改成功的文件数

        print("=== 开始批量修改文件名 ===")

        # 遍历所有文件
        for file_name in file_list:
            # 过滤无效文件
            if not self.is_valid_file(file_name):
                continue

            # 拆分文件名和后缀（os模块核心：路径处理）
            file_base, file_ext = os.path.splitext(file_name)

            # 新文件名：前缀 + 3位序号 + 后缀
            count += 1
            new_name = f"{self.prefix}_{count:03d}{file_ext}"

            # 拼接完整路径（必须用绝对/完整路径，否则会报错）
            old_path = os.path.join(self.folder_path, file_name)
            new_path = os.path.join(self.folder_path, new_name)

            # 执行重命名（文件操作）
            os.rename(old_path, new_path)
            print(f"已修改：{file_name} -> {new_name}")

        print(f"\n=== 完成！共修改 {count} 个文件 ===")


# ====================== 使用示例 ======================
'''if __name__ == "__main__":
    # 用 input 让用户输入文件夹路径
    target_folder = input("请输入文件夹路径：").strip()

    # 也可以让用户输入前缀
    name_prefix = input("请输入文件名前缀（例如：工作文件）：")

    # 3. 创建重命名对象并执行
    renamer = FileRenamer(target_folder, name_prefix)
    renamer.batch_rename()'''