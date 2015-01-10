import os, os.path, argparse, random, stat, distutils
from shutil import copy2, copytree, ignore_patterns

ABS_PATH = os.path.join(os.getcwd(), 'myvcs/')

def init_vcs_folder():
    '''creates myvcs folder in current 
    working directory'''
    try:
        os.mkdir('myvcs/') #permissions hmm
    except OSError as e:
        print e
        print "something went wrong!"
        
def commit_to_vcs(hashed_name):
    '''creates a folder for a commit
    in the myvcs folder and copies files'''
    try:
        print 'myvcs/' + hashed_name
        copytree(os.getcwd(), 'myvcs/' + hashed_name, ignore=ignore_patterns('myvcs'))
    except OSError as e:
        #os.chmod
        print e
        print "something went wrong!"   

def checkout(hashed_name):
    distutils.dir_util.copy_tree('myvcs/' + hashed_name, os.getcwd())
    # need to save working directory path if we want to use from subdirectory
    
def mk_hash():
    hash = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    #if myvcs directory has folder named hash
    if os.path.isdir(os.getcwd() + 'myvcs/' + hash):
        hash = mk_hash()
    return hash

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command you want to submit to VCS')
    parser.add_argument('action', nargs='*', type=str, help='init or commit or checkout')
    args = parser.parse_args()
    print args
    if args.action[0] == 'init':
        init_vcs_folder()
    elif args.action[0] == 'commit':
        commit_to_vcs(mk_hash())
    elif args.action[0] == 'checkout' :
        checkout_name = args.action[1]
        checkout(checkout_name)
    else:
        print 'Invalid command'
