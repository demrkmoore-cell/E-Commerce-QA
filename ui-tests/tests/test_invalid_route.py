def test_invalid_route_returns_404(page):
    response = page.goto("https://www.demoblaze.com/this-page-does-not-exist")

    assert response is not None
    assert response.status == 404
    assert page.title() == "404 Not Found"
