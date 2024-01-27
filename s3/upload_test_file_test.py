import s3_utils

def test_upload_test_file(bucket_name):
    # Test
    s3 = s3_utils.s3_utils(bucket_name)
    assert s3.exist_dir('sample-id/')
    assert s3.exist_dir('sample-id/input/')
    assert s3.check_uploaded_file('images.zip', 'sample-id/input/')
    assert s3.exist_dir('sample-id/output/')

if __name__ == "__main__":
    for bucket_name in ['bounding-box-suggestion', 'bounding-box-suggestion-test']:
        # create bucket
        s3 = s3_utils.s3_utils(bucket_name)

        # create sample user directory
        if not s3.exist_dir('sample-id/'):
            s3.mk_dir('sample-id/')
        
        # create input and output directory
        if not s3.exist_dir('sample-id/input/'):
            s3.mk_dir('sample-id/input/')
        if not s3.exist_dir('sample-id/output/'):
            s3.mk_dir('sample-id/output/')
        
        # upload sample file
        s3.upload_file('s3/images.zip', 'sample-id/input/')

        # Test
        test_upload_test_file(bucket_name)