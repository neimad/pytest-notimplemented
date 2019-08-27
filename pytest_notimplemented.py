"""A pytest plugin providing a marker for not implemented features and tests.

@mark.notimplemented
--------------------

The `notimplemented` marker is designed to be used for tests which should fail because
the feature is not yet implemented.

As tests on not implemented features should fail, it is just syntatic sugar for a
standard `xfail` marker with a "Not implemented" message.

```python
    from pytest import mark

    @mark.notimplemented
    def test_foo(foo):
        assert foo.baz()

    @mark.xfail("Not implemented")
    def test_bar(bar):
        assert bar.baz()
```

@mark.notwritten
-----------------

The `notwritten` marker is is designed to be used for tests which are declared but not
defined. Those kind of tests are just placeholders to help the developer remember that
the behavior must be tested. And that marker helps on it.

As not written tests (or tests not finished to write) are impredictable, they must be
skipped. That marker is just syntatic sugar for a standard `skip` marker with a
"Not written" message.

```python
    from pytest import mark

    @mark.notwritten
    def test_foo(foo):
        pass

    @mark.skip("Not written")
    def test_bar(bar):
        pass
```

"""

from pytest import hookimpl, mark


@hookimpl
def pytest_configure(config):
    """Registers additonal markers.

    Markers provided by this plugin are registered:

     - `notimplemented`
     - `notwritten`

    """
    config.addinivalue_line(
        "markers", "notimplemented: mark a test as related to a non implemented feature"
    )
    config.addinivalue_line("markers", "notwritten: mark a test as not written")


@hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Apply custom markers.

    Marks:

     - not implemented tests as expected to fail,
     - not written tests as skipped.
    """
    not_implemented = item.get_closest_marker("notimplemented")
    not_written = item.get_closest_marker("notwritten")

    if not_implemented:
        item.add_marker(mark.xfail(reason="Not implemented"))

    if not_written:
        item.add_marker(mark.skip(reason="Not written"))
