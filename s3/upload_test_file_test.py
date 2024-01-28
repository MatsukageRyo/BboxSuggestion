import s3_utils

def test_upload_test_file():
    bucket_name = 'bounding-box-suggestion-test'
    # Test
    s3 = s3_utils.s3_utils(bucket_name)
    assert s3.check_uploaded_file('images.zip', 'sample-id/input/')

if __name__ == "__main__":
    bucket_name = 'bounding-box-suggestion-test'
    # create bucket
    s3 = s3_utils.s3_utils(bucket_name)
    
    # upload sample file
    s3.upload_file('s3/images.zip', 'sample-id/input/')

    # Test
    test_upload_test_file()