import os
from git import Repo
repo = Repo.clone_from(url='git@github.com:Legilibre/Archeo-Lex.git',to_path='../Newnew')
remote = repo.create_remote(name='gitlab', url='git@github.com:Legilibre/Archeo-Lex.git')
with open(os.path.join(rw_dir,'Newnew.tar'),'wb') as fp:
    repo.archive(fp)

if：
 
else

dev 105%