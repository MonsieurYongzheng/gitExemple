from git import Repo
repo = Repo.clone_from(url='git@github.com:Legilibre/Archeo-Lex.git',to_path='../Newnew')
remote = repo.create_remote(name='gitlab', url='git@github.com:Legilibre/Archeo-Lex.git')