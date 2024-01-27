import subprocess, os
def test_exec_code():
    try:
        bucket_name = 'bounding-box-suggestion-test'
        
        is_github_actions = os.path.isdir('/home/runner/')
        if not is_github_actions
            if os.path.isfile('/home/exec.py'): os.remove('/home/exec.py')
            assert not os.path.isfile('/home/exec.py')
            cmd = ['bash', 'exec_code/mv_exec_code.sh']
            subprocess.check_output(cmd)
            assert os.path.isfile('/home/exec.py')

        cmd = ['python', '/home/exec.py', 'sample-id', bucket_name]
        subprocess.check_output(cmd)
    except:
        assert False

