import os

def test_mk_execution_file():
    # make execution file
    os.system('sh mk_execution_file.sh')
    assert os.path.isfile('./pyinstaller/dist/bbox_suggestion')

    # clear input and output
    if os.path.isfile('input.zip'): os.system('rm -rf input.zip')
    if os.path.isfile('output.zip'): os.system('rm -rf output.zip')

    # test execution file
    user_id:str = 'sample-id'
    os.system(f'./pyinstaller/dist/bbox_suggestion {user_id}')
    assert os.path.isfile('output.zip')

    # check output
    os.system('unzip -o output.zip')
    assert os.path.isdir('output')
    assert os.path.isfile('output/human.jpeg')
    assert os.path.isfile('output/dog.jpeg')

if __name__ == '__main__':
    test_mk_execution_file()
