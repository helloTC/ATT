# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode:nil -*-
# vi: set ft=python sts=4 sw=4 et:

import os
import shutil

verbose = True

class DeleteFile(object):
    """
    Delete file/directory
    --------------------------------
    Parameters:
        path: path for deleting

    >>> m = DeleteFile()
    >>> m.exexute(path)
    """
    def __init__(self):
        pass
    def execute(self, path):
        if verbose:
            print('Deleting {}'.format(path))
        if '.' in path:
            os.remove(path)
        else:
            shutil.rmtree(self._path)
    def undo(self):
        pass

class CopyFile(object):
    """
    Copy file/directory from source to destination
    ------------------------------------------------
    Parameters:
        path_src: source path
        path_dst: destination path

    >>> m = CopyFile()
    >>> m.execute(src, dst)
    """
    def __init__(self):
        pass
    def execute(self, src, dst):
        if verbose:
            print('Copying {0} to {1}'.format(src, dst))
        if '.' in src:
            shutil.copyfile(src, os.path.join(dst, [x for x in src.split('/') if x][-1]))
        else:
            shutil.copytree(src, os.path.join(dst, [x for x in src.split('/') if x][-1]))
    def undo(self):
        pass
    
class RenameFile(object):
    """
    Rename file or directory    
    ---------------------------
    Parameters:
        src: source file
        dst: destination file

    >>> m = RenameFile()
    >>> m.execute(src, dst)
    """
    def __init__(self):
        pass
    def execute(self, src, dst):
        if verbose:
            print('Renaming {0} to {1}'.format(src, dst))
        os.rename(src, dst)
    def undo(self):
        pass
  
class CreateFile(object):
    """
    Create file/directory
    ---------------------------
    Parameters:
        path: data path
              if it's a directory, create directory, 
              else create a file
        text: by default a text

    >>> a = CreateFile()
    >>> a.execute(path, text)
    """
    def __init__(self):
        pass
    def execute(self, path, text = 'Hello, world\n'):
        if verbose:
            print('Creating {}'.format(path))
        if '.' in path:
            with open(path, 'w') as out_file:
                out_file.write(text)
        else:
            os.mkdir(path)
    def undo(self):
        pass


         







