def test_a_not_implemented_feature_with_a_not_written_test(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notimplemented
        def test_not_implemented():
            assert False

        @mark.notwritten
        def test_not_written():
            assert False
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(xfailed=1, skipped=1)


def test_a_not_implemented_feature_with_a_not_written_test_and_a_normal_test(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notimplemented
        def test_not_implemented():
            assert False

        @mark.notwritten
        def test_not_written():
            assert False

        def test_pass():
            assert True
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(xfailed=1, skipped=1, passed=1)
