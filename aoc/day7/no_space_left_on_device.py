class Directory:
    """A directory in a file system.

    Attributes:
        name (str): The name of the directory.
        files (list): The list of file names in the directory.
        children (list): The list of child directories in the directory.
        parent (Directory): The parent directory of the directory.
        size (int): The total size of the files in the directory.
    """

    def __init__(self, name=''):
        self.name = name
        self.files = []
        self.children = []
        self.parent = None
        self.size = 0


class FileSystem:
    """A file system.

    Attributes:
        root (Directory): The root directory of the file system.
        pwd (Directory): The current working directory of the file system.
        tree_size (int): The total size of all directories in the file system.
        sizes (list): The list of sizes of all directories in the file system.
    """

    def __init__(self):
        self.root = None
        self.pwd = None
        self.tree_size = 0
        self.sizes = []

    def add_directory(self, name: str):
        """Add a new directory with the given name to the file system.

        Args:
            name (str): The name of the new directory.
        """
        dir = Directory(name)

        if not self.root:
            self.root = dir
            self.pwd = self.root
        else:
            dir.parent = self.pwd

            self.pwd.children.append(dir)

    def add_file(self, name: str, size: int):
        """Add a new file with the given name and size to the current working directory.

        Args:
            name (str): The name of the new file.
            size (int): The size of the new file.
        """
        self.pwd.files.append(name)
        self.pwd.size += size

    def change_directory(self, name: str):
        """Change the current working directory to the directory with the given name.

        If the given name is '..', the current working directory is changed to its parent directory.
        If the current working directory is the root directory and the given name is '..',
        the current working directory remains the root directory.

        Args:
            name (str): The name of the new current working directory.
        """
        if not self.pwd:
            self.add_directory(name)
        elif name == '..':
            self.pwd = self.pwd.parent
        else:
            self.pwd = next(
                (child for child in self.pwd.children if child.name == name), None)

    def traverse_directory(self, node=None):
        """Traverse the directories in the file system and return the total size of all directories.

        Args:
            node (Directory, optional): The root node of the directories to be traversed.
                If not provided, the root directory of the file system is used.

        Returns:
            int: The total size of all directories in the file system.
        """
        if node is None:
            node = self.root

        for item in node.children:
            node.size += self.traverse_directory(item)

        self.sizes.append(node.size)

        return node.size


def build_file_system(data: str) -> FileSystem:
    """Build a file system from the given input data.

    Args:
        data (str): The input data representing the file system.

    Returns:
        FileSystem: The file system built from the input data.
    """
    file_system = FileSystem()

    for line in data:
        if '$ cd' in line:
            dir_name = line.replace('$ cd', '').strip()

            file_system.change_directory(dir_name)
        elif 'dir' in line:
            dir_name = line.replace('dir', '').strip()

            file_system.add_directory(dir_name)
        elif '$ ls' in line:
            continue
        else:
            size, name = line.split(' ')

            file_system.add_file(name, int(size))

    return file_system


def find_matching_directories(file_system: FileSystem) -> int:
    """Find the total size of all directories in the file system whose size is less than or equal to 100000.

    Args:
        file_system (FileSystem): The file system.

    Returns:
        int: The total size of all directories in the file system whose size is less than or equal to 100000.
    """
    file_system.traverse_directory()
    total_size = 0

    for size in file_system.sizes:
        if size <= 100000:
            total_size += size

    return total_size


def find_min_directory(file_system: FileSystem) -> int:
    file_system.traverse_directory()
    sizes = []

    for size in file_system.sizes:
        if 70000000 - file_system.root.size + size >= 30000000:
            sizes.append(size)

    return min(sizes)
