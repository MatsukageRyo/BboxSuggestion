import subprocess, os
def test_exec_code():
    try:
        if os.path.isfile('/home/exec.py'): os.remove('/home/exec.py')
        cmd = ['bash', 'exec_code/mv_exec_code.sh']
        subprocess.check_output(cmd)
        assert os.path.isfile('/home/exec.py')

        cmd = ['python', '/home/exec.py', 'sample-id', 'bounding-box-suggestion']
        subprocess.check_output(cmd)
    except:
        assert False

