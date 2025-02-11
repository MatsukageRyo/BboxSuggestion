from s3_utils import s3_utils
import os

def test_s3_utils():
    from datetime import datetime
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    
    # Test for create bucket
    bucket_name = 'test-bucket-by-matsukage-' + current_datetime
    print(bucket_name)
    s3 = s3_utils(bucket_name)
    assert s3.exist_bucket()
    
    dir_name = 'test-dir-by-matsukage/'

    # Test for upload file
    test_file_name = 'test.txt'
    with open(test_file_name, 'w') as f:
        f.write(test_file_name)
    s3.upload_file(test_file_name, dir_name)
    assert s3.check_uploaded_file(test_file_name, dir_name)

    # Test for copy file
    new_file_name2 = 'test2.txt'
    s3.copy_file(dir_name + test_file_name, dir_name + new_file_name2)
    assert s3.check_uploaded_file(new_file_name2, dir_name)

    # Test for file_listup
    file_list = s3.listup_files(dir_name)
    assert 'test.txt' in file_list
    assert 'test2.txt' in file_list
    assert len(file_list) == 2

    # Test for delete file
    s3.del_file(test_file_name, dir_name)
    assert not s3.check_uploaded_file(test_file_name, dir_name)


    # Test for download file
    if os.path.isfile(new_file_name2): os.remove(new_file_name2)
    s3.download_file(new_file_name2, dir_name)
    assert s3.check_downloaded_file(new_file_name2)

    # Test for delete buckets
    s3.del_bucket()
    assert not s3.exist_bucket()

    print('Success')
    os.remove(test_file_name)
    os.remove(new_file_name2)    

if __name__ == "__main__":
    # Test
    test_s3_utils()