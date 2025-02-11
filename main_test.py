from main import main
from s3.s3_utils import s3_utils
import os

def test_main():
    user_id:str = 'sample-id'
    bucket_name:str = 'bounding-box-suggestion-test'
    s3 = s3_utils(bucket_name)

    # clear output on s3
    if s3.check_uploaded_file('output.zip', f'{user_id}/output/'): s3.del_file('output.zip', f'{user_id}/output/')

    # inference
    main(user_id, bucket_name)

    # clear output on local
    assert os.path.isfile('output.zip')
    os.system('rm -rf output.zip')
    assert not os.path.isfile('output.zip')

    assert os.path.isdir('output')
    os.system('rm -rf output')
    assert not os.path.isdir('output')

    # download output from s3
    assert s3.check_uploaded_file('output.zip', f'{user_id}/output/')
    s3.download_file('output.zip', f'{user_id}/output/')
    assert os.path.isfile('output.zip')

    # unzip
    os.system('unzip -o output.zip')
    assert os.path.isdir('output')
    assert os.path.isfile('output/person1.jpeg')
    assert os.path.isfile('output/dog.jpeg')
    assert os.path.isfile('output/person2.png')
    assert os.path.isfile('output/dog2.bmp')