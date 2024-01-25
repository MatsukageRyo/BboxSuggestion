from s3.s3_utils import s3_utils
import subprocess, os, shutil
def test_docker_run():
    user_id = 'sample-id'
    s3 = s3_utils('bounding-box-suggestion')

    # clear output on s3
    if s3.check_uploaded_file('output.zip', f'{user_id}/output/'):
        s3.del_file('output.zip', f'{user_id}/output/')
    assert not s3.check_uploaded_file('output.zip', f'{user_id}/output/')

    # docker run
    try:
        # docker run時に-itオプションをつけると、エラーで落ちるので、テスト時は-itオプションを外したものを実行する
        # 外したものをdocker_run_bak.shに保存して実行する
        assert os.path.isfile('docker_run.sh')
        with open('docker_run.sh', 'r') as f:
            lines = f.read()
        lines = lines.replace('-it', '')
        with open('docker_run_bak.sh', 'w') as f:
            print(lines)
            f.write(lines)
        # docker run   
        cmd = ['bash', 'docker_run_bak.sh']
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Command output: {e.output}")
        assert False
    assert s3.check_uploaded_file('output.zip', f'{user_id}/output/')

    # download output from s3
    s3.download_file('output.zip', f'{user_id}/output/')

    # unzip
    os.system('unzip -o output.zip')
    assert os.path.isdir('output')
    assert os.path.isfile('output/human.jpeg')
    assert os.path.isfile('output/dog.jpeg')

    os.remove('docker_run_bak.sh')