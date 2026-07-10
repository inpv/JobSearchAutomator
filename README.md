# JobSearchAutomator
<p>A Selenium-based utility to automatically update your CV on HeadHunter websites in headless mode.</p>
<p>Now with inbuilt OCR-based CAPTCHA solving and submitting (still WIP, though - expect inaccurate results without a special dataset to train the OCR engine on).</p>
<p>Requires Google Chrome executable installed on your server (not just the webdriver).</p>
<p>Use cron or systemd service/timer automation on your server to harness the benefits of this utility.</p>
<p>The reason behind writing this is simple - sure, using arbitrary Selenium code is slower than using their API, but 30 seconds to launch the webdriver is still less than waiting up to 15 days to get their developer's API validation (if you get it at all).</p>
<p>And now you won't get it, since the applicant API has been disabled.</p>

# TODO:
Implement job positions' filtering and CV sending.