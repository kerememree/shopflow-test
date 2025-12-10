import pytest
from playwright.sync_api import Page
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.failed:
            page = item.funcargs.get("page", None)
            if page:
                screenshot_name = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
                page.screenshot(path=screenshot_name)
                if pytest_html:
                    html = f'<div><img src="{screenshot_name}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra