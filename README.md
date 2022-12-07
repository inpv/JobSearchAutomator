# CVAutoUpdate
<p>A pytest/Selenium-based utility to automatically update your CV on HeadHunter websites in headless mode.</p>
<p>Requires Google Chrome executable installed on your server (not just the webdriver).</p>
<p>Use cron or systemd service/timer automation on your server to harness the benefits of this utility.</p>
<p>The reason behind writing this is simple - sure, using arbitrary Selenium code is slower than using their API, but 30 seconds to launch the webdriver is still less than waiting up to 15 days to get their developer's API validation (if you get it at all).</p>