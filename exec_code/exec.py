import os, sys
from main import main as BboxSuggestion
from s3.s3_utils import s3_utils

s3 = s3_utils('bounding-box-suggestion')

def mv_dir():
    if not os.path.isdir('/worker'):
        print('mkdir /worker')
        os.mkdir('/worker')
    assert os.path.isdir('/worker')
    os.chdir('/worker')

def git_clone():
    if not os.path.isdir('/worker/BboxSuggestion'):
        print('git clone BboxSuggestion')
        os.system('git clone git@github.com:MatsukageRyo/BboxSuggestion.git')
    assert os.path.isdir('/worker/BboxSuggestion')
    os.chdir('/worker/BboxSuggestion')

def check_input(user_id:str):
    if not s3.check_uploaded_file('images.zip', f'{user_id}/input/'):
        print('images.zip is not uploaded')
        return False
    return True

def check_output(user_id:str):
    if not s3.check_uploaded_file('output.zip', f'{user_id}/output/'):
        print('output.zip is not uploaded')
        return False
    return True

def main(user_id:str = 'sample-id'):
    mv_dir()
    git_clone()

    # check input
    if not check_input(user_id): return False

    # clear output on s3
    if s3.check_uploaded_file('output.zip', f'{user_id}/output/'):
        s3.del_file('output.zip', f'{user_id}/output/')

    # inference
    BboxSuggestion(user_id)

    # check output
    if not check_output(user_id): return False
    
    print('Success')
    return True

if __name__ == '__main__':
    main(sys.argv[1])