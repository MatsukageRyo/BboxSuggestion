import os, sys
s3 = None

def mv_dir():
    if not os.path.isdir('/worker'):
        print('mkdir /worker')
        os.mkdir('/worker')
    assert os.path.isdir('/worker')
    os.chdir('/worker')

def git_clone():
    if not os.path.isdir('/worker/BboxSuggestion'):
        print('git clone BboxSuggestion')
        os.system('git -c core.sshCommand="ssh -i /home/ssh/github_key -F /dev/null" clone git@github.com:MatsukageRyo/BboxSuggestion.git')
    assert os.path.isdir('/worker/BboxSuggestion')
    os.chdir('/worker/BboxSuggestion')
    os.system('git -c core.sshCommand="ssh -i /home/ssh/github_key -F /dev/null" pull')

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

def main(user_id:str, bucket_name:str):
    mv_dir()
    git_clone()

    sys.path.append('/worker/BboxSuggestion')
    from main import main as BboxSuggestion
    from s3.s3_utils import s3_utils
    global s3
    s3 = s3_utils(bucket_name)

    # check input
    if not check_input(user_id): return False

    # clear output on s3
    if s3.check_uploaded_file('output.zip', f'{user_id}/output/'):
        s3.del_file('output.zip', f'{user_id}/output/')

    # inference
    BboxSuggestion(user_id, bucket_name)

    # check output
    if not check_output(user_id): return False
    
    print('Success')
    return True

if __name__ == '__main__':
    print(f'sys.argv: {sys.argv}')
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        assert False