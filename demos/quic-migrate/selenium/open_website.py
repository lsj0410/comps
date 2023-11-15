import sys

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

if len(sys.argv) < 2:
  sys.exit("Please supply a hostname to fetch.")

hostname = sys.argv[1]

opt = ChromeOptions()
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-setuid-sandbox")
opt.add_argument("--enable-quic")
opt.add_argument("--origin-to-force-quic-on=%s" % hostname)

# remote driver
driver = webdriver.Remote("http://localhost:4444/wd/hub", options=opt) 

# driver = webdriver.Chrome()

driver.get("https://%s" % hostname)
assert "Goog" in driver.title
driver.close()
