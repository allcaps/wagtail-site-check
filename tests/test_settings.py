from wagtailsitecheck import defaults
from wagtailsitecheck.defaults import get_allowed_wagtail_sites


def test_allowed_wagtail_sites():
    expected = ["a.com:443", "b.com:443", "c.com:443"]
    assert defaults.ALLOWED_WAGTAIL_SITES == expected


def test_get_allowed_wagtail_sites():
    expected = ["*:443", "testserver:443"]
    assert get_allowed_wagtail_sites() == expected
